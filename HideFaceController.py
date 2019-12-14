#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import Qt, QtCore, QtGui, QtWidgets # используются для отрисовки окна

import cv2 # для обработки изображения
import time # для формирования уникального имени выходного видео
import platform # для определения системы

from HideFaceView import Ui_HideFaceView # сгенерированный файл графического интерфейса

prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, \
         37, 41, 43, 47, 53, 59, 61, 67, 71,  \
         73, 79, 83, 89, 97, 101, 103, 107,   \
         109, 113, 127, 131, 137, 139, 149,   \
         151, 157, 163, 167, 173, 179, ] # список доступных для выбора простых чисел

class HideFaceApp(QtWidgets.QWidget):
    '''
        Данный класс представляет собой логику работы программы. Он включает в себя функции покадрового чтения видео,
        обработку каждого кадра. обработку нажатий пользователя, отрисовку графического интерфейса
    '''
    def __init__(self):
        super().__init__()
        self.ui = Ui_HideFaceView()
        self.ui.setupUi(self)
        self.Configure(self.ui)
        
    def Configure(self, app):
        '''
            Функция выполняет настройку программы: перевод кнопок, инициализацию значний и загрузку каскада Хаара
        '''
        self.videoSource = 0
        self.videoOut = '' 
        self.face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt2.xml')
        if self.face_cascade.empty():
            QtWidgets.QMessageBox.information(app.centralwidget, "Error Loading cascade classifier" , "Unable to load the face cascade classifier xml file")
            sys.exit()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.GetFrame)
        app.fileCheckBox.setCheckState(False)
        app.fileButton.setEnabled(False)
        app.blurSlider.setValue(25)
        app.fileCheckBox.stateChanged.connect(self.ChangeInput)
        app.fileButton.clicked.connect(self.FileBrowse)
        app.saveButton.clicked.connect(self.FolderBrowse)
        app.accurancySpinBox.setValue(1.10)
        app.startButton.clicked.connect(self.ControlTimer)
        app.blurSlider.valueChanged.connect(self.SliderChange)

    def ChangeInput(self, state):
        '''
            Обработчик чекбокса файла
        '''
        if state == QtCore.Qt.Checked:
            self.ui.fileButton.setEnabled(True)
            self.videoSource = None
        else:
            self.ui.fileButton.setEnabled(False)
            self.videoSource = 0

    def FileBrowse(self):
        '''
            Обработчик кнопки выбора входного файла
        '''
        filePath = QtWidgets.QFileDialog.getOpenFileName(filter="Video File(*.mp4)")
        print(filePath[0])
        self.videoSource = filePath[0]
        
    def FolderBrowse(self):
        '''
            Обработчик кнопки выбора выходной директории
        '''
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()
        self.videoOut = folderPath
        
    def SliderChange(self):
        '''
            Обработчик слайдера
        '''
        value = self.ui.blurSlider.value()
        value = int(( len(prime) / 100 ) * value)
        self.ui.blurValueLabel.setText(str(prime[value]))
    
    def GetFrame(self):
        '''
            Читает кадр из входного потока и вызывает обработку и сохранение кадра
        '''
        ret, frame = self.cap.read()
        if not ret:
            self.timer.stop()
            self.cap.release()
            self.out.release()
            self.ui.startButton.setText("Start")
            return
        
        self.DetectFaces(frame)
        self.ShowSaveFrame(frame)
        
    def ShowSaveFrame(self, frame):
        '''
            Сохраняет кадр в итоговый видео файл и выводит полученное изображение на экран
        '''
        self.out.write(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        scaling_factor = 640 / frame.shape[1]
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        height, width, channel = frame.shape
        step = channel * width
        qImg = QtGui.QImage(frame.data, width, height, step, QtGui.QImage.Format_RGB888)
        self.ui.imageLabel.setPixmap(QtGui.QPixmap.fromImage(qImg))
    
    def DetectFaces(self, frame):
        '''
            С помощью загруженного каскада проводит сканирование кадра и размытие лиц
        '''
        newframe = cv2.resize(frame, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA) # сжатие изображения
        accuracy_val = self.ui.accurancySpinBox.value()
        face_rects = self.face_cascade.detectMultiScale(newframe, accuracy_val, 3)
        value = self.ui.blurSlider.value()
        value = int(( len(prime) / 100 ) * value)
        for (x, y, w, h) in face_rects:
            x *= 4 # относительное увеличение координат
            y *= 4
            w *= 4
            h *= 4
            sub_face = frame[y:y+h, x:x+w] # найденное лицо
            sub_face = cv2.GaussianBlur(sub_face,(prime[value], prime[value]), 30) # размытие лица
            frame[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face # перезапись пикселей на месте лица
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # обводка зеленым цветом

    def ControlTimer(self):
        '''
            Проведение проверки видео и обработка нажатия кнопки Start
        '''
        if not self.timer.isActive():
            if not self.videoOut:
                QtWidgets.QMessageBox.information(self.ui.centralwidget, "Error Choosing directory" , "Please choose the correct path to save video")
            elif self.videoSource is None:
                QtWidgets.QMessageBox.information(self.ui.centralwidget, "Error Choosing source" , "Please choose the correct source of video")
            else:
                self.cap = cv2.VideoCapture(self.videoSource)
                self.timer.start(20)
                vout = self.videoOut
                if platform.system() == 'Windows':
                    vout = vout + '\\'
                else:
                    vout = vout + '/'
                outname = vout + str(int(time.time())) + '.mp4'
                self.ui.outPathLabel.setText(outname)
                self.out = cv2.VideoWriter(outname, 0x7634706d, 20, (int(self.cap.get(3)), int(self.cap.get(4)))) # чтение файла со скоростью 20 fps
                self.ui.startButton.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.out.release()
            self.ui.startButton.setText("Start")
