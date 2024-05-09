import wx
from ClasesFunciones import *

#Definicion de funciones/clases extra

class Ventana(wx.Frame):
    def __init__(self):
        super(Ventana, self).__init__(None, title="BlackJack", size=(1080,720))
        self.Show(True)



#Definimos el main para ejecutar la aplicacion
def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()
    return None

main()

