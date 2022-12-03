from credenziali import *
import random

mydb = connect_databases()
mycursor = mydb.cursor()
query = "SELECT chat_id FROM partecipanti"
mycursor.execute(query)
records = mycursor.fetchall()
mycursor.close()
num_partecipanti = sum(1 for _ in records)
regalo = [""] * num_partecipanti
partecipanti = [""] * num_partecipanti
for num, partecipante in enumerate(records):
    partecipanti[num] = partecipante[0]
    regalo[num] = partecipante[0]
mischiato = False
debug=0
while not mischiato:
    debug+=1
    random.shuffle(regalo)
    mischiato = all(
        partecipanti[num] != regalo[num] for num in range(num_partecipanti)
    )

for num in range(num_partecipanti):
    print(partecipanti[num],regalo[num])
print(debug)

mycursor = mydb.cursor()
query = "UPDATE partecipanti SET destinatario = %s WHERE chat_id = %s"
for num in range(num_partecipanti):
    val = (regalo[num], partecipanti[num])
    mycursor.execute(query, val)
    mydb.commit()
mycursor.close()
