class Nodo:
    def __init__(self, pregunta, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no


def jugar_adivinanzas(nodo):
    respuesta = input(nodo.pregunta).lower()
    if respuesta == 'si':
        if nodo.si:
            jugar_adivinanzas(nodo.si)
        else:
            print("¡He adivinado!")
    elif respuesta == 'no':
        if nodo.no:
            jugar_adivinanzas(nodo.no)
        else:
            objeto = input("No sé qué es. ¿Qué estabas pensando? ")
            tipo = input("¿Es un animal, un objeto o un personaje? ").lower()
            pregunta_nueva = input("Ingresa una pregunta que distinga {} de {}: ".format(objeto, nodo.pregunta))
            respuesta_nueva = input("¿Cuál es la respuesta para {}? (si/no) ".format(objeto))
            nodo.no = Nodo(nodo.pregunta)
            nodo.si = Nodo(pregunta_nueva)
            if respuesta_nueva.lower() == 'si':
                nodo.si.si = Nodo(objeto)
            else:
                nodo.si.no = Nodo(objeto)
            nodo.si.si.tipo = tipo


arbol = Nodo("¿Es un animal, un objeto o un personaje?")
arbol.si = Nodo("¿Es un animal?")
arbol.no = Nodo("¿Es un objeto o un personaje?")
arbol.si.si = Nodo("¿Tiene cuatro patas?")
arbol.si.no = Nodo("¿Tiene ruedas?")
arbol.no.si = Nodo("¿Es algo que se pueda comer?")
arbol.no.no = Nodo("¿Es algo que se pueda llevar puesto?")

# Jugamos
jugar_adivinanzas(arbol)

# Preguntamos si quiere jugar de nuevo
jugar_nuevamente = input("¿Quieres jugar de nuevo? (si/no) ").lower()
while jugar_nuevamente == 'si':
    jugar_adivinanzas(arbol)
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (si/no) ").lower()
