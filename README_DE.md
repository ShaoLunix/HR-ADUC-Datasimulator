# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator ist ein Python-Skript, das simuliert Daten für die Attribute von Active Directory-Benutzern und Gruppen generiert. Es soll das Testen und die Demonstration von Datenextraktionsprozessen erleichtern und gleichzeitig die Vertraulichkeit durch Verwendung simulierter Daten anstelle von echten Benutzerinformationen wahren.

## Voraussetzungen

Damit dieses Skript ordnungsgemäß funktioniert, sind folgende Voraussetzungen zu erfüllen:
1. Python muss auf dem ausführenden Computer installiert sein. Die für die Entwicklung dieses Skripts verwendete Version ist 3.12.2. Es wird empfohlen, eine Version ab 3.6 zu verwenden.
2. Die folgenden Module müssen installiert sein:
	a. pandas:
		Diese Bibliothek bietet Datenstrukturen und Analysetools für Daten.
	b. configparser:
		Dieses Modul ermöglicht die Arbeit mit INI-Format-Konfigurationsdateien.
	c. Faker:
		Diese Bibliothek generiert fiktive Daten wie Namen, Adressen, Telefonnummern usw.
	d. random oder random2:
		Diese Module bieten Funktionen zum Generieren von Zufallszahlen.
	e. math:
		Dieses Modul bietet eine Reihe von Standardmathematikfunktionen wie trigonometrische, exponentielle, logarithmische Funktionen usw.
	f. unidecode:
		Dieses Modul ermöglicht die Transliteration von Unidecode-Zeichenfolgen in ASCII.

Die Module configparser, random und math sind normalerweise in Python enthalten.
Die Module pandas, Faker und unidecode sind externe Pakete.

## Funktionen

- Generiert zufällige Daten zur Simulation der Extraktion von Attributen von Active Directory (AD)-Konten.
- Hilft bei der Demonstration von Datenextraktionsprozessen, ohne echte Benutzerinformationen preiszugeben.
- Ermöglicht das Testen und Überprüfen der Datenkohärenz zwischen AD-Konten und Extraktionen aus den Personalressourcen (HR).
- Markiert Anomalien und schlägt Änderungen vor, um die Sicherheit auf dem ADUC-Server zu verbessern.

## Verwendung

1. Klonen oder laden Sie das Repository auf Ihren lokalen Computer herunter.
2. Duplizieren Sie die parameters_[XX].ini-Datei Ihrer Sprache und benennen Sie sie einfach in parameters.ini um.
3. Passen Sie die parameters.ini-Datei an, um spezifische Einstellungen für den Daten-Generierungsprozess festzulegen.
4. Führen Sie das Skript HR-ADUC-Datasimulator.py aus, um simulierte Daten zu generieren.
5. Analysieren Sie die Ausgabe und verwenden Sie sie zu Test-, Demonstrations- oder Sicherheitsverbesserungszwecken.

## Lizenz

HR-ADUC-Datasimulator steht unter der GNU Lesser General Public License v3.0 (LGPL-3.0). Sie dürfen dieses Skript gemäß den Bestimmungen der Lizenz verwenden, ändern und verteilen.

Weitere Informationen finden Sie in der Datei [LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE).

## Beiträge

Beiträge zu diesem Projekt sind willkommen. Wenn Sie auf Probleme stoßen, Vorschläge zur Verbesserung haben oder neue Funktionen beitragen möchten, öffnen Sie bitte ein Problem oder senden Sie eine Pull-Anfrage auf GitHub.

## Haftungsausschluss

Dieses Skript wird "wie es ist" bereitgestellt, ohne jegliche Garantie oder Gewährleistung jeglicher Art. Verwenden Sie es auf eigene Gefahr.

## Autor

Stéphane-Hervé

## Kontakt

Bei Fragen, Feedback oder Unterstützungsanfragen kontaktieren Sie bitte https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues.
