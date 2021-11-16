import telepot, time, mysql.connector
telegrambot = telepot.Bot("") #token del bot

def connect_databases():
  mydb = mysql.connector.connect(
    host="", #indirizzo del database
    user="", #utente del database
    passwd="", #password del database
    database="bns" #nome del database
  )
  return mydb

#Informazioni riguardo il bot
iscrizioni_aperte = True #True se le iscrizioni sono aperte, False se le iscrizioni sono chiuse
