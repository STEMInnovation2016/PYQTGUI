import sys

import socket

from PyQt4.QtCore import *
from PyQt4.QtGui import *

TCP_IP = '192.168.2.126'
TCP_PORT = 5005
BUFFER_SIZE = 1



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
   c1.clicked.connect(c1_clicked)

   c2 = QPushButton(win)
   c2.setText("left")
   c2.move(20,300)
   c2.clicked.connect(c2_clicked)

   c3 = QPushButton(win)
   c3.setText("right")
   c3.move(80,300)
   c3.clicked.connect(c3_clicked)

   c4 = QPushButton(win)
   c4.setText("backward")
   c4.move(50,340)
   c4.clicked.connect(c4_clicked)

   c5 = QPushButton(win)
   c5.setText("faster")
   c5.move(20,390)
   c5.clicked.connect(c5_clicked)

   c6 = QPushButton(win)
   c6.setText("slower")
   c6.move(80,390)
   c6.clicked.connect(c6_clicked)

   c7 = QPushButton(win)
   c7.setText("stop")
   c7.move(50,430)
   c7.clicked.connect(c7_clicked)



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

def c5_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("q")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def c6_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send("e")
   #data = s.recv(BUFFER_SIZE)
   s.close()

def c7_clicked():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   s.send(" ")
   #data = s.recv(BUFFER_SIZE)
   s.close()





if __name__ == '__main__':
   window()
