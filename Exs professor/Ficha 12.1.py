# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk # treeview
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk  


# Percorre toda a listbox e atualiza a variãvel lista
def lista_imagens():
  lista.clear()                                 # Limpa a lista de imagens a visualizar
  cont = lboxImg.size()                         # nº linhas na listbox
  for indice in range (cont):                   # para cada linha da listbox
     ficheiro = lboxImg.get(indice)             # Obtem conteúdo da linha da listbox
     img = ImageTk.PhotoImage(file = ficheiro)  # renderiza imagem a partir do ficheiro 
     lista.append(img)                          # criar imagem na lista de imagens


# seleciona imagem em disco e adiciona à listBox
def escolhe_imagem():
  # file dialog, para selecionar ficheiro em disco
  filename = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files", "*.png"), ("all files","*.*")))
# adiciona à listBox
  lboxImg.insert("end", filename)
  lista_imagens()
 
# Remove imagem da listBox
def remove_listbox():
  #remove da lisbox o item selecionado
  lboxImg.delete(lboxImg.curselection())
  lista_imagens()


def primeira_foto():
  global indexImagem
  indexImagem = 0
 # atualiza imagem no canvas
  canvas.itemconfig(imageId, image=lista[indexImagem])


def ultima_foto():
  global indexImagem
  indexImagem = len(lista)-1
 # atualiza imagem no canvas
  canvas.itemconfig(imageId, image=lista[indexImagem])


def anterior_foto():
   global indexImagem
   if indexImagem > 0:
         indexImagem-=1
 # atualiza imagem no canvas
   canvas.itemconfig(imageId, image=lista[indexImagem])


def seguinte_foto():
   global indexImagem
   indexImagem+=1
   if indexImagem > len(lista) - 1:
      indexImagem = len(lista)-1
 # atualiza imagem no canvas
   canvas.itemconfig(imageId, image=lista[indexImagem])


# ----- INICIO DA EXECUÇÃO DA APP
indexImagem =0     # índice (na lista) da imagem atual - a ser visualizada
lista = []         # Lista com imagems adicionadas à Listbox

window=Tk()        # invoca classe tk , cria a "main window"
window.geometry("700x450")
window.title('Gestor de Fotos')

lboxImg = Listbox(window, width = 40, height = 12, bd = "3", relief = "sunken")
lboxImg.place(x=10, y=30)


#----- Button 1 -------
btnAdicionar = Button(window, text = "Selecionar imagem", width=34, height = 3, command = escolhe_imagem)
btnAdicionar.place(x=10, y=250)

#----- Button 2 -------
btnEliminar = Button(window, text = "Remover imagem", width = 34, height = 3, command = remove_listbox)
btnEliminar.place(x=10, y=320)


# Panel -----------------------------------------
panel1 = PanedWindow(window, width = 320, height = 190, bd = "3", relief = "sunken")
panel1.place(x=300, y=30)

# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
canvas = Canvas(panel1, width = 280, height = 150, bd = 4, relief = "sunken")
canvas.place(x=10, y=10)

img = ImageTk.PhotoImage(file = "Imagens/profile.png")
# set first image on canvas
imageId = canvas.create_image(0, 0, anchor='nw', image=img)

#----- Button imagem PRIMEIRA -------
btnPrimeira = Button(window, text = "<<", width = 10, command = primeira_foto)
btnPrimeira.place(x=300, y=250)

#----- Button imagem ANTERIOR -------
btnAnt = Button(window, text = "<", width = 10, command = anterior_foto)
btnAnt.place(x=380, y=250)

#----- Button imagem SEGUINTE -------
btnSeguinte = Button(window, text = ">", width = 10, command = seguinte_foto)
btnSeguinte.place(x=460, y=250)

#----- Button imagem ULTIMA -------
btnUltima = Button(window, text = ">>", width = 10, command = ultima_foto)
btnUltima.place(x=540, y=250)

window.mainloop()   # event listening loop by calling the mainloop()