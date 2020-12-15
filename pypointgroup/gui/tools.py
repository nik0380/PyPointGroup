from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import os.path as pt

def TryExcept(target):

    def __do_target(self):
        try:
            target(self)
        except Exception as ex:
            QMessageBox.critical(self, 'Error', str(ex), QMessageBox.Ok)

    return __do_target

def GetIconPath(image_file:str=None):

    if image_file:
        return pt.join(*pt.split(pt.dirname(__file__))[:-1], "img", image_file)
    else:
        return pt.join(*pt.split(pt.dirname(__file__))[:-1], "img")

def LoadIcon(icon_file:str):
    return QIcon(GetIconPath(icon_file))