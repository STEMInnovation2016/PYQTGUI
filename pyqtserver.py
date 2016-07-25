import pygame, sys
from pygame.locals import *

import os

import socket

import subprocess

import webbrowser

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import time
from PIL import Image
import numpy
import urllib
from lxml import html
import shlex

from PIL import Image, ImageOps, ImageEnhance, ImageFont, ImageDraw

TCP_IP = '169.254.31.4' #other computer's IP
TCP_PORT = 5005
BUFFER_SIZE = 1
A = 0



class QWidget(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)

        #layout = QVBoxLayout()
        layout = QGridLayout()
        self.setLayout(layout)

        #self.l1 = QLabel("")
        #self.l1.setAlignment(Qt.AlignCenter)
        #layout.addWidget(self.l1)

        self.img = QPushButton()


        layout.addWidget(self.img)
        self.img.setText("DisplayIMG")
        self.img.clicked.connect(self.img_clicked)

        self.l1 = QPushButton()
        layout.addWidget(self.l1)
        self.l1.setText("LED On")
        self.l1.clicked.connect(self.l1_clicked)

        self.l2 = QPushButton()
        layout.addWidget(self.l2)
        self.l2.setText("LEF Off")
        self.l2.clicked.connect(self.l2_clicked)

        self.gstreamer = QPushButton()
        layout.addWidget(self.gstreamer)
        self.gstreamer.setText("Stream Video")
        self.gstreamer.clicked.connect(self.gstreamer_clicked)


        self.imagelabel = QLabel()
        layout.addWidget(self.imagelabel)
        self.imagelabel.setMouseTracking(True)


        self.tempLabel = QLabel()
        layout.addWidget(self.tempLabel)
        self.tempLabel.setText("TEMPERATURE")

        self.rawLabel = QLabel()
        layout.addWidget(self.rawLabel)
        self.rawLabel.setText("RAW")


    def l1_clicked(self):
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((TCP_IP, TCP_PORT))
       s.send("ledon")
       #data = s.recv(BUFFER_SIZE)
       s.close()

    def l2_clicked(self):
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((TCP_IP, TCP_PORT))
       s.send("ledoff")
       #data = s.recv(BUFFER_SIZE)
       s.close()

    def gstreamer_clicked(self):
        subprocess.Popen(["C:\Users\shoug\stream.bat"]) #put the stream file in the original directory


    def img_clicked(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send("frame")
        #data = s.recv(BUFFER_SIZE)
        s.close()
        #subprocess.Popen(["C:\Users\shoug\flir.bat"])
        print("TAKENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")

        time.sleep(2)


        text = 1
        tcolor = (255,255,0)
        text_pos = (0,0)
        framecounter = 0


        s = urllib.urlopen("http://169.254.31.4/A.dat").read()

        raw = s.split()

        CameraC = float(raw[0])
        CameraF = CameraC * 1.8 + 32



        #celsius = [[0 for y in range(60)] for x in range(80)]
        fheit = numpy.ndarray(shape = (60,80), dtype = float)
        for y in range(60):
            for x in range(80):
                #fheit[y][x] = 0.032622222 * float(raw[1+ 80 * y + x]) - 539.388883 + CameraK + 273.15
                fheit[y][x] = 0.05872 * float(raw[1+ 80 * y + x]) - 479.22999 + CameraF

        minT = float(130)
        maxT = float(300)



        colors = numpy.ndarray(shape = (60,80,3), dtype = 'uint8')
        for y in range(60):
            for x in range(80):
                a = (fheit[y][x] - minT)/(maxT - minT)
                if a < 0:
                    a = 0
                if a > 1:
                    a = 1
                colors[y][x][0] = 170 - a * 170
                colors[y][x][1] = 255
                colors[y][x][2] = 128



        framecounter = framecounter + 1
        #print "frame: " + str(framecounter)

        image = Image.fromarray(colors, mode = 'HSV').convert('RGB')


                        #image = image.rotate(90).resize((80*5, 60*5), Image.ANTIALIAS)
        image = image.rotate(0).resize((80*5, 60*5))

                    #draw = ImageDraw.Draw(image)
                    #draw.text(text_pos, str(framecounter), fill=tcolor, font=font)

        TmpFileName = "latest.jpg"


        quality_val = 80
        image.save(TmpFileName, quality=quality_val)

        with open(TmpFileName, 'rb') as f:
            data = f.read()
            f.close()

        def getPos(event):
            x = event.pos().x()
            y = event.pos().y()
            realx = int(x/5)
            realy = int(y/5)
            fheit_string = str(fheit[realy][realx])
            raw_string = str(raw[1+ 80 * realy + realx])
            self.tempLabel.setText(fheit_string)
            self.rawLabel.setText(raw_string)


        pixmap = QPixmap(os.getcwd() + '/latest.jpg')
        self.imagelabel.setPixmap(pixmap)
        self.imagelabel.mousePressEvent =  getPos

def window():

   app = QApplication(sys.argv)
   win = QWidget()

   win.setGeometry(20,40,410,5)
   win.setWindowTitle("PyQt")
   win.show()

   ###########################################################################
   max_speed = 30

   pygame.init()

   #windowSurface = pygame.display.set_mode((800, 600), 0, 32)

   ### Tells the number of joysticks/error detection
   joystick_count = pygame.joystick.get_count()
   print ("There is ", joystick_count, "joystick/s")
   if joystick_count == 0:
       print ("Error, I did not find any joysticks")
   else:
       my_joystick = pygame.joystick.Joystick(0)
       my_joystick.init()

   #crosshairs = pygame.image.load("crosshairs.png")
   #background = pygame.image.load("shooter/image_library/background.jpg")

   ##x = 300
   ##y = 300
   ##### Creates rectangle
   ##Rectangle = pygame.Rect( x, y, 100, 100)
   ##Back = pygame.Rect(0, 0, 800, 600)
   x_coord_inverted = 0
   y_coord = 0
   right_speed = 0
   left_speed = 0
   message = ""
   x_event_value = 0.0
   y_event_value = 0.0


   while True:
       global message
       global max_speed
       global x_coord_inverted
       global y_coord
       global right_speed
       global left_speed

       for event in pygame.event.get():
           print event
           #print event.type
           event_type = event.type
           #print str(event.value)

           if event.type == QUIT:
               pygame.quit()
               sys.exit()

           if event_type == 7:
               event_value = event.value
               event_axis = event.axis
               #print event_value
               if event_axis == 1 or event_axis == 0:

                   #print "Left Joystick"
                   if event_axis == 1:
                       y_coord = int(round(event_value*-100))
                       #print "y_coord: "
                       #print y_coord
                       #print abs(y_speed)

                   elif event_axis == 0:
                       x_coord_inverted = int(round(event_value*-100))


                   V = ((100 - abs(x_coord_inverted))*(y_coord/100)) + y_coord
                   W = ((100 - abs(y_coord))*(x_coord_inverted/100)) + x_coord_inverted
                   R = (((V + W)/2)*max_speed)/100
                   L = (((V - W)/2)*max_speed)/100
                   print "R: "
                   print R
                   right_speed = R
                   left_speed = L


                   ## Right now this is making it so back and to the left on the joystick makes the rover go back and to the right
                   ## to change this we would have to split off back half of the joystick and swap the directions
                   ## but this would make an unnatural jump in the steering
                   #print "R: " + str(right_speed)
                   #print "L: " + str(left_speed)


                   message = "R" + str(right_speed) + "L" + str(left_speed)

               ## Pan and tilt on Right Joystick
               elif event_axis == 3 or event_axis == 4:
                   global x_event_value
                   global y_event_value
                   #print "Right Joystick"

                   if event_axis == 3:
                       y_event_value = event.value

                   elif event_axis == 4:
                       x_event_value = event.value

                   if y_event_value < -0.9:
                       message = "up"
                   elif y_event_value > 0.9:
                       message = "down"
                   elif x_event_value < -0.9:
                       message = "left"
                   elif x_event_value > 0.9:
                       message = "right"
                   else:
                       message = "stop"
           ## Control pad to go straight forward, straight back, and rotate left and right
           elif event_type == 9:
               event_value = event.value

               if event_value == (0, 1):      #Forward
                   right_speed = max_speed
                   left_speed = max_speed
                   print "Constant Forward"

               elif event_value == (0, -1):   #Reverse
                   right_speed = -max_speed
                   left_speed = -max_speed
                   print "Constant Reverse"

               elif event_value == (1, 0):    #Rotate Right
                   right_speed = -max_speed
                   left_speed = max_speed
                   print "Rotate right"

               elif event_value == (-1,0):    #Rotate Left
                   right_speed = max_speed
                   left_speed = -max_speed
                   print "Rotate left"


               else:
                   while right_speed != 0 or left_speed != 0:
                       if right_speed != 0:
                           if right_speed > 0:
                               right_speed -= 1
                           else:
                               right_speed += 1
                       if left_speed != 0:
                           if left_speed > 0:
                               left_speed -= 1
                           else:
                               left_speed +=1
                       time.sleep(0.02)

                       temp_message = "R" + str(right_speed) + "L" + str(left_speed)
                       print temp_message
   ##                   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ##                    s.connect((TCP_IP, TCP_PORT))
   ##                    s.send(temp_message)
   ##                    #data = s.recv(BUFFER_SIZE)
   ##                    s.close()

               message = "R" + str(right_speed) + "L" + str(left_speed)


           ## Buttons
           elif event_type == 10:
               event_button = event.button

               ## Emergency stop button A
               if event_button == 0:
                   message = "R0L0"

               ## Left and Right Bumpers to change max_speed
               elif event_button == 4:
                   max_speed -= 5
               elif event_button == 5:
                   max_speed += 5

               elif event_button == 9:
                   message = "fwd"

               elif event_button == 1:
                   message = "ledon"

               elif event_button == 2:
                   message = "ledoff"



           print message
           #print "max_speed: "
           #print max_speed
           #if message != "":
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect((TCP_IP, TCP_PORT))
           s.send(message)
           #data = s.recv(BUFFER_SIZE)
           s.close()
       message = "filler"
       #print message
       time.sleep(.1)
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((TCP_IP, TCP_PORT))
       s.send(message)
       ##data = s.recv(BUFFER_SIZE)
       s.close()


   ########################################################################################
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()
