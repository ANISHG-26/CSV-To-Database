import sqlite3
import csv

conn = sqlite3.connect('lexis.db')
cur = conn.cursor()

fname = input('Enter the csv filename: ')
if len(fname) < 1:
    fname = "words.csv"

cur.execute('DROP TABLE IF EXISTS word_table')
cur.execute('''CREATE TABLE word_table (id INTEGER PRIMARY KEY,
		         word TEXT,
		         primary_meaning TEXT,
		         secondary_meaning TEXT,
		         sentence TEXT,
         	     synonym STRING,
		         antonym STRING,
		         date_added DATE
			)''')

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        word = row[0]
        primary_meaning = row[1]
        secondary_meaning = row[2]
        sentence = row[3]
        synonym = row[4]
        antonym = row[5]
        date_added = row[6]

        cur.execute('''INSERT INTO word_table 
            (word,
			primary_meaning,
		    secondary_meaning,
			sentence,
			synonym,
			antonym,
			date_added) 
            VALUES (?,?,?,?,?,?,?)''',
                    (
                        word, primary_meaning, secondary_meaning, sentence, synonym, antonym, date_added

                    ))

        conn.commit()
