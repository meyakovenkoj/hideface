#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import Qt, QtCore, QtGui, QtWidgets

import cv2
import time
import platform
import sys

prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, \
         37, 41, 43, 47, 53, 59, 61, 67, 71,  \
         73, 79, 83, 89, 97, 101, 103, 107,   \
         109, 113, 127, 131, 137, 139, 149,   \
         151, 157, 163, 167, 173, 179, ]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(826, 440)
        self.videosource = 0
        self.videoout = ''
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(10, 10, 640, 360))
        self.image_label.setObjectName("image_label")

        
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(680, 150, 121, 22))
        self.doubleSpinBox_2.setMaximum(1.99)
        self.doubleSpinBox_2.setMinimum(1.01)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(680, 210, 121, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setValue(25)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(680, 10, 121, 22))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggle()
        self.checkBox.stateChanged.connect(self.changeInput)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 340, 121, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.controlTimer)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 70, 121, 16))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(680, 190, 121, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 130, 121, 16))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 240, 121, 22))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 380, 800, 22))
        self.label_5.setObjectName("label_5")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 30, 121, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 90, 121, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 22))
        self.menubar.setObjectName("menubar")
        
        self.menuHideFace = QtWidgets.QMenu(self.menubar)
        self.menuHideFace.setObjectName("menuHideFace")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHideFace.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt2.xml')
        # self.eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
        # self.closed_eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye_closed.xml')
        if self.face_cascade.empty():
            QtWidgets.QMessageBox.information(self.centralwidget, "Error Loading cascade classifier" , "Unable to load the face cascade classifier xml file")
            sys.exit()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.detectFaces)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HideFace"))
        self.checkBox.setText(_translate("MainWindow", "File"))
        self.checkBox.setCheckState(False)
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Path to save"))
        self.label_2.setText(_translate("MainWindow", "Blur"))
        self.label_3.setText(_translate("MainWindow", "Scale Factor"))
        self.label_4.setText(_translate("MainWindow", "31"))
        self.label_5.setText(_translate("MainWindow", "Name of output file"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.menuHideFace.setTitle(_translate("MainWindow", "HideFace"))
        self.pushButton_2.clicked.connect(self.FileBrowse)
        self.pushButton_3.clicked.connect(self.FolderBrowse)
        self.doubleSpinBox_2.setValue(1.10)
        self.horizontalSlider.valueChanged.connect(self.v_change)

    def changeInput(self, state):
        if state == QtCore.Qt.Checked:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
            self.videosource = 0

    def FileBrowse(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(filter="Video File(*.mp4)")
        print(filePath[0])
        self.videosource = filePath[0]
        
    def FolderBrowse(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()
        self.videoout = folderPath
        
    def v_change(self):
        value = self.horizontalSlider.value()
        value = int(( len(prime) / 100 ) * value)
        self.label_4.setText(str(prime[value]))
    
    def detectFaces(self):
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
        accuracy_val = self.doubleSpinBox_2.value()
        face_rects = self.face_cascade.detectMultiScale(gray, accuracy_val, 3)
        value = self.horizontalSlider.value()
        value = int(( len(prime) / 100 ) * value)
        for (x, y, w, h) in face_rects:
            x *= 4
            y *= 4
            w *= 4
            h *= 4
            sub_face = frame[y:y+h, x:x+w]
            # eyes = self.eye_cascade.detectMultiScale(sub_face, accuracy_val, 3)
            # closed_eyes = self.closed_eye_cascade.detectMultiScale(sub_face, accuracy_val, 3)
            # if len(eyes) == 0 and len(closed_eyes) == 0:
            #     continue
            # else:
            sub_face = cv2.GaussianBlur(sub_face,(prime[value], prime[value]), 30)
            frame[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        self.out.write(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        scaling_factor = 0.5
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        height, width, channel = frame.shape
        step = channel * width
        qImg = QtGui.QImage(frame.data, width, height, step, QtGui.QImage.Format_RGB888)
        self.image_label.setPixmap(QtGui.QPixmap.fromImage(qImg))
        
    def controlTimer(self):
        if not self.timer.isActive():
            if not self.videoout:
                QtWidgets.QMessageBox.information(self.centralwidget, "Error Choosing directory" , "Please choose the correct path to save video")
            else:
                self.cap = cv2.VideoCapture(self.videosource)
                self.timer.start(20)
                vout = self.videoout
                if platform.system() == 'Windows':
                    vout = vout + '\\'
                else:
                    vout = vout + '/'
                outname = vout + str(int(time.time())) + '.mp4'
                self.label_5.setText(outname)
                print(outname)
                print(self.cap.get(3), self.cap.get(4))
                print(self.cap.get(cv2.CAP_PROP_FPS)) 
                self.out = cv2.VideoWriter(outname, 0x7634706d, 20, (int(self.cap.get(3)), int(self.cap.get(4))))
                self.pushButton.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.out.release()
            self.pushButton.setText("Start")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    