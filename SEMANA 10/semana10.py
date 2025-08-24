import random

# Función para mostrar conjuntos en varias líneas
def mostrar_por_lineas(conjunto, por_linea=10):
    lista = sorted(list(conjunto))
    for i in range(0, len(lista), por_linea):
        print(", ".join(lista[i:i+por_linea]))

# 1. Crear conjunto ficticio de 500 ciudadanos
ciudadanos = {f"Ciudadano {i}" for i in range(1, 501)}

# 2. Crear conjunto ficticio de 75 ciudadanos vacunados con Pfizer
pfizer = set()
while len(pfizer) < 75:
    pfizer.add(f"Ciudadano {random.randint(1, 500)}")

# 3. Crear conjunto ficticio de 75 ciudadanos vacunados con AstraZeneca
astrazeneca = set()
while len(astrazeneca) < 75:
    astraZeneca_candidate = f"Ciudadano {random.randint(1, 500)}"
    astrazeneca.add(astraZeneca_candidate)

# 4. Ciudadanos que han recibido ambas dosis (intersección)
ambas_dosis = pfizer & astrazeneca

# 5. Ciudadanos que solo han recibido Pfizer
solo_pfizer = pfizer - astrazeneca

# 6. Ciudadanos que solo han recibido AstraZeneca
solo_astrazeneca = astrazeneca - pfizer

# 7. Ciudadanos que no se han vacunado
no_vacunados = ciudadanos - pfizer - astrazeneca

# ---- Mostrar resultados en pantalla de forma legible ----
print("\nCiudadanos que no se han vacunado:")
mostrar_por_lineas(no_vacunados)

print("\nCiudadanos que han recibido ambas dosis:")
mostrar_por_lineas(ambas_dosis)

print("\nCiudadanos que solo han recibido Pfizer:")
mostrar_por_lineas(solo_pfizer)

print("\nCiudadanos que solo han recibido AstraZeneca:")
mostrar_por_lineas(solo_astrazeneca)

# ---- Guardar resultados en archivos de texto ----
def guardar_archivo(nombre_archivo, conjunto):
    with open(nombre_archivo, "w") as f:
        for c in sorted(conjunto):
            f.write(c + "\n")

guardar_archivo("no_vacunados.txt", no_vacunados)
guardar_archivo("ambas_dosis.txt", ambas_dosis)
guardar_archivo("solo_pfizer.txt", solo_pfizer)
guardar_archivo("solo_astrazeneca.txt", solo_astrazeneca)

print("\nArchivos generados: no_vacunados.txt, ambas_dosis.txt, solo_pfizer.txt, solo_astrazeneca.txt")
