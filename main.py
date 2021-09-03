import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
    QPlainTextEdit,
    QStackedWidget
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tugas Kecil IF4020")

        layout = QVBoxLayout()
        
        self.label1 = QLabel("Jenis Cipher:")
        self.jeniscipher = QComboBox()
        self.jeniscipher.addItems(["Vigénere", "Full Vigénere", "Auto-key Vigénere", "Extended Vigénere", "Playfair", "Affine", "Hill", "Enigma"])


        self.label2 = QLabel("Plainteks:")
        self.plainteks = QPlainTextEdit()

        self.label3 = QLabel("Cipherteks:")
        self.cipherteks = QPlainTextEdit()


        self.bukafile = QPushButton("Browse...")
        self.bukafile2 = QPushButton("Browse...")
        
        self.label4 = QLabel()
        self.enkripsi = QPushButton("Enkripsi")
        self.dekripsi = QPushButton("Dekripsi")

        self.enkripsi.setStyleSheet("background-color : #98d6ed")
        self.dekripsi.setStyleSheet("background-color : #98d6ed")
        
        # Buat menu beda sesuai jenis cipher
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack5 = QWidget()
        self.stack6 = QWidget()
        self.stack7 = QWidget()
        self.stack8 = QWidget()
        self.layout1()
        self.layout2()
        self.stack = QStackedWidget (self)
        self.stack.addWidget (self.stack1)
        self.stack.addWidget (self.stack2)
        self.stack.addWidget (self.stack3)
        self.stack.addWidget (self.stack4)
        self.stack.addWidget (self.stack5)
        self.stack.addWidget (self.stack6)
        self.stack.addWidget (self.stack7)
        self.stack.addWidget (self.stack8)

        

        self.jeniscipher.currentIndexChanged.connect(self.changemenus)

        
        # Masukkan menu ganti cipher
        layout.addWidget(self.label1)
        layout.addWidget(self.jeniscipher)
        layout.addWidget(self.stack)
        layout.addWidget(self.label2)
        layout.addWidget(self.plainteks)
        layout.addWidget(self.bukafile)
        layout.addWidget(self.label3)
        layout.addWidget(self.cipherteks)
        layout.addWidget(self.bukafile2)
        layout.addWidget(self.label4)
        layout.addWidget(self.enkripsi)
        layout.addWidget(self.dekripsi)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def layout1(self):
        # Layout 1. Vignere Cipher
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        spasi = QCheckBox("Tambahkan spasi di cipherteks")

        labelkey = QLabel("Kunci:")
        kunci = QLineEdit()
        

        #Button
        
        

        layout.addWidget(spasi)
        layout.addWidget(labelkey)
        layout.addWidget(kunci)
        layout.setAlignment(Qt.AlignTop)
        
        
        self.stack1.setLayout(layout)


    def layout2(self):
        # Layout 2. Full Vignere Cipher
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        spasi = QCheckBox("Tambahkan spasi di cipherteks")

        labelkey = QLabel("Kunci:")
        kunci = QLineEdit()

        tabel = QPushButton("Edit Tabel")

        layout.addWidget(spasi)
        layout.addWidget(labelkey)
        layout.addWidget(kunci)
        layout.addWidget(tabel)
        

        self.stack2.setLayout(layout)


    def changemenus(self, s):
        # Untuk ganti menu saat mengubah jenis cipher
        index = self.jeniscipher.currentIndex()
        print("Current index:", index)
        self.stack.setCurrentIndex(index)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
