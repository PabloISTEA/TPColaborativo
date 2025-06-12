import datetime
import time
from organizador import organizar_archivos, limpiar_pantalla



# Diccionario con horario y accion a ejecutar
acciones = {
    "21:07": lambda: organizar_archivos("D:/Descargas [D]/TP_Python/ejemplos") 
    }


def animacion_espera():
    """Muestra una animación mientras se espera que llegue la hora"""
    simbolos = ["¯", "-", "_"]
    indice = 0
    print("[*] Esperando que llegue la hora programada...\n")
    while True:
        ahora = datetime.datetime.now().strftime("%H:%M") # Muestra siempre el valor de la hora y minuto actual
        
        # Cuando "ahora" coincida con acciones, devuelve ahora
        if ahora in acciones: 
            return ahora
        
        limpiar_pantalla()
        
        print(f"[{simbolos[indice]}] Esperando que llegue la hora programada...\n")
        indice = (indice + 1) % len(simbolos)
        time.sleep(0.5)


def monitor_por_hora():
    """Ejecuta el archivador de archivos cuando llega la hora"""
    hora_ejecucion = animacion_espera() # Me guarda la hora que retorna la ahora
    print(f"\n[+] Ejecutando tarea programada para las {hora_ejecucion}...")
    acciones[hora_ejecucion]()  # Ejecuta la acción programada
    print("\n[!] Tarea completada. Finalizando script.")



# Ejecuta la funcion de automatizacion
if __name__ == "__main__":
    monitor_por_hora()