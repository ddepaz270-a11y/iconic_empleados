import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rabinal123",
    database="library"
)


def Create():
    studentName = input("ENTER STUDENT NAME: ")
    bookTitle = input("ENTER BOOK TITLE: ")
    loanDate = input("ENTER LOAN DATE: ")
    returnDate = input("ENTER RETURN DATE: ")
    status = input("ENTER STATUS: ")

    if status == "Borrowed":
        status = "Borrowed"
    elif status == "Returned":
        status = "Returned"
    elif status == "Overdue":
        status = "Overdue"
    else:
        print("INVALID STATUS.")
        return

    cursor = conexion.cursor()
    query = "INSERT INTO loans (studentName, bookTitle, loanDate, returnDate, status) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query,(studentName, bookTitle, loanDate, returnDate, status))
    conexion.commit()
    print("REGISTRATION COMPLETE.")


def Read():
    cursor = conexion.cursor()
    query = "SELECT * FROM loans"
    cursor.execute(query)
    for file in cursor.fetchall():
        print(file)


def Update():
    id = int(input("ENTER ID: "))
    status = input("ENTER NEW STATUS: ")
    if status == "Borrowed":
        status = "Borrowed"
    elif status == "Returned":
        status = "Returned"
    elif status == "Overdue":
        status = "Overdue"
    else:
        print("INVALID STATUS.")
        return
    cursor = conexion.cursor()
    query = "UPDATE loans SET status=% WHERE id=%s"
    cursor.execute(query, (status, id))
    conexion.commit()
    print("STATUS UPDATED.")


def Delete():
    id = int(input("ENTER ID: "))
    cursor = conexion.cursor()
    query = "DELETE FROM loans WHERE id=%s"
    cursor.execute(query, (id,))
    conexion.commit()
    print("DELETE COMPLETE.")


def menu():
    while True:
        file = ["1. CREATE", "2. READ", "3. UPDATE", "4. DELETE", "5. EXIT"]
        for opcion in file:
            print(opcion)
        desi = int(input("ENTER THE DESIRED OPTION: "))
        if desi == 1:
            Create()
        elif desi == 2:
            Read()
        elif desi == 3:
            Update()
        elif desi == 4:
            Delete()
        elif desi == 5:
            print("FINISHED")
            break
        else:
            print("ENTER A VALID OPTION.")

menu()