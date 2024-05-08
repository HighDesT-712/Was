import os
import subprocess
import sys
from datetime import datetime

def obtener_contenido_perfil_powershell():
    # Ejecutar el comando de PowerShell para obtener el contenido del perfil actual
    proceso = subprocess.Popen(["powershell", "Get-Content $PROFILE"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    salida, error = proceso.communicate()
    if proceso.returncode != 0:
        print("Error al obtener el contenido del perfil de PowerShell:", error.decode("utf-8"))
        return None
    return salida

def crear_archivo_perfil_python(ubicacion, nuevo_termino):
    # Obtener la fecha actual en formato numérico
    fecha_hoy_numerica = datetime.now().strftime("%Y%m%d")
    
    # Obtener el contenido del perfil de PowerShell
    contenido_perfil_powershell = obtener_contenido_perfil_powershell()
    if contenido_perfil_powershell is None:
        return
    
    # Nombre del archivo
    nombre_archivo_original = f"profile_{fecha_hoy_numerica}_pcdest.txt"
    
    # Reemplazar el término en el nombre del archivo
    nombre_archivo = nombre_archivo_original.replace("pcdest", nuevo_termino)
    
    # Ruta completa del archivo
    ruta_archivo = os.path.join(ubicacion, nombre_archivo)
    
    # Escribir el contenido en el archivo
    with open(ruta_archivo, "wb") as archivo:
        archivo.write(contenido_perfil_powershell)
    
    print(f"Archivo '{nombre_archivo}' creado exitosamente en {ubicacion}.")

if __name__ == "__main__":
    # Verificar si se proporcionaron suficientes argumentos
    if len(sys.argv) < 3:
        print("Por favor, proporcione la ubicación donde desea guardar el archivo y el nuevo término para el nombre del archivo.")
        print("Ejemplo: python main.py ubicacion nuevo_termino")
        sys.exit(1)
    
    ubicacion = sys.argv[1]  # Obtener la ubicación del primer argumento
    nuevo_termino = sys.argv[2]  # Obtener el nuevo término del segundo argumento
    
    # Llamar a la función para crear el archivo con la ubicación y el nuevo término proporcionados
    crear_archivo_perfil_python(ubicacion, nuevo_termino)
