from OpenGL.GL import *
from pypointgroup.gl._gconsts import *
from OpenGL.GLU import *
from PyQt5.Qt import QImage
from PyQt5.QtOpenGL import QGLWidget
import numpy as np
import os.path as pt
from pypointgroup.gui.tools import GetIconPath


def glRotate(Angle, axe):
     glRotated(Angle, *axe)


class GraphicsBuilder:
    
    IMAGE_PATH = None
    
    def __init__(self) -> None:
        self.flag:bool = True
        self.Gex:bool = False
        self.textures = dict()
        self.LoadTextures()

    def _load_texture(self, file, id):

        path = pt.join(self.IMAGE_PATH, file)     
        img = QImage()
        if img.load(path):
            self.textures[id] = QGLWidget.convertToGLFormat(img)
            print(f'Texture {path} loaded...[OK]')
        else:
            print(f'Texture {path} loaded...[FAIL]')


    def LoadTextures(self):
        self.flag = True
        self.IMAGE_PATH = GetIconPath()

        glEnable(GL_TEXTURE_2D)
        self.tex = glGenTextures(1)

        self._load_texture('2.bmp', a_2)
        self._load_texture('3.bmp', a_3)
        self._load_texture('4.bmp', a_4)
        self._load_texture('6.bmp', a_6)
        self._load_texture('4i.bmp', a_4i)
        self._load_texture('3i.bmp', a_3i)
        self._load_texture('6i.bmp', a_6i)

        self._load_texture('2SP.bmp', a_2sg)
        self._load_texture('21SPv.bmp', a_21sgv)
        self._load_texture('21SPh.bmp', a_21sgh)

        self._load_texture('m.bmp',  m_m)
        self._load_texture('ma.bmp', m_a)
        self._load_texture('mb.bmp', m_b)
        self._load_texture('md.bmp', m_d)

    def GetCub(self, x,y,z,a):

        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, Axies4_Color)
        a = a / 2
        glBegin(GL_QUADS)
        glNormal3f(-1, 0, 0)
        glTexCoord2f(0, 0)
        glVertex3f(x + a, y - a, z + a)
        glTexCoord2f(1, 0)
        glVertex3f(x + a, y + a, z + a)
        glTexCoord2f(1, 1)
        glVertex3f(x + a, y + a, z - a)
        glTexCoord2f(0, 1)
        glVertex3f(x + a, y - a, z - a)

        glNormal3f(-1, 0, 0)
        glTexCoord2f(0, 0)
        glVertex3f(x - a, y - a, z + a)
        glTexCoord2f(1, 0)
        glVertex3f(x - a, y + a, z + a)
        glTexCoord2f(1, 1)
        glVertex3f(x - a, y + a, z - a)
        glTexCoord2f(0, 1)
        glVertex3f(x - a, y - a, z - a)

        glNormal3f(0, -1, 0)
        glTexCoord2f(0, 0)
        glVertex3f(x + a, y + a, z + a)
        glTexCoord2f(1, 0)
        glVertex3f(x - a, y + a, z + a)
        glTexCoord2f(1, 1)
        glVertex3f(x - a, y + a, z - a)
        glTexCoord2f(0, 1)
        glVertex3f(x + a, y + a, z - a)

        glNormal3f(0, -1, 0)
        glTexCoord2f(0, 0)
        glVertex3f(x + a, y - a, z + a)
        glTexCoord2f(1, 0)
        glVertex3f(x - a, y - a, z + a)
        glTexCoord2f(1, 1)
        glVertex3f(x - a, y - a, z - a)
        glTexCoord2f(0, 1)
        glVertex3f(x + a, y - a, z - a)

        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(x + a, y - a, z + a)
        glTexCoord2f(1, 0)
        glVertex3f(x + a, y + a, z + a)
        glTexCoord2f(1, 1)
        glVertex3f(x - a, y + a, z + a)
        glTexCoord2f(0, 1)
        glVertex3f(x - a, y - a, z + a)

        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(x + a, y - a, z - a)
        glTexCoord2f(1, 0)
        glVertex3f(x + a, y + a, z - a)
        glTexCoord2f(1, 1)
        glVertex3f(x - a, y + a, z - a)
        glTexCoord2f(0, 1)
        glVertex3f(x - a, y - a, z - a)

        glEnd()

    def GetInvers(self):
        q1 = gluNewQuadric()
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, Invers_Color)
        gluSphere(q1, SizeAxis, 10, 10)

    def GetAxis(self, Orientation, TypAxe):

        glPushMatrix()
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, m_Color)

        if (TypAxe==a_3) or (TypAxe==a_3i):
            if Orientation == e_y: glRotated(90, 1, 0, 0)
            elif Orientation == e_x: glRotated(90, 0, 1, 0)
            elif Orientation == e_xy: glRotated(90, 1, 1, 0)
            elif Orientation == e_cub_1: glRotated(54, 1, 1, 0)
            elif Orientation == e_cub_2: glRotated(-54, 1, 1, 0)
            elif Orientation == e_cub_3: glRotated(54, -1, 1, 0)
            elif Orientation == e_cub_4: glRotated(-54, -1, 1, 0)
            elif Orientation == e__xy: glRotated(90, -1,1,0)
            elif Orientation == e_x_hex: glRotate(90, Axe_y)
            elif Orientation == e_y_hex: glRotate(90, Axe_u)
            elif Orientation == e_xy_Hex: glRotate(90, Axe__u)

            elif Orientation == e__xy_Hex: glRotate(90, Axe_x)
            elif Orientation == e_xy__Hex: glRotate(90, Axe_u2)
            elif Orientation == e__xy__Hex: glRotate(90, Axe_u3)
        else:
            if Orientation == e_y: glRotated(90, 1, 0, 0)
            elif Orientation == e_x: glRotated(90, 0, 1, 0)
            elif Orientation == e_xy: glRotated(90, 1, 1, 0)
            elif Orientation == e_cub_1: glRotated(45, 1, 0, 0)
            elif Orientation == e_cub_2: glRotated(-45, 1, 0, 0)
            elif Orientation == e_cub_3: glRotated(45, 0, 1, 0)
            elif Orientation == e_cub_4: glRotated(-45, 0, 1, 0)
            elif Orientation == e__xy: glRotated(90, -1,1,0)
            elif Orientation == e_x_hex: glRotate(90, Axe_x)
            elif Orientation == e_y_hex: glRotate(90, Axe_u2)
            elif Orientation == e_xy_Hex: glRotate(90, Axe_u3)

            elif Orientation == e__xy_Hex: glRotate(90, Axe_y)
            elif Orientation == e_xy__Hex: glRotate(90, Axe_u)
            elif Orientation == e__xy__Hex: glRotate(90, Axe__u)

        glBegin(GL_LINES)
        glVertex3f(0, 0, LenAxis)
        glVertex3f(0, 0, -LenAxis)
        glEnd()
        self.GetAxisSymbol(0, 0, LenAxis, TypAxe)
        self.GetAxisSymbol(0, 0, -LenAxis, TypAxe)
        glPopMatrix()


    def GetAxisSymbol(self, x,y,z, TypAxe):
        self.SetTexture(TypAxe)
        self.GetCub(x, y, z, SizeAxis)


    def Getm(self, AxiTipe):
        self.GetDisk(RadiusSpher, 30, AxiTipe)

    def GetDisk(self, R, n, Orientation):

        glPushMatrix()
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, m_Color)

        if Orientation == e_y: glRotated(90, 1, 0, 0)
        elif Orientation == e_x: glRotated(90, 0, 1, 0)
        elif Orientation == e_xy: glRotated(90, 1, 1, 0)
        elif Orientation == e_cub_1: glRotated(45, 1, 0, 0)
        elif Orientation == e_cub_2: glRotated(-45, 1, 0, 0)
        elif Orientation == e_cub_3: glRotated(45, 0, 1, 0)
        elif Orientation == e_cub_4: glRotated(-45, 0, 1, 0)
        elif Orientation == e__xy: glRotate(90, Axe__xy)

        elif Orientation == e_x_hex: glRotate(90, Axe_y)
        elif Orientation == e_y_hex: glRotate(90, Axe_u)
        elif Orientation == e_xy_Hex: glRotate(90, Axe__u)#

        elif Orientation == e__xy_Hex: glRotate(90, Axe_x)
        elif Orientation == e_xy__Hex: glRotate(90, Axe_u3) #
        elif Orientation == e__xy__Hex: glRotate(90, Axe_u2)

        glBegin(GL_POLYGON)
        glNormal3f(0, 0, -1)
        ph = np.linspace(0, 2*np.pi, n)
        X = R * np.sin(ph)
        Y = R * np.cos(ph)
        z = 0
        for x,y in zip(X,Y):
            glVertex3f(x, y, z)
        glEnd()
        glPopMatrix()

    def PointGroup(self, oList):

        self.Selector(oList)

        for opr in oList:
            if opr == '2Z':  self.GetAxis(e_z, a_2)
            elif opr == '2X':  self.GetAxis(e_x, a_2)
            elif opr == '2Y': self.GetAxis(e_y, a_2)
            elif opr == '2Y Hex':  self.GetAxis(e_y_hex, a_2)
            elif opr == '2X Hex': self.GetAxis(e_x_hex, a_2)
            elif opr == '2XY':
                if self.Gex : 
                    self.GetAxis(e__xy_Hex, a_2)
                else:
                    self.GetAxis(e_xy, a_2)

            elif opr == '2U' : self.GetAxis(e_y_hex, a_2)

            elif opr == '2X-Y' : self.GetAxis(e_xy__Hex, a_2)
            elif opr == '2-XY' : self.GetAxis(e__xy__Hex, a_2)

            elif opr == '2-X-Y':
                if self.Gex:
                    self.GetAxis(e_xy_Hex, a_2)
                else:
                    self.GetAxis(e__xy, a_2)

            elif opr == '2 Cub1' : self.GetAxis(e_cub_1, a_2)
            elif opr == '2 Cub2' : self.GetAxis(e_cub_2, a_2)
            elif opr == '2 Cub3' : self.GetAxis(e_cub_3, a_2)
            elif opr == '2 Cub4' : self.GetAxis(e_cub_4, a_2)

            elif opr == '3Z' : self.GetAxis(e_z, a_3)
            elif opr == '3XYZ' : self.GetAxis(e_cub_1, a_3)
            elif opr == '3XYZ3' : self.GetAxis(e_cub_2, a_3)
            elif opr == '3XYZ2' : self.GetAxis(e_cub_3, a_3)
            elif opr == '3XYZ1' : self.GetAxis(e_cub_4, a_3)
            elif opr == '3Zi' : self.GetAxis(e_z, a_3i)

            elif opr == '3XYZ1i' : self.GetAxis(e_cub_1, a_3i)
            elif opr == '3XYZ2i' : self.GetAxis(e_cub_2, a_3i)
            elif opr == '3XYZ3i' : self.GetAxis(e_cub_3, a_3i)
            elif opr == '3XYZ4i' : self.GetAxis(e_cub_4, a_3i)

            elif opr == '4Z' : self.GetAxis(e_z, a_4)
            elif opr == '4X' : self.GetAxis(e_x, a_4)
            elif opr == '4Y' : self.GetAxis(e_y, a_4)
            elif opr == '4Zi' : self.GetAxis(e_z, a_4i)
            elif opr == '4Xi' : self.GetAxis(e_x, a_4i)
            elif opr == '4Yi' : self.GetAxis(e_y, a_4i)

            elif opr == '6Z' : self. GetAxis(e_z, a_6)
            elif opr == '6Zi' : self. GetAxis(e_z, a_6i)

            elif opr == 'MZ' : self.Getm(e_z)
            elif opr == 'MX' : self.Getm(e_x)
            elif opr == 'MY' : self.Getm(e_y)

            elif opr == 'MXY':
                if self.Gex:
                    self.Getm(e_xy_Hex)
                else:
                    self.Getm(e_xy)

            elif opr == 'M-X-Y':
                if self.Gex :
                    self.Getm(e__xy_Hex)
                else:
                    self.Getm(e__xy)
            elif opr == 'MX Hex' : self.Getm(e_x_hex)
            elif opr == 'MY Hex' : self.Getm(e_y_hex)

            elif opr == 'M Cub1' : self.Getm(e_cub_1)
            elif opr == 'M Cub2' : self.Getm(e_cub_2)
            elif opr == 'M Cub3' : self.Getm(e_cub_3)
            elif opr == 'M Cub4' : self.Getm(e_cub_4)
            elif opr == 'MU' : self.Getm(e_xy__Hex)
            elif opr == 'M-U' : self.Getm(e__xy__Hex)

            elif opr == 'IN' : self.GetInvers()


    def Selector(self, oList:list):

        kill = lambda x:oList.remove(x) if x in oList else None

        if 'TR' in oList: oList.remove('TR')
        self.Gex = False

        if '4Z' in oList:
            kill('4Zi')
            kill('2Z')

        if '4X' in oList:
            kill('2X')
            kill('4Xi')

        if '4Y' in oList:
            kill('2Y')
            kill('4Yi')

        if '4Zi' in oList: kill('2Z')
        if '4Xi' in oList: kill('2X')
        if '4Yi' in oList: kill('2Y')

        if '3Z' in oList:
            kill('3Z2')
            self.Gex = True

        if '3XYZ1i' in oList:
            kill('3XYZ')
            kill('3XYZ1')
            kill('3XYZ2')
            kill('3XYZ3')
            kill('3XYZ4')

        if '3Zi' in oList:
            kill('3Z')
            kill('6S4')
            self.Gex = True

        if '6Zi' in oList:
            self.Gex = True

        if '6Z' in oList:
            kill('6Z5')
            kill('2Z')
            kill('3Z')
            self.Gex = True

    def SetTexture(self, id:int):

        img:QImage = self.textures[id]
        bits = img.bits()
        bits.setsize(img.byteCount())
        ptr = bits.asstring()

        glBindTexture(GL_TEXTURE_2D, self.tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 64, 64, 0, GL_RGBA, GL_UNSIGNED_BYTE, ptr)

    def Draw(self, oList:list):

        #if self.flag:
        #glNewList(1, GL_COMPILE_AND_EXECUTE)
        self.PointGroup(oList)
        #glEndList()
        #self.flag = False
        #else:
        #    glCallList(1)

if __name__ == "__main__":
    obj = GraphicsBuilder()