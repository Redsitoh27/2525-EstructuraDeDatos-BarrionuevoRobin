class Curso:
    def __init__(self):
        self.asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    def mostrar_asignaturas(self):
        print("Asignaturas del curso:")
        for asignatura in self.asignaturas:
            print(asignatura)

curso = Curso()
curso.mostrar_asignaturas()