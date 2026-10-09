import mysql.connector
conexion = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="rabinal123",
    database ="hotel"
)

def Create():
    firsname = input("ENTER YOUR NAME: ")
    lastname = input("ENTER YOUR LAST NAME: ")
    numberofguests = int(input("ENTER THE NUMBER OF PEOPLE: "))
    roomType = input("ENTER YOUR ROOM TYPE (Standard, Deluxe, Suite): ")

    if roomType == "Standard" or roomType == "Deluxe" or roomType == "Suite":
        cursor = conexion.cursor()

        query = "INSERT INTO hotel(firstName,lastName,numberOfGuests,roomType) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (firsname, lastname, numberofguests, roomType))
        conexion.commit()
        print("REGISTRATION COMPLETE")
    else:
        print("ROOM TYPE.")


def Read():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM hotel")
    for file in cursor.fetchall():
        print(file)

def update():
    id_actualizar = int(input("INGRESE SU ID: "))
    firsname = input("ENTER YOUR NAME: ")
    lastname= input("ENTER YOUR LAST NAME: ")
    numberofpeople = int(input("ENTER THE NUMBER OF PEOPLE: "))
    roomType = input("ENTER YOUR ROOM TYPE (Standard, Deluxe, Suite): ")

    if roomType == "Standard" or roomType == "Deluxe" or roomType == "Suite":
        cursor = conexion.cursor()

        query = "UPDATE reservas SET (firstName, lastName, numberOfGuests, roomType) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (firsname, lastname, numberofpeople, roomType, id_actualizar))
        conexion.commit()
        print("UPDATE COMPLETE!!!")
    else:
        print("INVALID ROOM TYPE :( )")


def delete():
    id = int(input("ENTER THE ID: "))

    cursor = conexion.cursor()
    query = "DELETE FROM hotel WHERE id=%s"
    cursor.execute(query, (id,))
    conexion.commit()

    print("proper disposal.")


def menu():
    while True:
        fila = ["1. CREATE", "2. READ", "3. UPDATE", "4. DELETE", "5. EXIT"]
        for opcion in fila:
            print(opcion)
        desi = int(input("ENTER THE DESIRED OPTION: "))
        if desi == 1:
            Create()
        elif desi == 2:
            Read()
        elif desi == 3:
            update()
        elif desi == 4:
            delete()
        elif desi == 5:
            print("FINALIZED")
            break
        else:
            print("ENTER A VALID OPTION")


menu()