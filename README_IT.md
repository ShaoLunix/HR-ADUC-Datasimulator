# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator è uno script Python progettato per generare dati simulati per gli attributi degli utenti e dei gruppi di Active Directory. È destinato a facilitare i test e la dimostrazione dei processi di estrazione dei dati, mantenendo al contempo la riservatezza utilizzando dati simulati invece di informazioni reali sugli utenti.

## Prerequisiti

Per funzionare correttamente, questo script richiede i seguenti prerequisiti:
1. Che Python sia installato sulla macchina che lo esegue. La versione utilizzata per lo sviluppo di questo script è la 3.12.2. È consigliabile utilizzare una versione a partire dalla 3.6.
2. Che siano installati i seguenti moduli:
    a. pandas:
        Questa libreria fornisce strutture dati e strumenti di analisi dati.
    b. configparser:
        Questo modulo consente di lavorare con file di configurazione in formato INI.
    c. Faker:
        Questa libreria genera dati falsi come nomi, indirizzi, numeri di telefono, ecc.
    d. random o random2:
        Questi moduli forniscono funzioni per generare numeri casuali.
    e. math:
        Questo modulo fornisce un insieme di funzioni matematiche standard come funzioni trigonometriche, esponenziali, logaritmiche, ecc.
    f. unidecode:
        Questo modulo consente la traslitterazione di stringhe Unidecode in ASCII.

I moduli configparser, random e math sono normalmente inclusi in Python.
I moduli pandas, Faker e unidecode sono pacchetti esterni.

## Caratteristiche

- Genera dati casuali per simulare l'estrazione degli attributi degli account Active Directory (AD).
- Aiuta a dimostrare i processi di estrazione dei dati senza rivelare informazioni reali sugli utenti.
- Consente di testare e verificare la coerenza dei dati tra gli account AD ed le estrazioni delle risorse umane (HR).
- Evidenzia anomalie e suggerisce modifiche per migliorare la sicurezza sul server ADUC.

## Utilizzo

1. Clonare o scaricare il repository sul proprio computer locale.
2. Duplica il file parameters_[XX].ini relativo alla tua lingua e rinominalo semplicemente in parameters.ini.
3. Personalizzare il file parameters.ini per definire impostazioni specifiche per il processo di generazione dei dati.
4. Eseguire lo script HR-ADUC-Datasimulator.py per generare dati simulati.
5. Analizzare l'output e utilizzarlo per scopi di test, dimostrazione o miglioramento della sicurezza.

## Licenza

HR-ADUC-Datasimulator è distribuito con licenza GNU Lesser General Public License v3.0 (LGPL-3.0). È possibile utilizzare, modificare e distribuire questo script secondo i termini della licenza.

Per maggiori dettagli, consultare il file [LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE).

## Contributi

I contributi a questo progetto sono benvenuti. Se riscontri problemi, hai suggerimenti per miglioramenti o desideri contribuire con nuove funzionalità, apri una segnalazione o invia una richiesta di pull su GitHub.

## Avvertenza

Questo script viene fornito "così com'è", senza alcuna garanzia o garanzia di alcun tipo. Usalo a tuo rischio.

## Autore

Stéphane-Hervé

## Contatto

Per domande, feedback o supporto, contattare https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues.
