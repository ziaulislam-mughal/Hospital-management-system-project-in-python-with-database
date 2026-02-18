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
        lbltitle = Label(
            self.root,
            text="Hospital Management System",
            font=("times new roman", 50, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbltitle.pack(side=TOP, fill=X)

        # ============= Dataframes =======================
        Datafram = Frame(self.root, bd=15, relief=RIDGE)
        Datafram.place(x=0, y=100, width=1350, height=380)

        Dataframe_left = LabelFrame(
            Datafram,
            text="Patient Information",
            bd=4,
            relief=RIDGE,
            font=("times new roman", 12, "bold"),
            fg="black",
            padx=10,
        )
        Dataframe_left.place(x=0, y=5, width=850, height=350)

        Dataframe_right = LabelFrame(
            Datafram,
            text="Prescription",
            bd=4,
            relief=RIDGE,
            fg="black",
            font=("times new roman", 12, "bold"),
            padx=10,
        )
        Dataframe_right.place(x=860, y=5, width=440, height=350)

        # ============= Buttons Frame ====================
        buttonframe = Frame(self.root, bd=15, relief=RIDGE)
        buttonframe.place(x=0, y=480, width=1350, height=70)

        # ============= Details Frame ====================
        detailframe = Frame(self.root, bd=15, relief=RIDGE)
        detailframe.place(x=0, y=550, width=1350, height=150)

        # ============= Input Fields (Left Frame) ========

        # Name of Tablets
        lbl_tablet = Label(
            Dataframe_left,
            text="Name of Tablet",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_tablet.grid(row=0, column=0, sticky=W)

        com_tablet = ttk.Combobox(
            Dataframe_left,
            textvariable=self.nameoftablets,
            font=("times new roman", 12, "bold"),
            width=33,
        )
        com_tablet["values"] = (
            "Brufen",
            "Paracetamol",
            "Dolo 650",
            "Crocin",
            "Disprin",
        )
        com_tablet.grid(row=0, column=1)

        # Reference No
        lbl_ref = Label(
            Dataframe_left,
            text="Reference No",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_ref.grid(row=1, column=0, sticky=W)
        txt_ref = Entry(
            Dataframe_left,
            textvariable=self.ref,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_ref.grid(row=1, column=1)

        # Dose
        lbl_dose = Label(
            Dataframe_left,
            text="Dose",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_dose.grid(row=2, column=0, sticky=W)
        txt_dose = Entry(
            Dataframe_left,
            textvariable=self.dose,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_dose.grid(row=2, column=1)

        # No of Tablets
        lbl_no = Label(
            Dataframe_left,
            text="No of Tablets",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_no.grid(row=3, column=0, sticky=W)
        txt_no = Entry(
            Dataframe_left,
            textvariable=self.nooftablets,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_no.grid(row=3, column=1)

        # Lot
        lbl_lot = Label(
            Dataframe_left,
            text="Lot",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_lot.grid(row=4, column=0, sticky=W)
        txt_lot = Entry(
            Dataframe_left,
            textvariable=self.lot,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_lot.grid(row=4, column=1)

        # Issue Date
        lbl_issue = Label(
            Dataframe_left,
            text="Issue Date",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_issue.grid(row=5, column=0, sticky=W)
        txt_issue = Entry(
            Dataframe_left,
            textvariable=self.issuedate,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_issue.grid(row=5, column=1)

        # Exp Date
        lbl_exp = Label(
            Dataframe_left,
            text="Exp Date",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_exp.grid(row=6, column=0, sticky=W)
        txt_exp = Entry(
            Dataframe_left,
            textvariable=self.expdate,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_exp.grid(row=6, column=1)

        # Daily Dose
        lbl_daily = Label(
            Dataframe_left,
            text="Daily Dose",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_daily.grid(row=7, column=0, sticky=W)
        txt_daily = Entry(
            Dataframe_left,
            textvariable=self.daily_dose,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_daily.grid(row=7, column=1)

        # Side Effect
        lbl_side = Label(
            Dataframe_left,
            text="Side Effect",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_side.grid(row=8, column=0, sticky=W)
        txt_side = Entry(
            Dataframe_left,
            textvariable=self.side_effect,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_side.grid(row=8, column=1)

        # Further Info (Column 2)
        lbl_further = Label(
            Dataframe_left,
            text="Further Info",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_further.grid(row=0, column=2, sticky=W)
        txt_further = Entry(
            Dataframe_left,
            textvariable=self.further_information,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_further.grid(row=0, column=3)

        # Blood Pressure
        lbl_bp = Label(
            Dataframe_left,
            text="Blood Pressure",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_bp.grid(row=1, column=2, sticky=W)
        txt_bp = Entry(
            Dataframe_left,
            textvariable=self.blood_pressure,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_bp.grid(row=1, column=3)

        # Storage Advice
        lbl_store = Label(
            Dataframe_left,
            text="Storage Advice",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_store.grid(row=2, column=2, sticky=W)
        txt_store = Entry(
            Dataframe_left,
            textvariable=self.storage_advice,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_store.grid(row=2, column=3)

        # Medication
        lbl_med = Label(
            Dataframe_left,
            text="Medication",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_med.grid(row=3, column=2, sticky=W)
        txt_med = Entry(
            Dataframe_left,
            textvariable=self.medication,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_med.grid(row=3, column=3)

        # Patient ID
        lbl_pid = Label(
            Dataframe_left,
            text="Patient ID",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_pid.grid(row=4, column=2, sticky=W)
        txt_pid = Entry(
            Dataframe_left,
            textvariable=self.patient_id,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_pid.grid(row=4, column=3)

        # NHS Number
        lbl_nhs = Label(
            Dataframe_left,
            text="NHS Number",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_nhs.grid(row=5, column=2, sticky=W)
        txt_nhs = Entry(
            Dataframe_left,
            textvariable=self.nhs_number,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_nhs.grid(row=5, column=3)

        # Patient Name
        lbl_pname = Label(
            Dataframe_left,
            text="Patient Name",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_pname.grid(row=6, column=2, sticky=W)
        txt_pname = Entry(
            Dataframe_left,
            textvariable=self.patient_name,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_pname.grid(row=6, column=3)

        # DOB
        lbl_dob = Label(
            Dataframe_left,
            text="Date of Birth",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_dob.grid(row=7, column=2, sticky=W)
        txt_dob = Entry(
            Dataframe_left,
            textvariable=self.dob,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_dob.grid(row=7, column=3)

        # Address
        lbl_addr = Label(
            Dataframe_left,
            text="Patient Address",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lbl_addr.grid(row=8, column=2, sticky=W)
        txt_addr = Entry(
            Dataframe_left,
            textvariable=self.patient_address,
            font=("times new roman", 12, "bold"),
            width=35,
        )
        txt_addr.grid(row=8, column=3)

        # ============= Text Area (Right Side) ===========
        self.txtPrescription = Text(
            Dataframe_right,
            font=("times new roman", 12, "bold"),
            width=45,
            height=16,
            padx=2,
            pady=6,
        )
        self.txtPrescription.grid(row=0, column=0)

        # ============= Buttons ==========================
        btnPrescription = Button(
            buttonframe,
            command=self.precription_show,
            text="Prescription",
            font=("times new roman", 12, "bold"),
            width=22,
            bg="black",
            fg="gold",
            padx=2,
            pady=6,
        )
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(
            buttonframe,
            command=self.iprescriptiondata,
            text="Prescription Data",
            font=("times new roman", 12, "bold"),
            width=22,
            bg="black",
            fg="gold",
            padx=2,
            pady=6,
        )
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(
            buttonframe,
            command=self.update_data,
            text="Update",
            font=("times new roman", 12, "bold"),
            width=22,
            bg="black",
            fg="gold",
            padx=2,
            pady=6,
        )
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(
            buttonframe,
            text="Delete",
            font=("times new roman", 12, "bold"),
            width=22,
            bg="black",
            fg="gold",
            padx=2,
            pady=6,
        )
        btnDelete.grid(row=0, column=3)

        btnClear = Button(
            buttonframe,
            text="Clear",
            font=("times new roman", 12, "bold"),
            width=22,
            bg="black",
            fg="gold",
            padx=2,
            pady=6,
        )
        btnClear.grid(row=0, column=4)

        btnExit = Button(
            buttonframe,
            text="Exit",
            font=("times new roman", 12, "bold"),
            width=22,
            bg="black",
            fg="gold",
            padx=2,
            pady=6,
        )
        btnExit.grid(row=0, column=5)

        # ============= Table Scrollbar ==================
        scroll_x = ttk.Scrollbar(detailframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(
            detailframe,
            columns=(
                "nameoftablets",
                "ref",
                "dose",
                "nooftablets",
                "lot",
                "issuedate",
                "expdate",
                "daily_dose",
                "side_effect",
                "further_information",
                "blood_pressure",
                "storage_advice",
                "medication",
                "patient_id",
                "nhs_number",
                "patient_name",
                "dob",
                "patient_address",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # ============= Table Headings ===================
        headings = [
            ("nameoftablets", "Name of Tablets"),
            ("ref", "Reference No"),
            ("dose", "Dose"),
            ("nooftablets", "No of Tablets"),
            ("lot", "Lot"),
            ("issuedate", "Issue Date"),
            ("expdate", "Exp Date"),
            ("daily_dose", "Daily Dose"),
            ("side_effect", "Side Effect"),
            ("further_information", "Further Info"),
            ("blood_pressure", "Blood Pressure"),
            ("storage_advice", "Storage Advice"),
            ("medication", "Medication"),
            ("patient_id", "Patient ID"),
            ("nhs_number", "NHS Number"),
            ("patient_name", "Patient Name"),
            ("dob", "DOB"),
            ("patient_address", "Address"),
        ]

        for col, text in headings:
            self.hospital_table.heading(col, text=text)
            self.hospital_table.column(col, width=100)

        self.hospital_table["show"] = "headings"
        # Jab table par click ho, to get_cursor function chale
        # Yeh line zaroori hai, iske bina click kaam nahi karega
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    # ============= Database Function ================
    def iprescriptiondata(self):
        if self.nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="WLAN703A9F",
                    database="mydata",
                )
                my_cursor = conn.cursor()

                # Query - 18 Values match karni chahiye
                query = "INSERT INTO hospital VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                my_cursor.execute(
                    query,
                    (
                        self.nameoftablets.get(),
                        self.ref.get(),
                        self.dose.get(),
                        self.nooftablets.get(),
                        self.lot.get(),
                        self.issuedate.get(),
                        self.expdate.get(),  # Fixed typo: was .det() now .get()
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
                        self.patient_address.get(),
                    ),
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
                self.fetch_data()

            except mysql.connector.IntegrityError:
                messagebox.showerror(
                    "Error",
                    "Reference Number already exists! Please use a unique Reference No.",
                )

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Could not connect to database: {str(es)}"
                )

    def fetch_data(self):
        # 1. Database se connection banane ke liye (taake hum data le sakein)
        conn = mysql.connector.connect(
            host="localhost", username="root", password="WLAN703A9F", database="mydata"
        )

        # 2. Cursor banana (Cursor ek tool hai jo SQL queries ko run karta hai)
        my_cursor = conn.cursor()

        # 3. SQL Query run karna: "select * from hospital" ka matlab hai "hospital table ka saara data le aao"
        my_cursor.execute("select * from hospital")

        # 4. Saara data jo database se mila, usay 'rows' naam ke variable mein store karna
        rows = my_cursor.fetchall()

        # 5. Check karna ki kya database mein koi data hai bhi ya nahi?
        if len(rows) != 0:

            # 6. Purana data hatana: Agar table mein pehle se kuch dikh raha hai to usay saaf kar do taake duplication na ho
            self.hospital_table.delete(*self.hospital_table.get_children())

            # 7. Loop chalana: Ek-ek karke saari lines ko table (GUI) mein daalna
            for i in rows:
                self.hospital_table.insert("", END, values=i)

            # 8. Changes ko final karna (Commit data fetch mein zaroori nahi hota par connection refresh rehta hai)
            conn.commit()

        # 9. Connection band karna taake PC slow na ho
        conn.close()

    def update_data(self):
        # 1. Validation: Agar Reference No khali hai to update kisko karenge?
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference No is required to update")
        else:
            try:
                # 2. Connection banaya
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="WLAN703A9F",
                    database="mydata",
                )
                my_cursor = conn.cursor()

                # 3. SQL Query (Dhyan se dekhein: hum Reference_No ko chor kar baaki sab update kar rahe hain)
                # Hum keh rahe hain: "SET column=%s WHERE Reference_No=%s"

                my_cursor.execute(
                    "UPDATE hospital SET Name_of_Tablets=%s, Dose=%s, No_of_Tablets=%s, Lot=%s, Issue_Date=%s, Exp_Date=%s, Daily_Dose=%s, Side_Effect=%s, Further_Information=%s, Blood_Pressure=%s, Storage_Advice=%s, Medication=%s, Patient_Id=%s, NHS_Number=%s, Patient_Name=%s, Date_of_Birth=%s, Patient_Address=%s WHERE Reference_No=%s",
                    (
                        self.nameoftablets.get(),
                        self.dose.get(),
                        self.nooftablets.get(),
                        self.lot.get(),
                        self.issuedate.get(),
                        self.expdate.get(),
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
                        self.patient_address.get(),
                        # Sabse last mein Reference No ayega kyunki Query mein 'WHERE Reference_No=%s' last mein hai
                        self.ref.get(),
                    ),
                )

                # 4. Save changes
                conn.commit()

                # 5. Table refresh karein taake naya data dikhe
                self.fetch_data()

                # 6. Connection close
                conn.close()

                messagebox.showinfo("Update", "Record has been updated successfully")

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

    def get_cursor(self, event=""):  # <--- Yahan 'event=""' likhna zaroori hai

        # 1. Jis row par click kiya hai usay select karein
        cursor_row = self.hospital_table.focus()

        # 2. Us row ka sara content nikalein
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        # 3. Data ko variables mein set karein (taake wo upar boxes mein aa jaye)
        if len(row) != 0:
            self.nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.dose.set(row[2])
            self.nooftablets.set(row[3])
            self.lot.set(row[4])
            self.issuedate.set(row[5])
            self.expdate.set(row[6])
            self.daily_dose.set(row[7])
            self.side_effect.set(row[8])
            self.further_information.set(row[9])
            self.blood_pressure.set(row[10])
            self.storage_advice.set(row[11])
            self.medication.set(row[12])
            self.patient_id.set(row[13])
            self.nhs_number.set(row[14])
            self.patient_name.set(row[15])
            self.dob.set(row[16])
            self.patient_address.set(row[17])


    def precription_show(self):
        self.txtPrescription.insert(END, f"Patient Name:\t\t{self.patient_name.get()}\n")
        self.txtPrescription.insert(END, f"Date of Birth:\t\t{self.dob.get()}\n")
        self.txtPrescription.insert(END, f"Patient Address:\t\t{self.patient_address.get()}\n")
        self.txtPrescription.insert(END, f"Name of Tablets:\t\t{self.nameoftablets.get()}\n")
        self.txtPrescription.insert(END, f"Reference No:\t\t{self.ref.get()}\n")
        self.txtPrescription.insert(END, f"Dose:\t\t{self.dose.get()}\n")
        self.txtPrescription.insert(END, f"No of Tablets:\t\t{self.nooftablets.get()}\n")   
        self.txtPrescription.insert(END, f"Lot:\t\t{self.lot.get()}\n")
        self.txtPrescription.insert(END, f"Issue Date:\t\t{self.issuedate.get()}\n")
        self.txtPrescription.insert(END, f"Exp Date:\t\t{self.expdate.get()}\n")
        self.txtPrescription.insert(END, f"Daily Dose:\t\t{self.daily_dose.get()}\n")
        self.txtPrescription.insert(END, f"Side Effect:\t\t{self.side_effect.get()}\n")
        self.txtPrescription.insert(END, f"Further Information:\t\t{self.further_information.get()}\n")
        self.txtPrescription.insert(END, f"Blood Pressure:\t\t{self.blood_pressure.get()}\n")
        self.txtPrescription.insert(END, f"Storage Advice:\t\t{self.storage_advice.get()}\n")
        self.txtPrescription.insert(END, f"Medication:\t\t{self.medication.get()}\n")
        self.txtPrescription.insert(END, f"Patient ID:\t\t{self.patient_id.get()}\n")
        self.txtPrescription.insert(END, f"NHS Number:\t\t{self.nhs_number.get()}\n")


if __name__ == "__main__":

    root = Tk()
    obj = Hospital(root)
    root.mainloop()
