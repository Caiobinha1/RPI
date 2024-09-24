import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import AngularServo
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import subprocess
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#config oled

RST = None
DC=23
SPI_PORT =0
SPI_device=0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width=disp.width
height=disp.height
image=Image.new('1',(width,height))
draw=ImageDraw.Draw(image)
draw.rectangle((0,0,width,height),outline=0,fill=0)
padding=-2
top = padding
bottom=height-padding
x=0
font = ImageFont.load_default()

#

reader = SimpleMFRC522()
servo = AngularServo(18, min_angle=-90, max_angle=90)
try:
        servo.angle=-90
        id, texto = reader.read()
        if (id == 357281625389 or id == 183838561683):
                draw.text((x,top), "ID: " + str(id), font=font, fill=255)
                draw.text((x,top+8),"Nome: " +str(texto),font=font,fill=255)
                draw.text((x,top+16), "Bem Vindo!!", font=font, fill=255)
                disp.image(image)
                disp.display()
                servo.angle=90
                sleep(3)
                servo.angle=-90
                sleep(3)
        else:
                draw.text((x,top), "Acesso negado!", font=font, fill=255)
                disp.image(image)
                disp.display()
        print(id)
        print(texto)
finally:
        GPIO.cleanup()