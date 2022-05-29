from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
from studentdet import Student
from attendance import Attendance
from recognizer import Recognize
import os


class face_Recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x800+0+0")
        self.root.title('face recognition')

        bg_img = self.root.configure(bg='alice blue')

        title_lbl = Label(self.root, text="Face Recognition Attendance System", font=(
            "times new roman", 35, "bold"), bg='alice blue', fg="black")
        title_lbl.place(x=-30, y=0, width=1400, height=50)

        # function to display current time
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman",
                    12, "bold"), bg="white", fg="black")
        lbl.place(x=30, y=0, width=100, height=30)
        time()

        # creating the required buttons to navigate through the application
        img_bg = Image.open(r'C:\Users\hp\Desktop\Project\images\bg.png')
        img_bg = img_bg.resize((600, 550), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        img_lbl = Label(self.root, image=self.photoimg_bg)
        img_lbl.place(x=50, y=80, width=600, height=550)

        img = Image.open(r'C:\Users\hp\Desktop\Project\images\stud.png')
        img = img.resize((50, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1 = Button(self.root, image=self.photoimg,
                    command=self.student_details, cursor="hand2")
        b1.place(x=750, y=100, width=50, height=50)
        b1_text = Button(self.root, text="Student details",
                         command=self.student_details, cursor="hand2", bg='white')
        b1_text.place(x=810, y=100, width=200, height=50)

        img2 = Image.open(r'C:\Users\hp\Desktop\Project\images\addatte.png')
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(self.root, image=self.photoimg2,
                    cursor="hand2", command=self.face_data)
        b2.place(x=750, y=200, width=50, height=50)
        b2_text = Button(self.root, text="Add attendance",
                         cursor="hand2", command=self.face_data, bg='white')
        b2_text.place(x=810, y=200, width=200, height=50)

        img3 = Image.open(r'C:\Users\hp\Desktop\Project\images\attend.jpg')
        img3 = img3.resize((50, 50), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(self.root, image=self.photoimg3,
                    cursor="hand2", command=self.attendance_data)
        b3.place(x=750, y=300, width=50, height=50)
        b3_text = Button(self.root, text="Attendance Record",
                         cursor="hand2", command=self.attendance_data, bg='white')
        b3_text.place(x=810, y=300, width=200, height=50)

        img5 = Image.open(r'images\phot.jpg')
        img5 = img5.resize((50, 50), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b5 = Button(self.root, image=self.photoimg5,
                    cursor="hand2", command=self.open_img)
        b5.place(x=750, y=400, width=50, height=50)
        b5_text = Button(self.root, text="Images", cursor="hand2",
                         command=self.open_img, bg='white')
        b5_text.place(x=810, y=400, width=200, height=50)

        img6 = Image.open(r'C:\Users\hp\Desktop\Project\images\exit.jpg')
        img6 = img6.resize((50, 50), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b6 = Button(self.root, image=self.photoimg6,
                    cursor="hand2", command=self.exit_page)
        b6.place(x=750, y=500, width=50, height=50)
        b6_text = Button(self.root, text="Exit", cursor="hand2",
                         command=self.exit_page, bg='white')
        b6_text.place(x=810, y=500, width=200, height=50)

    # these functions are defined to link new windows that are opened on clicking the above given buttons
    def open_img(self):
        os.startfile("image")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Recognize(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def exit_page(self):
        self.exit_page = tkinter.messagebox.askyesno(
            "Exit Window", "Are you sure you want to exit?", parent=self.root)
        if self.exit_page > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = face_Recog(root)
    root.mainloop()
