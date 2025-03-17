from view import View

# PRENDE LA VIEW E LA ISTANZIA
class Controller:
    def __init__(self,v: View):
        self._view=v

    def handleAdd(self,e):
        strIn=self._view._txtIn.value
        if strIn=="":
            self._view._txtOut.value="ERRORE: campo vuoto"
            self._view._page.update()
            return
        self._view._txtOut.value=strIn
        self._view._txtIn.value=""
        self._view._page.update()