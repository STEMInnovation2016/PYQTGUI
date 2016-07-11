import sys

import socket

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
        self.l1 = QLabel("Test")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(1)
        self.sl.setMaximum(19)
        self.sl.setValue(10)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(1)

        layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(layout)


    def valuechange(self):
        size = self.sl.value()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))

        if (size < 10):
            str_size = str(size)
            s.send(str_size)
            s.send("w")
        elif (size == 10):
            str_size = str(5)
            s.send(str_size)
            s.send(" ")
        else:
            str_size = str(size - 10)
            s.send(str_size)
            s.send("s")

        #data = s.recv(BUFFER_SIZE)
        s.close()


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

   label = QLabel(win)
   label.setText("PAN AND TILT:")
   label.move(50, 20)

   b1 = QPushButton(win)
   b1.setText("up")
   b1.move(50,50)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("left")
   b2.move(20,90)
   b2.clicked.connect(b2_clicked)

   b3 = QPushButton(win)
   b3.setText("right")
   b3.move(80,90)
   b3.clicked.connect(b3_clicked)

   b4 = QPushButton(win)
   b4.setText("down")
   b4.move(50,130)
   b4.clicked.connect(b4_clicked)

   b5 = QPushButton(win)
   b5.setText("for")
   b5.move(20,180)
   b5.clicked.connect(b5_clicked)

   b6 = QPushButton(win)
   b6.setText("back")
   b6.move(80,180)
   b6.clicked.connect(b6_clicked)

   label = QLabel(win)
   label.setText("CAR CONTROLS:")
   label.move(50, 230)

   c1 = QPushButton(win)
   c1.setText("forward")
   c1.move(50,260)
   c1.pressed.connect(c1_clicked)
   c1.released.connect(released)

   c2 = QPushButton(win)
   c2.setText("left")
   c2.move(20,300)
   c2.pressed.connect(c2_clicked)
   c2.released.connect(released)

   c3 = QPushButton(win)
   c3.setText("right")
   c3.move(80,300)
   c3.pressed.connect(c3_clicked)
   c3.released.connect(released)

   c4 = QPushButton(win)
   c4.setText("backward")
   c4.move(50,340)
   c4.pressed.connect(c4_clicked)
   c4.released.connect(released)

   l1 = QPushButton(win)
   l1.setText("on")
   l1.move(20,440)
   l1.clicked.connect(l1_clicked)

   l2 = QPushButton(win)
   l2.setText("off")
   l2.move(80,440)
   l2.clicked.connect(l2_clicked)


   win.setGeometry(100,100,200,470)
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

if __name__ == '__main__':
   window()
