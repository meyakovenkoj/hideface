# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hideface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HideFaceView(object):
    def setupUi(self, HideFaceView):
        HideFaceView.setObjectName("HideFaceView")
        HideFaceView.resize(820, 412)
        HideFaceView.setFixedSize(QtCore.QSize(820, 412))
        self.centralwidget = QtWidgets.QWidget(HideFaceView)
        self.centralwidget.setGeometry(QtCore.QRect(10, 0, 820, 412))
        self.centralwidget.setObjectName("centralwidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(10, 10, 640, 360))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageLabel.setLineWidth(2)
        self.imageLabel.setMidLineWidth(0)
        self.imageLabel.setObjectName("imageLabel")
        self.accurancySpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.accurancySpinBox.setGeometry(QtCore.QRect(680, 150, 121, 22))
        self.accurancySpinBox.setMinimum(1.01)
        self.accurancySpinBox.setMaximum(1.99)
        self.accurancySpinBox.setSingleStep(0.01)
        self.accurancySpinBox.setObjectName("accurancySpinBox")
        self.blurSlider = QtWidgets.QSlider(self.centralwidget)
        self.blurSlider.setGeometry(QtCore.QRect(680, 210, 121, 22))
        self.blurSlider.setMinimum(1)
        self.blurSlider.setMaximum(99)
        self.blurSlider.setProperty("value", 25)
        self.blurSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blurSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.blurSlider.setTickInterval(10)
        self.blurSlider.setObjectName("blurSlider")
        self.fileCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.fileCheckBox.setGeometry(QtCore.QRect(680, 10, 121, 20))
        self.fileCheckBox.setObjectName("fileCheckBox")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(680, 340, 121, 32))
        self.startButton.setObjectName("startButton")
        self.pathSaveLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathSaveLabel.setGeometry(QtCore.QRect(680, 70, 81, 16))
        self.pathSaveLabel.setObjectName("pathSaveLabel")
        self.blurLabel = QtWidgets.QLabel(self.centralwidget)
        self.blurLabel.setGeometry(QtCore.QRect(680, 190, 121, 16))
        self.blurLabel.setObjectName("blurLabel")
        self.scaleLabel = QtWidgets.QLabel(self.centralwidget)
        self.scaleLabel.setGeometry(QtCore.QRect(680, 130, 121, 16))
        self.scaleLabel.setObjectName("scaleLabel")
        self.blurValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.blurValueLabel.setGeometry(QtCore.QRect(680, 240, 121, 22))
        self.blurValueLabel.setObjectName("blurValueLabel")
        self.outPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.outPathLabel.setGeometry(QtCore.QRect(69, 380, 731, 22))
        self.outPathLabel.setObjectName("outPathLabel")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(680, 30, 121, 25))
        self.fileButton.setObjectName("fileButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(680, 90, 121, 25))
        self.saveButton.setObjectName("saveButton")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 380, 51, 22))
        self.outputLabel.setObjectName("outputLabel")

        self.retranslateUi(HideFaceView)
        QtCore.QMetaObject.connectSlotsByName(HideFaceView)

    def retranslateUi(self, HideFaceView):
        _translate = QtCore.QCoreApplication.translate
        HideFaceView.setWindowTitle(_translate("HideFaceView", "HideFace"))
        self.fileCheckBox.setText(_translate("HideFaceView", "File"))
        self.startButton.setText(_translate("HideFaceView", "Start"))
        self.pathSaveLabel.setText(_translate("HideFaceView", "Path to save"))
        self.blurLabel.setText(_translate("HideFaceView", "Blur"))
        self.scaleLabel.setText(_translate("HideFaceView", "Scale Factor"))
        self.blurValueLabel.setText(_translate("HideFaceView", "31"))
        self.outPathLabel.setText(_translate("HideFaceView", "..."))
        self.fileButton.setText(_translate("HideFaceView", "Browse"))
        self.saveButton.setText(_translate("HideFaceView", "Browse"))
        self.outputLabel.setText(_translate("HideFaceView", "Output:"))
