from networkx.algorithms.bipartite.basic import color

from scuola import Student
from testLibretto import myLib
from view import View
from voto.voto import Libretto, Voto
import flet as ft

# PRENDE LA VIEW E LA ISTANZIA
class Controller:
    def __init__(self,v: View):
        self._view=v
        self._student=Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro",
                animale="civetta", incantesimo="Expecto Patronum")
        self._model=Libretto(self._student,[])
        self._fillLibretto()

    def handleAggiungi(self,e):
        nome=self._view._txtNome.value
        if nome=="":
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Il campo nome non può essere vuoto", color="red")
            )
            self._view._page.update()
            return
        punti=self._view._ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Selezionare un voto", color="red")
            )
            self._view._page.update()
            return

        data=self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(
                ft.Text("Attenzione. Selezionare una data", color="red")
            )
            self._view._page.update()
            return

        if punti=="30L":
            self._model.append(Voto(nome,30,f"{data.year}-{data.month}-{data.day}",True))
        else:
            self._model.append(Voto(nome, int(punti), f"{data.year}-{data.month}-{data.day}", False))

        self._view._txtOut.controls.append(
            ft.Text("Voto aggiunto correttamente",color="green")
        )



    def handleStampa(self, e):
        self._view._txtOut.controls.append(
            ft.Text(str(self._model))
        )
        self._view._page.update()

    def getStudent(self):
        """
        Restituisce informazioni dello studente, usando il __str__ dello studente
        :return:
        """
        return str(self._student)

    def _fillLibretto(self):
        v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
        v2 = Voto("Pozioni", 27, "2022-02-17", True)

        self._model.voti.append(v1)
        self._model.voti.append(v2)
        self._model.voti.append(Voto("Difesa contro le arti oscure", 22, "2022-04-13", False))