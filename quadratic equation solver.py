from math import sqrt
from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout

def get_a():
    global a
    a = input_prompt.text()

def get_b():
    global b
    b = input_prompt.text()

def get_c():
    global c
    c = input_prompt.text()

def solvef():
    global total
    try:
        D = (float(b) * float(b) - 4 * float(a) * float(c))
        if D > 0:
            x1 = (- float(b) / 2 * float(a) + sqrt(D) / 2 * float(a))
            x2 = (- float(b) / 2 * float(a) - sqrt(D) / 2 * float(a))
            total += 'D = ' + str(D) + "\n" + 'x1 = ' + str(x1) + "\n" + 'x2 = ' + str(x2) + "\n"
        elif D == 0:
            x1 = (- float(b) / 2 * float(a))
            total += 'D = ' + str(D) + "\n" + 'x1 = ' + str(x1) + "\n" + 'x2 = ' + str(x1) + "\n"
        elif D < 0:
            total += 'D = ' + str(D) + "\n" + 'the equation is impossible\n'
        display.setText(total)
    except:
        total += 'μη κατανοητό'
        display.setText(total)

app = QApplication([])
w = QWidget()
w.setWindowTitle("Quadratic equation solver")
w.resize(1000, 800)
display = QTextEdit()
input_prompt = QLineEdit()
input_prompt.setPlaceholderText('Type here:')
pb1 = QPushButton("a")
pb2 = QPushButton("b")
pb3 = QPushButton("c")
pb4 = QPushButton("Find")
l1 = QVBoxLayout()
l2 = QHBoxLayout()
l3 = QHBoxLayout()
l1.addWidget(input_prompt)
l2.addWidget(pb1)
l2.addWidget(pb2)
l2.addWidget(pb3)
l1.addLayout(l2)
l1.addWidget(pb4)
l3.addWidget(display)
l3.addLayout(l1)
w.setLayout(l3)
w.show()
total = ''
welcome = 'The program displays the values of the discriminant, the x and y provided they exist\nthe form of the equation is a*(x*x) + b*x + c\ninput a, b and c\n'
total += welcome
display.setText(total)
pb1.clicked.connect(get_a)
pb2.clicked.connect(get_b)
pb3.clicked.connect(get_c)
pb4.clicked.connect(solvef)
app.exec_()