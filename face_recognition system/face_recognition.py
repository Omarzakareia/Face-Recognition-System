from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import customtkinter


class Face_recognition:
    def __init__(window,root):
        window.root=root
        
        #setting tkinter window size
        width= window.root.winfo_screenwidth()
        height= window.root.winfo_screenheight()
        window.root.geometry("%dx%d" % (width, height))
        window.root.title("Automated Attendance System")        
        # Icon
        p1 = PhotoImage(file = r'C:\Users\Omar\Desktop\face_recognition system\college_images\iconn.png')
        window.root.iconphoto(False, p1)                
        #background
        img3=Image.open(r"C:\Users\Omar\Desktop\face_recognition system\college_images\white.jpg")
        img3=img3.resize((1910,990),Image.Resampling.LANCZOS)
        window.photoimg3=ImageTk.PhotoImage(img3)        
        bg_img=Label(window.root,image=window.photoimg3)
        bg_img.place(x=0,y=0,width=1910,height=990)
        #top frame
        top_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,font=("Calibri",14,"bold"),bg="#FFFFFF")
        top_frame.place(x=0,y=0,width=1908,height=70) 

        title_lbl=Label(bg_img,relief=FLAT,text="Take Attendance using Face",font=("Calibri",25,"normal"),bg="#FFFFFF",fg="black")
        title_lbl.place(x=10,y=4,width=680,height=60)
        
        cent_frame=LabelFrame(bg_img,bd=2,relief=FLAT,font=("Calibri",14,"bold"),bg="white")
        cent_frame.place(x=735,y=300,width=440,height=470)      
        
        train_img = Image.open(r"college_images\recog.jpg")
        train_img=train_img.resize((540,400))
        window.train_img=ImageTk.PhotoImage(train_img)
        tr_img=Label(cent_frame,image=window.train_img)
        tr_img.place(x=0,y=0,width=440,height=300)        
        
        tr_b=Button(cent_frame,text="Take Attendance",relief=RIDGE,cursor="hand2",command=window.face_recog, font=("Calibri",15,"normal"),bg="#41ba9c",fg="white")
        tr_b.place(x=90,y=350,width=260,height=50)        
        
    def attend_csv(self, a, i, b, c):
        with open("Attendance.csv", "r+", newline="\n") as f:
            datalist = f.readlines()
            nam_list = []
            for line in datalist:
                entry = line.strip().split(",")
                nam_list.append(entry[0])
            
            f.seek(0)  # Move the file pointer to the beginning of the file
            
            if ((a not in nam_list) and (i not in nam_list) and (b not in nam_list) and (c not in nam_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S %p")
                
                new_entry = f"{a},{b},{i},{c},{dtString},{d1},Preset\n"
                f.write(new_entry + ''.join(datalist))  # Write the new entry followed by the existing data
            
            f.truncate()  # Remove any remaining data after the new entry
        
     
    ## face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,150,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",user="root",password="Anawebas0-",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select roll from student where roll="+str(id))
                a=my_cursor.fetchone()
                a="+".join(a) 
                
                my_cursor.execute("select name from student where roll="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i) 
                
                my_cursor.execute("select std_id from student where roll="+str(id))
                b=my_cursor.fetchone()
                b="+".join(b) 
                        
                my_cursor.execute("select dep from student where roll="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)              
               
                    
                if confidence>77:
                    cv2.putText(img,f"Name: {i}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID: {b}",(x,y-45),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {c}",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.attend_csv(a,i,b,c)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord = [x,y,w,y]
                
            return coord
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap=cv2.VideoCapture(0)
            
        while True:
            ret,img=video_cap.read()
            img= recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)
            
            key = cv2.waitKey(1) & 0xFF
            if cv2.waitKey(1)==13 or key == ord("q"):
                break     
            
        video_cap.release()
        cv2.destroyAllWindows()
            
            
                        
                        


                
if __name__ == "__main__":
    root=Tk() 
    obj=Face_recognition(root)
    root.mainloop()   