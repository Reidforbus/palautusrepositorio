# Tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus


logger("aloitetaan")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")
print(f"Lukujen {x} ja {y} summa on {erotus(x, y)}")

logger("lopetetaan")
print("heihei!")
