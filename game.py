"""Proyecto creado por Javier Calvo Porro, estudiante de Ingenieria Informática en la UVa. 2023/24
El código ha sido generado por mí (sin usar wxGlade) ya que me parecía más comodo"""

import wx
from ClasesFunciones import *

#Creacion de las clases/funciones para la interfaz

#Menu estático izquierdo
class LateralEstatico(wx.Panel):
    def __init__(self, parent):
        super(LateralEstatico, self).__init__(parent)
        
        # Creamos un sizer vertical para organizar los elementos
        sizer_lat_estatic = wx.BoxSizer(wx.VERTICAL)

        #Selección de Modo de Juego
        fieldset_mode = wx.StaticBox(self, label="Modo de Juego")
        sizer_mode = wx.StaticBoxSizer(fieldset_mode, wx.HORIZONTAL)
        self.manual = wx.RadioButton(self, label="Manual", style=wx.RB_GROUP)
        self.automatico = wx.RadioButton(self, label="Automatico")
        sizer_mode.Add(self.manual, 0, wx.TOP|wx.LEFT|wx.BOTTOM, 0)
        sizer_mode.Add(self.automatico, 0, wx.LEFT, 40)

        # Retardo
        sizer_retardo = wx.BoxSizer(wx.HORIZONTAL)
        self.label_retardo = wx.StaticText(self, label="Retardo: ")
        self.input_retardo = wx.TextCtrl(self, value="25", size=(60, 20), style=wx.TE_PROCESS_ENTER | wx.TE_RIGHT)
        self.label_ms = wx.StaticText(self, label=" ms.")
        sizer_retardo.Add(self.label_retardo, 0, wx.TOP|wx.LEFT, 4)
        sizer_retardo.Add(self.input_retardo, 0, wx.TOP, 2)
        sizer_retardo.Add(self.label_ms, 0, wx.TOP, 4)

        #Seleccion de la accion de la Jugada
        fieldset_accion = wx.StaticBox(self, label="Jugada")
        sizer_accion = wx.StaticBoxSizer(fieldset_accion, wx.VERTICAL)
        self.pedir = wx.Button(self, label="Pedir")
        self.doblar = wx.Button(self, label="Doblar")
        self.cerrar = wx.Button(self, label="Cerrar")
        self.separar = wx.Button(self, label="Separar")
        self.pedir.SetMinSize((0, 25))
        sizer_accion.Add(self.pedir, 1, wx.EXPAND|wx.ALL, 2)
        sizer_accion.Add(self.doblar, 1, wx.EXPAND|wx.ALL, 2)
        sizer_accion.Add(self.cerrar, 1, wx.EXPAND|wx.ALL, 2)
        sizer_accion.Add(self.separar, 1, wx.EXPAND|wx.ALL, 2)

        # Menu restante
        menu_info = wx.BoxSizer(wx.VERTICAL)

        #Partidas
        font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        fieldset_partidas = wx.StaticBox(self, label="Partidas")
        sizer_partidas = wx.StaticBoxSizer(fieldset_partidas, wx.VERTICAL)
        self.texto_partidas = wx.StaticText(self, label="0")
        self.texto_partidas.SetFont(font)
        sizer_partidas.Add(self.texto_partidas, 0, wx.ALIGN_CENTER)

        fieldset_balance = wx.StaticBox(self, label="Balance Global")
        slizer_balance = wx.StaticBoxSizer(fieldset_balance, wx.VERTICAL)
        self.texto_balance = wx.StaticText(self, label="1")
        self.texto_balance.SetFont(font)
        slizer_balance.Add(self.texto_balance, 0, wx.ALIGN_CENTER)

        fieldset_bal_partida = wx.StaticBox(self, label="Balance Partida Actual")
        slizer_bal_partida = wx.StaticBoxSizer(fieldset_bal_partida, wx.VERTICAL)
        self.texto_bal_partida = wx.StaticText(self, label="2")
        self.texto_bal_partida.SetFont(font)
        slizer_bal_partida.Add(self.texto_bal_partida, 0, wx.ALIGN_CENTER)

        fieldset_cuenta_atras = wx.StaticBox(self, label="Cuenta Atras")
        slizer_cuenta_atras = wx.StaticBoxSizer(fieldset_cuenta_atras, wx.VERTICAL)
        self.texto_cuenta_atras = wx.StaticText(self, label="3")
        self.texto_cuenta_atras.SetFont(font)
        slizer_cuenta_atras.Add(self.texto_cuenta_atras, 0, wx.ALIGN_CENTER)

        menu_info.Add(sizer_partidas, 0, wx.TOP|wx.EXPAND, 5)
        menu_info.Add(slizer_balance, 0, wx.TOP|wx.EXPAND, 5)
        menu_info.Add(slizer_bal_partida, 0, wx.TOP|wx.EXPAND, 5)
        menu_info.Add(slizer_cuenta_atras, 0, wx.TOP|wx.EXPAND, 5)
        

        #Añadimos al sizer_lateral nuestros paneles
        sizer_lat_estatic.Add(sizer_mode, 0, wx.ALL|wx.EXPAND, 10)
        sizer_lat_estatic.Add(sizer_retardo, 0, wx.ALL|wx.EXPAND, 10)
        sizer_lat_estatic.Add(sizer_accion, 0, wx.ALL|wx.EXPAND, 10)
        sizer_lat_estatic.Add(menu_info, 0, wx.ALL|wx.EXPAND, 10)

        self.SetSizer(sizer_lat_estatic)

    def cambiar_retardo(self, nuevo_valor):
        self.input_retardo.SetValue(str(nuevo_valor))    

# Menu Dinamico de mi Ventana
class MenuJuego(wx.ScrolledWindow):
    def __init__(self, parent):
        super(MenuJuego, self).__init__(parent)

        self.sizer_menu_juego = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer_menu_juego)

        #Paneles donde van las cartas
        wxPanels = []


#Ventana princiapl (juego)
class Ventana(wx.Frame):
    def __init__(self):
        super(Ventana, self).__init__(None, title="BlackJack", size=(1440,720))
                
        # Creamos el Panel Lateral (Estatico) y el Panel Derecho (Dinamico)
        panel_estatico = LateralEstatico(self)
        menu_juego = MenuJuego(self)

        # Creamos un sizer horizontal para organizar la ventana principal y el panel lateral
        sizer_ventana = wx.BoxSizer(wx.HORIZONTAL)
        sizer_ventana.Add(panel_estatico, 0, wx.EXPAND)
        sizer_ventana.Add(menu_juego, 0, wx.EXPAND)

        self.SetSizer(sizer_ventana)
        self.Show(True)

def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()
    return None

if __name__ == '__main__':
    main()