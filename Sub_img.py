from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SubWin
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.Qt import Qt
import cv2
import SubWin_img
from datetime import datetime
import Transformation as filters

# UI for gamma with paramenter
class Sub_img(QtWidgets.QMainWindow, SubWin_img.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Sub_img, self).__init__(parent)
        self.setupUi(self)
        self.origImage.clicked.connect(self.loadImage)
        self.Run.clicked.connect(self.RunBttn)
        self.destination.clicked.connect(self.saveImage)

    def loadImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Select Image for Transformation", "","All Files (*);;Python Files (*.py)",options=options)
        if self.fileName:
            print(self.fileName)
            pixmap = QtGui.QPixmap(self.fileName)
            self.OriginalImage.setPixmap(pixmap)
            #self.resize(pixmap.width(),pixmap.height())

    def saveImage(self):
    	options = QtWidgets.QFileDialog.Options()
    	options |= QtWidgets.QFileDialog.DontUseNativeDialog
    	self.savepath = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a directory","",options =options)
    	if self.savepath:
    		print(self.savepath)

    def RunBttn(self):
        try:
            self.displayProcessedIamge()
        except:
            box=QtWidgets.QMessageBox.about(self,"Select Input Image First","Input image is not selected")
        


    def displayProcessedIamge(self):
        input_image = self.openImage()
        img=self.processImage(input_image)

        pixmap=self.covertnumpyimg(img)
        self.processed.setPixmap(pixmap)


    def processImage(self,input_image):
        self.getParameterValue()
        img=filters.Transformation().adjust_gamma(input_image,self.value)
        return img

    def openImage(self):
        input_image = cv2.imread(self.fileName, 0)
        return input_image
    
    def covertnumpyimg(self,image):
        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]
        image = QtGui.QImage(image, image.shape[1],image.shape[0], image.strides[0], QtGui.QImage.Format_Indexed8)
        image.setColorTable(gray_color_table)
        pix = QtGui.QPixmap(image)
        return pix
    
    def getParameterValue(self):
        text = self.ParameterValue.toPlainText()
        try:
            self.value = float(text)
        except:
            box=QtWidgets.QMessageBox.about(self,"Invalid number","Type a valid number")
    
    def save(self,path,image):
        output_image_name = path + "/Gamma" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        cv2.imwrite(output_image_name, image)







def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Sub_img()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()