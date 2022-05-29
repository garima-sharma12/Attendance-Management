
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL import Image, ImageTk

import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x800+0+0")
        self.root.title('Attendance')

       
        title_lbl = Label(self.root, text="Attendance", font=(
            "times new roman", 25, "bold"), fg="black")
        title_lbl.place(x=-100, y=0, width=1400, height=50)

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=5, y=70, width=1400, height=570)

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance", font=(
            "times new roman", 12, "bold"))

        left_frame.place(x=20, y=10, width=600, height=550)

        # labels and entries for the left side of the window
        label_id = Label(left_frame, text="Attendance ID:",
                         font=("times new roman", 12, "bold"))
        label_id.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        entry_id = ttk.Entry(left_frame, textvariable=self.id,
                             width=20, font=("times new roman", 12, "bold"))
        entry_id.grid(row=0, column=1)


        label_name = Label(left_frame, text="Name:",
                           font=("times new roman", 12, "bold"))
        label_name.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        entry_name = ttk.Entry(left_frame, textvariable=self.name, width=20, font=(
            "times new roman", 12, "bold"))
        entry_name.grid(row=1, column=1)


        label_dep = Label(left_frame, text="Department:",
                          font=("times new roman", 12, "bold"))
        label_dep.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        entry_dep = ttk.Entry(left_frame, textvariable=self.dep, width=20, font=(
            "times new roman", 12, "bold"))
        entry_dep.grid(row=2, column=1)


        label_date = Label(left_frame, text="Date:",
                           font=("times new roman", 12, "bold"))
        label_date.grid(row=3, column=0, padx=5, pady=10, sticky=W)
        entry_date = ttk.Entry(left_frame, textvariable=self.date, width=20, font=(
            "times new roman", 12, "bold"))
        entry_date.grid(row=3, column=1)


        label_time = Label(left_frame, text="Time:",
                           font=("times new roman", 12, "bold"))
        label_time.grid(row=4, column=0, padx=5, pady=10, sticky=W)
        entry_time = ttk.Entry(left_frame, textvariable=self.time, width=20, font=(
            "times new roman", 12, "bold"))
        entry_time.grid(row=4, column=1)


        label_attend = Label(left_frame, text="Attendance",
                             font=("times new roman", 12, "bold"))
        label_attend.grid(row=5, column=0)
        self.attendance = ttk.Combobox(left_frame, textvariable=self.attend, width=20, font=(
            "times new roman", 12, "bold"), state="readonly")
        self.attendance["values"] = ("Status", "Present", "Absent")
        self.attendance.grid(row=5, column=1)
        self.attendance.current(0)


    #    options for importing and exporting csv file
        btn_frm = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frm.place(x=5, y=400, width=590, height=35)

        rst_btn = Button(btn_frm, command=self.reset_data, text="Reset", width=18, font=(
            "times new roman", 13, "bold"), bg="beige")
        rst_btn.grid(row=0, column=0)

        imp_btn = Button(btn_frm, command=self.import_csv, text="Import CSV", width=20, font=(
            "times new roman", 13, "bold"), bg="beige")
        imp_btn.grid(row=0, column=1)

        exp_btn = Button(btn_frm, command=self.export_csv, text="Export CSV", width=20, font=(
            "times new roman", 13, "bold"), bg="beige")
        exp_btn.grid(row=0, column=2, sticky=W)


        right_frame = LabelFrame(main_frame, bd=2, text="Attendance Record", font=(
            "times new roman", 12, "bold"))
        right_frame.place(x=630, y=10, width=600, height=550)



        #  creating an attendance table called attendancereport
        table_frame = LabelFrame(
            main_frame, bd=4, relief=RIDGE, bg="white", fg="white")
        table_frame.place(x=640, y=50, width=580, height=500)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendancereport = ttk.Treeview(table_frame, column=(
            "id", "name", "department", "date", "time", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendancereport.xview)
        scroll_y.config(command=self.attendancereport.yview)

        self.attendancereport.heading("id", text="Attendance ID")
        self.attendancereport.heading("name", text="Name")
        self.attendancereport.heading("department", text="Department")
        self.attendancereport.heading("date", text="Date")
        self.attendancereport.heading("time", text="Time")
        self.attendancereport.heading("attendance", text="Attendance")

        self.attendancereport["show"] = "headings"
        self.attendancereport.pack(fill=BOTH, expand=1)

        self.attendancereport.column("id", width=100)
        self.attendancereport.column("name", width=100)
        self.attendancereport.column("department", width=100)
        self.attendancereport.column("date", width=100)
        self.attendancereport.column("time", width=100)
        self.attendancereport.column("attendance", width=100)

        self.attendancereport.bind("<ButtonRelease>", self.get_cursor)

#  fetches data to display for the table
    def fetchdata(self, rows):
        self.attendancereport.delete(*self.attendancereport.get_children())
        for i in rows:
            self.attendancereport.insert("", END, values=i)


    def import_csv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*csv"), ("ALL File", ".")), parent=self.root)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)


    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "Error", "No data found", parent=self.root)
                return False
            else:
                file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                    ("CSV File", "*csv"), ("ALL File", ".")), parent=self.root)
                with open(file_name, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo(
                        "Message", "Data exported to"+os.path.basename(file_name)+" successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to:{str(es)}", parent=self.root)


    def get_cursor(self, event=""):
        cursor_row = self.attendancereport.focus()
        content = self.attendancereport.item(cursor_row)
        rows = content['values']
        self.id.set(rows[0])
        self.name.set(rows[1])
        self.dep.set(rows[2])
        self.date.set(rows[3])
        self.time.set(rows[4])
        self.attend.set(rows[5])
        

    def reset_data(self):
        self.id.set("")
        self.name.set("")
        self.dep.set("")
        self.date.set("")
        self.time.set("")
        self.attend.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
