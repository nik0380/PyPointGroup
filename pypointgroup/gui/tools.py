from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import os.path as pt
import sys

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

def CreateShortCuts(parent):

    try:
        from pyshortcuts import make_shortcut
    except:
        raise Exception("The system is missing package PyShortCuts. Please install it and try again: pip install pyshortcuts")

    bindir = 'bin'
    name = 'pypointgroup'
    if sys.platform.startswith('win'):
        bindir = 'Scripts'
        name = name + '.exe'
        run_path = pt.join(sys.prefix, bindir, name)
    else:
        home = pt.expanduser("~")
        run_path = pt.join(home, ".local", "bin", name)


    if not pt.exists(run_path):
        # print("Path ", run_path, " is not exist!")
        p_path, _ = pt.split(pt.dirname(__file__))
        p_path, _ = pt.split(p_path)
        run_path = pt.join(p_path, "pypointgroup.py")

    if pt.exists(run_path):
        print('[OK!]')
        QMessageBox.information(parent, 'Creating shortcuts', "OK", QMessageBox.Ok)

        make_shortcut(script=run_path, name='PyPointGroup', icon=GetIconPath('Icon.ico'),
                          desktop=True, startmenu=True, terminal=False)

        QMessageBox.information(parent, 'Creating shortcuts',
                                "Shortcuts have been successfully created!", QMessageBox.Ok)
    else:
        raise Exception("Can't create shortcuts. Start script not found! [%s]" % run_path)