import sys
from PyQt5.QtWidgets import QApplication, QWidget, QWidgetItem, QTabWidget, QMainWindow, QVBoxLayout, QLabel, \
    QPushButton, QSpacerItem, QTextEdit
from PyQt5 import QtWidgets



class MainForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.sale_list =None


        #creating the main layout
        layout= QVBoxLayout()
        #add layout
        label= QLabel('Nome: ')
        layout.addWidget(label)

        self.text_edit = QTextEdit('Add your name')
        self.text_edit.setFixedSize(800,50)
        layout.addWidget(self.text_edit)

        self.btn_load = QPushButton('Load Nome')
        layout.addWidget(self.btn_load)


        space = QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(space)



        self.setWindowTitle('Minha Primeira Janela')
        self.setGeometry(400, 250, 800, 600)

        container = QWidget(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.show()


        #configuring the windom


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    sys.exit(app.exec_())
