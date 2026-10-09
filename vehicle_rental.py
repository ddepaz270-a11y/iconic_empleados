import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rabinal123",
    database="parqueo"
)


def Create():
    ownerName = input("ENTER your NAME: ")
    licensePlate = input("ENTER LICENSE PLATE: ")
    vehicleType = input("ENTER VEHICLE TYPE (Car, Motorcycle, Truck): ")
    entryTime = input("ENTER ENTRY TIME: ")

    if vehicleType == "Car":
        vehicleType = "Car"
    elif vehicleType == "Motorcycle":
        vehicleType = "Motorcycle"
    elif vehicleType == "Truck":
        vehicleType = "Truck"
    else:
        print("INVALID VEHICLE TYPE.")
        return

    exitTime = "Pending"
    status = "Inside"

    cursor = conexion.cursor()
    query = "INSERT INTO vehiculos (ownerName, licensePlate, vehicleType, entryTime, exitTime, status) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, ( ownerName, licensePlate, vehicleType, entryTime, exitTime, status))
    conexion.commit()
    print("REGISTRATION COMPLETE.")


def Read():
    cursor = conexion.cursor()
    query = "SELECT * FROM vehiculos"
    cursor.execute(query)
    for vehiculo in cursor.fetchall():
        print(vehiculo)


def Update():
    id = int(input("ENTER ID: "))
    exitTime = input("ENTER EXIT TIME: ")
    status = "Exited"
    cursor = conexion.cursor()
    query = "UPDATE vehiculos SET exitTime=%s, status=%s WHERE id=%s"
    cursor.execute(query, (exitTime, status, id))
    conexion.commit()
    print("VEHICLE EXIT UPDATED.")


def Delete():
    id = int(input("ENTER ID: "))
    cursor = conexion.cursor()
    query = "DELETE FROM vehiculos WHERE id=%s"
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