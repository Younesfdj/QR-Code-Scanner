from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import qrcode
from pyzbar.pyzbar import decode
import re
import webbrowser
import os,sys

def ressource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except:
        base_path=os.path.abspath(".")

    return os.path.join(base_path,relative_path)

root = Tk()
root.geometry('600x400+360+130')
root.config(bg='white')
root.resizable(False,False)

# dont foerget to place 'images' folder in same directory as main.py
root.iconbitmap(ressource_path('images/iconphoto.ico'))
root.title('Qr Code Scanner')
list = []

def quit():
    response = messagebox.askyesno('Exit window', 'Are you sure wanna quit ?')
    if response == 1:
        root.quit()
    else :
        return
def trace_contact(var, index, mode):
    if name.get() == '' :
        dow_but.place_forget()
    else:
        if phone.get()=='' and email.get()=='':
            dow_but.place_forget()
        else :
            dow_but.place(x=160, y=260)

def tracevar(var, index, mode):
    if content.get()=='':
        dow_but.place_forget()
    else :
        dow_but.place(x=160, y=230)

def back(oldframe,newframe):
    oldframe.place_forget()
    newframe.place(x=21,y=18)

def simple_text():
    global content
    global dow_but
    page2.place_forget()
    page3 = Frame(root, width=560, height=360, bg='white',highlightcolor='white',relief=SOLID,bd=1)
    page3.place(x=21,y=18)
    content = StringVar()
    content.trace_add('write',tracevar)
    dow_but = Button(page3, image=downloadic,bd=0, command=lambda: make_qr(text_entry.get(), name_entry.get(),page3),activebackground="white",cursor='hand2')
    text_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black',bd=0,bg='white',textvariable=content)
    name_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black',bd=0,bg='white')
    Label(page3, text='Content:', font=('Consolas', 16), bg="white", fg='black').place(x=78, y=40)
    Label(page3, text='File Name:', font=('Consolas', 16), bg="white", fg='black').place(x=78, y=125)
    text_entry.place(x=110, y=74)
    Label(page3, image=textic, bd=0, bg='white').place(x=81, y=78)
    Label(page3, image=line, bg="white", bd=0).place(x=110, y=93)

    name_entry.place(x=110, y=157)
    Button(page3, image=backic, bd=0, bg='white',activebackground='white',command=lambda :back(page3,page2),cursor='hand2',highlightcolor='white').place(x=2, y=2)
    Label(page3, image=fileic, bd=0, bg='white').place(x=81, y=159)
    Label(page3, image=line, bg="white", bd=0).place(x=110, y=176)

def web_adr():
    global dow_but
    global content
    page2.place_forget()
    page3 = Frame(root, width=560, height=360, bg='white', highlightcolor='white', relief=SOLID, bd=1)
    page3.place(x=21, y=18)
    Button(page3, image=backic, bd=0, bg='white',activebackground='white',command=lambda :back(page3,page2),cursor='hand2',highlightcolor='white').place(x=2, y=2)
    dow_but = Button(page3, image=downloadic, bd=0, command=lambda: make_qr(text_entry.get(), name_entry.get(),page3),activebackground="white", cursor='hand2')
    content = StringVar()
    content.trace_add('write', tracevar)
    text_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black', bd=0, bg='white',textvariable=content)
    name_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black', bd=0, bg='white')
    Label(page3, text='Url Adress:', font=('Consolas', 16), bg="white", fg='black').place(x=76, y=40)
    Label(page3, text='File Name:', font=('Consolas', 16), bg="white", fg='black').place(x=78, y=125)
    text_entry.place(x=110, y=74)
    Label(page3, image=urlic, bd=0, bg='white').place(x=81, y=74)
    Label(page3, image=line, bg="white", bd=0).place(x=110, y=93)

    name_entry.place(x=110, y=157)
    Label(page3, image=fileic, bd=0, bg='white').place(x=81, y=159)
    Label(page3, image=line, bg="white", bd=0).place(x=110, y=176)
    Button(page3, image=backic, bd=0, bg='white', activebackground='white', command=lambda: back(page3, page2),cursor='hand2', highlightcolor='white').place(x=2, y=2)

def perso_contact():
    global dow_but
    global name
    global phone
    global email

    page2.place_forget()
    page3 = Frame(root, width=560, height=360, bg='white', highlightcolor='white', relief=SOLID, bd=1)
    page3.place(x=21, y=18)

    name = StringVar()
    name.trace_add('write', trace_contact)
    name_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black', bd=0, bg='white',textvariable=name)
    name_entry.place(x=70, y=89)
    Label(page3, text='Name:', font=('Consolas', 16), bg="white", fg='black').place(x=36, y=54)
    Label(page3, image=namic, bd=0, bg='white').place(x=35, y=85)
    Label(page3, image=line, bg="white", bd=0).place(x=70, y=110)

    phone = StringVar()
    phone.trace_add('write', trace_contact)
    phonenbr_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black', bd=0, bg='white', textvariable=phone)
    phonenbr_entry.place(x=320, y=89)
    Label(page3, text='Phone Number:', font=('Consolas', 16), bg="white", fg='black').place(x=285, y=53)
    Label(page3, image=phonic, bd=0, bg='white').place(x=286, y=89)
    Label(page3, image=line, bg="white", bd=0).place(x=320, y=110)

    email = StringVar()
    email.trace_add('write', trace_contact)
    Label(page3, text='E-mail:', font=('Consolas', 16), bg="white", fg='black').place(x=34, y=135)
    email_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black', bd=0, bg='white',textvariable=email)
    email_entry.place(x=70, y=169)
    Label(page3, image=emailic, bd=0, bg='white').place(x=39, y=174)
    Label(page3, image=line, bg="white", bd=0).place(x=70, y=188)

    filename_entry = Entry(page3, width=18, font=('Circular Std', 12), relief=SOLID, fg='black', bd=0, bg='white')
    filename_entry.place(x=320,y=169)
    Label(page3, text='File Name:', font=('Consolas', 16), bg="white", fg='black').place(x=285, y=135)
    Label(page3, image=fileic, bd=0, bg='white').place(x=286, y=172)
    Label(page3, image=line, bg="white", bd=0).place(x=320, y=188)

    mode_info='perso_contact'
    dow_but = Button(page3, image=downloadic, bd=0, command=lambda: make_qr(mode_info, filename_entry.get(),page3,name_entry.get(),phonenbr_entry.get(),email_entry.get())
                     ,activebackground="white", cursor='hand2')
    Button(page3, image=backic, bd=0, bg='white',activebackground='white',command=lambda :back(page3,page2),cursor='hand2',highlightcolor='white').place(x=2, y=2)

def make_qr(text,name,frame,perso_name=None,perso_phone=None,perso_email=None):
    if text=='perso_contact':
        text={
            'Name':perso_name,
            'Phone number':perso_phone,
            'E-mail':perso_email
        }
    try:
        if name=="":
            messagebox.showerror('Error', 'File name is important !')
        else:
            qr = qrcode.make(text)
            string = str(name) + '.png'
            qr.save(string)
            Label(frame,image=doneic,bg='white',bd=0).place(x=170,y=320)
            Label(frame,text='Successfully downloaded', font=('Circular Std',13),fg='#0D851D',bg='white',bd=0).place(x=197,y=322)
    except:
        messagebox.showerror('Error!', 'Something went wrong !')

def generate_qr():
    global page2
    page1.place_forget()
    page2 = Frame(root, width=560, height=360, bg='white',highlightcolor='white',relief=SOLID,bd=1)
    page2.place(x=21,y=18)

    text_image = ImageTk.PhotoImage(Image.open(ressource_path('images/texticon.png')))
    list.append(text_image)
    Button(page2,image=text_image,bg='white',relief=SOLID,activebackground='white',cursor='hand2',highlightcolor='white',command=simple_text).place(x=246,y=30)

    web_image = ImageTk.PhotoImage(Image.open(ressource_path('images/webicon.png')))
    list.append(web_image)
    Button(page2, image=web_image, bg='white', relief=SOLID, activebackground='white', cursor='hand2',highlightcolor='white',command=web_adr).place(x=246,y=140)

    contact_image = ImageTk.PhotoImage(Image.open(ressource_path('images/contacticon.png')))
    list.append(contact_image)
    Button(page2,image=contact_image,bg='white',relief=SOLID, activebackground='white', cursor='hand2',highlightcolor='white',command=perso_contact).place(x=246,y=250)

    Label(page2,text='Simple',bg='white',fg='black',font=('Circular Std',18)).place(x=161,y=50)
    Label(page2, text='Text', bg='white', fg='black', font=('Circular Std', 18)).place(x=320, y=50)

    Label(page2, text='Web', bg='white', fg='black', font=('Circular Std', 18)).place(x=182, y=160)
    Label(page2, text='Adress', bg='white', fg='black', font=('Circular Std', 18)).place(x=322, y=160)

    Label(page2, text='Personal', bg='white', fg='black', font=('Circular Std', 18)).place(x=136, y=270)
    Label(page2, text='Contact', bg='white', fg='black', font=('Circular Std', 18)).place(x=320, y=270)
    Button(page2, image=backic, bd=0, bg='white', activebackground='white', command=lambda: back(page2,page1),cursor='hand2',highlightcolor='white').place(x=2,y=2)

def qrscan_func(frame):
    path = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=[("All files","*.*")])
    try :
        if path!='' :
            fr = Frame(frame, relief=SOLID, bd=2, width=400, height=220)
            fr.place(x=80, y=55)
            Label(fr, text='Output:', font=('Consolas', 16), fg='black').place(x=2, y=2)
            pic = Image.open(path)
            data = decode(pic)
            d = data[0].data.decode()
            t = 40
            if "'Name'" in d or "'E-mail'" in d or "'Phone number'" in d :
                d = re.sub("[}{']", '', d)
                d = d.split(',')
                for i in d :
                    var = StringVar()
                    var.set(i.strip())
                    Entry(fr, font=('Consolas', 12), fg='black', bd=0, bg='white', textvariable=var,state='readonly',width=40).place(x=2, y=t)
                    t+=30
            elif 'www' in d or 'https' in d or 'http' in d:
                var = StringVar()
                var.set(d.strip())
                Entry(fr, font=('Consolas', 12), fg='black', bd=0, bg='white', textvariable=var, state='readonly',width=40).place(x=2, y=t)
                Button(fr,image=openlink,bd=0,cursor='hand2',command=lambda :webbrowser.open(d.strip())).place(x=369,y=38)
            else :
                var = StringVar()
                var.set(d.strip())
                Entry(fr,font=('Consolas', 12), fg='black',bd=0,bg='white',textvariable=var,state='readonly',width=40).place(x=2, y=t)
    except:
        messagebox.showerror('Error', 'You selected the wrong format !')
    else :
        return

def qr_scanner():
    page1.place_forget()
    page2 = Frame(root, width=560, height=360, bg='white', highlightcolor='white', relief=SOLID, bd=1)
    page2.place(x=21, y=18)
    Button(page2, image=backic, bd=0, bg='white', activebackground='white', command=lambda: back(page2,page1),cursor='hand2',highlightcolor='white').place(x=2,y=2)
    Button(page2, image=scanic,activebackground="white",cursor='hand2',bd=0,bg='white',command=lambda:qrscan_func(page2)).place(x=160, y=300)


image1 = ImageTk.PhotoImage(Image.open(ressource_path('images/generator.png')))
image2 = ImageTk.PhotoImage(Image.open(ressource_path('images/scanner.png')))
line = ImageTk.PhotoImage(Image.open(ressource_path('images/line.png')))
fileic = ImageTk.PhotoImage(Image.open(ressource_path('images/fileic.png')))
backic = ImageTk.PhotoImage(Image.open(ressource_path('images/back.png')))
urlic = ImageTk.PhotoImage(Image.open(ressource_path('images/urlicon.png')))
textic = ImageTk.PhotoImage(Image.open(ressource_path('images/text.png')))
exitic = ImageTk.PhotoImage(Image.open(ressource_path('images/exit.png')))
downloadic = ImageTk.PhotoImage(Image.open(ressource_path('images/download.png')))
namic = ImageTk.PhotoImage(Image.open(ressource_path('images/nameic.png')))
phonic = ImageTk.PhotoImage(Image.open(ressource_path('images/phoneic.png')))
emailic = ImageTk.PhotoImage(Image.open(ressource_path('images/emailic.png')))
doneic = ImageTk.PhotoImage(Image.open(ressource_path('images/doneic.png')))
scanic = ImageTk.PhotoImage(Image.open(ressource_path('images/scan code.png')))
openlink = ImageTk.PhotoImage(Image.open(ressource_path('images/openlink.png')))

page1 = Frame(root, width=560, height=360, bg='white',highlightcolor='white',relief=SOLID,bd=1)
page1.place(x=21,y=18)

Button(page1,image=image1,bg='white',relief=SOLID,borderwidth=5,activebackground='white',highlightcolor='white',command=generate_qr,cursor='hand2').place(x=100,y=103)
Button(page1,image=image2,bg='white',relief=SOLID,borderwidth=5,activebackground='white',highlightcolor='white',cursor='hand2',command=qr_scanner).place(x=320,y=103)
Label(page1,text='QR code generator',fg='black',font=('Circular Std',15),bg='white').place(x=80,y=243)
Label(page1, text='QR code scanner', fg='black', font=('Circular Std', 15), bg='white').place(x=309,y=243)
Button(page1,image=exitic,bg='white',activebackground='white',command=quit,cursor='hand2',bd=0,highlightcolor='white').place(x=2,y=2)

root.mainloop()