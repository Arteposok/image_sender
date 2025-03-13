from client_window import Ui_MainWindow
from PyQt5.QtWidgets import *
import socket as sc
import sys
import os

class Window(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file=""
        self.pick.clicked.connect(self.pick_file)
        self.send.clicked.connect(self.send_image)

    def send_image(self):
        try:
            with open(self.file, "rb") as file:
                img_bytes = file.read()
            with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as socket:
                socket.connect((self.ip.text(), int(self.port.text())))
                socket.send(str(os.path.getsize(self.file)).encode())
                socket.recv(1024)
                socket.send(img_bytes)
                success=QMessageBox(self)
                success.setWindowTitle("success")
                success.setText("successfully sent your image, let's hope server saves it")
                success.show()
        except IOError:
            error = QMessageBox(self)
            error.setWindowTitle("ERROR:)")
            error.setText("Some Socket Error, Ensure you have IP and"
                                                    " PORT, otherwise I messed something up hehe")
            error.setIcon(QMessageBox.Icon.Critical)
            error.exec_()

    def pick_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open An Image")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.file=selected_files[0]

app=QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec())