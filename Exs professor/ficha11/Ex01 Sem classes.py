# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk # treeview
from tkinter import messagebox 
from PIL import ImageTk,Image  
import datetime

ficheiro = "exs professor/ficha11/presencas.txt"


#--- Consulta de movimento

def consulta():
        
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Consultas")
    conWindow.focus_force()  # força o focus na window atual
    conWindow.grab_set()    # direciona todos os eventos para a window ativa 
    # Panel
    panel1 = PanedWindow(conWindow, width = 200, height = 270, bd = "3", relief = "sunken")
    panel1.place(x=15, y=20) 
    #Frame Tipo de Movimento - checkbuttons para entradas / saídas
    lframe = LabelFrame(panel1, width = 160, height=100, bd=3, text= "Tipo de Movimento", fg = "blue", relief = "sunken")
    lframe.place(x=5, y=5)
    global cb1
    global cb2
    global utilizador
    cb1 = IntVar()
    cb2 = IntVar()
    ck1 = Checkbutton(lframe, text = "Entrada", variable = cb1)
    ck1.place(x=15, y=15)
    ck2 = Checkbutton(lframe, text = "Saída", variable = cb2)
    ck2.place(x=15, y=40)

    #Frame Utilizador    - entry para indocar nº de utilizador a consultar
    lframe2 = LabelFrame(panel1, width = 160, height=100, bd=3, text= "Por Utilizador", fg = "blue", relief = "sunken")
    lframe2.place(x=5, y=120)
    lblUtilizador = Label(lframe2, text="Número: ")
    lblUtilizador.place(x=15, y=5)
        
    utilizador = StringVar()
    txtUtilizador = Entry(lframe2, width = 15, textvariable = utilizador)
    txtUtilizador.place(x=15, y=25)

    #  Button consultar dados
    btnConsultar = Button(panel1, width = 21, height= 2, text = "Consultar", relief = "raised", command = dados_treeview)
    btnConsultar.place(x=8, y=222)

    # Painel 2
    panel2 = PanedWindow(conWindow, width = 450, height = 270, bd = "3", relief = "sunken")
    panel2.place(x=220, y=20)
    # TreeView para consulta de movimentos
    global tree 
    tree = ttk.Treeview(panel2, selectmode = "browse", columns = ("Número", "Data", "Hora", "Movimento"), show = "headings")
 
    tree.column("Número", width = 100,   anchor="c")
    tree.column("Data", width = 100,  anchor="c")          # c- center, e - direita, w- esquerda
    tree.column("Hora", width = 100,   anchor="c")
    tree.column("Movimento", width = 140,   anchor="c")
    tree.heading("Número", text = "Número")
    tree.heading("Data", text = "Data")
    tree.heading("Hora", text = "Hora")
    tree.heading("Movimento", text = "Movimento")
    tree.place(x=5, y=5)




def dados_treeview():  # Remove TODAS as linhas da Treeview
    tree.delete(*tree.get_children()) 
    mov = ""
    if cb1.get() == True and cb2.get() == True:   # Se está checado entrada e saída (cb1 e cb2)
        mov = "T"
    else:
        if cb1.get() == True:                      # se está apenas checado cb1 (entrada)
            mov = "Entrada\n"
        if cb2.get() == True:                      # se está apenas checado cb2 (saida)
            mov = "Saída\n"
    f = open(ficheiro, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        if mov == "T" or  campos[3] == mov:
            if utilizador.get() == "" or utilizador.get() == campos[0]:
                    tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))




#----- registar movimentos no ficheiro e presenças
def registar_mov():
    f = open("presencas.txt", "a", encoding="utf-8")
    data =  str(datetime.date.today())
    hora = str(datetime.datetime.now().time())
    mov = selected.get()
    num = str(numero.get())
    linha = num  + ";" + data + ";" + hora + ";" + mov + "\n"
    f.write(linha)
    f.close()
    lboxMov.insert("end", linha)

   
def movimentos():
    movWindow = Toplevel()   # Objeto da classe Toplevel, janela principal
    movWindow.title("Entradas e Saídas") 
    movWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    movWindow.focus_force()     # Força toda a interação com a janela atual (top window)
    movWindow.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)
             
    lblNumero = Label(movWindow, text="Número de Estudante:")
    lblNumero.place(x=20, y=15)
    global numero
    numero = IntVar()
    txtNumero = Entry(movWindow, width = 20, textvariable = numero)
    txtNumero.place(x=150, y=15)

    #Radiobutton
    lframe = LabelFrame(movWindow, width = 200, height=130, bd=3, text= "Género", fg = "blue", relief = "sunken")
    lframe.place(x=25, y=60)
    global selected
    selected = StringVar()
    selected.set("Entrada")   # Opção selecionada por defeito 
    rd1 = Radiobutton(lframe, text = "Entrada", value = "Entrada", variable = selected)
    rd1.place(x=15, y=20)
    rd2 = Radiobutton(lframe, text = "Saída", value = "Saída", variable = selected)
    rd2.place(x=15, y=50)

    #Button
    btnRegistar = Button(movWindow, width = 12, height= 4, text = "Registar", command = registar_mov)
    btnRegistar.place(x=250, y=80)

    lblHistorico = Label(movWindow, text="Histórico de movimentos")
    lblHistorico.place(x=500, y=15)
    # Panel
    panel1 = PanedWindow(movWindow, width = 280, height = 200, bd = "3", relief = "sunken")
    panel1.place(x=400, y=50)
    #ListBox
    global lboxMov
    lboxMov =Listbox(panel1, width = 38, height=10, bd="3", selectmode = "single")
    lboxMov.place(x=6, y= 22)




#-----Arranque da aplicação 
#-------------------------------
window=Tk()   # invoca classe tk , cria a "main window"

global screenHeight
global screenWidth
global appHeight, appWidth
global x, y
#Get the current screen width and height
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 700                             # tamanho (pixeis) da window a criar
appHeight = 300
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

#window.geometry("700x300")
window.title('Gestão de Presenças')
img = ImageTk.PhotoImage(Image.open("Exs professor/ficha11/presencas.jpg"))

barraMenu = Menu(window)
# Constroi menu Simuladores, com 2 opções dropd-down
barraMenu.add_command(label = "Movimentos",command = movimentos)
barraMenu.add_command(label = "Consulta",command = consulta)
# Constroi menu Sair, com comando quit
barraMenu.add_command(label = "Sair", command = window.quit)
window.configure(menu=barraMenu)

lbl = Label(window, text = "Gestão de Presenças", font = ("Helvetica", 12))
lbl.place(x=450, y=120)
# ------- Imagem
# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
ctnCanvas = Canvas(window, width = 350, height = 200, bd = 4, relief = "sunken")
ctnCanvas.place(x=70, y=40)
ctnCanvas.create_image(175,100, image = img)


window.mainloop()   # event listening loop by calling the mainloop()
