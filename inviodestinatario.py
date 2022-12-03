from credenziali import *
mydb = connect_databases()
sql = "SELECT * FROM partecipanti"
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    try:
        time.sleep(2)
        telegrambot.sendMessage(x[0], f"Ciao {x[1]}, questo è un messaggio prova! 👌👌")
    except:
        print(x[0])
mycursor.close()
