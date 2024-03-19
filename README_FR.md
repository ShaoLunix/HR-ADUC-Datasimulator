# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator est un script Python conçu pour générer des données simulées pour les attributs des utilisateurs et des groupes Active Directory. Il vise à faciliter les tests et la démonstration des processus d'extraction de données, tout en maintenant la confidentialité en utilisant des données simulées au lieu d'informations réelles sur les utilisateurs.

## Pré-requis

Pour fonctionner correctement, ce script nécessite en pré-requis que :
1. Python soit installé sur la machine l'exécutant. La version ayant servi à l'élaboration de ce script est la 3.12.2. L'utilisation d'une version à partir de la 3.6 est recommandée.
2. Les modules ci-dessous soient installés :
	a. pandas :
		cette bibliothèque fournit des structures de données et outils d'analyse de données.
	b. configparser : 
		ce module permet de travailler avec des fichiers de configuration au format INI.
	c. Faker
		cette bibliothèque génère des données factices telles que des noms, des adresses, des numéros de téléphone, ...
	d. random ou random2
		ces modules fournissent des fonctions pour générer des nombres aléatoires.
	e. math
		ce module fournit un ensemble de fonctions mathématiques standard telles que les fonctions trigonométriques, exponentielles, logarithmiques, ...
	f. unidecode
		ce module permet de translittérer les chaînes de caractères Unidecode en ASCII.
		
Les modules configparser, random et math sont normalement fournis en standard dans Python.
Les modules pandas, Faker et unidecode sont des packages externes.


## Fonctionnalités

- Génère des données aléatoires pour simuler l'extraction des attributs des comptes Active Directory (AD).
- Aide à démontrer les processus d'extraction de données sans révéler d'informations réelles sur les utilisateurs.
- Permet de tester et de vérifier la cohérence des données entre les comptes AD et les extractions des ressources humaines (RH).
- Met en évidence les anomalies et suggère des modifications pour améliorer la sécurité sur le serveur ADUC.

## Utilisation

1. Clonez ou téléchargez le référentiel sur votre machine locale.
2. Dupliquez le fichier parameters_[XX].ini correspondant à votre langue et renommez-le parameters.ini.
3. Personnalisez le fichier parameters.ini pour définir des paramètres spécifiques pour le processus de génération de données.
4. Exécutez le script HR-ADUC-Datasimulator.py pour générer des données simulées.
5. Analysez la sortie et utilisez-la à des fins de test, de démonstration ou d'amélioration de la sécurité.

## Licence

HR-ADUC-Datasimulator est sous licence GNU Lesser General Public License v3.0 (LGPL-3.0). Vous pouvez utiliser, modifier et distribuer ce script selon les termes de la licence.

Pour plus de détails, veuillez consulter le fichier [LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE).

## Contributions

Les contributions à ce projet sont les bienvenues. Si vous rencontrez des problèmes, avez des suggestions d'amélioration ou souhaitez contribuer de nouvelles fonctionnalités, veuillez ouvrir un problème ou soumettre une demande de fusion sur GitHub.

## Avertissement

Ce script est fourni tel quel, sans aucune garantie ou garantie d'aucune sorte. Utilisez-le à vos propres risques.

## Auteur

Stéphane-Hervé

## Contact

Pour des questions, des commentaires ou du support, veuillez contacter https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues.
