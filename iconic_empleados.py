import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rabinal123",
    database="iconic_empleados"
)


def Crear():
    nombre = input("INGRESE EL NOMBRE DEL EMPLEADO/A: ")
    puesto = input("INGRESE EL PUESTO EN EL QUE ESTA: ")
    fecha = input("INGRESE LA FECHA ACTUAL (AÑO-MES-DIA): ")
    entrada = input("INGRESE LA HORA DE ENTRADA DEL EMPLEADO (HORA-MINUTO-SEGUNDO): ")
    salida = input("INGRESE LA HORA DE SALIDA DEL EMPLEADO (HORA, MINUTO, SEGUNDO): ")
    estado = input("INGRESE EL ESTADO EN EL QUE SE ENCUENTRA (Presente, Tarde, Ausente): ")
    observaciones = input("INGRESE LA OBSERVACION: ")

    if estado not in ["Presente", "Tarde", "Ausente"]:
        print("ESTADO NO VALIDO.")

    if estado == "Ausente":
        entrada = None
        salida = None
    cursor = conexion.cursor()

    consulta = "INSERT INTO asistencia (nombre, puesto, fecha, hora_entrada, hora_salida,estado, observaciones) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    datos = (nombre, puesto, fecha, entrada, salida, estado, observaciones)
    cursor.execute(consulta, datos)
    conexion.commit()
    print("REGISTRO COMPLETADO.")
    cursor.close()


def Leer():
    cursor = conexion.cursor()
    consulta = "SELECT * FROM asistencia"
    cursor.execute(consulta)
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)


def Actualizar():
    id_empleado = int(input("INGRESE EL ID DEL REGISTRO: "))
    estado = input("INGRESE EL NUEVO ESTADO (Presente, Tarde, Ausente): ")
    if estado not in ["Presente", "Tarde", "Ausente"]:
        print("ESTADO NO VALIDO.")

    cursor = conexion.cursor()
    consulta = "UPDATE asistencia SET estado=%s WHERE id=%s"
    cursor.execute(consulta, (estado, id_empleado))
    conexion.commit()
    print("REGISTRO ACTUALIZADO.")


def Eliminar():
    id_empleado = int(input("INGRESE EL ID DEL REGISTRO: "))
    cursor = conexion.cursor()
    consulta = "DELETE FROM asistencia WHERE id=%s"

    cursor.execute(consulta, (id_empleado,))
    conexion.commit()
    print("REGISTRO ELIMINADO.")

def Menu():
    while True:
        opciones = ["1. CREAR", "2. LEER", "3. ACTUALIZAR", "4. ELIMINAR", "5. SALIR"]
        for opcion in opciones:
            print(opcion)
        decision = int(input("INGRESE LA OPCION DESEADA: "))

        if decision == 1:
            Crear()
        elif decision == 2:
            Leer()
        elif decision == 3:
            Actualizar()
        elif decision == 4:
            Eliminar()
        elif decision == 5:
            print("PROGRAMA FINALIZADO.")
        else:
            print("INGRESE UNA OPCION VALIDA.")
Menu()