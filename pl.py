import wx

class MenuVertical(wx.Panel):
    def __init__(self, parent):
        super(MenuVertical, self).__init__(parent)
        
        # Creamos un box sizer vertical para organizar los elementos
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Creamos un grupo de opciones con un label
        box_prueba = wx.StaticBox(self, label="Prueba")
        sizer_prueba = wx.StaticBoxSizer(box_prueba, wx.VERTICAL)
        
        # Creamos los botones de radio
        self.radio_option1 = wx.RadioButton(self, label="Opción 1", style=wx.RB_GROUP)
        self.radio_option2 = wx.RadioButton(self, label="Opción 2")
        
        # Los añadimos al sizer del grupo
        sizer_prueba.Add(self.radio_option1, 0, wx.ALL, 5)
        sizer_prueba.Add(self.radio_option2, 0, wx.ALL, 5)
        
        # Añadimos el sizer del grupo al sizer principal
        sizer.Add(sizer_prueba, 0, wx.ALL|wx.EXPAND, 10)
        
        self.SetSizer(sizer)

class Ventana(wx.Frame):
    def __init__(self):
        super(Ventana, self).__init__(None, title="BlackJack", size=(400,300))
        
        # Creamos el menú vertical
        panel_menu = MenuVertical(self)
        
        # Añadimos el menú vertical a la ventana principal
        sizer_principal = wx.BoxSizer(wx.HORIZONTAL)
        sizer_principal.Add(panel_menu, 1, wx.EXPAND)
        
        self.SetSizer(sizer_principal)
        self.Show(True)

def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
