from TEORIA_UT7_PRACTICA_juegoderol.Definicion_clases import guerrero, arquero, mago, ladron

mago1=mago("Gandalf", 100, 20, 10)
guerrero1=guerrero("Aragorn", 120, 25, 15)
arquero1=arquero("Legolas", 90, 15, 5)
ladrón1=ladron("Frodo", 80, 10, 5)
jugador=input("Elige tu personaje (Gandalf, Aragorn, Legolas, Frodo): ")

#Al principio de cada turno, podremos atacar a uno de los demáss personajes, y luego cada uno de los personajes atacará a otro personaje de forma automática. El juego continuará hasta que uno de los personajes quede sin vida.
#En cada turno, el jugador podrá elegir a quién atacar, y luego cada personaje atacará a otro personaje de forma automática. El juego continuará hasta que uno de los personajes quede sin vida.
Turno = 1

while mago1.vida > 0 and guerrero1.vida > 0 and arquero1.vida > 0 and ladrón1.vida > 0:
    print(f"Turno {Turno}:")
    objetivo = input("¿A quién deseas atacar? (Gandalf, Aragorn, Legolas, Frodo): ")
    if objetivo == "Gandalf":
        jugador.atacar(mago1)
    elif objetivo == "Aragorn":
        jugador.atacar(guerrero1)
    elif objetivo == "Legolas":
        jugador.atacar(arquero1)
    elif objetivo == "Frodo":
        jugador.atacar(ladrón1)
    else:
        print("Objetivo inválido.")
        continue
    mago1.atacar(guerrero1)
    guerrero1.atacar(arquero1)
    arquero1.atacar(ladrón1)
    ladrón1.atacar(mago1)
    print(f"Turno {Turno}:")
    print(f"{mago1.nombre} tiene {mago1.vida} puntos de vida.")
    print(f"{guerrero1.nombre} tiene {guerrero1.vida} puntos de vida.")
    print(f"{arquero1.nombre} tiene {arquero1.vida} puntos de vida.")
    print(f"{ladrón1.nombre} tiene {ladrón1.vida} puntos de vida.")
    Turno += 1
    
if mago1.vida <= 0:
    print(f"{mago1.nombre} ha sido derrotado.")
if guerrero1.vida <= 0:
    print(f"{guerrero1.nombre} ha sido derrotado.")
if arquero1.vida <= 0:
    print(f"{arquero1.nombre} ha sido derrotado.")
if ladrón1.vida <= 0:
    print(f"{ladrón1.nombre} ha sido derrotado.")

