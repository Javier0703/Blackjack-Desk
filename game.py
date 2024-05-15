# Generado por wxGlade 1.0.5
"""Practica creada por Javier Calvo Porro, estudiante de Ingenieria Informatica, UVa"""

import wx
from ClasesFunciones import *

#Creacion de Funciones/Clases/Variables generales
reduccion = 0.25
tipo_apuesta = [2,10,50]
balance = 0

#Funcion para generar las cartas (Bitmap)
def generar_cartas():
    m = []
    for i in range(52):
        img = wx.Image(f"Imagenes//Cartas//{i}.png", wx.BITMAP_TYPE_ANY)
        #Reducimos su anchura, ya que por defecto son muy grandes
        img.Rescale(int(img.GetWidth() * reduccion), int(img.GetHeight() * reduccion))
        m.append(wx.Bitmap(img))
    return m

#Clase Ventana (Donde se encuentra la interfaz)
class Ventana(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Ventana.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        #Definimos el tamaño, titulo y lo centramos
        self.SetSize((1000, 600))
        self.SetTitle("BlackJack")
        self.Center()

        self.modo_juego = 'M'
        self.forma_texto = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "")
        self.texto_info_manos = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "")

        sizer_general = wx.BoxSizer(wx.HORIZONTAL)

        #Sizer de la colukna estatica (donde estan los botonos, el balance...)
        #Codigo generado por wx.Glade
        sizer_col_estatica = wx.BoxSizer(wx.VERTICAL)
        sizer_general.Add(sizer_col_estatica, 0, wx.EXPAND, 0)
        sizer_modo_juego = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Modo de Juego"), wx.HORIZONTAL)
        sizer_col_estatica.Add(sizer_modo_juego, 0, wx.ALL | wx.EXPAND, 10)
        self.boton_manual = wx.RadioButton(self, wx.ID_ANY, "Manual", style=wx.RB_GROUP)
        self.boton_manual.SetValue(1)
        sizer_modo_juego.Add(self.boton_manual, 0, wx.RIGHT, 10)
        self.boton_automatico = wx.RadioButton(self, wx.ID_ANY, "Automatico")
        sizer_modo_juego.Add(self.boton_automatico, 0, wx.LEFT, 10)
        sizer_retardo = wx.BoxSizer(wx.HORIZONTAL)
        sizer_col_estatica.Add(sizer_retardo, 0, wx.ALL | wx.EXPAND, 10)
        txt_retardo = wx.StaticText(self, wx.ID_ANY, "Retardo: ")
        sizer_retardo.Add(txt_retardo, 0, wx.TOP, 5)
        self.retardo = wx.TextCtrl(self, wx.ID_ANY, "25\n", style=wx.TE_RIGHT)
        self.retardo.SetMinSize((60, 20))
        sizer_retardo.Add(self.retardo, 0, 0, 0)
        txt_ms = wx.StaticText(self, wx.ID_ANY, " ms.")
        sizer_retardo.Add(txt_ms, 0, wx.TOP, 5)
        sizer_accion = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Accion"), wx.VERTICAL)
        sizer_col_estatica.Add(sizer_accion, 0, wx.ALL | wx.EXPAND, 10)
        self.boton_pedir = wx.Button(self, wx.ID_ANY, "Pedir")
        self.boton_pedir.SetMinSize((100, 25))
        self.boton_pedir.Enable(False)
        sizer_accion.Add(self.boton_pedir, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 3)
        self.boton_cerrar = wx.Button(self, wx.ID_ANY, "Cerrar")
        self.boton_cerrar.SetMinSize((186, 25))
        self.boton_cerrar.Enable(False)
        sizer_accion.Add(self.boton_cerrar, 0, wx.ALL | wx.EXPAND, 0)
        self.boton_doblar = wx.Button(self, wx.ID_ANY, "Doblar")
        self.boton_doblar.SetMinSize((186, 25))
        self.boton_doblar.Enable(False)
        sizer_accion.Add(self.boton_doblar, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 3)
        self.boton_separar = wx.Button(self, wx.ID_ANY, "Separar")
        self.boton_separar.SetMinSize((186, 25))
        self.boton_separar.Enable(False)
        sizer_accion.Add(self.boton_separar, 0, wx.ALL | wx.EXPAND, 0)
        sizer_conteos = wx.BoxSizer(wx.VERTICAL)
        sizer_col_estatica.Add(sizer_conteos, 0, wx.EXPAND, 10)
        sizer_num_partida = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Partida"), wx.HORIZONTAL)
        sizer_conteos.Add(sizer_num_partida, 0, wx.ALL | wx.EXPAND, 5)
        numero_partida = wx.StaticText(self, wx.ID_ANY, "1", style=wx.ALIGN_CENTER_HORIZONTAL)
        numero_partida.SetFont(self.forma_texto)
        sizer_num_partida.Add(numero_partida, 1, wx.ALL, 0)
        sizer_balance_partida = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Balance Partida"), wx.HORIZONTAL)
        sizer_conteos.Add(sizer_balance_partida, 1, wx.ALL | wx.EXPAND, 5)
        balance_partida = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER_HORIZONTAL)
        balance_partida.SetFont(self.forma_texto)
        sizer_balance_partida.Add(balance_partida, 1, wx.ALL, 0)
        sizer_balance_total = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Balance Total"), wx.HORIZONTAL)
        sizer_conteos.Add(sizer_balance_total, 1, wx.ALL | wx.EXPAND, 5)
        balance_total = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER_HORIZONTAL)
        balance_total.SetFont(self.forma_texto)
        sizer_balance_total.Add(balance_total, 1, wx.ALL, 0)
        sizer_tiempo = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Tiempo"), wx.HORIZONTAL)
        sizer_conteos.Add(sizer_tiempo, 1, wx.ALL | wx.EXPAND, 5)
        tiempo = wx.StaticText(self, wx.ID_ANY, "10", style=wx.ALIGN_CENTER_HORIZONTAL)
        tiempo.SetFont(self.forma_texto)
        sizer_tiempo.Add(tiempo, 1, wx.ALL, 0)

        #Panel dinamico (Manos)
        self.panel_dinamico = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.panel_dinamico.SetScrollRate(10, 10)
        sizer_general.Add(self.panel_dinamico, 1, wx.EXPAND, 0)

        #Slizer para las manos generadas
        self.sizer_manos_generales = wx.BoxSizer(wx.VERTICAL)

        #Aqui se generan los BoxSizer para las diferentes manos
        #Generamos el BoxSizer del Croupier con la lista de sus items.
        self.sizer_croupier = wx.BoxSizer(wx.HORIZONTAL)
        self.items_croupier = []
        self.sizer_manos_generales.Add(self.sizer_croupier, 0, wx.EXPAND, 0)

        #manos del Jugador
        #El metodo es usar una lista con los paneles (manos) los BoxSizer y su contenido
        self.sizer_paneles_jugador = []
        self.boxsizers_jugador = []
        self.items_jugador = [[]]

        #Generame un Panel dentro de la lista anterior
        self.panel_dinamico.SetSizer(self.sizer_manos_generales)
        self.SetSizer(sizer_general)
        self.Layout()

        #Definimos todos los eventos de la Ventana para tenerlos todos localizados por si hay fallos
        self.Bind(wx.EVT_RADIOBUTTON, self.cambiar_modo, self.boton_manual)
        self.Bind(wx.EVT_RADIOBUTTON, self.cambiar_modo, self.boton_automatico)

    #Se cambia el modo
    def cambiar_modo (self,event):
        self.modo_juego = 'M' if self.modo_juego == 'A' else 'A'
        print(self.modo_juego)

    #Funcion para añadir la información
    def anyadir_info_croupier(self, info):
        static_text = wx.StaticText(self.panel_dinamico, wx.ID_ANY, info, style=wx.ALIGN_CENTER_HORIZONTAL)
        static_text.SetFont(self.texto_info_manos)
        self.items_croupier.append(static_text)
        self.sizer_croupier.Add(self.items_croupier[0], 0, wx.ALL | wx.EXPAND, 5)
        self.Layout()

    #Funcion para añadir carta al croupier
    def anyadir_carta_croupier(self, cartas, id):
        static_bitmap = wx.StaticBitmap(self.panel_dinamico, wx.ID_ANY, cartas[id])
        self.items_croupier.append(static_bitmap)
        self.sizer_croupier.Add(self.items_croupier[-1], 0, wx.ALL | wx.EXPAND, 5)
        self.Layout()

    # Funcion para generar un nuevo panel
    def nuevo_panel (self, info):
        self.sizer_paneles_jugador.append(wx.Panel(self.panel_dinamico, wx.ID_ANY))
        self.sizer_manos_generales.Add(self.sizer_paneles_jugador[-1], 0, wx.EXPAND, 0)
        self.info_jugador = info
        self.nuevo_boxizer_jugador()

    # Funcion para generar un nuevo boxsizer
    def nuevo_boxizer_jugador (self):
        self.boxsizers_jugador.append(wx.BoxSizer(wx.HORIZONTAL))
        self.anyadir_info_jugador()

    #Funcion para anyadir información
    def anyadir_info_jugador(self):
        static_text = wx.StaticText(self.sizer_paneles_jugador[-1], wx.ID_ANY, self.info_jugador, style=wx.ALIGN_CENTER_HORIZONTAL)
        static_text.SetFont(self.texto_info_manos)
        self.items_jugador[len(self.boxsizers_jugador)-1].append(static_text)
        self.boxsizers_jugador[-1].Add(self.items_jugador[-1][0], 0, wx.ALL | wx.EXPAND, 5)
        self.sizer_paneles_jugador[-1].SetSizer(self.boxsizers_jugador[-1])
        self.Layout()
    
    #Añadir las cartas iniciales
    def anyadir_cartas_iniciales(self, cartas, id):
        static_bitmap = wx.StaticBitmap(self.sizer_paneles_jugador[-1], wx.ID_ANY, cartas[id])
        self.items_jugador[-1].append(static_bitmap)
        self.boxsizers_jugador[-1].Add(static_bitmap, 0, wx.ALL | wx.EXPAND, 5)
        self.Layout()

#Dialgo de Nueva Partida    
class NuevaPartida(wx.Dialog):
    def __init__(self, *args, **kwds):

        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.CENTRE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog")
        self.Center()

        self.apuesta = 0
        sizer_dialogo = wx.BoxSizer(wx.VERTICAL)
        sizer_apuesta = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Apuesta"), wx.VERTICAL)
        sizer_dialogo.Add(sizer_apuesta, 0, wx.ALL | wx.EXPAND, 30)
        self.apuesta_baja = wx.RadioButton(self, wx.ID_ANY, f"{tipo_apuesta[0]} €", style=wx.RB_GROUP)
        self.apuesta_baja.SetValue(1)
        sizer_apuesta.Add(self.apuesta_baja, 0, wx.ALL, 3)
        self.apuesta_media = wx.RadioButton(self, wx.ID_ANY, f"{tipo_apuesta[1]} €")
        sizer_apuesta.Add(self.apuesta_media, 0, wx.ALL, 3)
        self.apuesta_alta = wx.RadioButton(self, wx.ID_ANY, f"{tipo_apuesta[2]} €")
        sizer_apuesta.Add(self.apuesta_alta, 0, wx.ALL, 3)
        text_jugar = wx.StaticText(self, wx.ID_ANY, u"¿Quieres seguir jugando?", style=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_dialogo.Add(text_jugar, 0, wx.LEFT | wx.RIGHT, 30)
        sizer_accion_apuesta = wx.StdDialogButtonSizer()
        sizer_dialogo.Add(sizer_accion_apuesta, 0, wx.ALIGN_RIGHT | wx.ALL, 4)
        self.boton_si = wx.Button(self, wx.ID_YES, "")
        self.boton_si.SetDefault()
        sizer_accion_apuesta.AddButton(self.boton_si)
        self.boton_no = wx.Button(self, wx.ID_NO, "")
        sizer_accion_apuesta.AddButton(self.boton_no)
        sizer_accion_apuesta.Realize()
        self.SetSizer(sizer_dialogo)
        sizer_dialogo.Fit(self)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.seguir_jugando, self.boton_si)
        self.Bind(wx.EVT_BUTTON, self.cerrar_juego, self.boton_no)

    #Queremos seguir jugando, por lo que guardamos el valor de la apuesta
    def seguir_jugando(self,event):
        if self.apuesta_baja.GetValue():
            self.apuesta = tipo_apuesta[0]
        elif self.apuesta_media.GetValue():
            self.apuesta = tipo_apuesta[1]
        else:
            self.apuesta = tipo_apuesta[2]
        self.Close()

    #No queremos que siga jugando, cerramos el juego
    def cerrar_juego(self,event):
        self.GetParent().Close()

#Ventana de BlackJack
class BlackJackWindow(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: BlackJack.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("BlackJack")

        sizer_dialogo_blackjack = wx.BoxSizer(wx.VERTICAL)
        sizer_dialogo_blackjack.Add((0, 0), 0, 0, 0)
        sizer_info_blackjack = wx.BoxSizer(wx.HORIZONTAL)
        sizer_dialogo_blackjack.Add(sizer_info_blackjack, 0, wx.ALL | wx.EXPAND, 10)
        label_haganado = wx.StaticText(self, wx.ID_ANY, "Ganado:")
        label_haganado.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_info_blackjack.Add(label_haganado, 0, wx.LEFT, 5)
        label_dinero_blackjack = wx.StaticText(self, wx.ID_ANY, f"15 €")
        label_dinero_blackjack.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_info_blackjack.Add(label_dinero_blackjack, 0, wx.LEFT | wx.RIGHT, 15)
        self.boton_ok = wx.Button(self, wx.ID_ANY, "OK")
        sizer_info_blackjack.Add(self.boton_ok, 0, wx.TOP, 5)
        self.SetSizer(sizer_dialogo_blackjack)
        sizer_dialogo_blackjack.Fit(self)
        self.Layout()
    
class BlackJack(wx.App):
    def OnInit(self):
        self.frame = Ventana(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

#Definimos el main
def main():
    app = BlackJack(0)
    cartas = []
    cartas = generar_cartas()
    juego = 1
    estrategia = Estrategia(Mazo.NUM_BARAJAS)
    mazo = Mazo(Carta, estrategia)

    #Funciones para añadir una carta y generar las distintas manos
    def anyadirCartas(mano,numero_cartas):
        for i in range(len(mano)):
            for _ in range(numero_cartas):
                mano[i].append(mazo.reparte())
        return mano

    def createMano(mano,nombre,letter,centinela):
        h = []
        for element in mano:
            if len(mano)>1:
                tmpName = nombre+str(chr(ord(letter) + centinela))
                centinela+=1
                h.append(Mano(element,tmpName,apuesta))
            else:   
                h.append(Mano(element,nombre,apuesta))
        return h

    while True:
        #Definimos una ventana de Nueva partida que sea 'hija' de la Ventana main
        nueva_partida = NuevaPartida(app.frame, wx.ID_ANY, "")
        nueva_partida.Center()
        nueva_partida.ShowModal()
        #Guardamos la apuesta
        apuesta = nueva_partida.apuesta
        
        #Genramos las manos iniciales del Croupier y del Jugador
        nombre, letter = nombres[1], 'A'
        centinela, cartas_por_mano = 0,1

        croupier, mano_croupier = [[]],[]
        croupier = anyadirCartas(croupier,cartas_por_mano)
        mano_croupier = createMano(croupier,nombre,letter,centinela)

        nombre = nombres[0]
        cartas_por_mano =  2
        #Guardamos las cartas (Type Carta), las manos (Type Mano) y el formato carta para su impreson respectivamente
        jugador, mano_jugador = [[]], []
        jugador = anyadirCartas(jugador,cartas_por_mano)
        mano_jugador = createMano(jugador,nombre,letter,centinela)

        #Ya tenemos creada las manos iniciales, ahora toca colocarlas en la interfaz
        info_croupier = f"{mano_croupier[0].nombre}\n{mano_croupier[0].sumaCartas}\n{mano_croupier[0].estado}"
        carta = croupier[0][0].ind
        app.frame.anyadir_info_croupier(info_croupier)
        app.frame.anyadir_carta_croupier(cartas, carta)
        info_jugador = f"{mano_jugador[0].sumaCartas}\n{mano_jugador[0].apuesta} €\n{mano_jugador[0].estado}"
        app.frame.nuevo_panel(info=info_jugador)
        for i in range(2):
            app.frame.anyadir_cartas_iniciales(cartas=cartas,id=jugador[0][i].ind)
        break
    app.MainLoop()

    

if __name__ == "__main__":
    main()
