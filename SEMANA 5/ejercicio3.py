class NotasCurso:
    def __init__(self):
        self.asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        self.notas = {}

    def ingresar_notas(self):
        for asignatura in self.asignaturas:
            nota = float(input(f"Ingresa la nota de {asignatura}: "))
            self.notas[asignatura] = nota

    def mostrar_resultados(self):
        for asignatura, nota in self.notas.items():
            print(f"En {asignatura} has sacado {nota}")

curso = NotasCurso()
curso.ingresar_notas()
curso.mostrar_resultados()
