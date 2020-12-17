from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QMessageBox
from pypointgroup.core.Operators import Operator
from pypointgroup.gui.pgContextMenu import ContextMenu
from PyQt5.QtGui import QImage, QPixmap, QIcon, QPainter, QColor, QFont, QFontMetrics
from pypointgroup.gui.tools import TryExcept, LoadIcon


class PGOperatorListView(QListWidget):

    ICON_SIZE = 64

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.pg = list()
        self.init_control()
        self.font_size = None

    def init_control(self):
        self.setViewMode(QListWidget.IconMode)
        self.setSpacing(10)
        self.setIconSize(QSize(self.ICON_SIZE, self.ICON_SIZE))
        self.setResizeMode(QListWidget.Adjust)

    def setUI(self, ui):

        from pypointgroup.gui.ui.pgMainForm_ui import Ui_MainWindow
        self.ui: Ui_MainWindow = ui

    def addOperator(self, opr:Operator):

        self.pg.append(opr)
        ico = self.getIconOpr(opr) # LoadIcon('Icon.ico')
        item = QListWidgetItem(ico, opr.name)
        self.addItem(item)
        self.ui.bGenGroup.setEnabled(self.count() > 0)


    def removeOperator(self, index:int):
        self.pg.pop(index)
        self.takeItem(index)
        self.ui.bGenGroup.setEnabled(self.count() > 0)

    def clearOperators(self):
        self.pg.clear()
        self.clear()
        self.ui.bGenGroup.setEnabled(self.count() > 0)

    def getOperators(self):
        return self.pg

    def contextMenuEvent(self, a0: QtGui.QContextMenuEvent) -> None:
        menu = ContextMenu(self, self.ui)
        menu.exec(a0.globalPos())

    def getIconOpr(self, opr:Operator):

        bmp = QPixmap(self.ICON_SIZE,self.ICON_SIZE)
        bmp.fill(QColor('white'))
        cv = QPainter()
        cv.begin(bmp)

        cv.setPen(QColor('blue'))
        cv.drawRect(1,1,self.ICON_SIZE-2, self.ICON_SIZE-2)

        font = cv.font()
        font.setBold(True)

        if not self.font_size:

            font.setPointSize(10)
            fm = QFontMetrics(font)
            w10 = fm.width(' -1  -1  -1 ')

            font.setPointSize(12)
            fm = QFontMetrics(font)
            w12 = fm.width(' -1  -1  -1 ')

            k = (w12 - w10) / 2
            b = w10 - k*10
            s = (self.ICON_SIZE - b) / k
            self.font_size = int(s)

        font.setPointSize(self.font_size)
        cv.setFont(font)

        cv.setPen(QColor('red'))

        for i, row in enumerate(opr.m):
            cv.drawText(0, 14*(i+1)+7, " ".join(["%3d" % x for x in row]))

        cv.end()

        return QIcon(bmp)




