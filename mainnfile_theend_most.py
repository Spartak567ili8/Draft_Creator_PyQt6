import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import (QApplication, QInputDialog, QDialog,QLineEdit
, QFormLayout, QTextEdit,QDialogButtonBox, QWidget, QHBoxLayout,QPushButton, QVBoxLayout, QMainWindow, QSizePolicy)

import socket
import threading



class Create(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draft')
        self.setGeometry(0, 0, 200, 200)
        self.setMaximumSize(200, 200)
        self.setMinimumSize(200, 200)
        self.setStyleSheet('''QWidget {
        
                                background:#9483c1;
                            }''')

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.label = QLabel('Write a draft')
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily('Tempus Sans ITC')
        font.setBold(True)
        font.setPointSize(13)
        self.label.setFont(font)
        self.main_layout.addWidget(self.label)

        self.draft = QTextEdit()
        self.main_layout.addWidget(self.draft)
        self.draft.setStyleSheet('''QTextEdit {
                                    color:#FFFFFF;
                                }''')

        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.add_button = QPushButton('Add')
        self.add_button.setStyleSheet('''QPushButton {
                                                        background:#FAFEA2;
                                                    }
                                                    QPushButton:hover {
                                                        background:#FCFEBA;
                                                    }
                                                '''
                                         )
        self.delete_button = QPushButton('Del')
        self.delete_button.setStyleSheet('''QPushButton {
                                                        background:#FAFEA2;
                                                    }
                                                    QPushButton:hover {
                                                        background:#FCFEBA;
                                                    }
                                                '''
                                         )

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.delete_button)

        self.add_button.clicked.connect(self.create_text_from_draft)
        self.delete_button.clicked.connect(self.close_draft_window)


    def create_text_from_draft(self):
        text = self.draft.toPlainText()
        if len(text) > 0:
            folder_path = 'drafts'
            file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
            with open(f'{folder_path}/{file_count + 1}.txt', 'w') as file:
                file.write(text)
                self.close_draft_window()








    def close_draft_window(self):
        self.accept()



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 500)
        self.setWindowTitle('Create a draft')
        self.setMaximumSize(400, 500)
        self.setMinimumSize(400, 500)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setStyleSheet('''QWidget {

                                        background:#9483c1;
                                    }''')

        self.label = QLabel('Create and show a draft')
        self.main_layout.addWidget(self.label)
        self.label .setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        font = QtGui.QFont()
        font.setFamily('Consolas')
        font.setBold(True)
        font.setPointSize(22)
        self.label.setFont(font)

        self.create_button = QPushButton('Create a draft')
        self.main_layout.addWidget(self.create_button)
        self.create_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        font = QtGui.QFont()
        font.setFamily('Tempus Sans ITC')
        font.setBold(True)
        font.setPointSize(35)
        self.create_button.setFont(font)
        self.create_button.setStyleSheet('''QPushButton {
                                                background:#674ea7;
                                            }
                                            QPushButton:hover {
                                                background:#765faf;
                                            }
                                        '''
                                         )

        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.view_button = QPushButton('View')
        self.button_layout.addWidget(self.view_button)
        self.view_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        font = QtGui.QFont()
        font.setFamily('Tempus Sans ITC')
        font.setBold(True)
        font.setPointSize(20)
        self.view_button.setFont(font)
        self.view_button.setStyleSheet('''QPushButton {
                                                        background:#674ea7;
                                                    }
                                                    QPushButton:hover {
                                                        background:#765faf;
                                                    }
                                                '''
                                         )

        self.exit_button = QPushButton('Exit')
        self.button_layout.addWidget(self.exit_button)
        self.exit_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        font = QtGui.QFont()
        font.setFamily('Tempus Sans ITC')
        font.setBold(True)
        font.setPointSize(20)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet('''QPushButton {
                                                        background:#674ea7;
                                                    }
                                                    QPushButton:hover {
                                                        background:#765faf;
                                                    }
                                                '''
                                         )

        self.create_button.clicked.connect(self.show_new_window)
        self.view_button.clicked.connect(self.open_draft)

        self.exit_button.clicked.connect(self.exit)

    def open_draft(self):
        folder_path = 'drafts'
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(folder_path))

    def show_new_window(self):
        window = Create()
        window.exec()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()