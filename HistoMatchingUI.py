# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistoMatching.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy)
        self.Save.setMinimumSize(QtCore.QSize(449, 32))
        self.Save.setMaximumSize(QtCore.QSize(449, 32))
        self.Save.setObjectName("Save")
        self.gridLayout.addWidget(self.Save, 4, 1, 1, 1)
        self.imgref = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgref.sizePolicy().hasHeightForWidth())
        self.imgref.setSizePolicy(sizePolicy)
        self.imgref.setMinimumSize(QtCore.QSize(449, 32))
        self.imgref.setMaximumSize(QtCore.QSize(449, 32))
        self.imgref.setObjectName("imgref")
        self.gridLayout.addWidget(self.imgref, 2, 0, 1, 1)
        self.processed = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processed.sizePolicy().hasHeightForWidth())
        self.processed.setSizePolicy(sizePolicy)
        self.processed.setMaximumSize(QtCore.QSize(220, 213))
        self.processed.setObjectName("processed")
        self.gridLayout.addWidget(self.processed, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Run.sizePolicy().hasHeightForWidth())
        self.Run.setSizePolicy(sizePolicy)
        self.Run.setMinimumSize(QtCore.QSize(449, 32))
        self.Run.setMaximumSize(QtCore.QSize(449, 32))
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 3, 1, 1, 1)
        self.OriginalImage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OriginalImage.sizePolicy().hasHeightForWidth())
        self.OriginalImage.setSizePolicy(sizePolicy)
        self.OriginalImage.setMaximumSize(QtCore.QSize(220, 213))
        self.OriginalImage.setScaledContents(True)
        self.OriginalImage.setObjectName("OriginalImage")
        self.gridLayout.addWidget(self.OriginalImage, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.origImage = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.origImage.sizePolicy().hasHeightForWidth())
        self.origImage.setSizePolicy(sizePolicy)
        self.origImage.setMinimumSize(QtCore.QSize(449, 32))
        self.origImage.setMaximumSize(QtCore.QSize(449, 32))
        self.origImage.setObjectName("origImage")
        self.gridLayout.addWidget(self.origImage, 3, 0, 1, 1)
        self.destination = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destination.sizePolicy().hasHeightForWidth())
        self.destination.setSizePolicy(sizePolicy)
        self.destination.setMinimumSize(QtCore.QSize(449, 32))
        self.destination.setMaximumSize(QtCore.QSize(449, 32))
        self.destination.setObjectName("destination")
        self.gridLayout.addWidget(self.destination, 4, 0, 1, 1)
        self.imageRef = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageRef.sizePolicy().hasHeightForWidth())
        self.imageRef.setSizePolicy(sizePolicy)
        self.imageRef.setMaximumSize(QtCore.QSize(220, 212))
        self.imageRef.setObjectName("imageRef")
        self.gridLayout.addWidget(self.imageRef, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.histogram = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram.sizePolicy().hasHeightForWidth())
        self.histogram.setSizePolicy(sizePolicy)
        self.histogram.setMaximumSize(QtCore.QSize(480, 192))
        self.histogram.setObjectName("histogram")
        self.gridLayout.addWidget(self.histogram, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.imgref.setText(_translate("MainWindow", "Select Reference Image"))
        self.processed.setText(_translate("MainWindow", "Processed Image"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.OriginalImage.setText(_translate("MainWindow", "Original Image"))
        self.origImage.setText(_translate("MainWindow", "Select  Target Image "))
        self.destination.setText(_translate("MainWindow", "Select Directory to Save Transformed Image"))
        self.imageRef.setText(_translate("MainWindow", "Reference Image"))

