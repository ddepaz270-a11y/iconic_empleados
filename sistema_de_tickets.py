import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rabinal123",
    database="sistema_de_tickets"
)

def Create():
    cursor = conexion.cursor()
    firstName = input("ENTER YOUR NAME: ")
    lastName = input("ENTER YOUR LAST NAME: ")
    numberOfPeople = int(input("ENTER THE NUMBER OF PEOPLE: "))
    ticketType = input("ENTER YOUR TICKET TYPE (Normal, VIP, Diamante): ")
    
    query = "INSERT INTO sistema_de_tickets (firstName, lastName, numberOfPeople, ticketType) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (firstName, lastName, numberOfPeople, ticketType))
    conexion.commit()
    print("REGISTRATION COMPLETE")

def Read():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sistema_de_tickets")
    for row in cursor.fetchall():
        print(row)

def Update():
    cursor = conexion.cursor()
    ticket_id = int(input("ENTER THE ID OF THE TICKET TO UPDATE: "))
    firstName = input("ENTER NEW NAME: ")
    lastName = input("ENTER NEW LAST NAME: ")
    numberOfPeople = int(input("ENTER NEW NUMBER OF PEOPLE: "))
    ticketType = input("ENTER NEW TICKET TYPE (Normal, VIP, Diamante): ")
    
    query = "UPDATE sistema_de_tickets SET  (firstName, lastName, numberOfPeople, ticketType) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (firstName, lastName, numberOfPeople, ticketType, ticket_id))
    conexion.commit()
    print("UPDATE SUCCESSFUL")

def Delete():
    cursor = conexion.cursor()
    ticket_id = int(input("ENTER THE ID OF THE TICKET TO DELETE: "))
    
    query = "DELETE FROM sistema_de_tickets WHERE id = %s"
    cursor.execute(query, (ticket_id,))
    conexion.commit()
    print("DELETED SUCCESSFULLY")

def menu():
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    opcion = int(input("ENTER YOUR CHOICE: "))
    
    if opcion == 1:
        Create()
    elif opcion == 2:
        Read()
    elif opcion == 3:
        Update()
    elif opcion == 4:
        Delete()
    else:
        print("ENTER A VALID OPTION")

menu()