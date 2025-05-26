from collections import deque
from datetime import datetime

# Cola de notificaciones
cola_notificaciones = deque([
    {'hora': '10:15', 'app': 'Facebook', 'mensaje': 'Nuevo comentario en tu foto'},
    {'hora': '11:00', 'app': 'Twitter', 'mensaje': 'Aprendé Python con nosotros'},
    {'hora': '12:10', 'app': 'Instagram', 'mensaje': 'Tenés una nueva historia para ver'},
    {'hora': '13:45', 'app': 'Twitter', 'mensaje': 'Python es genial #programación'},
    {'hora': '14:30', 'app': 'WhatsApp', 'mensaje': 'Nuevo mensaje de tu grupo de estudio'},
    {'hora': '16:00', 'app': 'Facebook', 'mensaje': 'Alguien reaccionó a tu publicación'},
    {'hora': '15:30', 'app': 'Twitter', 'mensaje': '¿Querés aprender más sobre Python?'},
])

# a. eliminar notificaciones de Facebook
def eliminar_notificaciones_facebook(cola):
    nueva_cola = deque()
    while cola:
        noti = cola.popleft()
        if noti['app'].lower() != 'facebook':
            nueva_cola.append(noti)
    return nueva_cola

#b. Mostrar notificaciones de Twitter con "Python", sin perder datos
def mostrar_tweets_python(cola):
    print("Tweets con 'Python':")
    for noti in cola: 
        if noti['app'].lower() == 'twitter' and 'python' in noti['mensaje'].lower():
            print(f"- {noti['hora']} | {noti['mensaje']}")


# c. Usar una pila para notificaciones entre 11:43 y 15:57
def notificaciones_en_rango(cola):
    hora_inicio = datetime.strptime("11:43", "%H:%M") 
    hora_fin = datetime.strptime("15:57", "%H:%M")

    pila = []
    for noti in cola:
        hora_noti = datetime.strptime(noti['hora'], "%H:%M")
        if hora_inicio <= hora_noti <= hora_fin:
            pila.append(noti)
        

    return pila, len(pila)

cola_notificaciones = eliminar_notificaciones_facebook(cola_notificaciones)
mostrar_tweets_python(cola_notificaciones)
pila, cantidad = notificaciones_en_rango(cola_notificaciones)
print(f"\nCantidad de notificaciones entre 11:43 y 15:57: {cantidad}")
