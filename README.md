# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator is a Python script designed to generate simulated data for Active Directory User and Group attributes. It is intended to facilitate testing and demonstration of data extraction processes, while also maintaining confidentiality by using simulated data instead of real user information.

## Prerequisites

To function properly, this script requires the following prerequisites:
1. Python to be installed on the machine running it. The version used for developing this script is 3.12.2. Using a version from 3.6 onwards is recommended.
2. The following modules to be installed:
    a. pandas:
        This library provides data structures and data analysis tools.
    b. configparser:
        This module allows working with INI format configuration files.
    c. Faker:
        This library generates fake data such as names, addresses, phone numbers, etc.
    d. random or random2:
        These modules provide functions for generating random numbers.
    e. math:
        This module provides a set of standard mathematical functions such as trigonometric, exponential, logarithmic functions, etc.
    f. unidecode:
        This module allows transliteration of Unidecode strings into ASCII.

The configparser, random, and math modules are normally included with Python.
The pandas, Faker, and unidecode modules are external packages.

## Features

- Generates random data to simulate extraction of attributes of Active Directory (AD) accounts.
- Helps demonstrate data extraction processes without revealing real user information.
- Allows testing and verification of data coherence between AD accounts and human resources (HR) extractions.
- Highlights anomalies and suggests modifications to improve security on the ADUC server.

## Usage

1. Clone or download the repository to your local machine.
2. Duplicate the parameters_[XX].ini file corresponding to your language and rename it as parameters.ini.
3. Customize the parameters.ini file to define specific settings for the data generation process.
4. Run the HR-ADUC-Datasimulator.py script to generate simulated data.
5. Analyze the output and use it for testing, demonstration, or security improvement purposes.

## License

HR-ADUC-Datasimulator is licensed under the GNU Lesser General Public License v3.0 (LGPL-3.0). You may use, modify, and distribute this script under the terms of the license.

For more details, please see the [LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE) file.

## Contributions

Contributions to this project are welcome. If you encounter any issues, have suggestions for improvements, or want to contribute new features, please open an issue or submit a pull request on GitHub.

## Disclaimer

This script is provided as-is, without any warranty or guarantee of any kind. Use it at your own risk.

## Author

Stéphane-Hervé

## Contact

For questions, feedback, or support, please contact https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues.

