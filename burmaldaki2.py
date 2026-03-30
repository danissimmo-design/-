from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('я хочу быть как газан')
number = QLabel('?')
#winner.setText('?')
#winner.text()
buttom = QPushButton('Секретная кнопка')

#button.setText('Новый ')
v_line = QVBoxLayout()
v_line.addWidget(buttom, alignment = Qt.AlignCenter)

main_win.setLayout(v_line)
def show_winner():
    ch = QLabel('Ты просто чудо!!!🐺🐺🐺')
    v_line.addWidget(ch, alignment = Qt.AlignCenter)
buttom.clicked.connect(show_winner)
main_win.show()
app.exec_()
