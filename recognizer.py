import cv2
import face_recognition
import mysql.connector
from datetime import date, datetime
from tkinter import*
from tkinter import messagebox
import mysql.connector
import os
from PIL import Image, ImageTk
import numpy as np
from time import strftime
from datetime import datetime
from attendance import Attendance 


class Recognize:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x800+0+0")
        self.root.title('face recognition')

        title_lbl = Label(self.root, text="RECOGNIZER", font=(
            "times new roman", 25, "bold"), fg="black")
        title_lbl.place(x=-100, y=0, width=1400, height=50)

        img_bg = Image.open(r'C:\Users\hp\Desktop\Project\images\face.jpg')
        img_bg = img_bg.resize((500, 550), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        img_lbl = Label(self.root, image=self.photoimg_bg)
        img_lbl.place(x=50, y=80, width=500, height=550)

        img_bg2 = Image.open(r'C:\Users\hp\Desktop\Project\images\side.jpg')
        img_bg2 = img_bg2.resize((500, 400), Image.ANTIALIAS)
        self.photoimg_bg2 = ImageTk.PhotoImage(img_bg2)
        img_lbl2 = Label(self.root, image=self.photoimg_bg2)
        img_lbl2.place(x=650, y=80, width=500, height=400)

        btn_face = Button(self.root, command=self.face_rec, text="Add attendance", font=(
            "times new roman", 17, "bold"), cursor="hand2", bg="black", fg="green")
        btn_face.place(x=780, y=520, width=200, height=50)

        forexit = Label(self.root, text="Press enter to exit camera", font=(
            "times new roman", 17, "bold"), bg="black", fg="white")
        forexit.place(x=680, y=580, width=400, height=40)

    def face_rec(self):
        # path contains the path to folder named 'image' that has all the pictures as dataset to be required for face recognition
        path = 'image'
        images = []
        name_list = []

        mylist = os.listdir(path)
        # print(mylist)

        for l in mylist:
            cur_img = cv2.imread(f'{path}/{l}')
            images.append(cur_img)
            name_list.append(os.path.splitext(l)[0])
        # print(name_list)

        ids = []
        # list of unique ids
        for i in name_list:
            new = i.split(".")
            if new[1] not in ids:
                ids.append(new[1])
        print(ids)

        # to compute encodings

        def findencodings(images):
            encodelist = []
            for img in images:
                image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # computes 128 different measurements of the faces for comparision
                encode = face_recognition.face_encodings(image)[0]
                encodelist.append(encode)
            return encodelist

        # marks the attendance only once if name is already there
        def markattendance(id, name_res, dep_res):
            with open("attendance.csv", "r+", newline="\n") as f:
                mydatalist = f.readlines()
                name_list = []
                for line in mydatalist:
                    entry = line.split((","))
                    name_list.append(entry[0])
                if((id not in name_list) and (name_res not in name_list) and (dep_res not in name_list)):
                    now = datetime.now()
                    dl= now.strftime("%d/%m/%Y")
                    dtstring = now.strftime("%H:%M:%S")
                    f.writelines(
                        f"\n{id},{name_res},{dep_res},{dl},{dtstring},Present")
        messagebox.showinfo(
            "Please wait", "This may take a while.", parent=self.root)

        encodelistknown = findencodings(images)

        messagebox.showinfo("Message", "Dataset is ready.", parent=self.root)
        print('Encoding complete')
        # print(len(encodelistknown))

        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            img_resize = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            img = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)

            loc_cur = face_recognition.face_locations(img)
            encode_cur = face_recognition.face_encodings(img, loc_cur)

            for encodeface, faceloc in zip(encode_cur, loc_cur):
                matches = face_recognition.compare_faces(
                    encodelistknown, encodeface)
                facedis = face_recognition.face_distance(
                    encodelistknown, encodeface)
                # print(facedis)
                matchindex = np.argmin(facedis)

                if matches[matchindex]:
                    name = name_list[matchindex].upper()
                    id = name.split(".")[1]
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    print("id:", id)
                    # connecting to mysql db to get the respectives names and departments for given id
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="test@123", database="face_recognize", auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()

                    my_cursor.execute(
                        "select Name from student where ID="+str(id))
                    name_res = my_cursor.fetchone()
                    name_res = "+".join(name_res)
                    print(name_res)

                    my_cursor.execute(
                        "select Department from student where ID="+str(id))
                    dep_res = my_cursor.fetchone()
                    dep_res = "+".join(dep_res)
                    print(dep_res)

                    markattendance(id, name_res, dep_res)
           
                    text = "ID: "+id
                    text_1 = "Name: "+name_res
                    text_2 = "Dept: "+dep_res
                    cv2.putText(frame, text, (x1, y1-20),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(frame, text_1, (x1, y1+12),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                    cv2.putText(frame, text_2, (x1, y1+40),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)


                else:
                    # if the face does not match with the given data set
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, "Unknown", (x1, y1+12),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

            if cv2.waitKey(1) == 13:
                break

            cv2.imshow('webcam', frame)


if __name__ == "__main__":
    root = Tk()
    obj = Recognize(root)
    root.mainloop()
