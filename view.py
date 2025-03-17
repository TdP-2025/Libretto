import flet as ft

# CREA UN CONTROLLER VUOTO E HA UN METODO SET CONTROLLER
# PRENDE UNA PAGINA DA FUORI LA IMPOSTA COME INTERNA
class View:
    def __init__(self,page:ft.Page):
        self._txtOut = None
        self._btnIn = None
        self._txtIn = None
        self._controller = None
        self._page=page # VARIABILI UNDERSCORE PERCHE' VORREI CHE NESSUNO ME LE TOCCHI

    def loadInterface(self):
        """
        In questo metodo definiamo e carichiamo tutti i controlli dell'interfaccia e oggetti grafici,
        tutto il resto va nel controller.
        :return:
        """
        self._txtIn=ft.TextField(label="Inserisci nome") # self._ PER ESSERE ISTANZIABILI NELLA CLASSE CONTROLLER
        self._btnIn=ft.ElevatedButton("Aggiungi", on_click=self._controller.handleAdd)
        row=ft.Row(controls=[self._txtIn,self._btnIn])
        self._txtOut=ft.Text("")

        self._page.add(row,self._txtOut)

    def setController(self, c):
        self._controller=c