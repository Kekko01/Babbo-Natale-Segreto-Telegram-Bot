#!/usr/bin/env python3
'''
@author  Francesco Ciociola - https://kekko01.altervista.org/blog/
@license This software is free - http://www.apache.org/licenses/
'''
from credenziali import *

#Controlla se l'utente è registrato
def check(chat_id):
    sql = "SELECT * FROM partecipanti WHERE chat_id = %s"
    val = (chat_id,)
    mydb = connect_databases()
    mycursor = mydb.cursor()
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    mycursor.close()
    return myresult   

def telegram_chat(msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)
    except:
        print("Errore glance")
        return
    if content_type == "text":
        messaggio=str(msg['text'])
        nome_persona = str(msg['from']['first_name'])
        print("Messaggio da "+ nome_persona + ": " + messaggio)
        if messaggio == "/start":
            telegrambot.sendMessage(chat_id, f"Ciao {nome_persona}, benvenuto in Babbo Natale Segreto!\nSono stato creato da @Kekko01, visita il progetto del bot su: https://github.com/Kekko01/Babbo-Natale-Segreto-Telegram-Bot")
            telegrambot.sendMessage(chat_id,"/info per più informazioni.")
            telegrambot.sendMessage(chat_id, "Se non ti sei ancora iscritto: /iscriviti")
        elif messaggio == "/info":
            telegrambot.sendMessage(chat_id,"Il babbo natale segreto è un gioco di gruppo in cui ogni partecipante, tramite un'estrazione a sorte del nome di ciascun partecipante, farà un regalo alla persona pescata dal sorteggio. Essa però non saprà da chi invece riceverà il regalo.\nL'apertura dei regali avverrà nella settimana dal 20 in poi.")
        elif messaggio == "/iscriviti":
            if iscrizioni_aperte:
                myresult = check(chat_id)
                if myresult == None:
                    telegrambot.sendMessage(chat_id, "Per iscriverti, devi inoltrare il messaggio qui sotto a chi gestisce il bot.")
                    telegrambot.sendMessage(chat_id, str(chat_id))
                else:
                    telegrambot.sendMessage(chat_id, "Sei già iscritto! Per vedere i partecipanti: /chipartecipa")
            else:
                telegrambot.sendMessage(chat_id, "Purtroppo le iscrizioni al Babbo Natale Segreto sono chiuse... mi dispiace.")
        elif messaggio == "/chipartecipa":
            myresult = check(chat_id)
            if myresult != None:          
                sql = "SELECT nome FROM partecipanti ORDER BY nome ASC"
                mydb = connect_databases()
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                mycursor.close()
                num = 0
                messaggio = "Ecco i partecipanti:\n"
                for x in myresult:
                    messaggio += str(x[0]) + "\n"
                    num += 1
                messaggio += f"\nCi sono {num} partecipanti."
                try:
                    telegrambot.sendMessage(chat_id, messaggio)
                except:
                    telegrambot.sendMessage(chat_id, "Errore nel generare la lista partecipanti, inoltra questo messaggio a chi gestisce il bot.")
            else:
                telegrambot.sendMessage(chat_id, "Non sei iscritto al Babbo Natale Segreto")
        elif messaggio == "/destinatario":
            sql = "SELECT destinatario FROM partecipanti WHERE chat_id = %s"
            val = (chat_id,)
            mydb = connect_databases()
            mycursor = mydb.cursor()
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            sql = "SELECT nome FROM partecipanti WHERE chat_id = %s"
            val = (myresult[0],)
            mycursor = mydb.cursor()
            mycursor.execute(sql, val)
            destinatario = mycursor.fetchone()
            mycursor.close()
            try:
                telegrambot.sendMessage(chat_id, f"Dovrai fare il regalo a: {destinatario[0]}")
            except:
                telegrambot.sendMessage(chat_id, f"Non hai una persona a cui fare il regalo, probabilmente non è ancora partito il Babbo Natale Segreto! Se no, contatta chi gestisce il bot.")
            else:
                telegrambot.sendMessage(
                    chat_id, "Non sei iscritto al Babbo Natale Segreto.")

print("In funzione...")
try:
    telegrambot.message_loop(telegram_chat)
except:
    print("Errore nella funzione message_loop")

while True:
    time.sleep(1)

