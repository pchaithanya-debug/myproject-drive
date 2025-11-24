import sqlite3
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        roll INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        marks INTEGER
    )
    """)
    connection.commit()
create_table()
def roll_exists(roll):
    cursor.execute("SELECT 1 FROM students WHERE roll=?", (roll,))
    return cursor.fetchone() is not None
def add_student():
    while True:
        try:
            roll = int(input("Enter Roll Number: "))
            if roll_exists(roll):
                print("Roll number already exists! Try another.\n")
                continue
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            if not (3 < age < 100):
                print("Please enter valid Age!\n")
                continue
            marks = int(input("Enter Marks: "))
            cursor.execute("INSERT INTO students VALUES(?,?,?,?)", (roll, name, age, marks))
            connection.commit()
            print("Student added successfully!\n")
            break
        except ValueError:
            print("Please enter Roll Number, Age, Marks as integers\n")
def update_student():
    while True:
        try:
            roll = int(input("Enter Roll Number to Update: "))
            if not roll_exists(roll):
                print("Roll number not found! Try again.\n")
                continue
            break
        except ValueError:
            print("Please Enter valid Roll Number!")
    print("1. Name\n2. Age\n3. Marks")
    while True:
        try:
            choice = int(input("Enter choice: "))
            break
        except ValueError:
            print("Enter a number only!")
    if choice == 1:
        new_name = input("Enter new name: ")
        cursor.execute("UPDATE students SET name=? WHERE roll=?", (new_name, roll))
    elif choice == 2:
        while True:
            try:
                new_age = int(input("Enter new age: "))
                if 3 < new_age < 100:
                    break
                print("Enter valid age!")
            except ValueError:
                print("Enter valid age!")
        cursor.execute("UPDATE students SET age=? WHERE roll=?", (new_age, roll))
    elif choice == 3:
        while True:
            try:
                new_marks = int(input("Enter new marks: "))
                break
            except ValueError:
                print("Enter valid marks!")
        cursor.execute("UPDATE students SET marks=? WHERE roll=?", (new_marks, roll))
    else:
        print("Invalid choice!")
        return
    connection.commit()
    print("Student updated successfully!\n")
def delete_student():
    while True:
        try:
            roll = int(input("Enter Roll Number to Delete: "))
            if not roll_exists(roll):
                print("Roll number not found! Try again.\n")
                continue
            break
        except ValueError:
            print("Enter valid Roll Number!")
    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
    connection.commit()
    print("Student deleted successfully!\n")
def search_student():
    print("1. Roll Number\n2. Name")
    while True:
        try:
            choice = int(input("Enter choice: "))
            break
        except ValueError:
            print("Enter a number!")
    if choice == 1:
        try:
            roll = int(input("Enter Roll Number: "))
            if not roll_exists(roll):
                print("Roll number not found!\n")
                return
        except ValueError:
            print("Enter valid Roll Number!")
            return
        cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    else:
        name = input("Enter Name: ")
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    result = cursor.fetchall()
    if result:
        print("\n--- STUDENT DETAILS ---")
        for row in result:
            print(f"Roll: {row[0]}\nName: {row[1]}\nAge: {row[2]}\nMarks: {row[3]}")
    else:
        print("No student found!")
    print()
def display_all():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- ALL STUDENTS ---")
    for row in rows:
        print(f"Roll: {row[0]}\nName: {row[1]}\nAge: {row[2]}\nMarks: {row[3]}")
        print("-"*50)
    print()
def drop_table():
    cursor.execute("DROP TABLE students")
    connection.commit()
    print("Table dropped successfully!")
    create_table()
while True:
    print("+===== STUDENT MANAGEMENT SYSTEM ======+")
    print("| 1. Add Student                       |")
    print("| 2. Update Student                    |")
    print("| 3. Delete Student                    |")
    print("| 4. Search Student                    |")
    print("| 5. Display All Students              |")
    print("| 6. Drop student table                |")
    print("| 7. Exit                              |")
    print("+-------------------------------------+")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please Enter valid Choice!\n")
        continue
    print()
    if choice == 1:
        add_student()
    elif choice == 2:
        update_student()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        search_student()
    elif choice == 5:
        display_all()
    elif choice == 6:
        drop_table()
    elif choice == 7:
        print("Exited successfully!")
        break
    else:
        print("Invalid choice! Try again.\n")
connection.close()
