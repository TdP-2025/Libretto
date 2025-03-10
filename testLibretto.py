from main import mylib
from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro",
                animale="civetta", incantesimo="Expecto Patronum")
myLib=Libretto(Harry,[])
v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
v2 = Voto("Pozioni", 27, "2022-02-17", True)

myLib.append(v1)
myLib.append(v2)
myLib.append(Voto("Difesa contro le arti oscure", 22, "2022-04-13", False))

myLib.calcolaMedia()
votiFiltrati=myLib.getVotiByPunti(27,False)
print(votiFiltrati)
votoTrasfigurazione=myLib.getVotoByName("Trasfigurazione")
print(votoTrasfigurazione)
print()

print("---------------------------------------------")
print("Test voto già presente\n")
print(mylib.hasVoto(v1))
print(mylib.hasVoto(Voto("Aritmanzia",30,"2023-07-10",False)))
print()

print("---------------------------------------------")
print("Test conflitto\n")
print(mylib.hasConflitto(Voto("Pozioni", 22, "2022-02-17", True)))
print(mylib.hasConflitto(v1))
print()

mylib.append(Voto("Aritmanzia",30,"2023-07-10",False))
# myLib.append(v1) DA ERRORE
print("---------------------------------------------")
print("Libretto migliorato\n")
print(mylib.creaMigliorato())
print("---------------------------------------------")
print("Libretto originale\n")
print(mylib)
print("---------------------------------------------")
print("Test ordinamento MATERIA\n")
ordinato1=myLib.creaLibOrdinatoPerMateria()
print(ordinato1)
print("---------------------------------------------")
print("Test ordinamento VOTO \n")
ordinato2=myLib.creaLibOrdinatoPerVoto()
print(ordinato2)
print("---------------------------------------------")
print("Test cancella voti \n")
ordinato2.cancellaInferiori(23)
print((ordinato2))

