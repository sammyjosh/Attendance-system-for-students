from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNIZATION SYSTEM")

        #variables
        self.var_dep=StringVar()
        self.var_cou = StringVar()
        self.var_year = StringVar()
        self.var_stdid = StringVar()
        self.var_div= StringVar()
        self.var_roll = StringVar()
        self.var_email= StringVar()
        self.var_teacher= StringVar()




        # first image
        img = Image.open(r"C:\Users\kartikiaalhad\OneDrive\Pictures\face 1.jfif")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # 2nd image
        img1 = Image.open(r"C:\Users\kartikiaalhad\OneDrive\Pictures\face 2.jfif")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # 3rd image
        img2 = Image.open(r"C:\Users\kartikiaalhad\OneDrive\Pictures\face3.jfif")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # backgroundimage

        img3 = Image.open(r"C:\Users\kartikiaalhad\OneDrive\Pictures\face4.jfif")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGMENT SYSTEM ", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("types new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        # 3rd left image
        img_left = Image.open(r"C:\Users\kartikiaalhad\OneDrive\Pictures\face3.jfif")
        img_left = img_left.resize((750, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)

        # current course label frame
        Current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="CURRENT COURSE",
                                font=("types new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=135, width=720, height=150)

        #department
        dep_label=Label(Current_course_frame,text="DEPARTMENT",font=("types new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,pady=0)
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("types new roman",12,"bold"),state="Read only")
        dep_combo["values"] = ["Select Department", "CS", "IT", "ENTC", "MECH"]
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        cou_label = Label(Current_course_frame, text="COURSE", font=("types new roman", 12, "bold"))
        cou_label.grid(row=0, column=2, padx=10)

        cou_combo = ttk.Combobox(Current_course_frame,textvariable= self.var_cou, font=("types new roman", 12, "bold"), state="Read only")
        cou_combo["values"] = ["Select Year", "FY", "SY", "TY", "BTECH"]
        cou_combo.current(0)
        cou_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        #academic year
        aca_label = Label(Current_course_frame, text="YEAR", font=("types new roman", 12, "bold"))
        aca_label.grid(row=1, column=0, padx=10,sticky=W)

        aca_combo = ttk.Combobox(Current_course_frame,self.var_year, font=("types new roman", 12, "bold"), state="Read only")
        aca_combo["values"] = [" Year", "2020-21", "2021-22", "2022-23", "2023-24"]
        aca_combo.current(0)
        aca_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Class student info
        student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" studentinformation",font=("types new roman", 12, "bold"))
        student_frame.place(x=5,y=250,width=720,height=300)
        #stuID
        studentId_label=Label(student_frame,text="STUDENT ID",font=("types new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry=Entry(student_frame,self.var_stdid,width=20,font=("types new roman", 12, "bold"),bg="white")
        studentID_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #studentName
       # studenName_label = Label(student_frame, text="STUDENT Name", font=("types new roman", 12, "bold"), bg="white")
        #studenName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

       # studentName_entry = Entry(student_frame, width=20, font=("types new roman", 12, "bold"), bg="white")
        #studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #division
        div_label = Label(student_frame, text="DIVISION", font=("types new roman", 12, "bold"), bg="white")
        div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_entry = Entry(student_frame,self.var_div, width=20, font=("types new roman", 12, "bold"), bg="white")
        div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #roll no
        roll_label = Label(student_frame, text="ROLL NUMBER", font=("types new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_entry = Entry(student_frame,self.var_roll, width=20, font=("types new roman", 12, "bold"), bg="white")
        roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #email
        e_label = Label(student_frame, text="E-MAIL", font=("types new roman", 12, "bold"), bg="white")
        e_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        e_entry = Entry(student_frame, self.var_email,width=20, font=("types new roman", 12, "bold"), bg="white")
        e_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #teacher name
        tea_label = Label(student_frame, text="TEACHER NAME", font=("types new roman", 12, "bold"), bg="white")
        tea_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        tea_entry = Entry(student_frame, self.var_teacher,width=20, font=("types new roman", 12, "bold"), bg="white")
        tea_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=Radiobutton(student_frame,text="Take photo sample",value="YES")
        radiobtn1.grid(row=6,column=0)
        self.var_radio2 = StringVar()
        radiobtn2 = Radiobutton(student_frame, text="No photo sample", value="NO")
        radiobtn2.grid(row=6, column=1)
        #buttons frame
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="SAVE",width=17,font=("types new roman", 13, "bold"), bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="UPDATE",width=17, font=("types new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="DELETE",width=17, font=("types new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="RESET",width=17, font=("types new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="TAKE photo", width=35, font=("types new roman", 13, "bold"), bg="blue",
                           fg="white")
        take_photo_btn.grid(row=0, column=0)


        update_btn = Button(btn_frame1, text="UPDATE", width=35, font=("types new roman", 13, "bold"), bg="blue",
                           fg="white")
        update_btn.grid(row=0, column=1)

        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="STUDENT DETAILS",
                                 font=("types new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=660, height=580)

        img_right = Image.open(r"C:\Users\kartikiaalhad\OneDrive\Pictures\face3.jfif")
        img_right= img_right.resize((750, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=750, height=130)

        #search system

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text=" SEARCH",
                                   font=("types new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text="SEARCH BY", font=("types new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

         #combo
        search_combo = ttk.Combobox(search_frame, font=("types new roman", 12, "bold"), state="Read only")
        search_combo["values"] = ["Select","rollno"]
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = Entry(search_frame, width=12, font=("types new roman", 12, "bold"), bg="white")
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="SEARCH", width=8, font=("types new roman", 11, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(search_frame, text="SHOWALL", width=8, font=("types new roman", 11, "bold"), bg="blue",
                           fg="white")
        showall_btn.grid(row=0, column=4, padx=4)
#table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE )

        table_frame.place(x=5, y=210, width=650, height=350)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","id","div","roll","teacher name","email","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year", text ="Year")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("div", text="DIVISION")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("roll", text="ROLLNO")
        self.student_table.heading("teacher name", text="TEACHER NAME")
        self.student_table.heading("photo", text = "PHOTO SAMPLE STATUS")

        self.student_table["show"]="headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("teacher name", width=100)
        self.student_table.column("photo", width=150)



        self.student_table.pack(fill=BOTH,expand=1)

        #FUNCTION DECLARATION
#def add_data(self):








 if __name__ == "__main__":
     root = Tk()
     obj = Student(root)
     root.mainloop()






