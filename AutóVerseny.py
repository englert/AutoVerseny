''' autoverseny.csv
csapat;versenyzo;eletkor;palya;korido;kor
Versenylovak;Fürge Ferenc;29;Gran Prix Circuit;00:01:11;1
'''
# 2.
class Verseny:
    def __init__(self, sor):
        s                 = sor.strip().split(';')
        csapat,versenyzo,eletkor,palya,korido,kor = s
        self.csapat       = csapat
        self.versenyzo    = versenyzo
        self.eletkor      = int(eletkor)
        self.palya        = palya
        self.korido       = korido
        self.kor          = int(kor)
    def köridő_másodpercben(self):
        óra, perc, másodperc     = [ int(i)  for i in self.korido.split(':') ]
        return  3600 * óra + 60 * perc + másodperc

with open( 'autoverseny.csv', 'r', encoding='utf-8-sig' ) as f:
    fejléc = f.readline()
    mátrix = [ Verseny( sor ) for sor in f ]

# 3. Hány sornyi adat van a forrásállományban?

print( f'3. feladat: { len( mátrix ) }')

# 4. Fürge Ferenc a Gran Prix Circuit pályán futott 3. körét hány másodperc alatt teljesítette?

t = [sor.köridő_másodpercben() for sor in mátrix if sor.versenyzo == 'Fürge Ferenc' and sor.palya == 'Gran Prix Circuit' and sor.kor == 3 ][0]
print( f'4. feladat: { t } másodperc' )

# 5. Kérjen be egy nevet.

print( f'5. feladat:')
print( f'Kérem egy versenyző nevét:' )
név = input()

# 6. A {nev} versenyző hol futotta a leggyorsabb körét?

if név not in  [ sor.versenyzo for sor in mátrix ]:
    print( f'    Nincs ilyen versenyző az állományban!' )
else:
    res = { sor.köridő_másodpercben() : sor for sor in mátrix if sor.versenyzo == név }
    ido, sor = min(res.items())
    print( f'6. feladat: {sor.palya}, {sor.korido}')
