import tkinter as tk
from tkinter import messagebox

# ==================== Classes ====================
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ==================== Main GUI ====================
class HospitalGUI:
    def _init_(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("500x450")

        self.doctors = []
        self.patients = []

        tk.Label(root, text="Hospital Management System",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # ---- Doctor Section ----
        tk.Label(root, text="Doctor Name:").pack()
        self.doc_name = tk.Entry(root)
        self.doc_name.pack()

        tk.Label(root, text="Specialization:").pack()
        self.doc_spec = tk.Entry(root)
        self.doc_spec.pack()

        tk.Button(root, text="Add Doctor",
                  command=self.add_doctor).pack(pady=5)

        # ---- Patient Section ----
        tk.Label(root, text="Patient Name:").pack()
        self.patient_name = tk.Entry(root)
        self.patient_name.pack()

        tk.Label(root, text="Age:").pack()
        self.patient_age = tk.Entry(root)
        self.patient_age.pack()

        tk.Button(root, text="Add Patient",
                  command=self.add_patient).pack(pady=5)

        tk.Button(root, text="Show Doctors & Patients",
                  command=self.show_info).pack(pady=10)

    def add_doctor(self):
        name = self.doc_name.get()
        spec = self.doc_spec.get()
        if name and spec:
            self.doctors.append(Doctor(name, spec))
            messagebox.showinfo("Success", f"Doctor '{name}' added.")
            self.doc_name.delete(0, tk.END)
            self.doc_spec.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Fill all doctor fields.")

    def add_patient(self):
        name = self.patient_name.get()
        age = self.patient_age.get()
        if name and age.isdigit():
            self.patients.append(Patient(name, int(age)))
            messagebox.showinfo("Success", f"Patient '{name}' added.")
            self.patient_name.delete(0, tk.END)
            self.patient_age.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Enter valid age.")

    def show_info(self):
        info = "Doctors:\n"
        for d in self.doctors:
            info += f"- {d.name} ({d.specialization})\n"
        info += "\nPatients:\n"
        for p in self.patients:
            info += f"- {p.name}, Age: {p.age}\n"
        messagebox.showinfo("Hospital Info", info)

# ==================== Run ====================
if __name__ == "_main_":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()