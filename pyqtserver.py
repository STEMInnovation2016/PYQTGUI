import sys
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

TCP_IP = '192.168.2.125' #other computer's IP
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

        self.sl = QSlider(Qt.Vertical)
        self.sl.setMinimum(1)
        self.sl.setMaximum(19)
        self.sl.setValue(10)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(1)

        layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(layout)
        self.sl.sliderReleased.connect(self.sliderreleased)

        self.l2 = QLabel("")
        self.l2.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l2)

        self.sl2 = QSlider(Qt.Horizontal)
        self.sl2.setMinimum(1)
        self.sl2.setMaximum(19)
        self.sl2.setValue(10)
        self.sl2.setTickPosition(QSlider.TicksBelow)
        self.sl2.setTickInterval(1)

        layout.addWidget(self.sl2)
        self.sl2.valueChanged.connect(self.valuechange2)
        self.setLayout(layout)
        self.sl2.sliderReleased.connect(self.sliderreleased2)

        self.imagelabel = QLabel()
        layout.addWidget(self.imagelabel)


    def img_clicked(self):

        print("HEY")
        text = 1
        tcolor = (255,255,0)
        text_pos = (0,0)
        framecounter = 0


        s = urllib.urlopen("http://192.168.2.125/A.dat").read()

        raw = s.split()

        CameraK = float(raw[0])

        #celsius = [[0 for y in range(60)] for x in range(80)]
        celsius = numpy.ndarray(shape = (60,80), dtype = float)
        for y in range(60):
            for x in range(80):
                celsius[y][x] = 0.032622222 * float(raw[1+ 80 * y + x]) - 539.388883 + CameraK + 273.15

        minT = float(25)
        maxT = float(31)



        colors = numpy.ndarray(shape = (60,80,3), dtype = 'uint8')
        for y in range(60):
            for x in range(80):
                a = (celsius[y][x] - minT)/(maxT - minT)
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

        pixmap = QPixmap(os.getcwd() + '/latest.jpg')
        self.imagelabel.setPixmap(pixmap)



    def valuechange(self):
        size = self.sl.value()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))

        if (size < 10):
            str_size = str(10 - size)
            s.send(str_size)
            s.send("s")
            print(str_size)
        elif (size == 10):
            str_size = str(1)
            s.send(str_size)
            s.send(" ")
            print(str_size)
        else:
            str_size = str(size - 10)
            s.send(str_size)
            s.send("w")
            print(str_size)

        #data = s.recv(BUFFER_SIZE)
        s.close()

    def sliderreleased(self):
        print("x")
        self.sl.setValue(10)

    def valuechange2(self):
        size = self.sl2.value()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))

        if (size < 10):
            str_size = str(10 - size)
            s.send(str_size)
            s.send("d")
            print(str_size)
        elif (size == 10):
            str_size = str(1)
            s.send(str_size)
            s.send(" ")
            print(str_size)
        else:
            str_size = str(size - 10)
            s.send(str_size)
            s.send("a")
            print(str_size)

    #data = s.recv(BUFFER_SIZE)
        s.close()

    def sliderreleased2(self):
        print("x")
        self.sl2.setValue(10)


    def keyPressEvent(self, event):
        print event.text()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(event.text())
        #data = s.recv(BUFFER_SIZE)
        s.close()

    def keyReleaseEvent(self, event):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(" ")
        #data = s.recv(BUFFER_SIZE)
        s.close()


def window():

   app = QApplication(sys.argv)
   win = QWidget()



   reboot = QPushButton(win)
   reboot.setText("REBOOT")
   reboot.move(300,30)
   reboot.clicked.connect(reboot_clicked)

   b1 = QPushButton(win)
   b1.setText("Tilt up")
   b1.move(170,60)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Pan left")
   b2.move(110,90)
   b2.clicked.connect(b2_clicked)

   b3 = QPushButton(win)
   b3.setText("Pan right")
   b3.move(230,90)
   b3.clicked.connect(b3_clicked)

   b4 = QPushButton(win)
   b4.setText("Tilt down")
   b4.move(170,120)
   b4.clicked.connect(b4_clicked)

   b5 = QPushButton(win)
   b5.setText("Face front")
   b5.move(110,150)
   b5.clicked.connect(b5_clicked)

   b6 = QPushButton(win)
   b6.setText("Face back")
   b6.move(230,150)
   b6.clicked.connect(b6_clicked)

   c1 = QPushButton(win)
   c1.setText("Forward")
   c1.move(170,200)
   c1.pressed.connect(c1_clicked)
   c1.released.connect(released)

   c2 = QPushButton(win)
   c2.setText("Left")
   c2.move(110,230)
   c2.pressed.connect(c2_clicked)
   c2.released.connect(released)

   c3 = QPushButton(win)
   c3.setText("Right")
   c3.move(230,230)
   c3.pressed.connect(c3_clicked)
   c3.released.connect(released)

   c4 = QPushButton(win)
   c4.setText("Backward")
   c4.move(170,260)
   c4.pressed.connect(c4_clicked)
   c4.released.connect(released)

   l1 = QPushButton(win)
   l1.setText("LED On")
   l1.move(110,310)
   l1.clicked.connect(l1_clicked)

   l2 = QPushButton(win)
   l2.setText("LEF Off")
   l2.move(230,310)
   l2.clicked.connect(l2_clicked)

   browser = QPushButton(win)
   browser.setText("Stream Flir")
   browser.move(110,360)
   browser.clicked.connect(browser_clicked)

   gstreamer = QPushButton(win)
   gstreamer.setText("Stream Video")
   gstreamer.move(230,360)
   gstreamer.clicked.connect(gstreamer_clicked)

   cl1 = QPushButton(win)
   cl1.setText("Claw open")
   cl1.move(110,410)
   cl1.clicked.connect(cl1_clicked)

   cl2 = QPushButton(win)
   cl2.setText("Claw close")
   cl2.move(230,410)
   cl2.clicked.connect(cl2_clicked)

   cl3 = QPushButton(win)
   cl3.setText("Claw up")
   cl3.move(110,440)
   cl3.clicked.connect(cl3_clicked)

   cl4 = QPushButton(win)
   cl4.setText("Claw down")
   cl4.move(230,440)
   cl4.clicked.connect(cl4_clicked)

   numpey = QPushButton(win)
   numpey.setText("TakeIMG")
   numpey.move(110,490)
   numpey.clicked.connect(numpey_clicked)




   win.setGeometry(20,40,410,5)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())


def numpey_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send(",")
   #data = s.recv(BUFFER_SIZE)
   s.close()
   #subprocess.Popen(["C:\Users\shoug\flir.bat"])

def reboot_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("p")
   #data = s.recv(BUFFER_SIZE)
   s.close()



def b1_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("i")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def b2_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("j")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def b3_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("l")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def b4_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("k")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def b5_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("f")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def b6_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("b")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def c1_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("w")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def c2_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("a")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def c3_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("d")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def c4_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("s")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def released():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send(" ")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def l1_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("g")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def l2_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("h")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def cl1_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("r")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def cl2_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("t")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def cl3_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("y")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def cl4_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("u")
   #data = s.recv(BUFFER_SIZE)
   s.close()



def browser_clicked():
    webbrowser.open_new_tab("http://192.168.2.125:8080")

def gstreamer_clicked():
    subprocess.Popen(["C:\Users\shoug\stream.bat"]) #put the stream file in the original directory

if __name__ == '__main__':
   window()
