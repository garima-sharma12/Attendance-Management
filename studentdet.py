from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x800+0+0")
        self.root.title('face recognition')

        self.dep = StringVar()
        self.batch = StringVar()
        self.sem = StringVar()
        self.name = StringVar()
        self.gender = StringVar()
        self.id = StringVar()
        self.dob = StringVar()
        self.option = StringVar()
        self.opt_var = StringVar()

        title_lbl = Label(self.root, text="STUDENT DETAILS", font=(
            "times new roman", 25, "bold"), fg="black")
        title_lbl.place(x=-100, y=0, width=1400, height=50)

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=5, y=70, width=1400, height=570)

    # left window frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        left_frame.place(x=20, y=10, width=600, height=550)

    # labels and respective entry boxes and buttons
        dep_lbl = Label(left_frame, text="Department",
                        font=("times new roman", 12, "bold"))
        dep_lbl.grid(row=0, column=0)

        dep_option = ttk.Combobox(left_frame, textvariable=self.dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_option["values"] = (
            "Select Department", "CSE", "ECE", "EEE", "Civil", "Mechanical", "Architecture")
        dep_option.current(0)
        dep_option.grid(row=0, column=1, padx=5, pady=10)

        year_lbl = Label(left_frame, text="Batch Year",
                         font=("times new roman", 12, "bold"))
        year_lbl.grid(row=1, column=0)

        year_option = ttk.Combobox(left_frame, textvariable=self.batch, font=(
            "times new roman", 12, "bold"), state="readonly")
        year_option["values"] = (
            "Select Year", "2022", "2023", "2024", "2025", "2026")
        year_option.current(0)
        year_option.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        sem_lbl = Label(left_frame, text="Semester",
                        font=("times new roman", 12, "bold"))
        sem_lbl.grid(row=2, column=0)

        sem_option = ttk.Combobox(left_frame, textvariable=self.sem, font=(
            "times new roman", 12, "bold"), state="readonly")
        sem_option["values"] = ("Select Semester", "1",
                                "2", "3", "4", "5", "6", "7", "8")
        sem_option.current(0)
        sem_option.grid(row=2, column=1, padx=5, pady=10)

        name_lbl = Label(left_frame, text="Student Name",
                         font=("times new roman", 12, "bold"))
        name_lbl.grid(row=3, column=0)
        name_box = Entry(left_frame, textvariable=self.name,
                         width=20, font=("times new roman", 13, "bold"))
        name_box.grid(row=3, column=1, padx=5, pady=10)

        gen_lbl = Label(left_frame, text="Gender",
                        font=("times new roman", 12, "bold"))
        gen_lbl.grid(row=4, column=0)
        gen_option = ttk.Combobox(left_frame, textvariable=self.gender, font=(
            "times new roman", 12, "bold"), state="readonly")
        gen_option["values"] = ("Select gender", "Male", "Female", "Other")
        gen_option.current(0)
        gen_option.grid(row=4, column=1, padx=5, pady=10)

        id_lbl = Label(left_frame, text="Student ID",
                       font=("times new roman", 12, "bold"))
        id_lbl.grid(row=5, column=0)
        id_box = Entry(left_frame, textvariable=self.id,
                       width=20, font=("times new roman", 13, "bold"))
        id_box.grid(row=5, column=1, padx=5, pady=10)

        dob_lbl = Label(left_frame, text="DOB", font=(
            "times new roman", 12, "bold"))
        dob_lbl.grid(row=6, column=0)
        dob_box = Entry(left_frame, textvariable=self.dob,
                        width=20, font=("times new roman", 13, "bold"))
        dob_box.grid(row=6, column=1, padx=5, pady=10)

        self.radbt1 = StringVar()
        rd_bt1 = ttk.Radiobutton(
            left_frame, variable=self.radbt1, text="Input Image", value="Yes")
        rd_bt1.grid(row=7, column=0)

        rd_bt2 = ttk.Radiobutton(
            left_frame, variable=self.radbt1, text="No Input", value="No")
        rd_bt2.grid(row=7, column=1)

        # buttons for update,reset,save,delete options
        btn_frm = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frm.place(x=5, y=400, width=590, height=70)

        save_btn = Button(btn_frm, command=self.add_data, text="Save Data", width=14, font=(
            "times new roman", 13, "bold"), bg="beige")
        save_btn.grid(row=0, column=0)

        del_btn = Button(btn_frm, command=self.delete_data, text="Delete", width=14, font=(
            "times new roman", 13, "bold"), bg="beige")
        del_btn.grid(row=0, column=1)

        rst_btn = Button(btn_frm, command=self.reset_data, text="Reset", width=14, font=(
            "times new roman", 13, "bold"), bg="beige")
        rst_btn.grid(row=0, column=2)

        upd_btn = Button(btn_frm, command=self.update_data, text="Update", width=14, font=(
            "times new roman", 13, "bold"), bg="beige")
        upd_btn.grid(row=0, column=3, sticky=W)

        # button for taking a picture anf updating one
        btn_frm2 = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frm2.place(x=5, y=435, width=590, height=35)

        tkpic_btn = Button(btn_frm2, command=self.generate_data, text="Take photo", width=30, font=(
            "times new roman", 13, "bold"), bg="beige")
        tkpic_btn.grid(row=0, column=0)

        updpic_btn = Button(btn_frm2, command=self.update_data, text="Update photo", width=30, font=(
            "times new roman", 13, "bold"), bg="beige")
        updpic_btn.grid(row=0, column=1, sticky=W)

    #    right window frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Record", font=(
            "times new roman", 12, "bold"))
        right_frame.place(x=630, y=10, width=600, height=550)

    #  search frame
        search_frm = LabelFrame(right_frame, relief=RIDGE, text="Search System", font=(
            "times new roman", 12, "bold"))
        search_frm.place(x=5, y=5, width=580, height=100)
        search_lbl = Label(search_frm, text="Search by", font=(
            "times new roman", 12, "bold"), bg="purple", fg="white")
        search_lbl.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        opt = ttk.Combobox(search_frm, textvariable=self.opt_var, font=(
            "times new roman", 12, "bold"), state="readonly")
        opt["values"] = ("Search", "ID", "Name", "Department",
                         "Batch Year", "Semester")
        opt.current(0)
        opt.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        opt_box = Entry(search_frm, textvariable=self.option, width=15, font=(
            "times new roman", 13, "bold"))
        opt_box.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        search_btn = Button(search_frm, command=self.search, text="Search", width=6, font=(
            "times new roman", 13, "bold"), bg="beige")
        search_btn.grid(row=0, column=3, sticky=W)

        reset_btn = Button(search_frm, command=self.reset_for_search, text="Reset", width=6, font=(
            "times new roman", 13, "bold"), bg="beige")
        reset_btn.grid(row=0, column=4, sticky=W)

        # student table to display students detail
        table_frm = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frm.place(x=5, y=120, width=600, height=400)

        scroll_x = ttk.Scrollbar(table_frm, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm, orient=VERTICAL)

        self.student_tbl = ttk.Treeview(table_frm, column=(
            "dep", "year", "sem", "name", "gender", "id", "dob", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_tbl.xview)
        scroll_y.config(command=self.student_tbl.yview)

        self.student_tbl.heading("dep", text="Department")
        self.student_tbl.heading("year", text="Year")
        self.student_tbl.heading("sem", text="Semester")
        self.student_tbl.heading("name", text="Name")
        self.student_tbl.heading("gender", text="gender")
        self.student_tbl.heading("id", text="ID")
        self.student_tbl.heading("dob", text="DOB")
        self.student_tbl.heading("photo", text="Photo status")

        self.student_tbl["show"] = "headings"

        self.student_tbl.column("dep", width=100)
        self.student_tbl.column("year", width=100)
        self.student_tbl.column("sem", width=100)
        self.student_tbl.column("name", width=100)
        self.student_tbl.column("gender", width=100)
        self.student_tbl.column("id", width=100)
        self.student_tbl.column("dob", width=100)
        self.student_tbl.column("photo", width=100)

        self.student_tbl.pack(fill=BOTH, expand=1)
        self.student_tbl.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

# functions for creating,adding,updating,deleting data in the student table

    def add_data(self):
        # displays error if one of the given fields is mising
        if self.dep.get() == "Select Department" or self.batch == "Select Year" or self.sem == "Select Semester" or self.name.get() == "" or self.id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="test@123", database="face_recognize", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.dep.get(),
                    self.batch.get(),
                    self.sem.get(),
                    self.name.get(),
                    self.gender.get(),
                    self.id.get(),
                    self.dob.get(),
                    self.radbt1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data saved", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="test@123",
                                       database="face_recognize", auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_tbl.delete(*self.student_tbl.get_children())
            for i in data:
                self.student_tbl.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_tbl.focus()
        content = self.student_tbl.item(cursor_focus)
        data = content["values"]

        self.dep.set(data[0]),
        self.batch.set(data[1]),
        self.sem.set(data[2]),
        self.name.set(data[3]),
        self.gender.set(data[4]),
        self.id.set(data[5]),
        self.dob.set(data[6]),
        self.radbt1.set(data[7])

    def update_data(self):
        if self.dep.get() == "Select Department" or self.batch == "Select Year" or self.sem == "Select Semester" or self.name.get() == "" or self.id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to update the student detials", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="test@123", database="face_recognize", auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,DOB=%s,Input_image=%s where ID=%s", (
                        self.dep.get(),
                        self.batch.get(),
                        self.sem.get(),
                        self.name.get(),
                        self.gender.get(),
                        self.dob.get(),
                        self.radbt1.get(),
                        self.id.get(),
                    ))
                    face_classifier = cv2.CascadeClassifier(
                        "haarcascade_frontalface_default.xml")

                # deleting the previously captured images
                    id = self.id.get()
                    for img_id in range(1, 101):
                        os.remove(
                            f'C:/Users/hp/Desktop/Project/data/user.{id}.{img_id}.jpg')

                    def face_resize(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            face_resize = img[y:y+h, x:x+w]
                            return face_resize
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        val, frame = cap.read()
                        img_id = img_id+1
                        face_norm = cv2.resize(frame, (450, 450))
                        face = cv2.cvtColor(face_norm, cv2.COLOR_BGR2GRAY)
                        features = face_classifier.detectMultiScale(
                            face, 1.3, 5)
                        cv2.putText(face, str(
                            img_id), (50, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Face", face)
                        file_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        if val:
                            cv2.imwrite(file_path, face)
                        if int(img_id) > 70 and int(img_id) <= 80:
                            file_path2 = "image/user." + \
                                str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_path2, face)
                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student details updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    def delete_data(self):
        if self.id.get() == "":
            messagebox.showerror(
                "Error", "Student id is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete", "Do you want to delete the data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="test@123", database="face_recognize", auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID=%s"
                    val = (self.id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Data deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    def reset_data(self):
        self.dep.set("Select Department")
        self.batch.set("Select Year")
        self.sem.set("Select Semester")
        self.name.set("")
        self.gender.set("Select gender")
        self.id.set("")
        self.dob.set("")
        self.radbt1.set("")

    def generate_data(self):
        if self.dep.get() == "Select Department" or self.batch == "Select Year" or self.sem == "Select Semester" or self.name.get() == "" or self.id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="test@123", database="face_recognize", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()

                my_cursor.execute("update student set Department=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,DOB=%s,Input_image=%s where ID=%s", (
                    self.dep.get(),
                    self.batch.get(),
                    self.sem.get(),
                    self.name.get(),
                    self.gender.get(),
                    self.dob.get(),
                    self.radbt1.get(),
                    self.id.get(),
                ))
                id = self.id.get()
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_resize(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_resize = img[y:y+h, x:x+w]
                        return face_resize
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    val, frame = cap.read()
                    img_id = img_id+1
                    face_norm = cv2.resize(frame, (450, 450))
                    face = cv2.cvtColor(face_norm, cv2.COLOR_BGR2GRAY)
                    features = face_classifier.detectMultiScale(face, 1.3, 5)
                    cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Face", face)
                    file_path = "data/user." + str(id)+"."+str(img_id)+".jpg"
                    if val:
                        cv2.imwrite(file_path, face)
                    if int(img_id) > 70 and int(img_id) <= 80:
                        file_path2 = "image/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path2, face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success", "Data set generated",parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    def search(self):
        self.student_tbl.selection()
        data = self.student_tbl.get_children()
        for d in data:
            self.student_tbl.delete(d)
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="test@123",
                                           database="face_recognize", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()

            option = self.opt_var.get()
            if option == 'ID':
                query = "select * from student where ID=%s"
            elif option == 'Name':
                query = "select * from student where Name='%s'"
            elif option == 'Department':
                query = "select * from student where Department='%s'"
            elif option == 'Batch Year':
                query = "select * from student where Year=%s"
            elif option == 'Semester':
                query = "select * from student where Semester=%s"
            else:
                messagebox.showerror("Error", 'Please select an option',parent=self.root)

            get_option = self.option.get()
            my_cursor.execute(query % (get_option))
            new_data = my_cursor.fetchall()
            for d in new_data:
                self.student_tbl.insert("", END, values=d)
        except Exception as es:
            messagebox.showerror("Error", f"Due to:{str(es)}",parent=self.root)
        conn.close()

    def reset_for_search(self):
        self.fetch_data()


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
