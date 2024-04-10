from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import student
from help import Help
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(window,root):
        window.root=root
        
        #setting tkinter window size
        width= window.root.winfo_screenwidth()
        height= window.root.winfo_screenheight()
        window.root.geometry("%dx%d" % (width, height))
        window.root.title("Automated Attendance System") 
        
        # Icon
        p1 = PhotoImage(file = r'college_images\iconn.png')
        window.root.iconphoto(False, p1)
        
        # Background image
        img3=Image.open(r"college_images\white.jpg")
        img3=img3.resize((1910,990))
        window.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(window.root,image=window.photoimg3)
        bg_img.place(x=0,y=0,width=1910,height=990)
        
        top_frame=LabelFrame(bg_img,bd=3,relief=RIDGE,font=("Calibri",14,"bold"),bg="#FFFFFF")
        top_frame.place(x=0,y=0,width=1908,height=70) 
        
        title_lbl=Label(bg_img,relief=FLAT,text="AAS",font=("Calibri",30,"normal"),bg="#FFFFFF",fg="black")
        title_lbl.place(x=20,y=4,width=180,height=60)
        


        
        #buttons
        # 1 student button 
        img4=Image.open(r"college_images\info1.png")
        img4=img4.resize((262,262))
        window.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=window.photoimg4,command=window.student_details,cursor="hand2",relief=FLAT,bg="#FFFFFF")
        b1.place(x=300,y=140,width=320,height=280)
        
        b1_1=Button(bg_img,text="Student Details",command=window.student_details,relief=RIDGE,cursor="hand2", font=("Calibri",15,"bold"),bg="#e5e5e5",fg="black")
        b1_1.place(x=350,y=415,width=220,height=50)
       


        # 2 Detect face button
        img5=Image.open(r"college_images\detect.jpg")
        img5=img5.resize((320,280))
        window.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=window.photoimg5,cursor="hand2",command=window.face_reco,relief=FLAT,bg="#FFFFFF")
        b1.place(x=800,y=140,width=320,height=280)
        
        b1_1=Button(bg_img,text="Take Attendance",relief=RIDGE,command=window.face_reco,cursor="hand2", font=("Calibri",15,"bold"),bg="#e5e5e5",fg="black")
        b1_1.place(x=835,y=415,width=260,height=50)

        # 3 Attendence button
        img6=Image.open(r"college_images\attend.png")
        img6=img6.resize((320,280))
        window.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=window.photoimg6,cursor="hand2",relief=FLAT)
        b1.place(x=1320,y=140,width=260,height=280)
        
        b1_1=Button(bg_img,text="Attendance Details",command=window.attend,relief=RIDGE,cursor="hand2", font=("Calibri",15,"bold"),bg="#e5e5e5",fg="black")
        b1_1.place(x=1340,y=415,width=220,height=50) 

                 

        # 1 Train button
        img8=Image.open(r"college_images\Train.png")
        img8=img8.resize((320,280))
        window.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=window.photoimg8,command=window.train_button,cursor="hand2",relief=FLAT,bg="#FFFFFF")
        b1.place(x=300,y=542,width=320,height=280)
        
        b1_1=Button(bg_img,text="Train Data",relief=RIDGE,command=window.train_button,cursor="hand2", font=("Calibri",15,"bold"),bg="#e5e5e5",fg="black")
        b1_1.place(x=350,y=817,width=220,height=50)
        
        # 2 Photos button
        img9=Image.open(r"college_images\photo1.png")
        img9=img9.resize((262,262))
        window.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=window.photoimg9,cursor="hand2",relief=FLAT,command=window.open_img,bg="#FFFFFF")
        b1.place(x=800,y=542,width=320,height=280)
        
        b1_1=Button(bg_img,text="Photos",relief=RIDGE,command=window.open_img,cursor="hand2", font=("Calibri",15,"bold"),bg="#e5e5e5",fg="black")
        b1_1.place(x=850,y=817,width=220,height=50)  

        # Help button
        img10=Image.open(r"college_images\help1.jpg")
        img10=img10.resize((320,280))
        window.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=window.photoimg10,command=window.help_data,cursor="hand2",relief=FLAT)
        b1.place(x=1290,y=542,width=320,height=280)
        
        b1_1=Button(bg_img,text="Help",command=window.help_data,relief=RIDGE,cursor="hand2", font=("Calibri",15,"bold"),bg="#e5e5e5",fg="black")
        b1_1.place(x=1360,y=817,width=180,height=50)

        # 4 Quit button
        b1_1=Button(bg_img,text="Quit",command=window.quit_app,relief=RIDGE,cursor="hand2", font=("Calibri",15,"bold"),bg="red",fg="white")
        b1_1.place(x=1730,y=935,width=160,height=50)    
        
        
        
    def open_img(self):
        os.startfile("data")

    def quit_app(self):
        self.quit_app=tkinter.messagebox.askyesno("Quit Application","Are you sure you want to Quit application?",parent=self.root)
        if self.quit_app >0:
            self.root.destroy()           
        else:
            return 
    
   
        
        #### Functions Buttons
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student.Student(self.new_window)

    def train_button(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def face_reco(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    
    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    

        
        
        
                         

if __name__ == "__main__":
    root=Tk() 
    obj=Face_Recognition_System(root)
    root.mainloop()        