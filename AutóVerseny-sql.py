''' ﻿autoverseny.csv
csapat;          versenyzo;     eletkor;     palya;             korido;     kor
Versenylovak;    Fürge Ferenc;    29;      Gran Prix Circuit;   00:01:11;    1
'''
import sqlite3

def sql(c, sql_parancs, *args):
    c.execute(sql_parancs, *args)
    return c.fetchall()

conn = sqlite3.connect('data.db')
c = conn.cursor()

# 2.
sql(c," DROP TABLE IF EXISTS tb ")
sql(c,"""
    CREATE TABLE IF NOT EXISTS tb
    (csapat    TEXT,
    versenyzo  TEXT,
    eletkor    INTEGER,
    palya      TEXT,
    korido     TEXT,
    kor        INTEGER,
    sec        INTEGER)
    """)
conn.commit()

with open('autoverseny.csv', encoding='utf-8-sig') as f:
    fejlec = f.readline().strip()
    for sor in f:
        csapat, versenyzo, eletkor, palya, korido, kor = sor.strip().split(';')
        óra, perc, másodperc = korido.split(':')
        sec = int(óra)*3600 + int(perc)*60 + int(másodperc)
        sql(c," INSERT INTO tb VALUES (?,?,?,?,?,?,?) ", ( csapat, versenyzo, eletkor, palya, korido, kor, sec ) )
conn.commit()

# 3. Hány sornyi adat van a forrásállományban?

darab = sql(c, " SELECT COUNT() FROM tb  ")[0][0]     
print( f'3. feladat: { darab } ' )

# 4. Fürge Ferenc a Gran Prix Circuit pályán futott 3. körét hány másodperc alatt teljesítette?

másodperc = sql(c, " SELECT sec FROM tb WHERE versenyzo == 'Fürge Ferenc' AND palya == 'Gran Prix Circuit' AND kor == 3 ")[0][0]
print( f'4. feladat: { másodperc } másodperc ' )

#5. Kérjen be egy nevet.

print( f'5. feladat:      ' )
print( f'Kérem egy versenyző nevét:')
nev = input()

# 6. A {nev} versenyző hol futotta a leggyorsabb körét?

palya, korido = sql(c, " SELECT palya, MIN(korido) FROM tb WHERE versenyzo == ? ", (nev,) )[0]

if palya == None:
    print( f'6. feladat: Nincs ilyen versenyzo az állományban' )
else:    
    print( f'6. feladat: { palya },  {korido} ' )




