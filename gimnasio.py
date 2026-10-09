import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rabinal123",
    database="gimnasio"
)


def Create():
    clientName = input("ENTER CLIENT NAME: ")
    age = int(input("ENTER AGE: "))
    membershipType = input("ENTER MEMBERSHIP TYPE (Basic, Premium, VIP): ")
    months = int(input("ENTER MONTHS: "))

    if membershipType == "Basic":
        finalPrice = 100 * months
    elif membershipType == "Premium":
        finalPrice = 175 * months
    elif membershipType == "VIP":
        finalPrice = 250 * months
    else:
        print("INVALID MEMBERSHIP TYPE.")
        return

    if months >= 6:
        status = "ActivePlus"
    else:
        status = "Active"

    cursor = conexion.cursor()
    query = "INSERT INTO clientes (clientName, age, membershipType, months, finalPrice, status) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (clientName, age, membershipType, months, finalPrice, status)
    cursor.execute(query, valores)
    conexion.commit()
    print("REGISTRATION COMPLETE.")
    print("FINAL PRICE: Q", finalPrice)
    print("STATUS:", status)


def Read():
    cursor = conexion.cursor()
    query = "SELECT * FROM clientes"
    cursor.execute(query)
    for cliente in cursor.fetchall():
        print(cliente)


def Update():
    id = int(input("ENTER ID: "))
    clientName = input("ENTER NEW CLIENT NAME: ")
    age = int(input("ENTER NEW AGE: "))
    membershipType = input("ENTER NEW MEMBERSHIP TYPE (Basic, Premium, VIP): ")
    months = int(input("ENTER NEW MONTHS: "))

    if membershipType == "Basic":
        finalPrice = 100 * months
    elif membershipType == "Premium":
        finalPrice = 175 * months
    elif membershipType == "VIP":
        finalPrice = 250 * months
    else:
        print("INVALID MEMBERSHIP TYPE.")
        return
    if months >= 6:
        status = "ActivePlus"
    else:
        status = "Active"

    cursor = conexion.cursor()
    query = "UPDATE clientes SET clientName = %s, age = %s, membershipType = %s, months = %s, finalPrice = %s, status = %s WHERE id = %s"
    query = "UPDATE clientes SET clientName = %s, age = %s, membershipType = %s, months = %s, finalPrice = %s, status = %s WHERE id = %s"
    valores = (clientName, age, membershipType, months, finalPrice, status, id)
    cursor.execute(query, valores)
    conexion.commit()
    print("UPDATE COMPLETE.")


def Delete():
    id = int(input("ENTER ID: "))
    cursor = conexion.cursor()
    query = "DELETE FROM clientes WHERE id=%s"
    cursor.execute(query, (id,))
    conexion.commit()
    print("DELETE COMPLETE.")


def menu():
    while True:
        print("1. CREATE")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")

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
conexion.close()