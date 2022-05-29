from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from register import Register
from main import face_Recog



class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")
        
        bg_img = self.root.configure(bg='alice blue')

        frame=Frame(self.root,bg="black",bd=2)
        frame.place(x=450,y=150,width=400,height=400)

        img_bg = Image.open(r'C:\Users\hp\Desktop\Project\images\bgfor.jpg')
        img_bg = img_bg.resize((1500, 800), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(img_bg)
        imgbg_lbl = Label(self.root, image=self.photoimgbg)
        imgbg_lbl.place(x=0, y=0, width=1500, height=800)
        

        img = Image.open(r'C:\Users\hp\Desktop\Project\images\logo.png')
        img = img.resize((70, 70), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        img_lbl = Label(bg_img, image=self.photoimg)
        img_lbl.place(x=610, y=160, width=70, height=70)

        username=lbl=Label(bg_img,text='Username:',font=("times new roman",20,"bold"),fg="black")
        username.place(x=480,y=240)

        self.txt_user=ttk.Entry(bg_img,font=("times new roman",15,"bold"))
        self.txt_user.place(x=480,y=280,width=350,height=40)

        password=pw_lbl=Label(bg_img,text='Password:',font=("times new roman",20,"bold"),fg="black")
        password.place(x=480,y=350)

        self.txt_pw=ttk.Entry(bg_img,font=("times new roman",15,"bold"))
        self.txt_pw.place(x=480,y=390,width=350,height=40)

        login_btn=Button(bg_img,text="Login",command=self.main_wind,cursor="hand2",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        login_btn.place(x=620,y=450)

        newuser_btn=Button(bg_img,command=self.register_wind,text="Create new user",cursor="hand2",font=("times new roman",12,"bold"),fg="white",bg="black",borderwidth=0,activebackground="black",activeforeground="white")
        newuser_btn.place(x=597,y=510)


    def login(self):
        if self.txt_user.get()=="" or self.txt_pw.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        elif self.txt_user.get()=="garima" and self.txt_pw=="1234":
            messagebox.showinfo("Success","Login successful",parent=self.root)
        else:
            conn = mysql.connector.connect(
                    host="localhost", user="root", password="test@123", database="face_recognize", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from users where Email=%s and Password=%s",(
                self.email.get(),
                self.pw.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid login credentials",parent=self.root)  
            else:
                self.newwindow=Toplevel(self.newwindow)
                self.app=face_Recog(self.newwindow)

            conn.commit()
            conn.close()


            

    def main_wind(self):
        self.new_window = Toplevel(self.root)
        self.app =face_Recog(self.new_window)


    def register_wind(self):
        self.new_window = Toplevel(self.root)
        self.app =Register(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = login_system(root)
    root.mainloop()