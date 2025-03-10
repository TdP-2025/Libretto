import operator
from dataclasses import dataclass

cfuTot = 180

@dataclass(eq=False) # PER PREVENIRE CHE LA DATACLASS DEFINISCA IL __eq__() O QUALSIASI ALTRO METODO TU VOGLIA
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    # def __eq__(self, other): MEGLIO DI NO!
    #     return (self.materia==other.materia and
    #             self.punteggio==other.punteggio and
    #             self.lode==other.lode)

    def __copy__(self):
        return Voto(self.materia,self.punteggio,self.data,self.lode)

class Libretto:
    def __init__(self, proprietario, voti = None):
        self.proprietario = proprietario
        self.voti = voti if voti is not None else []

    def append(self, voto): # duck!
        if self.hasConflitto(voto) is False and self.hasVoto(voto) is False:
            self.voti.append(voto)
        else:
            raise ValueError("Il voto è già presente")

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr
    def __len__(self):
        return len(self.voti)

    def getVotiByPunti(self,punti,lode):

        """
        restituisce una lista di esami con un punteggio uguale a punti e lode (se applicato)
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: variabile di tipo booleano che indica se è presente la lode
        :return: lista di voti
        """
        votiFiltrati=[]
        for v in self.voti:
            if v.punteggio==punti and v.lode==lode:
                votiFiltrati.append(v)
        return votiFiltrati

    def getVotoByName(self,materia):
        """
        restituisce il voto che lo studente ha preso della materia messa in input
        :param materia: variabile stringa della materia di cui si vuole cercare il voto
        :return: voto materia
        """
        flag=False
        for v in self.voti:
            if v.materia==materia:
                flag=True
                return v
        if not flag:
            raise AttributeError("ERRORE: la materia non presenta voto")

    def calcolaMedia(self):

        """
        restituisce la media dei voti attualmente presenti nel libretto
        :return: valore numerico della media oppure ValueError in caso la lista fosse vuota
        """

        v=[v.punteggio for v in self.voti] # EQUIVALE AD APPENDERE UN CICLO FOR IN UNA LISTA VUOTA E VA A PRENDERE IL PUNTEGGIO
        if len(self.voti)==0:
            raise ValueError("ATTENZIONE: lista esami vuota.") # CONTROLLO CHE LA LISTA NON SIA VUOTA
        return sum(v)/len(v)
        # return math.mean(voti) IMPORTANDO math

    def hasVoto(self,voto):
        '''
        Questo metodo verifica se il libretto contiene già il voto "voto". Due voti sono considerati uguali per questo
        metodo se hanno lo stesso campo materia e lo stesso voto (voto è formato da 2 campi: punteggio e lode)
        :param voto: istanza dell'oggetto di tipo Voto
        :return: True se l'oggetto è stato trovato, False altrimenti
        '''

        for v in self.voti:
            # modo numero 1
            # if v==voto: confronto gli oggetti
            if v.materia==voto.materia and v.punteggio==voto.punteggio and v.lode==voto.lode:
                return True
        return False

    def hasConflitto(self,voto):
        '''
        Questo metodo controlla che il voto "voto" non rappresenti un conflitto con i voti già presenti nel libretto.
        Consideriamo due voti in conflitto quando hanno lo stesso campo materia, ma diversa coppia punteggio lode
        :param voto: istanza dell'oggetto voto
        :return: True se voto è in conflitto, False altrimenti
        '''

        for v in self.voti:
            if v.materia==voto.materia and not (v.punteggio==voto.punteggio and v.lode==voto.lode):
                return True
        return False

    def creaMigliorato(self):
        '''
        Crea un nuovo oggetto libretto in cui sono i voti sono migliorati secondo la seguente logica:
        se il voto è 18<=voto<=24 aggiungo +1
        se il voto è 24<=voto<=29 aggiungo +2
        se il voto è 29 aggiungo +1
        se il voto è 30 rimane 30
        :return: nuovo Libretto
        '''

        nuovo=self.__copy__() # DOBBIAMO CREARE UNA COPIA SE NO MODIFICA I VOTI ORIGINALI
        # TUTTAVIA CONTENGONO GLI STESSI OGGETTI!!!!!!!! CHE VENGONO MODIFICATI
        # for v in self.voti:
        #     nuovo.append(v.__copy__()) # COSI' CREO OGGETTI DIFFERENTI!!!!

        for v in nuovo.voti:
            if 18<=v.punteggio<24:
                v.punteggio+=1
            elif 24 <= v.punteggio < 29:
                v.punteggio += 2
            elif v.punteggio==29:
                v.punteggio=30
        return nuovo

    def __copy__(self):
        '''
        Crea una nuova copia del libretto
        :return: copia libretto
        '''
        nuovo=Libretto(self.proprietario,[])
        for v in self.voti:
            nuovo.append(v.__copy__())
        return nuovo

    def sortByMateria(self):
        self.voti.sort(key=operator.attrgetter("materia")) # IDENTICO DA FARRE voto.materia
        # COSI' NON DOBBIAMO CREARE UNA FUNZIONE FUORI

        # Opzione 1: creo 2 metodi di stampa, una che ordina e poi stampa
        # Opzione 2: creo due metodi che ordinano la lista di self e poi un unico metodo che stampa
        # Opzione 3: creo due metodi che si fanno una copia (deep) autonoma della lista, la ordinano e la restituiscono,
        # poi un altro metodo che si occuperà di stampare
        # Opzione 4: creo una shallow copy di self.voti e la ordino

    def creaLibOrdinatoPerMateria(self):
        '''
        Crea un nuovo oggetto Libretto e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        '''

        nuovo=self.__copy__()
        nuovo.sortByMateria()
        return nuovo

    def creaLibOrdinatoPerVoto(self):
        '''
        Crea un nuovo oggetto Libretto e lo ordina per voto
        :return: nuova istanza dell'oggetto Libretto
        '''

        nuovo=self.__copy__()
        nuovo.voti.sort(key=lambda v: (v.punteggio,v.lode), reverse=True) # lambda OGGETTO:  RESTITUISCE OGGETTO.QUELLO CHE VUOI ORDINARE
        # CON reverse=True INVERTI L'ORDINE
        return nuovo

    def cancellaInferiori(self,punteggio):
        '''
        Questo metodo agisce sul libretto corrente, eliminando tutti i voti inferiori al parametro punteggio
        :param punteggio: intero indicante il valore minimo
        :return: libretto aggiornato
        '''

        # modo 1 EVITARE
        # for v in self.voti:
        #     if v.punteggio < punteggio:
        #         self.voti.remove(v)

        # modo 2 EVITARE
        # for i in range(len(self.voti)):
        #     if self.voti[i].punteggio < punteggio:
        #         self.voti.pop(i)

        # modo 3 FACCIO IL CONTRARIO E AGGIUNGO AD UNA NUOVA LISTA QUELLI CHE RISPETTANO I PARAMETRI
        # nuovo=[]
        # for v in self.voti:
        #     if v.punteggio>=punteggio:
        #         nuovo.append(v)
        # self.voti=nuovo

        #modo 4 COMPRESSO DEL 3
        nuovo=[v for v in self.voti if v.punteggio >= punteggio]
        self.voti=nuovo

def estraiMateria(voto):
    '''
    Questo metodo restituisce il campo materia dell'oggetto voto
    :param voto: istanza della classe Voto
    :return: String rappresentatnte il nome della materia
    '''
    return voto.materia

def testVoto():
    print("Ho usato Voto in maniera standalone")
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
    print(v1)

    mylib = Libretto(None, [v1, v2])
    print(mylib)
    mylib.append(v3)
    print(mylib)

if __name__ == "__main__":
    testVoto()



# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"
