# Importar bibliotecas necesarias
import random

# Función para generar un número aleatorio dentro de un rango específico
def generar_numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

# Función para imprimir el menú principal del juego
def mostrar_menu():
    print("¡Bienvenido al juego RPG!")
    print("1. Comenzar una nueva partida")
    print("2. Salir")

# Función para manejar la selección del usuario en el menú principal
def manejar_seleccion_menu(seleccion):
    if seleccion == "1":
        comenzar_partida()
    elif seleccion == "2":
        salir_del_juego()
    else:
        print("ES 1 O 2 NO CUALQUIERT OTRO NUMERO ALEATOREO")
        comenzar_partida()
        print("no la gakes denuevo om ><;ú-<--(")
      

# Función para comenzar una nueva partida
def comenzar_partida():
    # Aquí es donde comienza el juego real
    print("\n¡Comenzando nueva partida!\n")
    
    nombre       = input('Ingrese su nombre: ')
    
    print('\nbien '+nombre+' tienes un nombre curioso ahora tienes que escoger tus caracteristicas principales\n')
    print('tienes solo reparte hasta 10 puntos como maximo y como minimo 0\n')
    
    while True:
                
        fuerzaM       = 10
        defensaM      = 10   
        velocidadM    = 10
        inteligenciaM = 10
        sigiloM       = 10
        suerteM       = 10

        fuerza       = int(input('\n Ingrese su nivel de fuerza: '))
            
        if 1 <= (fuerza) <= fuerzaM:  # Verifica si el número está dentro del rango permitido
                pass
        else:
                continue
                print("""\n ups quisiste pasarte de vivo y ponerte mas de 10 puntos
                      eso no se hace empieza de nuevo tramposo
                      mal jugador
                      timador 
                      mala persona...
                      argagrghgahg
                      \n""")
            
        defensa      = int(input('\n Ingrese su nivel de defensa: '))
        if 1 <=   (defensa) <= defensaM:  # Verifica si el número está dentro del rango permitido
                pass
        else:
                continue
                print("""\n ups quisiste pasarte de vivo y ponerte mas de 10 puntos
                      eso no se hace empieza de nuevo tramposo
                      mal jugador
                      timador 
                      mala persona...
                      argagrghgahg
                      \n""")
            
        velocidad    = int(input('\n Ingrese su nivel de velocidad: '))
        if 1 <= (velocidad) <= velocidadM:  # Verifica si el número está dentro del rango permitido
                pass
        else:
                continue
                print("""\n ups quisiste pasarte de vivo y ponerte mas de 10 puntos
                      eso no se hace empieza de nuevo tramposo
                      mal jugador
                      timador 
                      mala persona...
                      argagrghgahg
                      \n""")
            
        inteligencia = int(input('\n Ingrese su nivel de inteligencia: '))
        if 1 <= (inteligencia) <= inteligenciaM:  # Verifica si el número está dentro del rango permitido
                pass
        else:
                continue
                print("""\n ups quisiste pasarte de vivo y ponerte mas de 10 puntos
                      eso no se hace empieza de nuevo tramposo
                      mal jugador
                      timador 
                      mala persona...
                      argagrghgahg
                      \n""")
            
        sigilo       = int(input('\n Ingrese su nivel de sigilo: '))
        if 1 <= (sigilo) <= sigiloM:  # Verifica si el número está dentro del rango permitido
                pass
        else:
                continue
                print("""\n ups quisiste pasarte de vivo y ponerte mas de 10 puntos
                      eso no se hace empieza de nuevo tramposo
                      mal jugador
                      timador 
                      mala persona...
                      argagrghgahg
                      \n""")
            
        suerte       = int(input('\n Ingrese su nivel de suerte: '))
        if 1 <= (suerte) <= suerteM:  # Verifica si el número está dentro del rango permitido
            fdviss = fuerza+defensa+velocidad+inteligencia+sigilo+suerte
            
            fuerzaS       = 7 * fuerza
            defensaS      = 8 * defensa
            velocidadS    = 4 * velocidad
            inteligenciaS = 2 * inteligencia 
            sigiloS       = 3 * sigilo
            suerteS       = 2 * suerte
        
            salud = fuerzaS+defensaS+velocidadS+inteligenciaS+sigiloS+suerteS 
        
            
            if  fdviss < 26 :
    
                print("\nsu salud depende de sus habilidades\n")

                print('''
esta es una historia que no se muy bien como terminara
en fin podras de subir de nivel tal vez pasen cosas aleatorias tal vez...
si llegan a pasar tal vez subas de nivel...
las cosas aleatorias dependen mas de ti que de mi...  
al subir de nivel aumentas una especialiad
de momento es todo lo que necesitas saber 
'''
                , "\n"
                ,"Fuerza =", fuerza , "\n" 
                ,"Defensa =", defensa , "\n"
                ,"Velocidad =", velocidad , "\n"
                ,"Inteligencia =", inteligencia , "\n"
                ,"Sigilo =", sigilo , "\n"
                ,"Suerte =", suerte , "\n"
                ,"Salud =", salud, "\n"
                ,'''Espero que sea diverto... me refiero a programarlo...''')
                Despertar()
                break

            else:
                fdviss > 26

                print('oe ' + nombre + 'no te pases de vivo  solo tienes 26 puntos y tu te pusiste',fdviss)
                continue
        else:
                continue
                print("""\n ups quisiste pasarte de vivo y ponerte mas de 26 puntos
                      eso no se hace empieza de nuevo tramposo
                      mal jugador
                      timador 
                      mala persona...
                      argagrghgahg
                      \n""")
        

def Despertar():
    #Capitulo 0
    print('''
          te despiertas abrutamente dentro de una maleta en una colina con mucha vegetacion.
          En un dia muy caluroso y soleado... con el detalle de que no tienes memoria alguna
          es como si estuvieras vivo por primera vez de la nada.
          Que haces?
          ''')
# Mas fuerte esta es la parte mas fuerte
    if salud in range(166, 163):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            lucha = input("""En cuentras a un Enemigo muy poderoso y fuerte que te puede romper el poto
                  estas dispuesto a lucar con el 
                  (1)Si (2)No""")
            if lucha is 1 :
                print("")
        elif nume == 2:
            print("""No tienes idea de porque lo haces pero lo haces y se se suben los animos""")
        elif nume == 3:
            print("""El armamento eres tu papuri estas preparado y listo para el combate""")
        elif nume == 4:
            print("""Alcanzas a ver todo un valle enorme que parece casi interminable y por el otro la Megalopolis IKO""")
                            
    elif salud in range(162, 158):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            print("...1")
        elif nume == 2:
            print("...2")
        elif nume == 3:
            print("...3")
        elif nume == 4:
            print("...4")
    # -             
    elif salud in range(157, 155):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            print("...1")
        elif nume == 2:
            print("...2")
        elif nume == 3:
            print("...3")
        elif nume == 4:
            print("...4")
                     
    elif salud in range(153, 149):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            print("...1")
        elif nume == 2:
            print("...2")
        elif nume == 3:
            print("...3")
        elif nume == 4:
            print("...4")
    # Mitad                     
    elif salud in range(146,145):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            print("...1")
        elif nume == 2:
            print("...2")
        elif nume == 3:
            print("...3")
        elif nume == 4:
            print("...4")
                     
    elif salud in range(141,133):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            print("...1")
        elif nume == 2:
            print("...2")
        elif nume == 3:
            print("...3")
        elif nume == 4:
            print("...4")
    # -                            
    elif salud in range(130,120):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            print("...1")
        elif nume == 2:
            print("...2")
        elif nume == 3:
            print("...3")
        elif nume == 4:
            print("...4")
                     
    elif salud in range(115,95):
        nume = input('''
              (1) Mantener la Guardia e inspecionas la zona  
              (2) Lanzar un alarido
              (3) Preparar armamento
              (4) Buscar la zona mas alta para hacer un plano
              ''')
        if nume == 1:
            print("...1")
        elif nume == 2:
            print("...2")
        elif nume == 3:
            print("...3")
        elif nume == 4:
            print("...4")
                     
        
    elif salud in range(94,91):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(89,79):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(88,83):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(83,75):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(74,65):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(62,42):
        
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    
    elif salud in range(37,27):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(26,25):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(24,19):
        
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
    elif salud in range(18,5):
        print('''
              (1)
              (2)
              (3)
              (4)
              ''')
                
    else:
        pass
        

         

class Personaje:
    
    def __init__(self, nombre, salud, fuerza, defensa, velocidad, inteligencia, sigilo, suerte):
        self.nombre       = nombre
        self.salud        = salud
        self.fuerza       = fuerza
        self.defensa      = defensa
        self.velocidad    = velocidad
        self.inteligencia = inteligencia
        self.sigilo       = sigilo
        self.suerte       = suerte
        

    def atacar(self, enemigo):
        # Código para realizar un ataque contra un enemigo
        pass

class Habilidad:
    def __init__(self, nombre, costo, daño):
        self.nombre = nombre
        self.costo  = costo
        self.daño   = daño

    def usar(self, personaje, enemigo):
        # Código para usar la habilidad en el personaje y el enemigo
        pass


# Función para salir del juego
def salir_del_juego():
    print("¡Gracias por jugar! ¡Hasta luego!")
    exit()

# Función principal para ejecutar el juego
def main():
    mostrar_menu()
    seleccion = input("Ingrese su selección: ")
    manejar_seleccion_menu(seleccion)

# Ejecutar el juego
if __name__ == "__main__":
    main()
