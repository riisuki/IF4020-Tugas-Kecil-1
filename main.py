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
    QHBoxLayout,
    QWidget,
    QPlainTextEdit,
    QFileDialog,
    QStackedWidget
)

from vigenere import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tugas Kecil IF4020")

        hbox = QHBoxLayout()
        layout = QVBoxLayout()
        
        self.label1 = QLabel("Jenis Cipher:")
        self.jeniscipher = QComboBox()
        self.jeniscipher.addItems(["Vigénere", "Full Vigénere", "Auto-key Vigénere", "Extended Vigénere", "Playfair", "Affine", "Hill", "Enigma"])


        self.spasi = QCheckBox("Tambahkan spasi di cipherteks")

        
        self.label2 = QLabel("Input:")
        self.inputfield = QPlainTextEdit()

        self.label3 = QLabel("Output:")
        self.outputfield = QPlainTextEdit()
        self.outputfield.setReadOnly(True)


        self.bukafile = QPushButton("Berkas...")
        self.labelpath = QLabel("")
        self.bukafile.clicked.connect(self.open)
        self.bukafile2 = QPushButton("Simpan...")
        
        self.label4 = QLabel()
        self.enkripsi = QPushButton("Enkripsi")
        self.enkripsi.clicked.connect(self.fungsi_enkripsi)
        self.dekripsi = QPushButton("Dekripsi")
        self.dekripsi.clicked.connect(self.fungsi_dekripsi)

        self.enkripsi.setStyleSheet("background-color : #98d6ed")
        self.dekripsi.setStyleSheet("background-color : #98d6ed")

        # Extra fields
        self.vigenere_kunci = QLineEdit()
        
        # Buat menu beda sesuai jenis cipher
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack5 = QWidget()
        self.stack6 = QWidget()
        self.layout1()
        self.layout2()
        self.stack = QStackedWidget (self)
        self.stack.addWidget (self.stack1)
        self.stack.addWidget (self.stack2)
        self.stack.addWidget (self.stack3)
        self.stack.addWidget (self.stack4)
        self.stack.addWidget (self.stack5)
        self.stack.addWidget (self.stack6)

        

        self.jeniscipher.currentIndexChanged.connect(self.changemenus)

        

        # Masukkan menu ganti cipher
        #layout.addWidget(self.label1)
        #layout.addWidget(self.jeniscipher)
        #layout.addWidget(self.stack)
        layout.addWidget(self.spasi)
        layout.addWidget(self.label2)
        layout.addWidget(self.inputfield)
        layout.addWidget(self.bukafile)
        layout.addWidget(self.labelpath)
        layout.addWidget(self.label3)
        layout.addWidget(self.outputfield)
        layout.addWidget(self.bukafile2)
        layout.addWidget(self.label4)
        #layout.addWidget(self.enkripsi)
        #layout.addWidget(self.dekripsi)

        widget = QWidget()
        hbox.addLayout(layout)
        hbox.addWidget(self.stack)
        layoutall = QVBoxLayout()
        layoutall.addWidget(self.label1)
        layoutall.addWidget(self.jeniscipher)
        layoutall.addLayout(hbox)
        layoutall.addWidget(self.enkripsi)
        layoutall.addWidget(self.dekripsi)
        widget.setLayout(layoutall)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def layout1(self):
        # Layout 1. Vignere Cipher
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 23, 0, 0)

        
        labelkey = QLabel("Kunci:")
        
        layout.addWidget(labelkey)
        layout.addWidget(self.vigenere_kunci)
        layout.setAlignment(Qt.AlignTop)
        
        
        self.stack1.setLayout(layout)


    def layout2(self):
        # Layout 2. Full Vignere Cipher
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 23, 0, 0)

        labelkey = QLabel("Kunci:")
        kunci = QLineEdit()

        tabel = QPushButton("Edit Tabel")

        layout.addWidget(labelkey)
        layout.addWidget(kunci)
        layout.addWidget(tabel)
        layout.setAlignment(Qt.AlignTop)
        

        self.stack2.setLayout(layout)


    def changemenus(self, s):
        # Untuk ganti menu saat mengubah jenis cipher
        index = self.jeniscipher.currentIndex()
        print("Current index:", index)
        if index == 0 or index == 2 or index == 3:
            self.stack.setCurrentIndex(0)
        else:
            self.stack.setCurrentIndex(1)

    def fungsi_enkripsi(self):
        index = self.jeniscipher.currentIndex()
        teksinput = self.inputfield.toPlainText()
        output = ''
        
        
        if index == 0:
            tekskunci = self.vigenere_kunci.text()
            output = vigenere(tekskunci, teksinput, True, False, False)

        elif index == 2:
            tekskunci = self.vigenere_kunci.text()
            output = vigenere(tekskunci, teksinput, True, True, False)

        elif index == 3:
            tekskunci = self.vigenere_kunci.text()
            output = vigenere(tekskunci, teksinput, True, False, True)

        # Tambah spasi jika opsi dipilih
        if self.spasi.isChecked():
            output = ' '.join(output[i:i+5] for i in range(0,len(output),5))

        self.outputfield.setPlainText(output)

    def fungsi_dekripsi(self):
        index = self.jeniscipher.currentIndex()
        teksinput = self.inputfield.toPlainText()
        output = ''
        
        
        if index == 0:
            tekskunci = self.vigenere_kunci.text()
            output = vigenere(tekskunci, teksinput, False, False, False)

        elif index == 2:
            tekskunci = self.vigenere_kunci.text()
            output = vigenere(tekskunci, teksinput, False, True, False)

        elif index == 3:
            tekskunci = self.vigenere_kunci.text()
            output = vigenere(tekskunci, teksinput, False, False, True)

        self.outputfield.setPlainText(output)

    def open(self):
        fileName = ''
        index = self.jeniscipher.currentIndex()
        if index != 3:
            fileName, _ = QFileDialog.getOpenFileName(self, 'File Input','.', "Text Files (*.txt)")
        else:
            fileName, _ = QFileDialog.getOpenFileName(self, 'File Input')
        content = ''
        if fileName.endswith('.txt'):
           # File txt
           with open(fileName, 'r') as f:
               content = f.read()
               self.inputfield.setPlainText(content)
        else:
            # File biner
            #with open(fileName, 'rb') as f:
               #bytecontent = f.read()
            self.inputfield.setPlainText(fileName)

               
            


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
