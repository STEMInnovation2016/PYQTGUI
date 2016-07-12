import sys

import socket

import subprocess

import webbrowser

from PyQt4.QtCore import *
from PyQt4.QtGui import *

TCP_IP = '192.168.2.125'
TCP_PORT = 5005
BUFFER_SIZE = 1
A = 0


class QWidget(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)

        layout = QVBoxLayout()
        self.l1 = QLabel("")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

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

   b1 = QPushButton(win)
   b1.setText("Tilt up")
   b1.move(170,60)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Pan left")
   b2.move(110,80)
   b2.clicked.connect(b2_clicked)

   b3 = QPushButton(win)
   b3.setText("Pan right")
   b3.move(230,80)
   b3.clicked.connect(b3_clicked)

   b4 = QPushButton(win)
   b4.setText("Tilt down")
   b4.move(170,100)
   b4.clicked.connect(b4_clicked)

   b5 = QPushButton(win)
   b5.setText("Face front")
   b5.move(110,120)
   b5.clicked.connect(b5_clicked)

   b6 = QPushButton(win)
   b6.setText("Face back")
   b6.move(230,120)
   b6.clicked.connect(b6_clicked)

   c1 = QPushButton(win)
   c1.setText("Forward")
   c1.move(170,180)
   c1.pressed.connect(c1_clicked)
   c1.released.connect(released)

   c2 = QPushButton(win)
   c2.setText("Left")
   c2.move(110,200)
   c2.pressed.connect(c2_clicked)
   c2.released.connect(released)

   c3 = QPushButton(win)
   c3.setText("Right")
   c3.move(230,200)
   c3.pressed.connect(c3_clicked)
   c3.released.connect(released)

   c4 = QPushButton(win)
   c4.setText("Backward")
   c4.move(170,220)
   c4.pressed.connect(c4_clicked)
   c4.released.connect(released)

   l1 = QPushButton(win)
   l1.setText("LED On")
   l1.move(110,280)
   l1.clicked.connect(l1_clicked)

   l2 = QPushButton(win)
   l2.setText("LEF Off")
   l2.move(230,280)
   l2.clicked.connect(l2_clicked)

   browser = QPushButton(win)
   browser.setText("Stream Flir")
   browser.move(110,340)
   browser.clicked.connect(browser_clicked)

   gstreamer = QPushButton(win)
   gstreamer.setText("Stream Video")
   gstreamer.move(230,340)
   gstreamer.clicked.connect(gstreamer_clicked)


   win.setGeometry(0,0,410,500)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())



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

def browser_clicked():
    webbrowser.open_new_tab("http://192.168.2.127:8080")

def gstreamer_clicked():
    subprocess.Popen(["gst-launch-1.0", "-v", "tcpclientsrc", "host=192.168.2.127", "port=5000", "!", "gdpdepay", "!", "rtph264depay", "!", "avdec_h264", "!", "videoconvert", "!", "autovideosink", "sync=false"])


if __name__ == '__main__':
   window()
