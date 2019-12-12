#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import Qt, QtCore, QtGui, QtWidgets

import cv2
import time
import platform
import sys

from HideFaceView import Ui_HideFaceView

prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, \
         37, 41, 43, 47, 53, 59, 61, 67, 71,  \
         73, 79, 83, 89, 97, 101, 103, 107,   \
         109, 113, 127, 131, 137, 139, 149,   \
         151, 157, 163, 167, 173, 179, ]

class HideFaceApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HideFaceView()
        self.ui.setupUi(self)
        
        self.videosource = 0
        self.videoout = '' 
        self.face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt2.xml')
        if self.face_cascade.empty():
            QtWidgets.QMessageBox.information(self.ui.centralwidget, "Error Loading cascade classifier" , "Unable to load the face cascade classifier xml file")
            sys.exit()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.detectFaces)
        self.ui.fileCheckBox.setCheckState(False)
        self.ui.blurSlider.setValue(25)
        self.ui.fileCheckBox.toggle()
        self.ui.fileCheckBox.stateChanged.connect(self.changeInput)
        self.ui.fileButton.clicked.connect(self.FileBrowse)
        self.ui.saveButton.clicked.connect(self.FolderBrowse)
        self.ui.accurancySpinBox.setValue(1.10)
        self.ui.startButton.clicked.connect(self.controlTimer)
        self.ui.blurSlider.valueChanged.connect(self.v_change)

    def changeInput(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.fileButton.setEnabled(True)
        else:
            self.ui.fileButton.setEnabled(False)
            self.videosource = 0

    def FileBrowse(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(filter="Video File(*.mp4)")
        print(filePath[0])
        self.videosource = filePath[0]
        
    def FolderBrowse(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()
        self.videoout = folderPath
        
    def v_change(self):
        value = self.ui.blurSlider.value()
        value = int(( len(prime) / 100 ) * value)
        self.ui.blurValueLabel.setText(str(prime[value]))
    
    def detectFaces(self):
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
        accuracy_val = self.ui.accurancySpinBox.value()
        face_rects = self.face_cascade.detectMultiScale(gray, accuracy_val, 3)
        value = self.ui.blurSlider.value()
        value = int(( len(prime) / 100 ) * value)
        for (x, y, w, h) in face_rects:
            x *= 4
            y *= 4
            w *= 4
            h *= 4
            sub_face = frame[y:y+h, x:x+w]
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
        self.ui.imageLabel.setPixmap(QtGui.QPixmap.fromImage(qImg))
        
    def controlTimer(self):
        if not self.timer.isActive():
            if not self.videoout:
                QtWidgets.QMessageBox.information(self.ui.centralwidget, "Error Choosing directory" , "Please choose the correct path to save video")
            else:
                self.cap = cv2.VideoCapture(self.videosource)
                self.timer.start(20)
                vout = self.videoout
                if platform.system() == 'Windows':
                    vout = vout + '\\'
                else:
                    vout = vout + '/'
                outname = vout + str(int(time.time())) + '.mp4'
                self.ui.outPathLabel.setText(outname)
                self.out = cv2.VideoWriter(outname, 0x7634706d, 20, (int(self.cap.get(3)), int(self.cap.get(4))))
                self.ui.startButton.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.out.release()
            self.ui.startButton.setText("Start")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = HideFaceApp()
    MainWindow.show()
    sys.exit(app.exec_())
    
    
# FIXME
# app crashes when video ends
# init doesnt turn off file browse button
# app chooses webcam by default while file button is active
