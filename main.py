import tkinter as tk
from tkinter import ttk, messagebox
from calculator import calculate_result
from dashboard import get_statistics
from student_manager import StudentManager
from validation import validate_student
from config import APP_TITLE, WINDOW_SIZE

class GradeMarkPro:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.manager = StudentManager()
        self.edit_roll = None
        self.setup_ui()
        self.load_table()
        self.update_dashboard()

    def setup_ui(self):
        head = ttk.Frame(self.root); head.pack(fill="x", padx=15, pady=10)
        ttk.Label(head, text=APP_TITLE, font=("Arial",18,"bold")).pack(side="left")
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=5)
        self.tab_dash, self.tab_students, self.tab_calc = ttk.Frame(self.tabs), ttk.Frame(self.tabs), ttk.Frame(self.tabs)
        self.tabs.add(self.tab_dash, text="Dashboard")
        self.tabs.add(self.tab_students, text="Students")
        self.tabs.add(self.tab_calc, text="Calculator")
        self.build_dashboard(); self.build_students(); self.build_calculator()

    def build_dashboard(self):
        ttk.Label(self.tab_dash,text="Class Performance",font=("Arial",14,"bold")).pack(pady=20)
        frame=ttk.Frame(self.tab_dash); frame.pack(pady=10)
        self.lbl_count=ttk.Label(frame,text="Students\n0",font=("Arial",14),anchor="center")
        self.lbl_avg=ttk.Label(frame,text="Average\n--",font=("Arial",14),anchor="center")
        self.lbl_pass=ttk.Label(frame,text="Passed\n--",font=("Arial",14),anchor="center")
        self.lbl_fail=ttk.Label(frame,text="Failed\n--",font=("Arial",14),anchor="center")
        for i,lbl in enumerate((self.lbl_count,self.lbl_avg,self.lbl_pass,self.lbl_fail)):
            lbl.grid(row=0,column=i,padx=20,ipadx=15)

    def build_students(self):
        form=ttk.Frame(self.tab_students); form.pack(pady=10)
        self.entries={}
        fields=[("Roll No","roll"),("Name","name"),("Branch","branch"),("Semester","sem"),("Marks","marks")]
        for r,(label,key) in enumerate(fields):
            ttk.Label(form,text=f"{label}:").grid(row=r,column=0,padx=5,pady=4,sticky="e")
            e=ttk.Entry(form,width=25); e.grid(row=r,column=1,padx=5,pady=4); self.entries[key]=e
        buttons=ttk.Frame(form); buttons.grid(row=5,column=0,columnspan=2,pady=10)
        self.btn_save=ttk.Button(buttons,text="Add Student",command=self.save_student); self.btn_save.pack(side="left",padx=4)
        ttk.Button(buttons,text="Edit",command=self.load_edit).pack(side="left",padx=4)
        ttk.Button(buttons,text="Delete",command=self.delete_student).pack(side="left",padx=4)
        ttk.Button(buttons,text="Clear",command=self.clear_form).pack(side="left",padx=4)
        cols=("roll","name","branch","sem","marks")
        self.tree=ttk.Treeview(self.tab_students,columns=cols,show="headings")
        headers={"roll":"Roll No","name":"Name","branch":"Branch","sem":"Semester","marks":"Marks"}
        for c in cols:
            self.tree.heading(c,text=headers[c]); self.tree.column(c,width=120,anchor="center")
        self.tree.pack(fill="both",expand=True,padx=15,pady=10)

    def build_calculator(self):
        box=ttk.Frame(self.tab_calc); box.pack(pady=20)
        ttk.Label(box,text="Obtained Marks:").grid(row=0,column=0,padx=5,pady=5)
        self.calc_got=ttk.Entry(box,width=15); self.calc_got.grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(box,text="Total Marks:").grid(row=1,column=0,padx=5,pady=5)
        self.calc_max=ttk.Entry(box,width=15); self.calc_max.grid(row=1,column=1,padx=5,pady=5)
        ttk.Button(box,text="Calculate",command=self.calculate).grid(row=2,column=0,columnspan=2,pady=10)
        self.calc_out=ttk.Label(self.tab_calc,text="Enter marks above.",font=("Arial",12)); self.calc_out.pack(pady=10)

    def load_table(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        for s in self.manager.students:
            self.tree.insert("",tk.END,values=(s["roll"],s["name"],s["branch"],s["sem"],s["marks"]))

    def save_student(self):
        try:
            data=validate_student({k:v.get().strip() for k,v in self.entries.items()})
            if self.edit_roll:
                self.manager.update(self.edit_roll,data); messagebox.showinfo("Success","Student updated.")
            else:
                self.manager.add(data); messagebox.showinfo("Success","Student added.")
            self.clear_form(); self.load_table(); self.update_dashboard()
        except ValueError as e: messagebox.showerror("Error",str(e))

    def load_edit(self):
        sel=self.tree.selection()
        if not sel: return messagebox.showwarning("Warning","Select a student to edit.")
        roll=self.tree.item(sel[0],"values")[0]; student=self.manager.find(roll)
        if student:
            self.edit_roll=roll
            for k,e in self.entries.items():
                e.delete(0,tk.END); e.insert(0,str(student[k]))
            self.btn_save.config(text="Update Student")

    def delete_student(self):
        sel=self.tree.selection()
        if not sel: return messagebox.showwarning("Warning","Select a student to delete.")
        roll=self.tree.item(sel[0],"values")[0]
        if messagebox.askyesno("Confirm",f"Delete roll number {roll}?"):
            self.manager.delete(roll); self.clear_form(); self.load_table(); self.update_dashboard()

    def clear_form(self):
        for e in self.entries.values(): e.delete(0,tk.END)
        self.edit_roll=None; self.btn_save.config(text="Add Student")

    def calculate(self):
        try:
            pct,grade,points=calculate_result(self.calc_got.get(),self.calc_max.get())
            self.calc_out.config(text=f"Score: {pct:.1f}%\nGrade: {grade} ({points} pts)")
        except ValueError as e: messagebox.showerror("Error",str(e))

    def update_dashboard(self):
        s=get_statistics(self.manager.students)
        self.lbl_count.config(text=f"Students\n{s['total']}")
        self.lbl_avg.config(text=f"Average\n{s['average']:.1f}" if s["total"] else "Average\n--")
        self.lbl_pass.config(text=f"Passed\n{s['passed']}/{s['total']}" if s["total"] else "Passed\n--")
        self.lbl_fail.config(text=f"Failed\n{s['failed']}/{s['total']}" if s["total"] else "Failed\n--")

if __name__=="__main__":
    root=tk.Tk(); GradeMarkPro(root); root.mainloop()
