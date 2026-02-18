from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root 
        self.root.title("Hospital Management System")
        self.root.geometry("1350x700+0+0")

        # ============= Variables ========================
        self.nameoftablets = StringVar()
        self.ref = StringVar()
        self.dose = StringVar()
        self.nooftablets = StringVar()
        self.lot = StringVar()
        self.issuedate = StringVar()
        self.expdate = StringVar()
        self.daily_dose = StringVar()
        self.side_effect = StringVar()
        self.further_information = StringVar()
        self.blood_pressure = StringVar()
        self.storage_advice = StringVar()
        self.medication = StringVar()
        self.patient_id = StringVar()
        self.nhs_number = StringVar()
        self.patient_name = StringVar()
        self.dob = StringVar()
        self.patient_address = StringVar()

        # ============= Title ============================
        lbltitle = Label(self.root, text="Hospital Management System", font=("times new roman", 50, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbltitle.pack(side=TOP, fill=X)

        # ============= Dataframes =======================
        Datafram = Frame(self.root, bd=15, relief=RIDGE)
        Datafram.place(x=0, y=100, width=1350, height=380)

        Dataframe_left = LabelFrame(Datafram, text="Patient Information", bd=4, relief=RIDGE, font=("times new roman", 12, "bold"), fg='black', padx=10)
        Dataframe_left.place(x=0, y=5, width=850, height=350)

        Dataframe_right = LabelFrame(Datafram, text="Prescription", bd=4, relief=RIDGE, fg="black", font=("times new roman", 12, "bold"), padx=10)
        Dataframe_right.place(x=860, y=5, width=440, height=350)

        # ============= Buttons Frame ====================
        buttonframe = Frame(self.root, bd=15, relief=RIDGE)
        buttonframe.place(x=0, y=480, width=1350, height=70)

        # ============= Details Frame ====================
        detailframe = Frame(self.root, bd=15, relief=RIDGE)
        detailframe.place(x=0, y=550, width=1350, height=150)

        # ============= Input Fields (Left Frame) ========

        # Name of Tablets
        lbl_tablet = Label(Dataframe_left, text="Name of Tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_tablet.grid(row=0, column=0, sticky=W)
        
        com_tablet = ttk.Combobox(Dataframe_left, textvariable=self.nameoftablets, font=("times new roman", 12, "bold"), width=33)
        com_tablet['values'] = ("Brufen", "Paracetamol", "Dolo 650", "Crocin", "Disprin")
        com_tablet.grid(row=0, column=1)

        # Reference No
        lbl_ref = Label(Dataframe_left, text="Reference No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_ref.grid(row=1, column=0, sticky=W)
        txt_ref = Entry(Dataframe_left, textvariable=self.ref, font=("times new roman", 12, "bold"), width=35)
        txt_ref.grid(row=1, column=1)

        # Dose
        lbl_dose = Label(Dataframe_left, text="Dose", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_dose.grid(row=2, column=0, sticky=W)
        txt_dose = Entry(Dataframe_left, textvariable=self.dose, font=("times new roman", 12, "bold"), width=35)
        txt_dose.grid(row=2, column=1)

        # No of Tablets
        lbl_no = Label(Dataframe_left, text="No of Tablets", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_no.grid(row=3, column=0, sticky=W)
        txt_no = Entry(Dataframe_left, textvariable=self.nooftablets, font=("times new roman", 12, "bold"), width=35)
        txt_no.grid(row=3, column=1)

        # Lot
        lbl_lot = Label(Dataframe_left, text="Lot", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_lot.grid(row=4, column=0, sticky=W)
        txt_lot = Entry(Dataframe_left, textvariable=self.lot, font=("times new roman", 12, "bold"), width=35)
        txt_lot.grid(row=4, column=1)

        # Issue Date
        lbl_issue = Label(Dataframe_left, text="Issue Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_issue.grid(row=5, column=0, sticky=W)
        txt_issue = Entry(Dataframe_left, textvariable=self.issuedate, font=("times new roman", 12, "bold"), width=35)
        txt_issue.grid(row=5, column=1)

        # Exp Date
        lbl_exp = Label(Dataframe_left, text="Exp Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_exp.grid(row=6, column=0, sticky=W)
        txt_exp = Entry(Dataframe_left, textvariable=self.expdate, font=("times new roman", 12, "bold"), width=35)
        txt_exp.grid(row=6, column=1)

        # Daily Dose
        lbl_daily = Label(Dataframe_left, text="Daily Dose", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_daily.grid(row=7, column=0, sticky=W)
        txt_daily = Entry(Dataframe_left, textvariable=self.daily_dose, font=("times new roman", 12, "bold"), width=35)
        txt_daily.grid(row=7, column=1)

        # Side Effect
        lbl_side = Label(Dataframe_left, text="Side Effect", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_side.grid(row=8, column=0, sticky=W)
        txt_side = Entry(Dataframe_left, textvariable=self.side_effect, font=("times new roman", 12, "bold"), width=35)
        txt_side.grid(row=8, column=1)

        # Further Info (Column 2)
        lbl_further = Label(Dataframe_left, text="Further Info", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_further.grid(row=0, column=2, sticky=W)
        txt_further = Entry(Dataframe_left, textvariable=self.further_information, font=("times new roman", 12, "bold"), width=35)
        txt_further.grid(row=0, column=3)

        # Blood Pressure
        lbl_bp = Label(Dataframe_left, text="Blood Pressure", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_bp.grid(row=1, column=2, sticky=W)
        txt_bp = Entry(Dataframe_left, textvariable=self.blood_pressure, font=("times new roman", 12, "bold"), width=35)
        txt_bp.grid(row=1, column=3)

        # Storage Advice
        lbl_store = Label(Dataframe_left, text="Storage Advice", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_store.grid(row=2, column=2, sticky=W)
        txt_store = Entry(Dataframe_left, textvariable=self.storage_advice, font=("times new roman", 12, "bold"), width=35)
        txt_store.grid(row=2, column=3)

        # Medication
        lbl_med = Label(Dataframe_left, text="Medication", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_med.grid(row=3, column=2, sticky=W)
        txt_med = Entry(Dataframe_left, textvariable=self.medication, font=("times new roman", 12, "bold"), width=35)
        txt_med.grid(row=3, column=3)

        # Patient ID
        lbl_pid = Label(Dataframe_left, text="Patient ID", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_pid.grid(row=4, column=2, sticky=W)
        txt_pid = Entry(Dataframe_left, textvariable=self.patient_id, font=("times new roman", 12, "bold"), width=35)
        txt_pid.grid(row=4, column=3)

        # NHS Number
        lbl_nhs = Label(Dataframe_left, text="NHS Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_nhs.grid(row=5, column=2, sticky=W)
        txt_nhs = Entry(Dataframe_left, textvariable=self.nhs_number, font=("times new roman", 12, "bold"), width=35)
        txt_nhs.grid(row=5, column=3)

        # Patient Name
        lbl_pname = Label(Dataframe_left, text="Patient Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_pname.grid(row=6, column=2, sticky=W)
        txt_pname = Entry(Dataframe_left, textvariable=self.patient_name, font=("times new roman", 12, "bold"), width=35)
        txt_pname.grid(row=6, column=3)

        # DOB
        lbl_dob = Label(Dataframe_left, text="Date of Birth", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_dob.grid(row=7, column=2, sticky=W)
        txt_dob = Entry(Dataframe_left, textvariable=self.dob, font=("times new roman", 12, "bold"), width=35)
        txt_dob.grid(row=7, column=3)

        # Address
        lbl_addr = Label(Dataframe_left, text="Patient Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_addr.grid(row=8, column=2, sticky=W)
        txt_addr = Entry(Dataframe_left, textvariable=self.patient_address, font=("times new roman", 12, "bold"), width=35)
        txt_addr.grid(row=8, column=3)

        # ============= Text Area (Right Side) ===========
        self.txtPrescription = Text(Dataframe_right, font=("times new roman", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ============= Buttons ==========================
        btnPrescription = Button(buttonframe, text="Prescription", font=("times new roman", 12, "bold"), width=22, bg="black", fg="gold", padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(buttonframe, command=self.iprescriptiondata, text="Prescription Data", font=("times new roman", 12, "bold"), width=22, bg="black", fg="gold", padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(buttonframe, text="Update", font=("times new roman", 12, "bold"), width=22, bg="black", fg="gold", padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(buttonframe, text="Delete", font=("times new roman", 12, "bold"), width=22, bg="black", fg="gold", padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(buttonframe, text="Clear", font=("times new roman", 12, "bold"), width=22, bg="black", fg="gold", padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(buttonframe, text="Exit", font=("times new roman", 12, "bold"), width=22, bg="black", fg="gold", padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # ============= Table Scrollbar ==================
        scroll_x = ttk.Scrollbar(detailframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailframe, orient=VERTICAL)
        
        self.hospital_table = ttk.Treeview(detailframe, columns=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "daily_dose", "side_effect", "further_information", "blood_pressure", "storage_advice", "medication", "patient_id", "nhs_number", "patient_name", "dob", "patient_address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # ============= Table Headings ===================
        headings = [
            ("nameoftablets", "Name of Tablets"), ("ref", "Reference No"), ("dose", "Dose"),
            ("nooftablets", "No of Tablets"), ("lot", "Lot"), ("issuedate", "Issue Date"),
            ("expdate", "Exp Date"), ("daily_dose", "Daily Dose"), ("side_effect", "Side Effect"),
            ("further_information", "Further Info"), ("blood_pressure", "Blood Pressure"),
            ("storage_advice", "Storage Advice"), ("medication", "Medication"), ("patient_id", "Patient ID"),
            ("nhs_number", "NHS Number"), ("patient_name", "Patient Name"), ("dob", "DOB"),
            ("patient_address", "Address")
        ]

        for col, text in headings:
            self.hospital_table.heading(col, text=text)
            self.hospital_table.column(col, width=100)

        self.hospital_table['show'] = 'headings'
        self.hospital_table.pack(fill=BOTH, expand=1)

    # ============= Database Function ================
    def iprescriptiondata(self):
        if self.nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="WLAN703A9F", database="mydata")
                my_cursor = conn.cursor()
                
                # Query - 18 Values match karni chahiye
                query = "INSERT INTO hospital VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
                my_cursor.execute(query, (
                    self.nameoftablets.get(),
                    self.ref.get(),
                    self.dose.get(),
                    self.nooftablets.get(),
                    self.lot.get(),
                    self.issuedate.get(),
                    self.expdate.get(),   # Fixed typo: was .det() now .get()
                    self.daily_dose.get(),
                    self.side_effect.get(),
                    self.further_information.get(),
                    self.blood_pressure.get(),
                    self.storage_advice.get(),
                    self.medication.get(),
                    self.patient_id.get(),
                    self.nhs_number.get(),
                    self.patient_name.get(),
                    self.dob.get(),
                    self.patient_address.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
            
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Reference Number already exists! Please use a unique Reference No.")
            
            except Exception as es:
                messagebox.showerror("Error", f"Could not connect to database: {str(es)}")

if __name__ == "__main__":
    root = Tk()
    obj = Hospital(root)
    root.mainloop()