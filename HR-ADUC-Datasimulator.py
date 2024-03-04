# *************************************************************************** #
# -----                     HR ADUC Data Simulator                      ----- #
#                              by Stéphane-Hervé                              #
#                                                                             #
# This script generates a set of simulated data for Active Directory User and #
# Computer (ADUC) attributes. It is designed to facilitate data analysis and  #
# security verification processes by providing  realistic but anonymized data #
# for use in comparing HR and ADUC extractions. The simulated data generated  #
# by this script can be utilized to demonstrate the functionality of          #
# associated data analysis tools, ensuring data privacy and confidentiality   #
# while allowing for comprehensive testing and validation.                    #
#                                                                             #
# Versions                                                                    #
# [2024-02-29] [1.0.0.0] [Stéphane-Hervé] - First version                     #
# *************************************************************************** #

import pandas as pd
import configparser
from faker import Faker
import random
import math
from unidecode import unidecode

# Parameters
parameters_inifile = "parameters.ini"
lang = "lang"

txt_lists_gen = "txt_lists_gen"
txt_user_acc_def = "txt_user_acc_def"
txt_files_def = "txt_files_def"
txt_rh_users_list = "txt_rh_users_list"
txt_files_gen = "txt_files_gen"

min_nbofgp_kname = "min_numberof_groups"
max_nbofgp_kname = "max_numberof_groups"
generic_accounts_rate_kname = "generic_accounts_rate"
system_service_accounts_rate_kname = "system_service_accounts_rate"
pf_kname = "paid_functions"
unpf_kname = "unpaid_functions"
addgp_kname = "additional_groups"
genacc_kname = "generic_accounts"
sysserv_kname = "system_service_accounts"
pfminocc_kname = "pf_min_occurrences"
pfmaxocc_kname = "pf_max_occurrences"
unpfminocc_kname = "unpf_min_occurrences"
unpfmaxocc_kname = "unpf_max_occurrences"


# Load parameters from INI file
def load_parameters_from_ini(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    parameters = {}
    for section in config.sections():
        for key, value in config.items(section):
            if key == lang or \
                key == pf_kname or key == unpf_kname or key == addgp_kname or \
                key == genacc_kname or key == sysserv_kname or \
                key == pfminocc_kname or key == pfmaxocc_kname or \
                key == unpfminocc_kname or key == unpfmaxocc_kname:
                    parameters[key] = value.split(", ")
            else:
                parameters[key] = [int(x) for x in value.split(", ")]

    return parameters


ini_parameters = load_parameters_from_ini(parameters_inifile)

# Initialization of Faker
language = ini_parameters[lang]
fake = Faker(language)

# Access parameters
min_numberof_groups = ini_parameters[min_nbofgp_kname]
min_numberof_groups = int(min_numberof_groups[0])
max_numberof_groups = ini_parameters[max_nbofgp_kname]
max_numberof_groups = int(max_numberof_groups[0])


print(ini_parameters[txt_lists_gen])

# Creation of the list of remunerated functions associated with the accounts with their autorized number of occurrences
functions_str = ini_parameters[pf_kname]
min_occurrences = [int(x) for x in ini_parameters[pfminocc_kname]]
max_occurrences = [int(x) for x in ini_parameters[pfmaxocc_kname]]
random_occurrences = [random.randint(min_occ, max_occ) for min_occ, max_occ in zip(min_occurrences, max_occurrences)]
remunerated_functions = list(zip(functions_str, random_occurrences))

# The number of users is randomly chosen up to 30% less of the maximum users
#max_numberof_users = sum(random_occurrences)
#min_numberof_users = math.floor(max_numberof_users * 0.3)
#numberof_users = random.randint(min_numberof_users, max_numberof_users)
numberof_users = sum(random_occurrences)

# Creation of the list of non paid functions associated with the accounts
functions_str = ini_parameters[unpf_kname]
min_occurrences = [int(x) for x in ini_parameters[unpfminocc_kname]]
max_occurrences = [int(x) for x in ini_parameters[unpfmaxocc_kname]]
random_occurrences = [
    random.randint(min_occ, max_occ)
    for min_occ, max_occ
    in zip(min_occurrences, max_occurrences)
]
non_remunerated_functions = list(zip(functions_str, random_occurrences))
del functions_str, min_occurrences, max_occurrences, random_occurrences

# Creation of the list of group names
additional_groups_str = ini_parameters.get(addgp_kname, "")
additional_groups_list = list(additional_groups_str)
groups = []
for row in remunerated_functions:
    groups.append(row[0])
for row in non_remunerated_functions:
    groups.append(row[0])
groups.extend(additional_groups_list)

# Creation of the list of generic accounts
generic_accounts_str = ini_parameters[genacc_kname]
generic_accounts = generic_accounts_str

# The number of generic accounts is randomly chosen up to 30% lower than
# the maximum generic accounts
generic_accounts_rate = ini_parameters[generic_accounts_rate_kname]
generic_accounts_rate = int(generic_accounts_rate[0]) / 100
max_numberof_generic_accounts = len(generic_accounts)
min_numberof_generic_accounts = math.floor(max_numberof_generic_accounts * generic_accounts_rate)
numberof_generic_accounts = random.randint(min_numberof_generic_accounts, max_numberof_generic_accounts)

# Liste des comptes des services système
# Creation of the list of system services accounts
system_service_accounts_str = ini_parameters[sysserv_kname]
system_service_accounts = system_service_accounts_str

# The number of system service accounts is randomly chosen up to 30% lower than
# the maximum system service accounts
system_service_accounts_rate = ini_parameters[system_service_accounts_rate_kname]
system_service_accounts_rate = int(system_service_accounts_rate[0]) / 100
max_numberof_system_service_accounts = len(system_service_accounts)
min_numberof_system_service_accounts = math.floor(max_numberof_system_service_accounts * system_service_accounts_rate)
numberof_system_service_accounts = random.randint(min_numberof_system_service_accounts, max_numberof_system_service_accounts)

print(ini_parameters[txt_user_acc_def])
# Generation of a unique SamAccountName
def generate_unique_samaccountname(first_name, last_name, existing_samaccountnames):
    # Handle cases where first or last name is empty
    if not first_name:
        first_name = "unknown"
    if not last_name:
        last_name = "unknown"
    
    # Generation of the SamAccountName
    initials = "".join(word[0] for word in first_name.split())
    samaccountname = f"{initials.lower()}.{last_name.lower()}"
    samaccountname = samaccountname.replace(" ", "")
    
    # Make sure the SamAccountName is unique
    while samaccountname in existing_samaccountnames:
        # Generate the SamAccountName again if it already exists
        first_name = fake.first_name()
        last_name = fake.last_name()
        initials = "".join(word[0] for word in first_name.split())
        samaccountname = f"{initials.lower()}.{last_name.lower()}"
        samaccountname = samaccountname.replace(" ", "")
    
    return samaccountname

# Get a RH tuple from the username
def find_index(samaccountname, column, dataframe):
    # Handle cases where one of the arguments is empty
    if not samaccountname:
        samaccountname = "unknown"
    if not column:
        column = "unknown"
    if dataframe.empty:
        dataframe = "unknown"
    indices = dataframe[dataframe[column] == samaccountname].index.tolist()
    if indices:
        selected_tuple = dataframe.iloc[indices[0]]
    return selected_tuple

# Check that a user function exists and does not exceed the set number of occurrences
# Update the function table if the function is found and the usage is not saturated
# Return the corresponding boolean
def check_function_occurrences(function, existing_functions):
    # Handle empty argument cases
    if not function:
        function = "unknown"
    if not existing_functions:
        existing_functions = "unknown"
    for i, (uf_name, nb_max_occurrences) in enumerate(existing_functions):
        if uf_name == function and nb_max_occurrences > 0:
            existing_functions[i] = (uf_name, nb_max_occurrences - 1)
            return True
    return False

# Randomly assign a function
def assign_user_function(existing_user_functions):
    while True:
        user_function_names = [item[0] for item in existing_user_functions]
        user_function = random.choice(user_function_names)
        if check_function_occurrences(user_function, existing_user_functions):
            return user_function
        elif all(item[1] == 0 for item in existing_user_functions):
            raise ValueError("All user functions have reached their maximum occurrences.")

print(ini_parameters[txt_files_def])
print(ini_parameters[txt_rh_users_list])
# Generation of CSV files
def generate_csv_files():
    try:
        
        # -- FIRST CSV FILE --
        # Generation of data for RH_Users_extract
        data_rh_users = []
        existing_samaccountnames = set()
        for _ in range(numberof_users):

            first_name = fake.first_name()
            sam_first_name = unidecode(first_name)

            last_name = fake.last_name()

            use_name = fake.last_name()
            sam_use_name = unidecode(use_name)

            samaccountname = generate_unique_samaccountname(sam_first_name, sam_use_name, existing_samaccountnames)
            existing_samaccountnames.add(samaccountname)

            # Generate a user table
            data_rh_users.append({
                "Agent-etab.": "",
                "Nom d'usage": use_name,
                "Nom de famille": last_name,
                "Prénom": first_name,
                "Position": "",
                "Etablissement": "",
                "Structure": "",
                "Fonction": assign_user_function(remunerated_functions),
                "Username": samaccountname
            })

        df_rh_users = pd.DataFrame(data_rh_users)

        # Reorder the DataFrame by “User Name” and “First Name”
        df_rh_users = df_rh_users.sort_values(by=["Nom d'usage", "Prénom"])
        # Reset indexes
        df_rh_users.reset_index(drop=True, inplace=True)

        # Save first CSV file
        df_rh_users.to_csv("RH_Users_extract.csv", index=False, sep=";")

        # -- SECOND CSV FILE --
        # Generation of data for AD_Users_extract
        data_ad_users = []
        existing_user_samaccountnames = set()
        for _ in range(numberof_users):
            samaccountname = df_rh_users["Username"].sample().values[0]
            while samaccountname in existing_user_samaccountnames:
                samaccountname = df_rh_users["Username"].sample().values[0]
            existing_user_samaccountnames.add(samaccountname)

            # Find the index of the relevant HR entry
            current_RH_tuple = find_index(samaccountname, "Username", df_rh_users)

            data_ad_users.append({
                "CannotChangePassword": random.choice(['Yes', 'No']),
                "Department": "",
                "DistinguishedName": "",
                "Enabled": random.choice(['Yes', 'No']),
                # This below instruction randomly gets Username
                # while the GivenName should be the first name
                "GivenName": current_RH_tuple["Nom d'usage"],
                "LockedOut": random.choice(['Yes', 'No']),
                "MemberOf": "",
                "Name": current_RH_tuple["Prénom"] + " " + current_RH_tuple["Nom d'usage"],
                "ObjectClass": "",
                "ObjectGUID": "",
                "PasswordExpired": random.choice(['Yes', 'No']),
                "PasswordLastSet": fake.date_time_between(start_date='-20y', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
                "PasswordNeverExpires": random.choice(['Yes', 'No']),
                "PasswordNotRequired": random.choice(['Yes', 'No']),
                "PrimaryGroup": "",
                "SamAccountName": samaccountname,
                "SID": "",
                # This below instruction randomly gets last name
                # while the Surname should be the current use name
                "Surname": current_RH_tuple["Nom d'usage"],
                "UserPrincipalName": f"{samaccountname}@mairie.local",
                "WhenCreated": fake.date_time_between(start_date='-20y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
            })

        df_ad_users = pd.DataFrame(data_ad_users)

        # Reorder the DataFrame by user account name
        df_ad_users = df_ad_users.sort_values(by=["SamAccountName"])
        # Reset indexes
        df_ad_users.reset_index(drop=True, inplace=True)

        # Saving the second CSV file
        df_ad_users.to_csv("AD_Users_extract.csv", index=False, sep=";")

        # -- THIRD CSV FILE --
        # Generation of data for AD_Generic_Users_extract
        data_ad_generic_accounts = []
        existing_generic_samaccountnames = set()
        for _ in range(numberof_generic_accounts):
            samaccountname = unidecode(random.choice(generic_accounts))
            while samaccountname in existing_generic_samaccountnames:
                samaccountname = random.choice(generic_accounts)
            existing_generic_samaccountnames.add(samaccountname)

            data_ad_generic_accounts.append({
                "CannotChangePassword": random.choice(['Yes', 'No']),
                "Department": "",
                "DistinguishedName": "",
                "Enabled": random.choice(['Yes', 'No']),
                "GivenName": "",
                "LockedOut": random.choice(['Yes', 'No']),
                "MemberOf": "",
                "Name": "",
                "ObjectClass": "",
                "ObjectGUID": "",
                "PasswordExpired": random.choice(['Yes', 'No']),
                "PasswordLastSet": fake.date_time_between(start_date='-20y', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
                "PasswordNeverExpires": random.choice(['Yes', 'No']),
                "PasswordNotRequired": random.choice(['Yes', 'No']),
                "PrimaryGroup": "",
                "SamAccountName": samaccountname,
                "SID": "",
                "Surname": "",
                "UserPrincipalName": f"{samaccountname}@mairie.local",
                "WhenCreated": fake.date_time_between(start_date='-20y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
            })

        df_ad_generic_accounts = pd.DataFrame(data_ad_generic_accounts)

        # Reorder the DataFrame by user account name
        df_ad_generic_accounts = df_ad_generic_accounts.sort_values(by=["SamAccountName"])
        # Reset indexes
        df_ad_generic_accounts.reset_index(drop=True, inplace=True)

        # Saving the third CSV file
        df_ad_generic_accounts.to_csv("AD_Generic_Users_extract.csv", index=False, sep=";")

        # -- FOURTH CSV FILE --
         # Generation of data for AD_System_Services_extract
        data_system_services = []
        existing_system_service_samaccountnames = set()
        for _ in range(numberof_system_service_accounts):
            samaccountname = unidecode(random.choice(system_service_accounts))
            while samaccountname in existing_system_service_samaccountnames:
                samaccountname = random.choice(system_service_accounts)
            existing_system_service_samaccountnames.add(samaccountname)

            data_system_services.append({
                "CannotChangePassword": "Yes",
                "Department": "",
                "DistinguishedName": "",
                "Enabled": random.choice(['Yes', 'No']),
                "GivenName": "",
                "LockedOut": random.choice(['Yes', 'No']),
                "MemberOf": "",
                "Name": "",
                "ObjectClass": "",
                "ObjectGUID": "",
                "PasswordExpired": random.choice(['Yes', 'No']),
                "PasswordLastSet": fake.date_time_between(start_date='-20y', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
                "PasswordNeverExpires": random.choice(['Yes', 'No']),
                "PasswordNotRequired": random.choice(['Yes', 'No']),
                "PrimaryGroup": "",
                "SamAccountName": samaccountname,
                "SID": "",
                "Surname": "",
                "UserPrincipalName": f"{samaccountname}@mairie.local",
                "WhenCreated": fake.date_time_between(start_date='-20y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
            })

        df_system_services = pd.DataFrame(data_system_services)

        # Reorder the DataFrame by user account name
        df_system_services = df_system_services.sort_values(by=["SamAccountName"])
        # Reset indexes
        df_system_services.reset_index(drop=True, inplace=True)

        # Saving the fourth CSV file
        df_system_services.to_csv("AD_System_Services_extract.csv", index=False, sep=";")

        # -- FIFTH CSV FILE --
         # Generation of data for AD_Users_and_Groups_extract
        data_ad_users_and_groups = []
        
        for index, row in df_ad_users.iterrows():
            number_of_groups = random.randint(min_numberof_groups, max_numberof_groups)
            member_of = random.sample(groups, number_of_groups)
            # Ensure all elements in member_of are strings
            member_of = [str(item) for item in member_of]
            # Getting corresponding function value from the RH users array
            function_value = df_rh_users[df_rh_users["Username"] == row["SamAccountName"]]["Fonction"].values[0]
            # Join the list elements into a single string without square brackets
            member_of_strings = ",".join(member_of)
            
            data_ad_users_and_groups.append({
                "SamAccountName": row["SamAccountName"],
                "MemberOf": f"{function_value},{member_of_strings}"
            })
        
        for index, row in df_ad_generic_accounts.iterrows():
            data_ad_users_and_groups.append({
                "SamAccountName": row["SamAccountName"],
                "MemberOf": row["MemberOf"]
            })
        
        for index, row in df_system_services.iterrows():
            data_ad_users_and_groups.append({
                "SamAccountName": row["SamAccountName"],
                "MemberOf": row["MemberOf"]
            })

        df_ad_users_and_groups = pd.DataFrame(data_ad_users_and_groups)

        # Reorder the DataFrame by user account name
        df_ad_users_and_groups = df_ad_users_and_groups.sort_values(by=["SamAccountName"])
        # Reset indexes
        df_ad_users_and_groups.reset_index(drop=True, inplace=True)

        # Saving the fifth CSV file
        df_ad_users_and_groups.to_csv("AD_Users_and_Groups_extract.csv", index=False, sep=";")
    except ValueError as e:
        print(f"ValueError: {e}")
        
# Call the function to generate the CSV files
print ("Génération des fichiers CSV.")
generate_csv_files()