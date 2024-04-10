from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from tkcalendar import Calendar, DateEntry
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(window,root):
        window.root=root
        
        #setting tkinter window size    
        width= window.root.winfo_screenwidth()
        height= window.root.winfo_screenheight()
        window.root.geometry("%dx%d" % (width, height))
        window.root.title("Automated Attendance System") 
        
        ## Variables 
        window.var_student_id=StringVar()
        window.var_roll=StringVar()
        window.var_name=StringVar()
        window.var_dep=StringVar()
        window.var_time=StringVar()
        window.var_date=StringVar()
        window.var_attend=StringVar()
        
        # Icon
        p1 = PhotoImage(file = r'C:\Users\Omar\Desktop\face_recognition system\college_images\iconn.png')
        window.root.iconphoto(False, p1)      
          
        #background
        img3=Image.open(r"C:\Users\Omar\Desktop\face_recognition system\college_images\white.jpg")
        img3=img3.resize((1910,990),Image.Resampling.LANCZOS)
        window.photoimg3=ImageTk.PhotoImage(img3)        
        bg_img=Label(window.root,image=window.photoimg3)
        bg_img.place(x=0,y=0,width=1910,height=990)
        
        top_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,font=("Calibri",14,"bold"),bg="#FFFFFF")
        top_frame.place(x=0,y=0,width=1908,height=70) 
        
        title_lbl=Label(window.root,relief=FLAT,text=" Attendance Management",font=("Calibri",25,"bold"),bg="#FFFFFF",fg="Black")
        title_lbl.place(x=20,y=4,width=550,height=60)
        
        
        #main frame
        main_frm = LabelFrame(bg_img,relief=RIDGE,bg="white")
        main_frm.place(x=10,y=100,width=1890,height=870) 
        #Left Label frame
        left_framee=LabelFrame(main_frm,bd=2,relief=RIDGE,text="Student Attendance Details",font=("Calibri",14,"bold"),bg="White")
        left_framee.place(x=10,y=30,width=920,height=800)
        
        left_small_frame=LabelFrame(left_framee,bd=2,relief=RIDGE,bg="white")
        left_small_frame.place(x=15,y=30,width=880,height=700)

        #student id 
        stu_lab=Label(left_small_frame,text="Student ID:",font=("Calibri",14,"bold"),bg="#90EE90")
        stu_lab.grid(row=0,column=0,padx=15)   
        stu_entry=ttk.Entry(left_small_frame,textvariable=window.var_student_id,width=20,font=("Calibri",14,"bold"))          
        stu_entry.grid(row=0,column=1,pady=20,sticky=W) 

        #Roll
        roll_label=Label(left_small_frame,text="Roll:",font=("Calibri",14,"bold"),bg="#90EE90")
        roll_label.grid(row=0,column=2,padx=5)   
        roll_entry=ttk.Entry(left_small_frame,textvariable=window.var_roll,width=20,font=("Calibri",14,"bold"))          
        roll_entry.grid(row=0,column=3,pady=20,sticky=W) 

        #Name
        name_label=Label(left_small_frame,text="Name:",font=("Calibri",14,"bold"),bg="#90EE90")
        name_label.grid(row=1,column=0,padx=5)   
        name_entry=ttk.Entry(left_small_frame,textvariable=window.var_name,width=20,font=("Calibri",14,"bold"))          
        name_entry.grid(row=1,column=1,pady=20,sticky=W)

        #Department
        dep_label=Label(left_small_frame,text="Department:",font=("Calibri",14,"bold"),bg="#90EE90")
        dep_label.grid(row=1,column=2,padx=15)   
        dep_label=ttk.Entry(left_small_frame,textvariable=window.var_dep,width=20,font=("Calibri",14,"bold"))          
        dep_label.grid(row=1,column=3,pady=20,sticky=W) 

        #time
        time_label=Label(left_small_frame,text="Time:",font=("Calibri",14,"bold"),bg="#90EE90")
        time_label.grid(row=2,column=0,padx=5)   
        time_entry=ttk.Entry(left_small_frame,textvariable=window.var_time,width=20,font=("Calibri",14,"bold"))          
        time_entry.grid(row=2,column=1,pady=20,sticky=W)
        
        #date
        date_label=Label(left_small_frame,text="Date:",font=("Calibri",14,"bold"),bg="#90EE90")
        date_label.grid(row=2,column=2,padx=5)   
        date_entry=ttk.Entry(left_small_frame,textvariable=window.var_date,width=20,font=("Calibri",14,"bold"))          
        date_entry.grid(row=2,column=3,pady=20,sticky=W)     
        
        #status
        stat_label=Label(left_small_frame,text="Status:",font=("Calibri",14,"bold"),bg="#90EE90")
        stat_label.grid(row=3,column=0,padx=5)   
        stat_entry=ttk.Entry(left_small_frame,textvariable=window.var_attend,width= 20,font=("Calibri",14,"bold"))          
        stat_entry.grid(row=3,column=1,pady=20,sticky=W) 
                      
        #buttons frame 
        btn_frame=Frame(left_small_frame,bd=2,relief=FLAT,bg="white")
        btn_frame.place(x=30,y=320,width=830,height=47)
        
        import_csv=Button(btn_frame,text="Import CSV",width=17,command=window.import_csv,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        import_csv.grid(row=0,column=0)

        export_csv=Button(btn_frame,text="Export CSV",command=window.export_csv,width=17,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        export_csv.grid(row=0,column=1,padx=15)

        update_buttn=Button(btn_frame,text="Update",width=17,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        update_buttn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",textvariable=window.reset,width=17,font=("Calibri",13,"bold"),bg="#000000",fg="white")
        reset_btn.grid(row=0,column=3,padx=15)

        #Right Label frame
        right_framee=LabelFrame(main_frm,bd=2,relief=RIDGE,text="Attendance Details",font=("Calibri",14,"bold"),bg="white")
        right_framee.place(x=950,y=30,width=915,height=800) 
        
        table_frm=Frame(right_framee,bd=2,relief=RIDGE,bg="white")
        table_frm.place(x=15,y=30,width=880,height=700) 
        
        #### scroll bar for the right frame
        scroll_x=ttk.Scrollbar(table_frm,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frm,orient=VERTICAL)
        window.AttendReportTable = ttk.Treeview(table_frm,column=("roll","id","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        s=ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', rowheight=24)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=window.AttendReportTable.xview)
        scroll_y.config(command=window.AttendReportTable.yview)
        
        window.AttendReportTable.heading("roll",text="Roll")
        window.AttendReportTable.heading("id",text="Student ID")
        window.AttendReportTable.heading("name",text="Name")
        window.AttendReportTable.heading("dep",text="Department")
        window.AttendReportTable.heading("time",text="Time")
        window.AttendReportTable.heading("date",text="Date")
        window.AttendReportTable.heading("attendance",text="Attendance")       
        window.AttendReportTable["show"]="headings"
        
        window.AttendReportTable.column("roll",width=100,anchor=CENTER)
        window.AttendReportTable.column("id",width=100,anchor=CENTER)
        window.AttendReportTable.column("name",width=120,anchor=CENTER)
        window.AttendReportTable.column("dep",width=100,anchor=CENTER)
        window.AttendReportTable.column("time",width=100,anchor=CENTER)
        window.AttendReportTable.column("date",width=120,anchor=CENTER)
        window.AttendReportTable.column("attendance",width=100,anchor=CENTER)
        
        window.AttendReportTable.pack(fill=BOTH,expand=1)

        window.AttendReportTable.bind("<ButtonRelease>",window.get_cursor)

        
        # Fetch Data 
    def fetch_data(self,rows):
        self.AttendReportTable.delete(*self.AttendReportTable.get_children())
        for i in rows:
            self.AttendReportTable.insert("",END,values=i)

    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
        #export csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","You Data Exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
                            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    def get_cursor(self,event=""):
        cursor_row=self.AttendReportTable.focus()
        content=self.AttendReportTable.item(cursor_row)
        row=content["values"]
        self.var_student_id.set(row[0]),
        self.var_roll.set(row[1]),
        self.var_name.set(row[2]),
        self.var_dep.set(row[3]),
        self.var_time.set(row[4]),
        self.var_date.set(row[5]),
        self.var_attend.set(row[6])                                                      

    def reset(self):
        self.var_student_id.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_dep.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_attend.set("")    

if __name__ == "__main__":
    root=Tk() 
    obj=Attendance(root)
    root.mainloop()    