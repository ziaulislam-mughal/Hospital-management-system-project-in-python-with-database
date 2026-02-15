
from tkinter import *  # used for making GUI application
from tkinter import ttk  # Themd TKinter is used for making GUI application
import random # used for generating random numbers
import time  # used for getting current time and date
import datetime # used for getting current time and date
from tkinter import messagebox  # used for showing message box in GUI application
import mysql.connector # used for connecting to MySQL database



class Hospital:
    def __init__(self,root):
        self.root = root 
        self.root.title("Hospital Management System") # set title of the window
        self.root.geometry("1350x700+0+0") # set size of the window

        # set background color of the Top label of window
        lbltitle = Label(self.root , text = "Hospital Managment System" , font=("times new roman" , 50 , "bold") , bg = "black" , fg = "gold" , bd = 4 , relief = RIDGE)
        lbltitle.pack(side = TOP , fill = X)

        # Dataframe  
        Datafram = Frame(self.root , bd = 15 , relief=RIDGE )
        Datafram.place(x=0 , y=100 , width = 1350 , height = 380)

        #Dataframe Left 
        Dataframe_left = LabelFrame(Datafram , text=("Patient Information") , bd = 4 , relief = RIDGE , font=("times new roman",10,"bold") , fg = 'black' , padx = 18)
        Dataframe_left.place(x = 0 , y = 6, width = 850 , height= 350)

        #Dataframe Right 
        Dataframe_right = LabelFrame(Datafram , text=("Prescription" ) , bd = 4 , relief=RIDGE , fg = "black", font=("times new roman",10,"bold"), padx= 18)
        Dataframe_right.place(x = 860 ,y = 6 , width = 450, height= 350 )


        #button frame
        buttonframe = Frame(self.root , bd = 15 , relief = RIDGE)
        buttonframe.place(x=0 , y=480 , width = 1350 , height = 70)

        #details frame 
        detailframe = Frame(self.root , bd = 15 , relief = RIDGE)
        detailframe.place(x=0 , y=550 , width = 1350 , height = 150)

        #Entites in Dataframe in left side

        #Name of Tablets

        name_of_tablets = Label(Dataframe_left,text=("Name of Tablet"),font=("times new roman" , 10 , "bold"),padx=0,pady=6)
        name_of_tablets.grid(row=0,column=0)
    
        option_of_tablets = ttk.Combobox(Dataframe_left, font=("times new roman" , 10 , "bold"),width=33)
        option_of_tablets['values'] = ("Brufen","Paracetamol","Dolo 650","Crocin","Disprin")
        option_of_tablets.grid(row=0,column=1)

        #Reference Number

        reference_no = Label(Dataframe_left , text=("Reference No") , font=("times new roman" , 10 , "bold"),padx=0,pady=6)
        reference_no.grid(row=1,column=0,sticky=W)
        txtinref = Entry(Dataframe_left , font=("times new roman" , 10 , "bold") , width=35)
        txtinref.grid(row=1,column=1)

        # Dose

        dose = Label(Dataframe_left , text=("Dose") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        dose.grid(row=2 ,column=0 , sticky=W)
        input_dose = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_dose.grid(row=2 , column=1)

        
        # No of Tablets 

        nooftablets = Label(Dataframe_left , text=("No of Tablets") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        nooftablets.grid(row=3 ,column=0 , sticky=W)
        input_nooftablets = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_nooftablets.grid(row=3 , column=1)

        # lot 
        
        dose = Label(Dataframe_left , text=("Dose") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        dose.grid(row=2 ,column=0 , sticky=W)
        input_dose = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_dose.grid(row=2 , column=1)

        # issue date 

        issue_date = Label(Dataframe_left , text=("Issue Date") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        issue_date.grid(row=3 ,column=0 , sticky=W)
        input_issue_date = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_issue_date.grid(row=3 , column=1)

        # exp date 

        expire_date = Label(Dataframe_left , text=("Expire Date") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        expire_date.grid(row=4 ,column=0 , sticky=W)
        input_expire_date = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_expire_date.grid(row=4 , column=1)


        # daily dose 

        daily_dose = Label(Dataframe_left , text=("Daily Dose") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        daily_dose.grid(row=5 ,column=0 , sticky=W)
        input_daily_dose = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_daily_dose.grid(row=5 , column=1)


        # side effect 

        side_effect  = Label(Dataframe_left , text=("Side Effect") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        side_effect.grid(row=6 ,column=0 , sticky=W)
        input_side_effect = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_side_effect.grid(row=6 , column=1)

        # furthar information 

        furthar_information = Label(Dataframe_left , text=("Furthar Information") , font=("times new roman" , 10 , "bold"), padx=0 , pady=6)
        furthar_information.grid(row=7 ,column=0 , sticky=W)
        input_furthar_information = Entry(Dataframe_left,font = ("times new roman" , 10 , "bold"),width=35)
        input_furthar_information.grid(row=7 , column=1)

        # blood pressure 

        blood_pressure = Label(Dataframe_left,text=("Blood Pressure"),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        blood_pressure.grid(row=0,column=2)
        input_blood_pressure = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        input_blood_pressure.grid(row=0,column=3)

                
        # storage advice

        storage_advice = Label(Dataframe_left,text=("Storage Advice"),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        storage_advice.grid(row=1,column=2)
        input_storage_advice = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        input_storage_advice.grid(row=1,column=3)

        # medication 
        
        medication = Label(Dataframe_left,text=("Medication"),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        medication.grid(row=2,column=2)
        input_med = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        input_med.grid(row=2,column=3)

        # patient id 
        

        patient_id = Label(Dataframe_left,text=("Patient id "),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        patient_id.grid(row=3,column=2)
        patient_id_input = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        patient_id_input.grid(row=3,column=3)

        # NHS Number 

        nhs_number = Label(Dataframe_left,text=("NHS Number"),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        nhs_number.grid(row=4,column=2)
        nhs_number_input = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        nhs_number_input.grid(row=4,column=3)

        # Patient Name 

        patient_name = Label(Dataframe_left,text=("Patient Name"),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        patient_name.grid(row=5,column=2)
        input_patient_name = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        input_patient_name.grid(row=5,column=3)
    
        # Date of Birth 
        
        date_of_birth = Label(Dataframe_left,text=("Date of Birth"),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        date_of_birth.grid(row=6,column=2)
        input_dob = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        input_dob.grid(row=6,column=3)

        # Patient Address

        patient_address = Label(Dataframe_left,text=("Patient Address"),font=("times new roman",10,"bold"),padx=2 ,pady=6)
        patient_address.grid(row=7,column=2)
        input_PA = Entry(Dataframe_left,font=("times new roman",10,"bold"),width=35)
        input_PA.grid(row=7,column=3)


        #===================================Dataframe Right Side========================================================

        self.text_prec = Text(Dataframe_right,font=("times new roman",10,"bold"),width = 55, height= 20 ,padx=2,pady=6)
        self.text_prec.grid(row=0,column=0)



        #===================================Button Frame========================================================

        prescription_btn = Button(buttonframe,text=("Prescription"),font=("times new roman",12,"bold"),width=23,bg="black",fg="gold",padx=2,pady=6)
        prescription_btn.grid(row=0,column=0)
    
        prescription_data = Button(buttonframe,text=("Prescription Data"),font=("times new roman",12,"bold"),width=23,bg="black",fg="gold",padx=2,pady=6)
        prescription_data.grid(row=0,column=1)
    

        update_btn = Button(buttonframe,text=("Update"),font=("times new roman",12,"bold"),width=23,bg="black",fg="gold",padx=2,pady=6)
        update_btn.grid(row=0,column=2)


        delet_btn = Button(buttonframe,text=("Delete"),font=("times new roman",12,"bold"),width=23,bg="black",fg="gold",padx=2,pady=6)
        delet_btn.grid(row=0,column=3)
    
        clear_btn = Button(buttonframe,text=("Clear"),font=("times new roman",12,"bold"),width=23,bg="black",fg="gold",padx=2,pady=6)
        clear_btn.grid(row=0,column=4)
    
        exit_btn = Button(buttonframe,text=("Exit"),font=("times new roman",12,"bold"),width=23,bg="black",fg="gold",padx=2,pady=6)
        exit_btn.grid(row=0,column=5)
    






        

        




    
    

        




root = Tk()
obj = Hospital(root)
root.mainloop()