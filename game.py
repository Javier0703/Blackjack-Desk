# Generado por wxGlade 1.0.5
"""Practica creada por Javier Calvo Porro, estudiante de Ingenieria Informatica, UVa"""

import wx
from ClasesFunciones import *

#Creacion de Funciones/Clases
tipo_apuesta = [2,10,50]
max_value = [17,21]

#Funcion para generar las cartas (Bitmap)
def generar_cartas(reduccion):
    m = []
    for i in range(52):
        img = wx.Image(f"Imagenes//Cartas//{i}.png", wx.BITMAP_TYPE_ANY)
        #Reducimos su anchura, ya que por defecto son muy grandes
        img.Rescale(int(img.GetWidth() * reduccion), int(img.GetHeight() * reduccion))
        m.append(wx.Bitmap(img))
    return m

#CLASE PAEL JUGADOR (Contendra toda la info -> Mano y Cartas)
class PanelJugador(wx.Panel):
    def __init__(self, parent, id, index, cartas_jugador, mano_jugador, cartas, *args, **kwds):
        super().__init__(parent, id, *args, **kwds)
 
        self.index = index
        self.cartas_jugador = cartas_jugador
        self.mano_jugador = mano_jugador  
        self.cartas = cartas     

        # Creamos la estructura
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Información a añadir
        self.informacion = f"({mano_jugador.sumaCartas})\n{mano_jugador.apuesta} €\n{mano_jugador.estado}"
        self.info = wx.StaticText(self, wx.ID_ANY, self.informacion, style=wx.ALIGN_CENTER_HORIZONTAL)
        self.info.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.info.SetMinSize((150, 100))
        self.sizer.Add(self.info, 0, wx.ALL | wx.EXPAND, 5)

        # Bucle para añadir las imágenes
        for carta in cartas_jugador:
            static_bitmap = wx.StaticBitmap(self, wx.ID_ANY, self.cartas[carta.ind])
            self.sizer.Add(static_bitmap, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(self.sizer)
        self.Layout()

    # Funcion que indica si es comparable o no
    def comprobar_separable(self):
        if len(self.mano_jugador.valorCartas) == 2 and (self.mano_jugador.valorCartas[0][0] == self.mano_jugador.valorCartas[1][0]):
            return True
        else:
            return False

    # Funcion ejecutada por ventana por pedir    
    def pedir(self):
        self.mano_jugador.datos == self.cartas_jugador
        self.mano_jugador.actualizarDatosMano()
        self.actualizar_info_panel()


    # Funcion par aactualizar el panel
    def actualizar_info_panel(self):

        # Eliminar todos los widgets hijos del panel
        self.sizer.Clear(delete_windows=True)

        # Actualizar la información del jugador
        self.informacion = f"({self.mano_jugador.sumaCartas})\n{self.mano_jugador.apuesta} €\n{self.mano_jugador.estado}"

        # Crear nuevos widgets
        self.info = wx.StaticText(self, wx.ID_ANY, self.informacion, style=wx.ALIGN_CENTER_HORIZONTAL)
        self.info.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.info.SetMinSize((150, 100))
        self.sizer.Add(self.info, 0, wx.ALL | wx.EXPAND, 5)

        for carta in self.cartas_jugador:
            static_bitmap = wx.StaticBitmap(self, wx.ID_ANY, self.cartas[carta.ind])
            self.sizer.Add(static_bitmap, 0, wx.ALL | wx.EXPAND, 5)

        # Refrescar el layout del panel
        self.Refresh()
        self.Layout() 

#CLASE VENTANA (Donde se encuentra la interfaz)
class Ventana(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Ventana.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        #Definimos el tamaño, titulo y lo centramos por si se minimiza
        self.SetSize((1000, 600))
        self.SetTitle("BlackJack")
        self.Center()
        self.Maximize()

        #Propiedades creadas a mano para su uso
        self.apuesta = 0
        self.modo_juego = 'M'
        self.tiempo_retardo = 100
        self.juego_actual = 0
        self.balance = 0
        self.balance_global = 0
        self.reduccion = 0.25
        self.cartas = generar_cartas(reduccion=self.reduccion)
        self.panel_seleccionado = 0
        self.blackjack = False

        # Generamos la estrategia y el mazo como en la practica anterior
        self.estrategia = Estrategia(Mazo.NUM_BARAJAS)
        self.mazo = Mazo(Carta, self.estrategia)

        #Informacion del croupier
        self.cartas_croupier = []
        self.mano_croupier = ""
        self.info_mano_croupier = ""

        # Propiedades wx.Python
        self.forma_texto = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "")
        self.texto_info_manos = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "")
        self.panel_activo = wx.Colour(255, 255, 204)
        self.panel_perdido = wx.Colour(255, 0, 0)
        self.panel_ganado =  wx.Colour(0, 128, 0)
        self.panel_cerrado = wx.Colour(211, 211, 211)
        self.panel_pasado = wx.Colour(105, 105, 105)

        #Sizer general de la ventana (Dos columnas)
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
        self.retardo = wx.TextCtrl(self, wx.ID_ANY, f"{self.tiempo_retardo}\n", style=wx.TE_RIGHT)
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
        self.numero_partida = wx.StaticText(self, wx.ID_ANY, f"{self.juego_actual}", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.numero_partida.SetFont(self.forma_texto)
        sizer_num_partida.Add(self.numero_partida, 1, wx.ALL, 0)
        sizer_balance_partida = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Balance Partida"), wx.HORIZONTAL)
        sizer_conteos.Add(sizer_balance_partida, 1, wx.ALL | wx.EXPAND, 5)
        self.balance_partida = wx.StaticText(self, wx.ID_ANY, f"{self.balance}", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.balance_partida.SetFont(self.forma_texto)
        sizer_balance_partida.Add(self.balance_partida, 1, wx.ALL, 0)
        sizer_balance_total = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Balance Total"), wx.HORIZONTAL)
        sizer_conteos.Add(sizer_balance_total, 1, wx.ALL | wx.EXPAND, 5)
        self.balance_total = wx.StaticText(self, wx.ID_ANY, f"{self.balance_global}", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.balance_total.SetFont(self.forma_texto)
        sizer_balance_total.Add(self.balance_total, 1, wx.ALL, 0)
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
        self.sizer_manos_generales.Add(self.sizer_croupier, 0, wx.EXPAND, 0)

        # Manos del Jugador
        # Se van a crear paneles que pueda interactuar con ellos ( hacer click ) A poder ser usando la clase PanelJugador. Como lo hago?
        self.paneles_jugador = []

        #Generame un Panel dentro de la lista anterior
        self.panel_dinamico.SetSizer(self.sizer_manos_generales)
        self.SetSizer(sizer_general)
        self.Layout()

        #Definimos todos los eventos de la Ventana para tenerlos todos localizados por si hay fallos
        self.Bind(wx.EVT_RADIOBUTTON, self.cambiar_modo, self.boton_manual)
        self.Bind(wx.EVT_RADIOBUTTON, self.cambiar_modo, self.boton_automatico)
        self.Bind(wx.EVT_TEXT, self.actualizar_retardo, self.retardo)

        #Eventos de los botones
        self.Bind(wx.EVT_BUTTON, self.accion_pedir, self.boton_pedir)
        self.Bind(wx.EVT_BUTTON, self.accion_cerrar, self.boton_cerrar)
        
        
        # Inicializamos el Juego
        self.nuevo_juego()
     
    # GLOBAL: Se cambia el modo
    def cambiar_modo (self,event):
        self.modo_juego = 'M' if self.modo_juego == 'A' else 'A'

    #GLOBAL: Actualizar el retardo cada vez que hay cambios (sin necesidad de enter)
    def actualizar_retardo(self,event):
        #Modificacion del retardo, por si hay 
        retardo_texto = self.retardo.GetValue()
        try:
            self.tiempo_retardo = int(retardo_texto)
        except ValueError:
            pass      
        self.Layout()

    #GLOBAL: Agregar una partida mas
    def agregar_partida(self):
        self.juego_actual += 1
        self.numero_partida.SetLabel(f"{self.juego_actual}")
        self.Layout()  

    # INICIAL: Funcion para iniciar un nuevo juego
    def nuevo_juego(self):
        self.blackjack = False
        wx.CallLater(10, self.init_game)

    #INICIAL :Creacion del juego -> Apertura de dialogo    
    def init_game(self):
        #Seleccion de la Apuesta
        nueva_ventana = NuevaPartida(self)
        nueva_ventana.Center()
        nueva_ventana.ShowModal()

        if nueva_ventana.querer_jugar == False:
            self.Close()

        else:
            self.apuesta = nueva_ventana.apuesta
            self.vaciar_balance_partida()
            self.eliminar_elementos()
            self.agregar_partida()
            self.generar_manos()
            self.deshabilitar_botones()

    # INICIAL: Generar las diversas manos
    def generar_manos(self):
        wx.CallLater(self.tiempo_retardo, self.anyadir_croupier)
        wx.CallLater(self.tiempo_retardo*2, self.anyadir_primer_panel)
    
    # GLOBAL: Funcion para eliminar los elementos
    def eliminar_elementos(self):
        #Eliminamos elementos del jugador
        for panel in self.paneles_jugador:
            panel.GetSizer().Clear(True)
        self.paneles_jugador = []    

        # Elementos del Croupier
        self.sizer_croupier.Clear(delete_windows=True)
        self.mano_croupier = []
        self.cartas_croupier = []
        self.Layout()

    # INICIAL: Funcion añadir elementos al croupier  
    def anyadir_croupier(self):
        self.cartas_croupier.append(self.mazo.reparte())
        self.mano_croupier = Mano(self.cartas_croupier,'Croupier', self.apuesta)
        self.generar_info_croupier()
        self.modificar_info_croupier()
        self.anyadir_carta_panel(indice = self.cartas_croupier[0].ind)

    # INICIAL: Funcion para generar la info del croupier
    def generar_info_croupier(self):
        self.info_croupier = wx.StaticText(self.panel_dinamico, wx.ID_ANY, self.info_mano_croupier, style=wx.ALIGN_CENTER_HORIZONTAL)
        self.info_croupier.SetFont(self.texto_info_manos)
        self.info_croupier.SetMinSize((150,100))
        self.sizer_croupier.Add(self.info_croupier, 0, wx.ALL | wx.EXPAND, 5)
        self.Layout()

    # GLOBAL: Funcion para modificar la info del croupier
    def modificar_info_croupier(self):
        self.mano_croupier.actualizarDatosMano()
        info = f"{self.mano_croupier.nombre}\n({self.mano_croupier.sumaCartas})\n{self.mano_croupier.estado}"
        self.info_croupier.SetLabel(info)
        self.Layout()  

    # GLOBAL: Funcion para añadir una carta al panel
    def anyadir_carta_panel(self, indice):
        carta = wx.StaticBitmap(self.panel_dinamico, wx.ID_ANY, self.cartas[indice])  
        self.sizer_croupier.Add(carta, 0, wx.ALL | wx.EXPAND, 5)  
        self.Layout() 

    # INICIAL: Genera el primer panel y lo añade
    def anyadir_primer_panel(self):
        numero_cartas = 2
        cartas_mazo = []
        for _ in range(numero_cartas):
            cartas_mazo.append(self.mazo.reparte())
        mano_panel = Mano(cartas_mazo, 'Jugador', self.apuesta)
        self.nuevo_panel = PanelJugador(parent=self.panel_dinamico, id=wx.ID_ANY, index= len(self.paneles_jugador), cartas_jugador=cartas_mazo, mano_jugador=mano_panel, cartas= self.cartas)
        self.nuevo_panel.Bind(wx.EVT_LEFT_DOWN, self.seleccionar_panel)
        self.paneles_jugador.append(self.nuevo_panel)
        self.sizer_manos_generales.Add(self.nuevo_panel, 0, wx.EXPAND, 0 )
        self.Layout()
        # HACER
        wx.CallLater(self.tiempo_retardo, self.comprobar_blackjack)

    # GLOBAL: Seleccionar panel
    def seleccionar_panel(self, event):
 
        # Comprobamos los paneles. Activar el seleccionado, desactivar el resto (activo)
        for panel in self.paneles_jugador:
            if panel == event.GetEventObject():
                self.panel_seleccionado = panel.index
                if (panel.mano_jugador.estado).upper() == "ACTIVA":
                    self.boton_pedir.Enable()
                    self.boton_cerrar.Enable()
                    self.boton_doblar.Enable()
                    panel.SetBackgroundColour(self.panel_activo)
                    if panel.comprobar_separable() == True:
                        self.boton_separar.Enable()
                    else:
                        self.boton_separar.Disable()
            else:
                if (panel.mano_jugador.estado).upper() == "ACTIVA":
                    panel.SetBackgroundColour(wx.NullColour)
            self.Refresh()   

    #GLOBAL: Funcion para deshabilitar botones
    def deshabilitar_botones(self):
        self.boton_separar.Disable()
        self.boton_pedir.Disable()
        self.boton_cerrar.Disable()
        self.boton_doblar.Disable()

    # INICIAL: Comprobamos el BlackJack
    def comprobar_blackjack(self):
        for panel in self.paneles_jugador:
            if panel.mano_jugador.sumaCartas == max_value[1]:
                self.blackjack = True
                self.apuesta *= (3/2)
                self.apuesta =  int(self.apuesta)
                # Creamos La ventana de BlackJack
                blackjack = BlackJackWindow(self)
                blackjack.cambiar_apuesta(str(self.apuesta))
                blackjack.mostrar_ventana()
                self.cambiar_valores_apuesta_bj()
                wx.CallLater(2000, self.nuevo_juego)
                  
    # FINAL: Funcion para cambiar los valores de la apuesta
    def cambiar_valores_apuesta_bj(self):
        self.balance = self.apuesta
        self.balance_global += self.apuesta
        self.modificar_paneles_balance()

    # INICIAL: Poner a 0 el balance de la partida
    def vaciar_balance_partida(self):
        self.balance = 0
        self.balance_partida.SetLabel(f"{self.balance} €")
        self.balance_partida.SetForegroundColour(wx.Colour(0, 0, 0))
        self.Layout()

    # GLOBAL-ACCIONES: ACCIONES BOTONES

    # GLOBAL: Funcion para añadir una carta
    def accion_pedir(self,event):
        self.paneles_jugador[self.panel_seleccionado].cartas_jugador.append(self.mazo.reparte())
        # Cambiar los valores dentro del objeto
        self.paneles_jugador[self.panel_seleccionado].pedir()
        self.Layout()
        self.Refresh()
        self.comprobar_panel_accionado()
        # Comprobamos las manos para colorearlas
        self.comprobacion_manos()

    # GLOBAL: Funcion para cerrar una apuesta
    def accion_cerrar(self,event):
        self.paneles_jugador[self.panel_seleccionado].mano_jugador.estado = 'Cerrada'
        self.paneles_jugador[self.panel_seleccionado].actualizar_info_panel()
        self.Layout()
        self.Refresh()
        self.comprobar_panel_accionado()
        self.comprobacion_manos()

    # GLOBAL: Funcion llamada por una accion para comprobar si es posible seguir accionando
    def comprobar_panel_accionado(self):
        if self.paneles_jugador[self.panel_seleccionado].mano_jugador.sumaCartas > 21:
            self.deshabilitar_botones()

    def comprobacion_manos(self):
        self.manos_activas = 0
        self.manos_pasadas = 0
        for panel in self.paneles_jugador:
            if panel.mano_jugador.estado.upper() == 'PASADA':
                panel.SetBackgroundColour(self.panel_pasado)
                self.manos_pasadas +=1
            elif panel.mano_jugador.estado.upper() == 'CERRADA':
                panel.SetBackgroundColour(self.panel_cerrado)
            else:
                self.manos_activas +=1
            # Coloreamos el panel de amarillo si es el activado
            if panel.index == self.panel_seleccionado and panel.mano_jugador.estado.upper() == 'ACTIVA':
                panel.SetBackgroundColour(self.panel_activo)

        #Si no quedan manos activas, se finaliza el juego. --> Conteo resultados
        # Si todas las manos son pasadas, al conteo, si no, añadimos al croupier
        if(self.manos_activas == 0):
            if self.manos_pasadas == len(self.paneles_jugador):
                self.conteo_final()
            else:
                self.anyadir_cartas_croupier()

    # FINAL: Añadir Cartas al Croupier hasta 17
    def anyadir_cartas_croupier(self):
        suma_mano = self.mano_croupier.sumaCartas
        # Miestras sea menor de 17, se genera una carta
        while suma_mano<max_value[0]:
            carta = self.mazo.reparte()
            self.mano_croupier.addCarta(carta)
            self.mano_croupier.actualizarDatosMano() 
            self.modificar_info_croupier()
            self.anyadir_carta_panel(indice=carta.ind)
            suma_mano = self.mano_croupier.sumaCartas

        self.conteo_final()

    # FINAL: Conteo de resultados
    def conteo_final(self):
        suma_croup = self.mano_croupier.sumaCartas

        for panel in self.paneles_jugador:
            suma_jug = panel.mano_jugador.sumaCartas
            apuesta = panel.mano_jugador.apuesta

            if (suma_croup > max_value[1] and suma_jug > max_value[1]) or (suma_croup == suma_jug):
                self.balance += 0
                self.balance_global += 0

            elif suma_croup > max_value[1]:  # Se pasa el Croupier
                self.balance += apuesta
                self.balance_global += apuesta
                panel.SetBackgroundColour(self.panel_ganado)

            elif suma_jug > max_value[1]:  # Se pasa el Jugador
                self.balance -= apuesta
                self.balance_global -= apuesta
                panel.SetBackgroundColour(self.panel_perdido)

            elif suma_croup > suma_jug:  # El Croupier gana
                self.balance -= apuesta
                self.balance_global -= apuesta
                panel.SetBackgroundColour(self.panel_perdido)

            else:  # El Jugador gana
                self.balance += apuesta
                self.balance_global += apuesta
                panel.SetBackgroundColour(self.panel_ganado)

            self.Layout()
            self.Refresh()

        self.modificar_paneles_balance()

    #FINAL: Modificar Paneles --> Luego nuevo juego
    def modificar_paneles_balance(self): 
        self.balance_partida.SetLabel(f"{self.balance} €")
        if self.balance > 0:
            self.balance_partida.SetForegroundColour(wx.Colour(0, 128, 0))
        elif self.balance < 0:
            self.balance_partida.SetForegroundColour(wx.Colour(255, 0, 0))
        self.balance_partida.Refresh()
        self.balance_total.SetLabel(f"{self.balance_global} €")
        if self.balance_global > 0:
            self.balance_total.SetForegroundColour(wx.Colour(0, 128, 0))
        elif self.balance_global < 0:
            self.balance_total.SetForegroundColour(wx.Colour(255, 0, 0))
        self.balance_total.Refresh()
        self.Layout()

        if self.blackjack == False:
            self.nuevo_juego()

#DIALOGO DE NUEVA PARTIDA    
class NuevaPartida(wx.Dialog):
    def __init__(self ,*args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.CENTRE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog")
        self.Center()

        self.apuesta = 0
        self.querer_jugar = False

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
        self.querer_jugar = True
        if self.apuesta_baja.GetValue():
            self.apuesta = tipo_apuesta[0]
        elif self.apuesta_media.GetValue():
            self.apuesta = tipo_apuesta[1]
        else:
            self.apuesta = tipo_apuesta[2]
        self.Close()

    #No queremos que siga jugando, cerramos el juego
    def cerrar_juego(self,event):
        self.querer_jugar = False
        self.Close()

#Ventana de BlackJack
class BlackJackWindow(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: BlackJack.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("BlackJack")
        self.apuesta = 0
        sizer_dialogo_blackjack = wx.BoxSizer(wx.VERTICAL)
        imagen = wx.Image(f"Imagenes//blackjack.jpg", wx.BITMAP_TYPE_ANY)
        imagen_blackjack = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(imagen))
        sizer_dialogo_blackjack.Add(imagen_blackjack, 0, wx.ALL | wx.EXPAND, 5)
        sizer_info_blackjack = wx.BoxSizer(wx.HORIZONTAL)
        sizer_dialogo_blackjack.Add(sizer_info_blackjack, 0, wx.ALL | wx.EXPAND, 10)
        label_haganado = wx.StaticText(self, wx.ID_ANY, "Ganado:")
        label_haganado.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_info_blackjack.Add(label_haganado, 0, wx.LEFT, 5)
        self.label_dinero_blackjack = wx.StaticText(self, wx.ID_ANY, f"{self.apuesta} €")
        self.label_dinero_blackjack.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_info_blackjack.Add(self.label_dinero_blackjack, 0, wx.LEFT | wx.RIGHT, 15)
        self.boton_ok = wx.Button(self, wx.ID_ANY, "OK")
        sizer_info_blackjack.Add(self.boton_ok, 0, wx.TOP, 5)
        self.SetSizer(sizer_dialogo_blackjack)
        sizer_dialogo_blackjack.Fit(self)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.cerrar_ventana, self.boton_ok)

    #Funcion para cambiar el valor del label
    def cambiar_apuesta(self, apuesta_ganada):
        self.label_dinero_blackjack.SetLabel(f"{apuesta_ganada} €")
        self.Layout()

    #Funcion para mostrar la ventana
    def mostrar_ventana(self):
        self.Center()
        self.Show()
        wx.CallLater(2000,self.cerrar_ventana_automatico)

    # Funcion pra cerrar la ventana ( se llama solo desdela anterior)
    def cerrar_ventana_automatico(self):
        self.Close()

    # Funcion de cerrar la ventnana mediante un EVT_BUTTON
    def cerrar_ventana(self,event):
        self.Close()

#CLASE BLACKJACK (Applicacion) 
class BlackJack(wx.App):
    def OnInit(self):
        self.frame = Ventana(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
    
#Main
if __name__ == "__main__":
    app = BlackJack(0)
    app.MainLoop()