
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1500x800+0+0")

        self.fname=StringVar()
        self.lname=StringVar()
        self.email=StringVar()
        self.pw=StringVar()
        self.cpw=StringVar()


        bg_img = self.root.configure(bg='alice blue')

        img_bg = Image.open(r'C:\Users\hp\Desktop\Project\images\backg.jpg')
        img_bg = img_bg.resize((1500, 800), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(img_bg)
        imgbg_lbl = Label(self.root, image=self.photoimgbg)
        imgbg_lbl.place(x=0, y=0, width=1500, height=800)

        frame=Frame(self.root,bg="white")
        frame.place(x=200,y=130,width=900,height=400)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=5,y=10)

        fname=Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=5,y=80)
        fname_entry=ttk.Entry(frame,textvariable=self.fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=170,y=80)

        lname=Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=5,y=130)
        lname_entry=ttk.Entry(frame,textvariable=self.lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=170,y=130)

        username=Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=5,y=180)
        username_entry=ttk.Entry(frame,textvariable=self.email,font=("times new roman",15,"bold"))
        username_entry.place(x=170,y=180)

        pw=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        pw.place(x=5,y=230)
        pw_entry=ttk.Entry(frame,textvariable=self.pw,font=("times new roman",15,"bold"))
        pw_entry.place(x=170,y=230)

        cpw=Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpw.place(x=5,y=280)
        cpw_entry=ttk.Entry(frame,textvariable=self.cpw,font=("times new roman",15,"bold"))
        cpw_entry.place(x=170,y=280)
 
        self.var_check=IntVar()      
        check_btn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms and conditions",font=("times new roman",12,"bold"))
        check_btn.place(x=5,y=340)
        

        img_box = Image.open(r'C:\Users\hp\Desktop\Project\images\reg.jpg')
        img_box = img_box.resize((400, 300), Image.ANTIALIAS)
        self.photoimgbox = ImageTk.PhotoImage(img_box)
        imgbox_lbl = Label(frame, image=self.photoimgbox)
        imgbox_lbl.place(x=450, y=50, width=400, height=300)

        img_reg=Image.open(r'images/register.jpg')
        img_reg=img_reg.resize((200,55),Image.ANTIALIAS)
        self.photo_imgreg=ImageTk.PhotoImage(img_reg)
        register_btn=Button(frame,image=self.photo_imgreg,command=self.register_data,borderwidth=0,cursor="hand2",fg="white")
        register_btn.place(x=580,y=300,width=200)

    #    function


    def register_data(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.email.get()=="" or self.pw.get()=="" or self.cpw.get()=="":
            messagebox.showerror("Error","Fields are required",parent=self.root)
        elif self.cpw.get()!=self.pw.get():
            messagebox.showerror("Error","Passwords do not match",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the terms and conditions",parent=self.root)
        else:
            conn = mysql.connector.connect(
                    host="localhost", user="root", password="test@123", database="face_recognize", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            query=("select * from users where Email=%s")
            value=(self.email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                my_cursor.execute("insert into users values(%s,%s,%s,%s,%s,%s)",(
                    self.fname.get(),
                    self.lname.get(),
                    self.email.get(),
                    self.pw.get(),
                    self.cpw.get(),
                    self.var_check.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registeration complete",parent=self.root)
            else:
                messagebox.showerror("Error","User already exists.",parent=self.root)

        
        
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()        