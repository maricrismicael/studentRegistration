import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
from data_analytics import *

# Database Connection
conn = sqlite3.connect('database.db')
# Creating a Table
table_create_query = '''CREATE TABLE IF NOT EXISTS studentInfo
(Student_ID int primary key, First_Name text, Last_Name text, Age int, Year int,
Section int, Gender text, Mode_Learning text, Final_Grade int)
'''
conn.execute(table_create_query)

# Table window
def display_table():
    conn = sqlite3.connect('database.db')
    table_window = Toplevel(window)
    table_window.grab_set()
    table_window.geometry("800x350")
    table_window.title('Table Display')
    table_window.resizable(0, 0)

    r_set = conn.execute('SELECT * from studentInfo')
    i = 0   # row value inside the loop
    for studentInfo in r_set:
        for j in range(len(studentInfo)):
            e = Entry(table_window, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, studentInfo[j])
        i = i+1
    conn.close()

# Editor window
def edit():
    editor = Tk()
    editor.title("Record Editor")
    editor_frame = tkinter.Frame(editor)
    editor_frame.pack()
    editor_frame.config(bg="light blue")

    e_student_info = tkinter.LabelFrame(editor_frame, text="Student Information")
    e_student_info.grid(row=0, column=0, padx=20, pady=20)

    # Label
    e_student_id_label = tkinter.Label(e_student_info, text="Student ID")
    e_student_id_label.grid(row=0, column=0)
    e_first_name_label = tkinter.Label(e_student_info, text="First Name")
    e_first_name_label.grid(row=0, column=1)
    e_last_name_label = tkinter.Label(e_student_info, text="Last Name")
    e_last_name_label.grid(row=0, column=2)

    # Text Box
    global e_student_id_entry
    global e_first_name_entry
    global e_last_name_entry
    e_student_id_entry = tkinter.Entry(e_student_info)
    e_first_name_entry = tkinter.Entry(e_student_info)
    e_last_name_entry = tkinter.Entry(e_student_info)
    e_student_id_entry.grid(row=1, column=0)
    e_first_name_entry.grid(row=1, column=1)
    e_last_name_entry.grid(row=1, column=2)

    # Spinbox
    global e_age_spinbox
    e_age_label = tkinter.Label(e_student_info, text="Age")
    e_age_label.grid(row=2, column=0)
    e_age_spinbox = tkinter.Spinbox(e_student_info)
    e_age_spinbox.grid(row=3, column=0)


    # Combobox
    global e_year_combobox
    e_year_label = tkinter.Label(e_student_info, text="Year")
    e_year_combobox = ttk.Combobox(e_student_info, values=["1", "2", "3", "4", "5"])
    e_year_label.grid(row=2, column=1)
    e_year_combobox.grid(row=3, column=1)

    global e_section_combobox
    e_section_label = tkinter.Label(e_student_info, text="Section")
    e_section_combobox = ttk.Combobox(e_student_info, values=["1", "2", "3", "4", "5"])
    e_section_label.grid(row=2, column=2)
    e_section_combobox.grid(row=3, column=2)

    global e_gender_combobox
    e_gender_label = tkinter.Label(e_student_info, text="Gender")
    e_gender_combobox = ttk.Combobox(e_student_info, values=["Prefer Not to Answer", "Female", "Male"])
    e_gender_label.grid(row=4, column=0)
    e_gender_combobox.grid(row=5, column=0)

    global e_mode_learn_combobox
    e_mode_learn_label = tkinter.Label(e_student_info, text="Mode of Learning")
    e_mode_learn_combobox = ttk.Combobox(e_student_info, values=["Synchronous", "Asynchronous"])
    e_mode_learn_label.grid(row=4, column=1)
    e_mode_learn_combobox.grid(row=5, column=1)
    # Text box
    global e_final_entry
    e_final_label = tkinter.Label(e_student_info, text="Final Grade")
    e_final_label.grid(row=4, column=2)
    e_final_entry = tkinter.Entry(e_student_info)
    e_final_entry.grid(row=5, column=2)

    # Button Frame
    e_button_frame = tkinter.LabelFrame(editor_frame, bg="light blue")
    e_button_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)
    e_clear_button = tkinter.Button(e_button_frame, text='Clear Input', command=lambda: e_clear())  # Clear
    e_clear_button.grid(row=0, column=1, padx=100)
    e_save_button = tkinter.Button(e_button_frame, text='Save Changes', command=lambda: update_record())
    e_save_button.grid(row=0, column=2, padx=100)

    # Clear Input in Editor window
    def e_clear():
        for widget in e_student_info.winfo_children():
            if isinstance(widget, tkinter.Entry):
                widget.delete(0, 'end')
            if isinstance(widget, tkinter.Spinbox):
                widget.delete(0, 'end')
            if isinstance(widget, ttk.Combobox):
                widget.delete(0, 'end')

    for widget in e_student_info.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #Database Connection
    conn = sqlite3.connect('database.db')
    # Create cursor
    c = conn.cursor()

    # Show old record content in editor window
    record_id = search_entry.get()
    # Query the database
    c.execute("SELECT * FROM studentInfo WHERE oid=" + record_id)
    records = c.fetchall()
    for record in records:
        e_student_id_entry.insert(0, record[0])
        e_first_name_entry.insert(0, record[1])
        e_last_name_entry.insert(0, record[2])
        e_age_spinbox.insert(0, record[3])
        e_year_combobox.insert(0, record[4])
        e_section_combobox.insert(0, record[5])
        e_gender_combobox.insert(0, record[6])
        e_mode_learn_combobox.insert(0, record[7])
        e_final_entry.insert(0, record[8])

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
# End of Editor window

# Start of Main window
window = Tk()
window.title("Project")
# window.config(bg="light blue")

frame = tkinter.Frame(window)
frame.pack()
frame.config(bg="light blue")

student_info = tkinter.LabelFrame(frame, text="Student Information")
student_info.grid(row=0, column=0, padx=20, pady=20)

# Label
student_id_label = tkinter.Label(student_info, text="Student ID")
student_id_label.grid(row=0, column=0)
first_name_label = tkinter.Label(student_info, text="First Name")
first_name_label.grid(row=0, column=1)
last_name_label = tkinter.Label(student_info, text="Last Name")
last_name_label.grid(row=0, column=2)


# Text Box
student_id_entry = tkinter.Entry(student_info)
first_name_entry = tkinter.Entry(student_info)
last_name_entry = tkinter.Entry(student_info)
student_id_entry.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

# Spinbox
age_label = tkinter.Label(student_info, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(student_info, from_= 16, to = 100)
age_spinbox.grid(row=3, column=0)

# Combobox
year_label = tkinter.Label(student_info, text="Year")
year_combobox = ttk.Combobox(student_info, values=["1", "2", "3", "4", "5"])
year_label.grid(row=2, column=1)
year_combobox.grid(row=3, column=1)

section_label = tkinter.Label(student_info, text="Section")
section_combobox = ttk.Combobox(student_info, values=["1", "2", "3", "4", "5"])
section_label.grid(row=2, column=2)
section_combobox.grid(row=3, column=2)

gender_label = tkinter.Label(student_info, text="Gender")
gender_combobox = ttk.Combobox(student_info, values=["Prefer Not to Answer", "Female", "Male"])
gender_label.grid(row=4, column=0)
gender_combobox.grid(row=5, column=0)

mode_learn_label = tkinter.Label(student_info, text="Mode of Learning")
mode_learn_combobox = ttk.Combobox(student_info, values=["Synchronous", "Asynchronous"])
mode_learn_label.grid(row=4, column=1)
mode_learn_combobox.grid(row=5, column=1)

# Text box
final_label = tkinter.Label(student_info, text="Final Grade")
final_label.grid(row=4, column=2)
final_entry = tkinter.Entry(student_info)
final_entry.grid(row=5, column=2)

for widget in student_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Search Frame
search_frame = tkinter.LabelFrame(frame)
search_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)
search_label = tkinter.Label(search_frame, text="Search Record Number:")
search_label.grid(row=0, column=0, padx= 20)
search_entry = tkinter.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=20)

# Button Frame
button_frame = tkinter.LabelFrame(frame, bg="light blue")
button_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

clear_button = tkinter.Button(button_frame, text='Clear Input', command=lambda: clear())  # Clear input
clear_button.grid(row=0, column=0, padx=10)
display_button = tkinter.Button(button_frame, text='Display Table', command=display_table)  # Display Table
display_button.grid(row=0, column=1, padx=10)
add_button = tkinter.Button(button_frame, text='Create Record', command=lambda: create_record())  # Create record
add_button.grid(row=0, column=2, padx=10)
delete_button = tkinter.Button(button_frame, text='Delete Record', command=lambda: delete_record())  # Delete record
delete_button.grid(row=0, column=3, padx=10)
update_button = tkinter.Button(button_frame, text='Update Record', command=lambda: edit())  # Update/Edit record
update_button.grid(row=0, column=4, padx=10)


#Data Analytics
DA_frame = tkinter.LabelFrame(frame, bg="light blue")
DA_frame.grid(row=3, column=0, sticky="news", padx=20, pady=20)
DA_label = tkinter.Label(DA_frame, text="DATA ANALYTICS:")
DA_label.grid(row=0, column=0, padx= 0)

grade_button = tkinter.Button(DA_frame, text='Grades Analytics', command=grade)  # grades analytics
grade_button.grid(row=0, column=1, padx=10)
year_button = tkinter.Button(DA_frame, text='Year Analytics', command=year)  # year analytics
year_button.grid(row=0, column=2, padx=10)
age_button = tkinter.Button(DA_frame, text='Age Analytics', command=age)  # age analytics
age_button.grid(row=0, column=3, padx=10)

# Display Result/Output
output_frame =tkinter.LabelFrame(frame)
output_frame.grid(row=4, column=0, sticky="news", padx=20, pady=20)

output = tkinter.Label(output_frame, text='Output: ')
output.grid(row=0, column=0, padx=20)

my_str = tkinter.StringVar()
l9 = tkinter.Label(output_frame, textvariable=my_str)
l9.grid(row=0, column=1, padx=20)
my_str.set("")

# Create record
def create_record():
    flag_validation = True  # set the flag
    stud_id = student_id_entry.get()  # read id
    firstname = first_name_entry.get()  # read first name
    lastname = last_name_entry.get()  # read last name
    age = age_spinbox.get()  # read age
    year = year_combobox.get()  # read year
    section = section_combobox.get()    # read section
    gender = gender_combobox.get()  # read gender
    mode = mode_learn_combobox.get()  # read mode
    final = final_entry.get()  # read final

    # length of name and ender more than 2
    if len(firstname) < 2 or len(lastname) < 2 or len(gender) < 2 or len(mode) < 2:
        flag_validation = False
    try:
        val = int(age)
        val = int(year)
        val = int(section)
        val = int(final)  # checking mark as integer
    except:
        flag_validation = False

    if flag_validation:
        my_str.set("Creating record...")
        try:
            # print("Connected to database successfully")
            data = (stud_id, firstname, lastname, age, year, section, gender, mode, final)

            query = "INSERT INTO studentInfo values(?,?,?,?,?,?,?,?,?)"
            conn.execute(query, data)
            conn.commit()

            l9.grid()
            l9.config(fg='green')  # foreground color
            l9.config(bg='white')  # background color
            my_str.set("Record successfully created!")
            l9.after(3000, lambda: l9.grid_remove())

        except sqlite3.Error as my_error:
            l9.grid()
            # return error
            l9.config(fg='red')  # foreground color
            l9.config(bg='yellow')  # background color
            print(my_error)
            my_str.set(my_error)
    else:
        l9.grid()
        l9.config(fg='red')  # foreground color
        l9.config(bg='yellow')  # background color
        my_str.set("check inputs.")
        l9.after(3000, lambda: l9.grid_remove())

# Clear input in main window
def clear():
    for widget in student_info.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, 'end')
        if isinstance(widget, tkinter.Spinbox):
            widget.delete(0, 'end')
        if isinstance(widget, ttk.Combobox):
            widget.delete(0, 'end')
        for widget in search_frame.winfo_children():
            if isinstance(widget, tkinter.Entry):
                widget.delete(0, 'end')

# Deleting record
def delete_record():
    conn = sqlite3.connect('database.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from studentInfo WHERE oid=" + search_entry.get())

    # Commit Changes
    conn.commit()
    l9.grid()
    l9.config(fg='green')  # foreground color
    l9.config(bg='white')  # background color
    my_str.set("Record successfully deleted!")
    l9.after(3000, lambda: l9.grid_remove())

    # Close Connection
    conn.close()


# Update/Edit record
def update_record():
    conn = sqlite3.connect('database.db')
    # Create cursor
    c = conn.cursor()

    # Update a record
    record_id = search_entry.get()

    c.execute("""UPDATE studentInfo SET
        Student_ID = :sID,
        First_Name = :first,
        Last_Name = :last,
        Age = :age,
        Year = :year,
        Section = :section,
        Gender = :gender,
        Mode_learning = :mode,
        Final_Grade = :final
    
        WHERE oid = :oid""",
        {
        'sID': e_student_id_entry.get(),
        'first': e_first_name_entry.get(),
        'last': e_last_name_entry.get(),
        'age': e_age_spinbox.get(),
        'year': e_year_combobox.get(),
        'section': e_section_combobox.get(),
        'gender': e_gender_combobox.get(),
        'mode': e_mode_learn_combobox.get(),
        'final': e_final_entry.get(),
        'oid': record_id
        })

    # Commit Changes
    conn.commit()
    l9.grid()
    l9.config(fg='green')  # foreground color
    l9.config(bg='white')  # background color
    my_str.set("Record successfully updated!")
    l9.after(3000, lambda: l9.grid_remove())

    # Close Connection
    conn.close()


window.mainloop()

conn.close()
