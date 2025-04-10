import tkinter
from tkinter import Label, ttk
from tkinter import Entry
from tkinter import Frame
#----------------------------
#------ Hauptprogramm--------
#----------------------------

def check(userid,passwort):
    return userid == "Hi" and passwort == "123"

def login_app():
    print('Du warst hier')
    userid = ef_userid.get()
    passwort=ef_passwort.get()
    user_bekannt = check(userid, passwort)
    if user_bekannt:
        print('user bekannt')
    else:
        print('Angriff')


def close_app():
    window.destroy()

#----------------------------
#------ Hauptprogramm--------
#----------------------------
window = tkinter.Tk() #Tk ist ein Klasse
window.geometry('400x400')
window.resizable(False, False)
window.config(background='#f1e1f1')
window.title('Mein Programm')

my_frame = ttk.Frame(window,
                     borderwidth=2, relief="sunken"
                     )
my_frame.place(x=50,y=200, width=300, height=100)

lable_userid = Label(window,
                     text='UserID:',
                     font=('Arial', 14),
                     background='#f1e1f1'
                     )
lable_userid.place(x=20, y=50)

ef_userid = Entry(window,
                  width=20,
                  font=('Arial', 14),
                  background='#ffffff')
ef_userid.place(x=150,y=50)

label_passwort = Label(window,
                       text='UserID:',
                       font=('Arial', 14),
                       background='#f1e1f1'
                       )
label_passwort.place(x=20, y=100)

ef_passwort = Entry(window,
                  width=20,
                  font=('Arial', 14),
                  background='#ffffff',
                  show='*')
ef_passwort.place(x=150,y=100)


botton_login = tkinter.Button(my_frame,
                              text='Login',
                              command=login_app,
                              width=10,
                              font=('Calibri',14)
                             )
botton_login.place(x=30, y=30)

botton_close = tkinter.Button(my_frame,
                              text='Close',
                              command=close_app,
                              width=10,
                              font=('Calibri',14)
                              )
botton_close.place(x=150, y=30)


window.mainloop()
