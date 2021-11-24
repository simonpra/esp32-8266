# This is your main script.
from time import sleep
from machine import Pin, I2C


led = Pin(2, Pin.OUT)
signal = I2C( scl=Pin(5), sda=Pin(4) )

def read_temp() :
    ### DEFAULT address du sensor en I2C = 24
    ### l'adresse de registre où est stockée la température = 5
    ### On récupère 16bits = 2 bytes !
    ### [up] contien le UpperByte et [low] le LowerByte
    [up, low] = signal.readfrom_mem(24, 5, 2)

    ### la dataSheet pour le MCP9808 donne la correspondance des bits
    ### les 4 premiers bits de [up] définissent différents éléments de précision
    ### on récupère la valeur des 4 derniers bits du UpperByte (masque binaire)
    upVal = up & 0xF
    ### on prend directement la valeur du LowerByte
    lowVal = low

    ### calcul de la température en °C
    temp = upVal*16 + lowVal/16

    ### le 4ème bits (0x10) définit le SIGN demandant de soustraire la valeur à 256 (pour les températures négatives)
    if( up & 0x10 ) :
        temp = 256 - temp

    return temp

while True:
    led.value( not led.value() )
    print( read_temp() )
    sleep(5)
