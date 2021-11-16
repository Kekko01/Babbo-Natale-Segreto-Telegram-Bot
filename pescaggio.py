from credenziali import *
import random

mydb = connect_databases()
mycursor = mydb.cursor()
query = "SELECT chat_id FROM partecipanti"
mycursor.execute(query)
records = mycursor.fetchall()
mycursor.close()
num_partecipanti = 0
for record in records:
    num_partecipanti += 1
regalo = [""] * num_partecipanti
partecipanti = [""] * num_partecipanti
num = 0
for partecipante in records:
    partecipanti[num] = partecipante[0]
    regalo[num] = partecipante[0]
    num += 1
mischiato = False
debug=0
while not mischiato:
    debug+=1
    mischiato = True
    random.shuffle(regalo)
    for num in range(num_partecipanti):
        if partecipanti[num] == regalo[num]:
            mischiato = False

for num in range(num_partecipanti):
    print(partecipanti[num],regalo[num])
print(debug)

mycursor = mydb.cursor()
for num in range(num_partecipanti):
    query = "UPDATE partecipanti SET destinatario = %s WHERE chat_id = %s"
    val = (regalo[num], partecipanti[num])
    mycursor.execute(query, val)
    mydb.commit()
mycursor.close()
