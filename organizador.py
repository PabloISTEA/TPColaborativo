import os # Permite interactuar con rutas, archivos, carpetas
import shutil # Permite mover archivos, copiar, eliminar, etc.


def organizar_archivos(ruta):
    """Organiza archivos segun sus extensiones recorriendo una carpeta especifica"""
    # Diccionario tipos que relaciona carpetas con extensiones
    tipos = {
        "Excel": [".xls", ".xlsx"],
        "Word": [".doc", ".docx"],
        "PDF": [".pdf"],
        "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mov", ".avi", ".mp4", ".mkv"],
        "iReport": [".jrxml"],
        "SQL": [".sql"],
        "Python": [".py"],
        "Notas": [".txt"]
    }

    # Crea carpeta "Otros" para extensiones que no fueron clasificadas en el diccionario
    otros_dir = os.path.join(ruta, "Otros")
    os.makedirs(otros_dir,exist_ok = True)

    # Recorre todos los elementos en la carpeta indicada
    for archivo in os.listdir(ruta):
        origen = os.path.join(ruta, archivo)

        # Solo busca archivos, no carpetas
        if os.path.isfile(origen):
            extension = os.path.splitext(archivo)[1].lower()
            movido = False

            # Busca la categoria de la extension y lo mueve a la carpeta correspondiente
            for carpeta, extensiones in tipos.items():
                if extension in extensiones:
                    destino_dir = os.path.join(ruta, carpeta)
                    os.makedirs(destino_dir, exist_ok = True)
                    shutil.move(origen, os.path.join(destino_dir, archivo))
                    print(f"[+] Movido: {archivo} --> {carpeta}/")
                    movido = True
                    break
            
            # Si no se encontro la categoria lo mueve a "Otros"
            if not movido:
                shutil.move(origen, os.path.join(otros_dir, archivo))
                print(f"[-] Movido: {archivo} --> Otros/")



# Limpia la pantalla de la terminal
def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')