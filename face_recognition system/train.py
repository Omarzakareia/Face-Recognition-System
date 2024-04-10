from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
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
        
        top_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,font=("Calibri",14,"bold"),bg="#FFFFFF")
        top_frame.place(x=0,y=0,width=1908,height=70) 
        
        title_lbl=Label(window.root,relief=FLAT,text="Train Dataset",font=("Calibri",25,"bold"),bg="#FFFFFF",fg="Black")
        title_lbl.place(x=30,y=4,width=250,height=60)
        
        cent_frame=LabelFrame(bg_img,bd=2,relief=FLAT,font=("Calibri",14,"bold"),bg="#FFFFFF")
        cent_frame.place(x=635,y=300,width=640,height=470) 
        
        
        train_img = Image.open(r"college_images\fac.png")
        train_img=train_img.resize((640,300))
        window.train_img=ImageTk.PhotoImage(train_img)
        tr_img=Label(cent_frame,image=window.train_img)
        tr_img.place(x=0,y=0,width=640,height=300)        
        
        tr_b=Button(cent_frame,text="Train Dataset",relief=RIDGE,cursor="hand2",command=window.train_im, font=("Calibri",15,"normal"),bg="#41ba9c",fg="white")
        tr_b.place(x=210,y=350,width=220,height=50)
    
    def train_im(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ]
        
        faces=[]
        ids=[]
        
        for image in path:
            img = Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #### train and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!")
        
            
                       
if __name__ == "__main__":
    root=Tk() 
    obj=Train(root)
    root.mainloop()    