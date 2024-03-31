#Analizador de Log Mejorado.
import re

def analizar_log(archivo_log):
    # Patrones de error que se quieren buscar en el log
    patrones_error = [
        r'ERROR:',
        r'Exception:',
        r'Error de conexión:'
        # Agregar aquí más patrones de error si es necesario
    ]

    try:
        with open(archivo_log, 'r') as archivo:
            lineas = archivo.readlines()
            for num_linea, linea in enumerate(lineas, start=1):
                for patron in patrones_error:
                    if re.search(patron, linea):
                        print(f"Se encontró un error en la línea {num_linea}: {linea.strip()}")
    except FileNotFoundError:
        print(f"No se encontró el archivo de log: {archivo_log}")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo de log: {e}")

# Ruta al archivo de log que se desea analizar
archivo_log = 'C:/Users/pipe2/Documents/Inicio Python/Taller_Fundamentos_BackEnd/Trabajo_Con_Archivos'
analizar_log(archivo_log)
