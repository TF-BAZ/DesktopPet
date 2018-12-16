import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap,QPainter,QBitmap,QCursor
import PyQt5.QtCore as QtCore


class MainWIndow(QWidget):                            #不规则窗体
    def __init__(self, parent=None):
        super(MainWIndow, self).__init__(parent)

        self.pix=QBitmap('b00.png')                        #蒙版
        self.resize(self.pix.size())
        self.move(100,100)
        self.setMask(self.pix)

        self.setWindowFlags(Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)        # 设置无边框和置顶窗口样式

    def paintEvent(self, QPaintEvent):                     #绘制窗口
        paint=QPainter(self)
        paint.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('00.png'))

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_position=event.globalPos()- self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self,event):
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPos()-self.m_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if Qt.LeftButton:
            self.m_drag=False
            self.setCursor(QCursor(Qt.ArrowCursor))
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWIndow()
    win.show()
    sys.exit(app.exec_())