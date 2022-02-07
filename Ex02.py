from queue import Empty
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
from functools import partial


window = Tk()
window.geometry("800x600")
window.title("EXAME AED")

timers_file = "tempos.txt"
activities_file = "atividades.txt"



def data_treeview(l_activities, tree):  # Remove TODAS as linhas da Treeview
    tree.delete(*tree.get_children())
    activity_type = l_activities.get(l_activities.curselection())
    formatted_activity_type = activity_type.rstrip("\n")
    #num_laps = entry_num_laps.get()  
    #messagebox.showinfo("test1", activity_type)

    f = open(timers_file, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    num_laps = 0
    timers = []
    for linha in lista:
        campos = linha.split(";")
        if campos[3].rstrip("\n") == formatted_activity_type:
            #messagebox.showinfo("test2", user_type)
            timers.append(campos[2])
            tree.insert("", "end", values = (campos[0],campos[1], campos[2],campos[3]))
            num_laps = num_laps + 1

    entry_num_laps.configure(state="normal")
    entry_num_laps.delete(0, END)
    entry_num_laps.insert(END, num_laps)
    entry_num_laps.configure(state="disabled")

    
    entry_best_time.configure(state="normal")
    entry_best_time.delete(0, END)
    entry_best_time.insert(END, min(timers))
    entry_best_time.configure(state="disabled")


panel1 = PanedWindow(window,width=200, height=200, bg="white", bd=2, relief="sunken")
panel1.place(x= 20, y= 20 )

l_activities = Listbox(panel1, width = 18, height = 10, relief = "sunken", font = ("Helvetica", "14"))
l_activities.place (x=0,y=0)

f = open(activities_file, "r")

lista = f.readlines()
f.close()
for activity in lista:
    formatted_activity = activity.rstrip("\n")
    #re.sub('\s+','',user_type)
    l_activities.insert(END, formatted_activity)




panel2 = PanedWindow(window,width=200, height=200, bg="white", bd=2, relief="sunken")
panel2.place(x= 20, y= 300 )

canvas_profile = Canvas(panel2, width=200, height=200)
canvas_profile.place(x=0, y=0)   

#login_image = Image.open("images/profile.png")
img = PhotoImage(file ="Imagens/profile.png")
canvas_profile.create_image(64,64, image=img)       
canvas_profile.image = img

panel3 = PanedWindow(window,width=500, height=200, bg="white", bd=2, relief="sunken")
panel3.place(x= 280, y= 20 )

tree = ttk.Treeview(panel3, selectmode = "browse", columns = ("Data", "Prova", "Tempo"), show = "headings")

tree.column("Data", width = 170,   anchor="c")
tree.column("Prova", width = 170,  anchor="c") 
tree.column("Tempo", width = 170,  anchor="c")    # c- center, e - direita, w- esquerda
tree.heading("Data", text = "Data")
tree.heading("Prova", text = "Prova")
tree.heading("Tempo", text = "Tempo")
tree.place(x=5, y=5)

panel4 = PanedWindow(window,width=500, height=50, bd=2, relief="sunken")
panel4.place(x= 280, y= 260 )

label_num_laps = Label(panel4, text="Número de provas:", fg="black", font=("Rubik",12))
label_num_laps.place(x=10, y=10)

entry_num_laps = Entry(panel4, width= 8, font=("Rubik",12))
entry_num_laps.configure(state="disabled")
entry_num_laps.place(x=150, y=10)


label_best_time = Label(panel4, text="Melhor Tempo:", fg="black", font=("Rubik",12))
label_best_time.place(x=280, y=10)

entry_best_time = Entry(panel4, width= 8, font=("Rubik",12))
entry_best_time.configure(state="disabled")
entry_best_time.place(x=400, y=10)



panel5 = PanedWindow(window,width=500, height=100, bd=2, relief="sunken")
panel5.place(x= 280, y= 350 )

label_filter_lap = Label(panel5, text="Prova:", fg="black", font=("Rubik",12))
label_filter_lap.place(x=10, y=10)

entry_lap = Entry(panel5, width= 15, font=("Rubik",12))
#entry_lap.insert(END, "Enter the new category name here")
entry_lap.place(x=65, y=10)

btn1 = Button(window, text=">", width=2, height=1 ,bg="gray",  fg="white", font=("Rubik",12), command = partial(data_treeview, l_activities, tree))
btn1.place(x=235,y=80)

btn2 = Button(window, text="+", width=2, height=1 ,bg="gray",  fg="white", font=("Rubik",12), command = "")
btn2.place(x=235,y=120)

btn3 = Button(panel5, text="Filtrar", width=8, height=3 ,bg="gray",  fg="white", font=("Rubik",12), command = "")
btn3.place(x=250,y=10)




window.mainloop()