import wx

def main():
    app = wx.App()
    # widget padre es None. title y size son personalizados
    ven= wx.Frame(None, title='BlackJack', size=(1024,720))
    ven.Show() # Obligatorio mostrar siempre la ventana
    app.MainLoop()  #La ventana no se cierre al instante
    return None

main()


