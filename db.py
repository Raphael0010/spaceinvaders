import sqlite3
from random import *

conn = sqlite3.connect('spaceinvaders.db')


def createDB():
    c = conn.cursor()
    c.execute('''CREATE TABLE score (id real, score real)''')
    conn.commit()


def insertScore(score):
    n = randint(1, 100000)
    c.execute("INSERT INTO score VALUES ("+n+","+score+")")
    conn.commit()


def closeDB():
    conn.close()
