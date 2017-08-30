# Importera klassen TVApparat
from TVclass import TvApparat


 # en funktion för att spara aktuellt tillstånd i en fil
def sparFil(filnamn):
    fil=open(filnamn, 'w')
    lista=[tv.namn, tv.program, tv.kanal, str(tv.volym)]
    for element in lista:
        fil.write(element+ '\n')
    fil.close()

# en funktion för att öppna filen och läsa av den
def lasFil(filnamn):
    fil=open(filnamn, 'r')
    tvApparatNamn=fil.readline().strip()
    program=fil.readline().strip()
    kanal=fil.readline().strip()
    volym=int(fil.readline().strip())
    fil.close()
    return tvApparatNamn, program, kanal, volym
    

#Hanterar alla undermenyer
def main(indata_undermeny, filnamn):
    text='Välj:'
    while True:
        if indata_undermeny==1:
            print(tv.menyer(indata_undermeny))
            while True:
                try:
                    start_kanal=int(input(text))
                    if 1 <= start_kanal <= 4:                        
                        print()
                        tv.bytKanal(start_kanal)   
                        print(tv)
                        
                        break
                    else:
                        text='Fel val, försök igen:'
                except:
                    text='Fel val, försök igen:'
        elif indata_undermeny==2:
            if tv.volym <= 0:
                print('***Minimal volym är 0!***')
            else:
                tv.sank_volym()
            print(tv)
        elif indata_undermeny==3:
            if tv.volym >= 10:
                print('***Maximal volym är 10!***')
            else:
                tv.hoj_volym()
            print(tv) 
        elif indata_undermeny==4:
            sparFil(filnamn)
            print('1. VardagsrumsTV\n2. Köks TV\n3. Avsluta')
            break

        print(tv.menyer(0))
        text='Välj:'
        while True:
            try:
                indata_undermeny=int(input(text))
                if 1 <= indata_undermeny <= 4: 
                    print()
                    break
                else:
                    text='Fel val, försök igen:'                        
            except:
                text='Fel val, försök igen:'
    
#hanterar huvudmenyn
def huvudmeny(filnamn):
     print(tv.menyer(0))
     text='Välj:'
     while True:
         try:
             indata_undermeny=int(input(text))
             if 1 <= indata_undermeny <=4:
                print()
                main(indata_undermeny, filnamn)
                text='Välj:'
                break
             else:
                text='Fel val, försök igen:'
         except:
             text='Fel val, försök igen:'

#*************************************** Huvudprogram ***************************************


if __name__=='__main__':
    print('***Välkommen till TV-simulatorn, vi har två TV-apparater som kan användas i simuleringen***')

# köra program
    print('1. VardagsrumsTV\n2. Köks TV\n3. Avsluta')
    lista=[('MTv', 'Music is life'), ('Tv 3', 'Har du tur i kärlek?'), ('Svt 1', 'Pengar är inte allt'), ('Kanal 4', 'Vem vill inte bli miljonär?')]
    text='Välj:'
    while True:
        try:
            indata_huvudmeny=int(input(text))
            if indata_huvudmeny==1:
                print()
                filnamn='vardagsrumsTV.txt'
                aktuell_tvApparat, aktuell_program, aktuell_kanal, aktuell_volym=lasFil(filnamn)
                tv=TvApparat(lista, aktuell_tvApparat, aktuell_program, aktuell_kanal, aktuell_volym)
                print(tv)
                huvudmeny(filnamn)
                text='Välj:'
            elif indata_huvudmeny==2:
                print()
                filnamn='köksTV.txt'
                aktuell_tvApparat, aktuell_program, aktuell_kanal, aktuell_volym=lasFil(filnamn)
                tv=TvApparat(lista, aktuell_tvApparat, aktuell_program, aktuell_kanal, aktuell_volym)
                print(tv)
                huvudmeny(filnamn)
                text='Välj:'
            elif indata_huvudmeny==3:
                print()
                print('Simuleringen avslutas')
                text='Välj:'
                break
            else:
                text='Fel val, försök igen:'
        except:
            text='Fel val, försök igen:'
        
            

    

