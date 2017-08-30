#jagoetze@csc.kth.se

# En klass som repsesentarar en TV apparat
class TvApparat():

# En konstruktor som initierar attribut
    def __init__(self, lista, namn, aktuell_program, aktuell_kanal, aktuell_volym):
        self.lista=lista
        self.namn=namn
        self.program=aktuell_program
        self.kanal=aktuell_kanal
        self.volym=aktuell_volym

# En strängrepresentation av objektet
    def __str__(self):

        return self.namn+':\n'+'Tv-program: '+self.program+'\n'+'Kanal: '+self.kanal+'\n'+'Ljudvolymen: '+str(self.volym)+'\n'

# En metod för att byta kanal
    def bytKanal(self, value):
        self.kanal=self.lista[value-1][0]
        self.program=self.lista[value-1][1]

# En metod för att sänka volymen
    def sank_volym(self):
        if 0 < self.volym:
            self.volym -=1
 

# En metod för att höja volymen
    def hoj_volym(self):
        if self.volym < 10:
            self.volym += 1
      

# EN metod som skapar menyer 
    def menyer(self, value):
        huvudmeny='1. VardagsrumsTV\n2. Köks TV\n3. Avsluta'
        undermeny='1. Byt kanal\n2. Sänk ljudvolym\n3. Höj ljudvolym\n4. Gå till huvudmenyn'
        kanalmeny='1. MTv: Music is life\n2. Tv 3: Har du tur i kärlek?\n3. Svt 1: Pengar är inte allt\n4. Kanal 4: Vem inte vill bli miljonär?'
        if value==4:
            return huvudmeny
        elif value==1:
            return kanalmeny
        elif value== 0:
            return undermeny


    
        
