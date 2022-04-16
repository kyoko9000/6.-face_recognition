import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from NewTest import Ui_MainWindow

import cv2
import face_recognition

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai báo nút ấn chạy
        self.uic.Start_Button.clicked.connect(self.openfiles)
        # khai báo nút chọn ảnh trên máy tính
        self.uic.Browser_button.clicked.connect(self.browserfuntion)

    def browserfuntion(self):
        #********* A1:tạo đường truyền files hình ********
        # tìm đường truyền file hình
        link = QFileDialog.getOpenFileName(filter='*.jpg *.jpeg *.png ')
        # hiện đường truyền file hình lên trên lineEdit
        self.uic.line_Edit.setText(link[0])
        # lấy link trên cửa sổ lineEdit
        linkA = self.uic.line_Edit.text()

        # ******** A2:đánh dấu khuông mặt = hình vuông ********
        # giúp biến hoạt động giữ các def
        global image_1
        # mở ảnh lên bằng CV2 với đường truền mục A1
        image_1 = cv2.imread(linkA)
        # chuyển ảnh vừa có được thành màu xám
        image_2 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
        # Dò tìm vị trí khuôn mặt để tìm ra (top, right, bottom, left)
        point = face_recognition.face_locations(image_2)
        # vẽ hình vuông lên khuôn mặt (top, right, bottom, left)
        for (top, right, bottom, left) in point:
            cv2.rectangle(image_1, (right, top), (left, bottom), (0, 255, 0), 3)

    def openfiles(self):
        #******A3: chuyển hình từ CV2 thành Pyqt5 *******
        # lấy hình từ A2 sau khi đã vẽ hình chữ nhật lên mặt
        image = image_1
        # khai báo kích thước hình ảnh
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        # chuyển đổi ảnh CV2 thành Pyqt5
        image = QtGui.QImage(image.data, width, height, bytesPerLine,
                                  QtGui.QImage.Format_RGB888).rgbSwapped()
        # trình diễn ảnh Pyqt5 lên màn hình
        self.uic.Screen.setPixmap(QtGui.QPixmap.fromImage(image))

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())