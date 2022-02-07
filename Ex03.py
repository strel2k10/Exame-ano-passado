from queue import Empty
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
import os



window = Tk()
window.geometry("800x600")
window.title("EXAME AED")

timers_file = "tempos.txt"
activities_file = "atividades.txt"
setup_file = "setup.txt"
notifications_file = "AgendaProvas.txt"

Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()

def chose_image():
    filepath = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files", "*.png"), ("all files","*.*")))
    # # adiciona à listBox
    # lboxImg.insert("end", filename)
    # lista_imagens()

    image = Image.open(filepath)
    img = PhotoImage(file = filepath)
    canvas_logo.create_image(64,64, image=img)       
    canvas_logo.image = img

    f = open(setup_file, "a")
    linha = os.path.basename(filepath) + ";" + filepath + "\n"
    f.write(linha)
    f.close()
    
def show_notifications(check_5k, check_10k,check_21k):
    l_notifications.delete(0,END)   
    if Checkbutton1.get() == 1:
        f = open(notifications_file, "r")
        lista = f.readlines()
        f.close()

        for linha in lista:
            #campos = linha.split(";")
            formatted_campos = []
            formatted_campos.extend(linha.strip().split(";"))
            #formatted_campos = campos.rstrip("\n")
            if formatted_campos[1] == "5K":
                l_notifications.insert(END,formatted_campos[0])
    if Checkbutton2.get() == 1:      
        f = open(notifications_file, "r")
        lista = f.readlines()
        f.close()

        for linha in lista:
            #campos = linha.split(";")
            formatted_campos = []
            formatted_campos.extend(linha.strip().split(";"))
            #formatted_campos = campos.rstrip("\n")
            if formatted_campos[1] == "10K":
                l_notifications.insert(END,formatted_campos[0])

    if Checkbutton3.get() == 1:        
        f = open(notifications_file, "r")
        lista = f.readlines()
        f.close()

        for linha in lista:
            #campos = linha.split(";")
            formatted_campos = []
            formatted_campos.extend(linha.strip().split(";"))
            #formatted_campos = campos.rstrip("\n")
            if formatted_campos[1] == "21K":
                l_notifications.insert(END,formatted_campos[0])


               
           
        # for notification in lista:
        #     formatted_notification = notification.rstrip("\n")
        #     #re.sub('\s+','',user_type)
        #     l_notifications.insert(END, formatted_notification)
            



panel1 = PanedWindow(window,width=300, height=500, bd=2, relief="sunken")
panel1.place(x= 20, y= 20 )

label_my_laps = Label(panel1, text="As Minhas Provas", fg="black", font=("Rubik Bold",12))
label_my_laps.place(x=80, y=50)

label_select_logo = Label(panel1, text="Logotipo da prova:", fg="black", font=("Rubik",10))
label_select_logo.place(x=15, y=120)

btn1 = Button(panel1, text="Selecionar", width=10, height=1 , font=("Rubik",12),  bg="light gray", command = partial(chose_image))
btn1.place(x=130,y=110)

btn2 = Button(panel1, text="Guardar", width=25, height=1 , font=("Rubik",12),  bg="light gray", command = "")
btn2.place(x=30,y=440)

panel2 = PanedWindow(window,width=200, height=200, bd=2, relief="sunken")
panel2.place(x= 90, y= 210)
canvas_logo = Canvas(panel2, width=200, height=200)
canvas_logo.place(x=0, y=0)



panel3 = PanedWindow(window,width=430, height=500, bd=2, relief="sunken")
panel3.place(x= 350, y= 20 )

label_my_notifications = Label(panel3, text="As Minhas Notificações", fg="black", font=("Rubik Bold",12))
label_my_notifications.place(x=80, y=50)

label_my_notifications_type = Label(panel3, text="Ver Notificações de:", fg="black", font=("Rubik Bold",12))
label_my_notifications_type.place(x=60, y=100)


check_5k = Checkbutton(panel3, text = "5k", variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 10)
check_5k.place(x=20, y = 120)

check_10k = Checkbutton(panel3, text = "10k", variable = Checkbutton2, onvalue = 1, offvalue = 0, height = 2, width = 10)
check_10k.place(x=120, y = 120)

check_21k = Checkbutton(panel3, text = "21k", variable = Checkbutton3, onvalue = 1, offvalue = 0, height = 2, width = 10)
check_21k.place(x=220, y = 120)

btn2 = Button(panel3, text="Ver", width=25, height=1 , font=("Rubik",12),  bg="light gray", command = partial(show_notifications,check_5k, check_10k,check_21k))
btn2.place(x=30,y=200)

l_notifications = Listbox(panel3, width = 50, height = 10, relief = "sunken", font = ("Helvetica", "10"))
l_notifications.place (x=30,y=250)

# f = open(activities_file, "r")

# lista = f.readlines()
# f.close()
# for activity in lista:
#     formatted_activity = activity.rstrip("\n")
#     #re.sub('\s+','',user_type)
#     l_activities.insert(END, formatted_activity)




# panel2 = PanedWindow(window,width=200, height=200, bg="white", bd=2, relief="sunken")
# panel2.place(x= 20, y= 300 )










# btn2 = Button(window, text="+", width=2, height=1 ,bg="gray",  fg="white", font=("Rubik",12), command = "")
# btn2.place(x=235,y=120)

# btn3 = Button(panel5, text="Filtrar", width=8, height=3 ,bg="gray",  fg="white", font=("Rubik",12), command = "")
# btn3.place(x=250,y=10)




window.mainloop()