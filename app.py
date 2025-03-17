# FILE CHIAMATO App SOLO PERCHE' GIA' PRESENTE UN FILE main

import flet as ft
from view import View
from controller import Controller

def main(page:ft.Page):
    v=View(page) # CREA UNA NUOVA VIEW A CUI PASSA COME ARGOMENTO LA PAGINA
    c=Controller(v) # CREA UN NUOVO CONTROLLER A CUI PASSA LA VIEW
    v.setController(c) # LO SETTA
    v.loadInterface() # COMPLETA LA STRUTTURA MVC

ft.app(target=main)