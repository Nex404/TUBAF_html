# #Abfrage machen und einzelne Zeilen auswerten
# import sqlite3

# conn = sqlite3.connect("Personal.db")
# cursor = conn.cursor()

# query = "Select Distinct taet From besch"

# cursor.execute(query)

# row = cursor.fetchone()
# print(f"{type(row)}, {row}")

# # conn.commit falls wir Änderungen gemacht haben

# conn.close()


#############################################################

#Alle Zeilen ausgeben
# import sqlite3

# conn = sqlite3.connect("Personal.db")
# cursor = conn.cursor()

# query = "Select Distinct taet From besch"

# cursor.execute(query)

# print("Es gibt folgende Tätigkeiten unter den Beschäftigten:")
# for row in cursor:
#     print(row[0])

# conn.close()

# #####################################################################

# #Abteilung einfügen und alle anzeigen

import sqlite3

conn = sqlite3.connect("Personal.db")
cursor = conn.cursor()

query = "Insert Into abt Values (50, 'Management', 'Paris')"
cursor.execute(query)

query = "Select * From abt"
cursor.execute(query)
for row in cursor:
    print(row)
    
conn.commit() # Wichtig!

conn.close()


# ##############################################################

# #Abteilung löschen und alle anzeigen

# import sqlite3

# conn = sqlite3.connect("Personal.db")
# cursor = conn.cursor()

# query = "Delete From abt Where abtnr=50"
# cursor.execute(query)

# query = "Select * From abt"
# cursor.execute(query)
# for row in cursor:
#     print(row)
    
# conn.commit() # Wichtig!

# conn.close()