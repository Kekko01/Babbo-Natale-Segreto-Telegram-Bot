from credenziali import *
mydb = connect_databases()
sql = "SELECT * FROM partecipanti"
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    try:
        time.sleep(2)
        telegrambot.sendMessage(x[0], "Ciao " + x[1] + ", questo รจ un messaggio prova! ๐๐")
    except:
        print(x[0])
mycursor.close()
