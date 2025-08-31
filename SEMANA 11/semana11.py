#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traductor Básico Inglés-Español
Aplicación que permite traducir frases entre inglés y español
utilizando diccionarios como estructura de datos principal.
"""

import os
import json
import re


class TraductorBasico:
    """Clase principal del traductor básico inglés-español"""

    def __init__(self):
        """Inicializa el traductor con diccionarios base"""
        # Diccionario inglés a español
        self.dict_eng_esp = {
            "time": "tiempo",
            "person": "persona",
            "year": "año",
            "way": "camino",
            "day": "día",
            "thing": "cosa",
            "man": "hombre",
            "world": "mundo",
            "life": "vida",
            "hand": "mano",
            "part": "parte",
            "child": "niño",
            "eye": "ojo",
            "woman": "mujer",
            "place": "lugar",
            "work": "trabajo",
            "week": "semana",
            "case": "caso",
            "point": "punto",
            "government": "gobierno",
            "company": "empresa"
        }

        # Diccionario español a inglés (inverso)
        self.dict_esp_eng = {v: k for k, v in self.dict_eng_esp.items()}

        # Archivo para persistencia
        self.archivo_diccionario = "diccionario_personalizado.json"
        self.cargar_diccionario_personalizado()

    def cargar_diccionario_personalizado(self):
        """Carga palabras personalizadas desde archivo JSON"""
        try:
            if os.path.exists(self.archivo_diccionario):
                with open(self.archivo_diccionario, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    # Actualizar diccionarios con palabras personalizadas
                    self.dict_eng_esp.update(datos.get('eng_esp', {}))
                    self.dict_esp_eng.update(datos.get('esp_eng', {}))
                print("✓ Diccionario personalizado cargado exitosamente.")
        except Exception as e:
            print(f"⚠ Advertencia: No se pudo cargar el diccionario personalizado: {e}")

    def guardar_diccionario_personalizado(self):
        """Guarda las palabras personalizadas en archivo JSON"""
        try:
            # Solo guardamos las palabras que no están en el diccionario base
            dict_base_eng_esp = {
                "time": "tiempo", "person": "persona", "year": "año", "way": "camino",
                "day": "día", "thing": "cosa", "man": "hombre", "world": "mundo",
                "life": "vida", "hand": "mano", "part": "parte", "child": "niño",
                "eye": "ojo", "woman": "mujer", "place": "lugar", "work": "trabajo",
                "week": "semana", "case": "caso", "point": "punto", "government": "gobierno",
                "company": "empresa"
            }

            nuevas_eng_esp = {k: v for k, v in self.dict_eng_esp.items()
                              if k not in dict_base_eng_esp}
            nuevas_esp_eng = {k: v for k, v in self.dict_esp_eng.items()
                              if v not in dict_base_eng_esp}

            datos = {
                'eng_esp': nuevas_eng_esp,
                'esp_eng': nuevas_esp_eng
            }

            with open(self.archivo_diccionario, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"⚠ Error al guardar el diccionario: {e}")

    def detectar_idioma(self, frase):
        """Detecta si la frase está principalmente en inglés o español"""
        palabras = re.findall(r'\b\w+\b', frase.lower())
        palabras_eng = sum(1 for palabra in palabras if palabra in self.dict_eng_esp)
        palabras_esp = sum(1 for palabra in palabras if palabra in self.dict_esp_eng)

        if palabras_eng > palabras_esp:
            return "ingles"
        elif palabras_esp > palabras_eng:
            return "español"
        else:
            return "desconocido"

    def traducir_frase(self, frase):
        """Traduce una frase completa palabra por palabra"""
        idioma_origen = self.detectar_idioma(frase)

        if idioma_origen == "desconocido":
            print("⚠ No se pudo detectar el idioma de origen. Intentando traducir...")

        # Separar palabras manteniendo puntuación y espacios
        tokens = re.findall(r'\b\w+\b|\W+', frase)
        traduccion = []
        palabras_traducidas = 0
        palabras_totales = len(re.findall(r'\b\w+\b', frase))

        for token in tokens:
            if re.match(r'\b\w+\b', token):  # Es una palabra
                palabra_lower = token.lower()

                # Intentar traducir de inglés a español
                if palabra_lower in self.dict_eng_esp:
                    traduccion.append(self.dict_eng_esp[palabra_lower])
                    palabras_traducidas += 1
                # Intentar traducir de español a inglés
                elif palabra_lower in self.dict_esp_eng:
                    traduccion.append(self.dict_esp_eng[palabra_lower])
                    palabras_traducidas += 1
                else:
                    # Mantener la palabra original si no está en el diccionario
                    traduccion.append(token)
            else:
                # Mantener puntuación y espacios
                traduccion.append(token)

        resultado = ''.join(traduccion)
        porcentaje = (palabras_traducidas / palabras_totales * 100) if palabras_totales > 0 else 0

        return resultado, palabras_traducidas, palabras_totales, porcentaje

    def agregar_palabra(self):
        """Permite al usuario agregar nuevas palabras al diccionario"""
        print("\n" + "=" * 50)
        print("📝 AGREGAR NUEVA PALABRA AL DICCIONARIO")
        print("=" * 50)

        try:
            palabra_eng = input("Ingrese la palabra en inglés: ").strip().lower()
            if not palabra_eng:
                print("❌ La palabra en inglés no puede estar vacía.")
                return

            palabra_esp = input("Ingrese la traducción en español: ").strip().lower()
            if not palabra_esp:
                print("❌ La traducción en español no puede estar vacía.")
                return

            # Verificar si ya existe
            if palabra_eng in self.dict_eng_esp:
                print(f"⚠ La palabra '{palabra_eng}' ya existe en el diccionario.")
                print(f"  Traducción actual: {self.dict_eng_esp[palabra_eng]}")
                continuar = input("¿Desea sobrescribirla? (s/n): ").strip().lower()
                if continuar != 's':
                    print("❌ Operación cancelada.")
                    return

            # Agregar palabra a ambos diccionarios
            self.dict_eng_esp[palabra_eng] = palabra_esp
            self.dict_esp_eng[palabra_esp] = palabra_eng

            # Guardar en archivo
            self.guardar_diccionario_personalizado()

            print(f"✅ Palabra agregada exitosamente:")
            print(f"   {palabra_eng} → {palabra_esp}")

        except KeyboardInterrupt:
            print("\n❌ Operación cancelada por el usuario.")
        except Exception as e:
            print(f"❌ Error al agregar la palabra: {e}")

    def mostrar_estadisticas(self):
        """Muestra estadísticas del diccionario"""
        total_palabras = len(self.dict_eng_esp)
        print(f"\n📊 Estadísticas del diccionario:")
        print(f"   • Total de palabras: {total_palabras}")
        print(f"   • Direcciones de traducción: Inglés ↔ Español")

    @staticmethod
    def mostrar_menu():
        """Muestra el menú principal de opciones"""
        print("\n" + "=" * 50)
        print("🌐 TRADUCTOR BÁSICO INGLÉS-ESPAÑOL")
        print("=" * 50)
        print("1. Traducir una frase")
        print("2. Agregar palabras al diccionario")
        print("3. Ver estadísticas del diccionario")
        print("0. Salir")
        print("=" * 50)

    def ejecutar(self):
        """Ejecuta el bucle principal del programa"""
        print("🌟 ¡Bienvenido al Traductor Básico Inglés-Español!")
        print("   Este traductor funciona palabra por palabra usando diccionarios.")

        while True:
            try:
                self.mostrar_menu()
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    self.traducir_interactivo()
                elif opcion == "2":
                    self.agregar_palabra()
                elif opcion == "3":
                    self.mostrar_estadisticas()
                elif opcion == "0":
                    print("\n👋 ¡Gracias por usar el Traductor Básico!")
                    print("   Hasta luego 😊")
                    break
                else:
                    print("❌ Opción no válida. Por favor, seleccione una opción del menú.")

                # Pausa para que el usuario pueda leer el resultado
                input("\nPresione Enter para continuar...")

            except KeyboardInterrupt:
                print("\n\n👋 Programa interrumpido por el usuario. ¡Hasta luego!")
                break
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                input("Presione Enter para continuar...")

    def traducir_interactivo(self):
        """Interfaz interactiva para traducir frases"""
        print("\n" + "=" * 50)
        print("🔄 TRADUCIR FRASE")
        print("=" * 50)
        print("💡 Consejo: El traductor detecta automáticamente el idioma")
        print("   y traduce las palabras que están en el diccionario.")
        print("-" * 50)

        try:
            frase = input("Ingrese la frase a traducir: ").strip()
            if not frase:
                print("❌ No se ingresó ninguna frase.")
                return

            print(f"\n📝 Frase original:")
            print(f"   {frase}")

            # Realizar traducción
            traduccion, palabras_traducidas, palabras_totales, porcentaje = self.traducir_frase(frase)

            print(f"\n🔄 Traducción:")
            print(f"   {traduccion}")

            print(f"\n📊 Resultado:")
            print(f"   • Palabras traducidas: {palabras_traducidas}/{palabras_totales}")
            print(f"   • Porcentaje de traducción: {porcentaje:.1f}%")

            if porcentaje < 50:
                print("\n💡 Sugerencia: Para mejorar la traducción, agregue más")
                print("   palabras al diccionario usando la opción 2 del menú.")

        except KeyboardInterrupt:
            print("\n❌ Traducción cancelada por el usuario.")
        except Exception as e:
            print(f"❌ Error durante la traducción: {e}")


def main():
    """Función principal del programa"""
    try:
        traductor = TraductorBasico()
        traductor.ejecutar()
    except Exception as e:
        print(f"❌ Error al inicializar el traductor: {e}")
        print("   Por favor, verifique que tiene permisos de escritura en el directorio.")


if __name__ == "__main__":
    main()