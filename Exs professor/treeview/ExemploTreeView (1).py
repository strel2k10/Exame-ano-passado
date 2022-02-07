from tkinter import *
from tkinter import ttk # treeview




def dados_treeview():
        i=0
        tree.delete(*tree.get_children())
        mov = ""
        if cb1.get() == True and cb2.get() == True:
            mov = "T"
        else:
            if cb1.get() == True:
                mov = "Entrada\n"
            if cb2.get() == True:
                mov = "Saída\n"

        f = open(ficheiro, "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if mov == "T" or  campos[3] == mov:
                if utilizador.get() == "" or utilizador.get() == campos[0]:
                    listaTree.append([])   # append de uma sublista vazia
                    listaTree[i].append(campos[0])
                    listaTree[i].append(campos[1])
                    listaTree[i].append(campos[2])
                    listaTree[i].append(campos[3])
                    i+=1
                    tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))


# renderiza TreeView com dados da lista
def renderizaTree():
    row_id= tree.index(tree.selection())   # linha selecionada
    listaTree[row_id][0] = value_num.get()
    listaTree[row_id][1] = value_data.get()
    listaTree[row_id][2] = value_hora.get()

# remove linhas da treeview
    tree.delete(*tree.get_children())
#renderiza treeviw com dados da listaTree    
    for i in range (len(listaTree)-1):
         tree.insert("", "end", values = (listaTree[i][0], listaTree[i][1], listaTree[i][2], listaTree[i][3]))
    

# Obter dados da linha selecionada da TreeView
def dados_linha_tree():
    row_id = tree.focus()   # obter o id da linha ativa / selecionada
    lista = tree.item(row_id)
 # dados obtidos da treeView sáo atribuidos às variáveis associadas às Entrys   
    value_num.set(lista["values"][0])
    value_data.set(lista["values"][1])
    value_hora.set(lista["values"][2])
    value_mov.set(lista["values"][3])
    





ficheiro = "presencas.txt"        
listaTree=[[]]

ConWindow = Tk()
ConWindow.geometry("700x400")
ConWindow.title("Consultas")


        # Panel
panel1 = PanedWindow(ConWindow, width = 200, height = 270, bd = "3", relief = "sunken")
panel1.place(x=15, y=20)
    
#Frame Tipo de Movimento
lframe = LabelFrame(panel1, width = 160, height=100, bd=3, text= "Tipo de Movimento", fg = "blue", relief = "sunken")
lframe.place(x=5, y=5)
cb1 = IntVar()
cb2 = IntVar()
ck1 = Checkbutton(lframe, text = "Entrada", variable = cb1)
ck1.place(x=15, y=15)
ck2 = Checkbutton(lframe, text = "Saída", variable = cb2)
ck2.place(x=15, y=40)

#Frame Utilizador
lframe2 = LabelFrame(panel1, width = 160, height=100, bd=3, text= "Por Utilizador", fg = "blue", relief = "sunken")
lframe2.place(x=5, y=120)
lbl_utilizador = Label(lframe2, text="Número: ")
lbl_utilizador.place(x=15, y=5)
global utilizador
utilizador = StringVar()
txt_utilizador = Entry(lframe2, width = 15, textvariable = utilizador)
txt_utilizador.place(x=15, y=25)
        
btn_consultar = Button(panel1, width = 21, height= 2, text = "Consultar", relief = "raised", command = dados_treeview)
btn_consultar.place(x=8, y=222)
        
        # Painel 2
panel2 = PanedWindow(ConWindow, width = 450, height = 270, bd = "3", relief = "sunken")
panel2.place(x=220, y=20)

tree = ttk.Treeview(panel2, columns = ("Número", "Data", "Hora", "Movimento"), show = "headings")
tree.column("Número", width = 100,   anchor="c")
tree.column("Data", width = 100,  anchor="c")          # c- center, e - direita, w- esquerda
tree.column("Hora", width = 100,   anchor="c")
tree.column("Movimento", width = 140,   anchor="c")
tree.heading("Número", text = "Número")
tree.heading("Data", text = "Data")
tree.heading("Hora", text = "Hora")
tree.heading("Movimento", text = "Movimento")
tree.place(x=5, y=5)

#---------------------------------------
# Componentes abaixo da treeview
lbl_numero = Label(ConWindow, text="Número: ")
lbl_numero.place(x=230, y=310)

value_num = StringVar()
t_numero = Entry(ConWindow, width = 10, textvariable = value_num)
t_numero.place(x=330, y=310)

lbl_data = Label(ConWindow, text="Data: ")
lbl_data.place(x=230, y=330)

value_data = StringVar()
t_data = Entry(ConWindow, width = 10, textvariable = value_data)
t_data.place(x=330, y=330)

lbl_hora = Label(ConWindow, text="Hora: ")
lbl_hora.place(x=230, y=350)

value_hora = StringVar()
t_hora = Entry(ConWindow, width = 10, textvariable = value_hora)
t_hora.place(x=330, y=350)

lbl_mov = Label(ConWindow, text="Movimento: ")
lbl_mov.place(x=230, y=370)

value_mov = StringVar()
t_mov = Entry(ConWindow, width = 10, textvariable = value_mov)
t_mov.place(x=330, y=370)
btn_consultar1 = Button(ConWindow, width = 21, height= 2, text = "Obter Dados", relief = "raised", command = dados_linha_tree)
btn_consultar1.place(x=8, y=322)

btn_Update = Button(ConWindow, width = 21, height= 2, text = "Update TreeView", relief = "raised", command = renderizaTree)
btn_Update.place(x=450, y=322)

ConWindow.mainloop()