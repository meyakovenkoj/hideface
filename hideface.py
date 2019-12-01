# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hideface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QWidget, QSlider, QPushButton, QGraphicsView, QDoubleSpinBox, QCheckBox, QLabel, \
    QMenuBar, QFileDialog, QApplication, QMainWindow, QStatusBar, QMenu, QMessageBox 
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject, QTimer
from PyQt5.QtGui import QImage, QPixmap

import cv2
import time
import platform


prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, \
        103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, ]





        

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 440)
        self.videosource = 0
        self.videoout = ''
        # load face cascade classifier
        

        # set control_bt callback clicked  function
        
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setGeometry(QRect(10, 10, 640, 360))
        self.image_label.setObjectName("image_label")

        
        self.doubleSpinBox_2 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QRect(680, 150, 121, 22))
        self.doubleSpinBox_2.setMaximum(1.99)
        self.doubleSpinBox_2.setMinimum(1.01)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QRect(680, 210, 121, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setValue(25)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QRect(680, 10, 121, 22))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggle()
        self.checkBox.stateChanged.connect(self.changeInput)
        
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(680, 340, 121, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.controlTimer)
        
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(680, 70, 121, 16))
        self.label.setObjectName("label")
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(680, 190, 121, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(680, 130, 121, 16))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(680, 240, 121, 22))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QRect(10, 380, 800, 22))
        self.label_5.setObjectName("label_5")
        
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(680, 30, 121, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(680, 90, 121, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 626, 22))
        self.menubar.setObjectName("menubar")
        
        self.menuHideFace = QMenu(self.menubar)
        self.menuHideFace.setObjectName("menuHideFace")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHideFace.menuAction())

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
        self.face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt2.xml')
        if self.face_cascade.empty():
            QMessageBox.information(self.centralwidget, "Error Loading cascade classifier" , "Unable to load the face	cascade classifier xml file")
            sys.exit()

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.detectFaces)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
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
        # self.pushButton.clicked.connect(self.face_recognition)
        self.horizontalSlider.valueChanged.connect(self.v_change)

    def changeInput(self, state):
        if state == Qt.Checked:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
            self.videosource = 0

    def FileBrowse(self):
        filePath = QFileDialog.getOpenFileName(filter="Video File(*.mp4)")
        print(filePath[0])
        self.videosource = filePath[0]
        # fileHandle = open(filePath)
        
    def FolderBrowse(self):
        folderPath = QFileDialog.getExistingDirectory()
        self.videoout = folderPath
        
    def v_change(self):
        value = self.horizontalSlider.value()
        value = int(( len(prime) / 100 ) * value)
        self.label_4.setText(str(prime[value]))
        

        
        
    def detectFaces(self):
        # read frame from video capture
        ret, frame = self.cap.read()
        
        # resize frame image
        

        # convert frame to GRAY format
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        accuracy_val = self.doubleSpinBox_2.value()
        # detect rect faces
        face_rects = self.face_cascade.detectMultiScale(gray, accuracy_val, 5)
        value = self.horizontalSlider.value()
        value = int(( len(prime) / 100 ) * value)
        # for all detected faces
        for (x, y, w, h) in face_rects:
            # draw green rect on face
            sub_face = frame[y:y+h, x:x+w]
            
            sub_face = cv2.GaussianBlur(sub_face,(prime[value], prime[value]), 30)
            

            frame[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # convert frame to RGB format
        self.out.write(frame)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        scaling_factor = 0.5
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        # get frame infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from RGB frame
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # show frame in img_label
        self.image_label.setPixmap(QPixmap.fromImage(qImg))
        
        
    def controlTimer(self):

        if not self.timer.isActive():
            if not self.videoout:
                QMessageBox.information(self.centralwidget, "Error Choosing directory" , "Please choose the correct path to save video")
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
                self.out = cv2.VideoWriter(outname, 0x7634706d, 10, (int(self.cap.get(3)), int(self.cap.get(4))))


                self.pushButton.setText("Stop")

        else:

            self.timer.stop()

            self.cap.release()
            self.out.release()
            self.pushButton.setText("Start")
        

if __name__ == "__main__":
    import sys
    import platform
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
