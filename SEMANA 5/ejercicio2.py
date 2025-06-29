class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    def estudiar(self):
        for asignatura in self.asignaturas:
            print(f"{self.nombre} estudia {asignatura}")

alumno = Estudiante("Carlos")
alumno.estudiar()
