# Tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo
from osamaara import osamaara


logger("aloitetaan laskuohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}")
print(f"{x} * {y} = {tulo(x, y)}")
print(f"{x} / {y} = {osamaara(x, y)}")

logger("lopetetaan")
print("heihei!")
