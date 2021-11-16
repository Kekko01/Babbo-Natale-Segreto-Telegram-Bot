# Babbo Natale Segreto: Telegram Bot
 Bot Telegram per creare e gestire un Babbo Natale Segreto con amici ecc.

 [![GitHub issues](https://img.shields.io/github/issues/Kekko01/Babbo-Natale-Segreto-Telegram-Bot)](https://github.com/Kekko01/Babbo-Natale-Segreto-Telegram-Bot/issues)
[![GitHub forks](https://img.shields.io/github/forks/Kekko01/Babbo-Natale-Segreto-Telegram-Bot)](https://github.com/Kekko01/Babbo-Natale-Segreto-Telegram-Bot/network)
[![GitHub stars](https://img.shields.io/github/stars/Kekko01/Babbo-Natale-Segreto-Telegram-Bot)](https://github.com/Kekko01/Babbo-Natale-Segreto-Telegram-Bot/stargazers)
[![GitHub license](https://img.shields.io/github/license/Kekko01/Babbo-Natale-Segreto-Telegram-Bot)](https://github.com/Kekko01/Babbo-Natale-Segreto-Telegram-Bot/blob/main/LICENSE)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FKekko01%2FBabbo-Natale-Segreto-Telegram-Bot)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FKekko01%2FBabbo-Natale-Segreto-Telegram-Bot)
## Che cos'è?
Il Babbo Natale Segreto è un gioco di gruppo in cui ogni partecipante, tramite un'estrazione a sorte del nome di ciascun partecipante, farà un regalo alla persona pescata dal sorteggio. Essa però non saprà da chi invece riceverà il regalo.
L'apertura dei regali avverrà nella settimana dal 20 in poi.
## Come scaricare e configurare bot
1. Scarica il pacchetto di Python da: https://github.com/Kekko01/Babbo-Natale-Segreto-Telegram-Bot/archive/refs/heads/main.zip
2. Estrailo ed e nella cartella
3. Modificare il file **credenziali.py** con le informazioni del Database e con il token di Telegram
	```python
	telegrambot = telepot.Bot("") #token del bot
	host="", #indirizzo del database
	user="", #utente del database
	passwd="", #password del database
	database="bns" #nome del database
	```
4. Creare un database su MySQL o simili (MariaDB ecc) col nome `bns` ed importare il file `bns.sql`
5. Installare da pip telepot e mysql.connector tramite i comandi:
	```bash
	pip install telepot
	pip install mysql-connector-python
	```
6. Avviare il bot con il comando:
	```bash
	python bot.py
	```


------------

# Come gestire il Babbo Natale Segreto
Quando si avvia il bot, il bot puo ricevere già le iscrizioni.
#### Come gestisco le iscrizioni?
Chi parteciperà dovrà inviare il comando /iscriviti e il bot ti risponderà con il suo ID, lui ti inoltrerà questo messaggio e dovrai inserirlo nel database, nella tabella *partecipanti*, in *chat_id* metterai l'ID che ti invierà la persona da iscrivere, e in *nome* il nome della persona.
#### Come faccio a chiudere le iscrizioni?
Molto semplice, in **credenziali.py** c'è la variabile *iscrizioni_aperte*, basta cambiarlo con **False**,
#### Come faccio a fare l'estrazione
Basterà lanciare **pescaggio.py**.
```bash
python pescaggio.py
```
#### Come si fa a controllare a chi bisogna fare il regalo?
Basterà fare **/destinario**.
#### Come faccio ad inviare un messaggio ai partecipanti del Babbo Natale Segreto?
Basterà usare il file **inviadestinatario.py** e scrivere il messaggio alla riga 11.

------------

# FAQ
#### Come installo Python?
Basta andare su https://www.python.org/downloads/ e scaricare la versione per il tuo computer (io consiglio installare python 3.9.x, e se avete Windows 10 o Windows 11 dallo [Store di Microsoft](https://www.microsoft.com/store/productId/9P7QFQMJRFP7 "Store di Microsoft")).
#### Come installo un Database MySQL?
Ci sono varie strade, se avete un Raspberry e volete usarlo per il bot potete installarlo lì, sennò puoi usare [XAMPP](https://www.apachefriends.org/download.html "XAMPP").
#### Come creo il bot su Telegram?
Telegram ha scritto una guida breve qui: https://core.telegram.org/bots#3-how-do-i-create-a-bot (è in inglese ma è molto semplice).
#### Che comandi devo inserire da Bot Father?
```
start - Mostra il messaggio di avvio
info - Mostra le info sull'attività
iscriviti - Iscriviti a Babbo Natale Segreto!
chipartecipa - Vedi la lista delle persone che devono partecipare!
destinatario - Vedi a chi devi fare il regalo
```
#### Ho un problema, cose posso fare?
Molto semplice, basta segnalarlo o trovarlo su: https://github.com/Kekko01/Babbo-Natale-Segreto-Telegram-Bot/issues.