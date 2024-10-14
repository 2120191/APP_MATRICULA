# - registrar alumnos
# - generar fiches de matricula
# - mostrar la lista de todos los matriculados
# - filtrar matriculados por programa de estudio
lista_alumnos = []
while True:
    opcion = input("*elije lo que deseas hacer*\n escribe (f) si deseas registrar un alumno\n escribe (n) si deseas salir del programa\n escribe tu respuesta: ---")
    if opcion.lower() == "n":
        break
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    alumno = {
        "nombre": nombre,
        "apellido": apellido
    }
    lista_alumnos.append(alumno)
print(lista_alumnos)