import typing

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QOpenGLWidget, QWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from pypointgroup.gl.gbuilder import GraphicsBuilder


class PGView(QOpenGLWidget):

    def __init__(self, parent=None) -> None:

        super().__init__(parent)
        self.x0 = 0
        self.y0 = 0
        self.dx = 0
        self.dy = 0
        self.flag = False
        self.GB = None
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.x = 0
        self.y = 0
        self.z = -5
        self.group = []

    def setPointGroup(self, group:list):

        self.group = group

        self.ax = 0
        self.ay = 0
        self.az = 0
        self.x = 0
        self.y = 0
        self.z = -5
        self.flag = False
        self.repaint()


    def paintGL(self) -> None:

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0.8, 1)
        if not self.flag:
            glLoadIdentity()
            glTranslatef(self.x, self.y, self.z)
            glRotated(-self.ay, 1, 0, 0)
            glRotated(self.ax, 0, 1, 0)
            glRotated(self.az, 0, 0, 1)
            self.GB.Draw(self.group)
            glFinish()

    def initializeGL(self) -> None:

        coor = [0.0, 0.0, 1.0, 1.0]
        dirt = [0.0, 0.0, -1.0, 1.0]

        glEnable(GL_DEPTH_TEST) # разрешаем    тест  глубины
        glEnable(GL_LIGHTING) # разрешаем  работу  с  освещенностью
        glLightfv(GL_LIGHT0, GL_POSITION, coor)
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, dirt)
        glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, 1)
        glEnable(GL_LIGHT0) # включаем   источник  света    0

        self.GB = GraphicsBuilder()


    def resizeGL(self, w: int, h: int) -> None:

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(20.0, w / h, 1, 20.0)
        glViewport(0, 0, w, h)
        glMatrixMode(GL_MODELVIEW)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0.8, 1)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:

        x = a0.x()
        y = a0.y()

        self.dx = x - self.x0
        self.dy = y - self.y0
        self.x0 = x
        self.y0 = y

        if a0.buttons() == QtCore.Qt.LeftButton:

            self.ax = self.ax + self.dx
            self.ay = self.ay - self.dy
            if self.ax > 360: self.ax = self.ax-360
            if self.ax < 0: self.ax = self.ax+360

            if self.ay > 360: self.ay = self.ay-360
            if self.ay < 0: self.ay = self.ay+360

            self.repaint()

        elif a0.buttons() == QtCore.Qt.RightButton:

            self.x = self.x + self.dx / 300
            self.z = self.z - self.dy / 100

            self.repaint()





