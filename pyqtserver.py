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
from PIL import ImageGrab
import numpy
import urllib
from lxml import html
import shlex
import datetime
from PIL import Image, ImageOps, ImageEnhance, ImageFont, ImageDraw

TCP_IP = '169.254.31.4' #other computer's IP
TCP_PORT = 5005
BUFFER_SIZE = 1
A = 0
VIDEO = 0

minT = float(50)
maxT = float(250)

class CustomMessageBox(QMessageBox):

    def __init__(self, *__args):
        QMessageBox.__init__(self)
        self.timeout = 0
        self.autoclose = False
        self.currentTime = 0

    def showEvent(self, QShowEvent):
        self.currentTime = 0
        if self.autoclose:
            self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        self.currentTime += 1
        if self.currentTime >= self.timeout:
            self.done(0)

    @staticmethod
    def showWithTimeout(timeoutSeconds, message, title, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        w = CustomMessageBox()
        w.autoclose = True
        w.timeout = timeoutSeconds
        w.setText(message)
        w.setWindowTitle(title)
        w.setIcon(icon)
        w.setStandardButtons(buttons)
        w.exec_()


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


        '''layout.addWidget(self.img)
        self.img.setText("DisplayIMG")
        self.img.clicked.connect(self.img_clicked)'''

        '''self.l1 = QPushButton()
        layout.addWidget(self.l1)
        self.l1.setText("LED On")
        self.l1.clicked.connect(self.l1_clicked)

        self.l2 = QPushButton()
        layout.addWidget(self.l2)
        self.l2.setText("LEF Off")
        self.l2.clicked.connect(self.l2_clicked)'''


        '''self.sshot = QPushButton()
        layout.addWidget(self.sshot)
        self.sshot.setText("Screen capture")
        self.sshot.clicked.connect(self.sshot_clicked)'''

        self.imagelabel = QLabel()
        layout.addWidget(self.imagelabel)
        self.imagelabel.setMouseTracking(True)
        pixmap = QPixmap(os.getcwd() + '/filler-image.jpg')
        self.imagelabel.setPixmap(pixmap)

        self.scaleLabel = QLabel()
        layout.addWidget(self.scaleLabel)
        pixmap2 = QPixmap(os.getcwd() + '/filler-scale.jpg')
        self.scaleLabel.setPixmap(pixmap2)

        self.tempLabel = QLabel()
        layout.addWidget(self.tempLabel)
        self.tempLabel.setText("TEMPERATURE")







        '''self.sp = QSpinBox()
        layout.addWidget(self.sp)
        self.sp.setMinimum(-999)
        self.sp.setMaximum(999)
        self.sp.setSingleStep(5)
        self.sp.valueChanged.connect(self.valuechange)'''

        style = """QSlider::groove:horizontal {
    border: 1px solid #999999;
    height: 2px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
    margin: 2px 0;
}

QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
    border: 1px solid #5c5c5c;
    width: 60px;
    margin: -40px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
    border-radius: 3px;
}
        """
        self.sp = QSlider(Qt.Horizontal)
        layout.addWidget(self.sp)
        self.sp.setMinimum(-100)
        self.sp.setMaximum(200)
        self.sp.setValue(50)
        self.sp.setTickPosition(QSlider.TicksBelow)
        self.sp.setTickInterval(5)
        self.sp.setStyleSheet(style)
        self.sp.valueChanged.connect(self.valuechange)

        self.l11 = QLabel("Minimum: 50 degree F")
        self.l11.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l11)



        '''self.sp2 = QSpinBox()
        layout.addWidget(self.sp2)
        self.sp2.setMinimum(-999)
        self.sp2.setMaximum(999)
        self.sp2.setSingleStep(5)
        self.sp2.valueChanged.connect(self.valuechange2)'''

        self.sp2 = QSlider(Qt.Horizontal)
        layout.addWidget(self.sp2)
        self.sp2.setMinimum(100)
        self.sp2.setMaximum(400)
        self.sp2.setValue(250)
        self.sp2.setTickPosition(QSlider.TicksBelow)
        self.sp2.setTickInterval(5)
        self.sp2.setStyleSheet(style)
        self.sp2.valueChanged.connect(self.valuechange2)

        self.l12 = QLabel("Maximum: 250 degree F")
        self.l12.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l12)


        # self.gstreamer = QPushButton()
        # layout.addWidget(self.gstreamer)
        # self.gstreamer.setText("Stream Video")
        # self.gstreamer.clicked.connect(self.gstreamer_clicked)


    def sshot_clicked(self):
        screenshot_name = str(datetime.datetime.now().strftime("//MIDDFACILITIES/Users/facilities/Desktop/screenshots/%I-%M-%S-%p-%B-%d-%Y.jpeg"))
        #screenshot_name = "image" + str(datetime.datetime.now()) + ".jpg"
        ImageGrab.grab().save(screenshot_name, "JPEG")
        CustomMessageBox.showWithTimeout(1, "SCREENSHOT", "Screenshot Taken", icon=QMessageBox.Information)


    def valuechange(self):
        self.l11.setText("Minimum: "+str(self.sp.value()) + " degree F")
        global minT
        minT = float(self.sp.value())

    def valuechange2(self):
        self.l12.setText("Maximum: "+str(self.sp2.value()) + " degree F")
        global maxT
        maxT = float(self.sp2.value())

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

    # def gstreamer_clicked(self):
    #     subprocess.Popen(["C:\\Users\\facilities\\stream.bat"]) #put the stream file in the original directory

    def img_clicked(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send("frame")
        #data = s.recv(BUFFER_SIZE)
        s.close()


        time.sleep(2)

        text = 1
        tcolor = (255,255,0)
        text_pos = (0,0)
        framecounter = 0



        try:
            s = urllib.urlopen("http://169.254.31.4/A.dat").read()
            #s = urllib.urlopen("A.dat").read()
            raw = s.split()

            CameraC = float(raw[0])
            CameraF = CameraC * 1.8 + 32



            #celsius = [[0 for y in range(60)] for x in range(80)]
            fheit = numpy.ndarray(shape = (60,80), dtype = float)
            for y in range(60):
                for x in range(80):
                    #fheit[y][x] = 0.032622222 * float(raw[1+ 80 * y + x]) - 539.388883 + CameraK + 273.15
                    #fheit[y][x] = 0.05872 * float(raw[1+ 80 * y + x]) - 479.22999 + CameraF
                    fheit[y][x] = 0.03826 * float(raw[1+ 80 * y + x]) - 270.2783 + (0.6515*CameraF)



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
            image = image.rotate(0).resize((80*11, 60*11))

                        #draw = ImageDraw.Draw(image)
                        #draw.text(text_pos, str(framecounter), fill=tcolor, font=font)

            TmpFileName = "latest.jpg"


            quality_val = 80
            image.save(TmpFileName, quality=quality_val)


            colArray = [float(0)]*80
            difference = float(maxT - minT)
            oneHop = 0
            oneHopTemp = difference/80
            for col in range(80):
                colArray[col] = oneHop + minT
                oneHop = oneHop + oneHopTemp

            #print colArray

            colors2 = numpy.ndarray(shape = (1,80,3), dtype = 'uint8')
            for y in range(1):
                for x in range(80):
                    a = (colArray[x] - minT)/(maxT - minT)
                    if a < 0:
                        a = 0
                    if a > 1:
                        a = 1
                    colors2[y][x][0] = 170 - a * 170
                    colors2[y][x][1] = 255
                    colors2[y][x][2] = 128

            #print colors2
            #image = Image.fromarray(colors2, mode = 'HSV').convert('RGB')

            image2 = Image.fromarray(colors2, mode = 'HSV').convert('RGB')


                            #image = image.rotate(90).resize((80*5, 60*5), Image.ANTIALIAS)
            image2 = image2.rotate(0).resize((80*11, 6*11))


            draw = ImageDraw.Draw(image2)
            #draw.text((0,10), "This is a test", (255,255,0))
            for degree in range(80):
                if ((degree+5) % 10 == 0):
                    font = ImageFont.truetype("calibri.ttf", 20)
                    font2 = ImageFont.truetype("calibri.ttf", 25)

                    draw.text((degree*11,-7),".", (255,255,255), font = font2)
                    draw.text((degree*11-12,13), str(int(colArray[degree])), (255,255,255), font=font)
            TmpFileName2 = "scale.jpg"


            quality_val2 = 80
            image2.save(TmpFileName2, quality=quality_val2)

            with open(TmpFileName2, 'rb') as f:
                data = f.read()
                f.close()


            with open(TmpFileName, 'rb') as f:
                data = f.read()
                f.close()

            def getPos(event):
                x = event.pos().x()
                y = event.pos().y()
                realx = int(x/11)
                realy = int(y/11)
                fheit_string = str(fheit[realy][realx])
                raw_string = str(raw[1+ 80 * realy + realx])
                self.tempLabel.setText(fheit_string)
                #self.rawLabel.setText(raw_string)


            pixmap = QPixmap(os.getcwd() + '/latest.jpg')
            self.imagelabel.setPixmap(pixmap)
            self.imagelabel.mousePressEvent = getPos

            pixmap2 = QPixmap(os.getcwd() + '/scale.jpg')
            self.scaleLabel.setPixmap(pixmap2)
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Could not take image. Please try again!")
            msg.setWindowTitle("No Image Taken")
            msg.exec_()


def window():

   while(VIDEO == 0):
        subprocess.Popen(["C:\\Users\\facilities\\stream.bat"])
        global VIDEO
        VIDEO = 1

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
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText("Could not find joystick. Please connect one and restart the application!")
       msg.setWindowTitle("Joystick Not Found")
       msg.exec_()

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
   led_status = "off"


   while True:
       global message
       global max_speed
       global x_coord_inverted
       global y_coord
       global right_speed
       global left_speed

       for event in pygame.event.get():
           event
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
                   #print "R: "
                   #print R
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


               elif event_axis == 2:
                   if event_value < -0.6:
                       print("Hello")
                       win.img_clicked()
                   elif event_value > 0.6:
                       print("Screenshot")
                       win.sshot_clicked()





           ## Control pad to go straight forward, straight back, and rotate left and right
           elif event_type == 9:
               event_value = event.value

               if event_value == (0, 1):
                   max_speed += 5

               elif event_value == (0, -1):
                   max_speed -= 5


               print str(max_speed)




               message = "R" + str(right_speed) + "L" + str(left_speed)


           ## Buttons
           elif event_type == 10:
               event_button = event.button

               ## Emergency stop button B
               if event_button == 1:
                   message = "R0L0"



               elif event_button == 9:
                   message = "fwd"

               elif event_button == 3:

                   if led_status == "off":
                       message = "ledon"
                       led_status = "on"
                       print "LED ON"
                   else:
                       message = "ledoff"
                       led_status = "off"
                       print "LED OFF"




           #print message
           #print "max_speed:
           #print max_speed
           #if message != "":
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect((TCP_IP, TCP_PORT))
           s.send(message)
           #data = s.recv(BUFFER_SIZE)
           s.close()
       try:

           message = "filler"
           #print message
           time.sleep(.1)
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect((TCP_IP, TCP_PORT))
           s.send(message)
           ##data = s.recv(BUFFER_SIZE)
           s.close()
       except socket.error:
           msg = QMessageBox()
           msg.setIcon(QMessageBox.Warning)
           msg.setText("Connection could not be established between the car and the computer. Check the connection, restart the car and restart this app!")
           msg.setWindowTitle("TCP Connection Cannot Be Made")
           msg.exec_()

           ########################################################################################
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()
