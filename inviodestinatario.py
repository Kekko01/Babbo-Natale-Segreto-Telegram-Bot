from credenziali import *
mydb = connect_databases()
sql = "SELECT * FROM partecipanti"
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:

    time.sleep(2)
    sql = "SELECT nome FROM partecipanti WHERE chat_id=" + str(x[2])
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult2 = mycursor.fetchone()
    telegrambot.sendMessage(x[0], "Allora " + x[1] + " devi fare il regalo a " + myresult2[0])

mycursor.close()
