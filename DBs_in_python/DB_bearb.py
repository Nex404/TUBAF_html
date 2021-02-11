#Abfrage machen und einzelne Zeilen auswerten
# import sqlite3

# conn = sqlite3.connect("Personal.db")
# cursor = conn.cursor()

# query = "SELECT taet FROM besch;"

# cursor.execute(query)

# row = cursor.fetchone()
# print(f"{type(row)}, {row}")

# # conn.commit()

# conn.close()


#########################################
#Alle Zeilen ausgeben lassen

# import sqlite3

# conn = sqlite3.connect("Personal.db")
# cursor = conn.cursor()

# query = "SELECT DISTINCT taet FROM besch;"

# cursor.execute(query)

# for row in cursor:
#     print(row[0])


# # conn.commit()

# conn.close()


#############################################
# Abteilung einfügen und alle anzeigen lassen

# import sqlite3

# conn = sqlite3.connect("Personal.db")
# cursor = conn.cursor()

# query = "INSERT INTO abt VALUES (50, 'Management', 'Paris');"
# cursor.execute(query)


# query = "SELECT * FROM abt;"
# cursor.execute(query)

# for row in cursor:
#     print(row)


# conn.commit() #das speichern Wichtig wenn die änderung permanent bleiben soll

# conn.close()


#################################################
# Abteilung löschen und alle anzeigen lassen

import sqlite3

conn = sqlite3.connect("Personal.db")
cursor = conn.cursor()

query = "DELETE FROM abt WHERE abtnr=50;"
cursor.execute(query)


query = "SELECT * FROM abt;"
cursor.execute(query)

for row in cursor:
    print(row)


conn.commit() #das speichern Wichtig wenn die änderung permanent bleiben soll

conn.close()