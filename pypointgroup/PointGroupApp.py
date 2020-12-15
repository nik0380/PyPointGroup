from pypointgroup.gui.PGMainForm import PGMainForm, LoadIcon
from PyQt5.QtWidgets import QApplication
import sys

def main():

    if sys.platform == 'win32':
        try:
            import ctypes
            myappid = 'unn.pypointgroup.viewer.1'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except:
            pass

    app = QApplication(sys.argv)
    form = PGMainForm()
    app.setWindowIcon(LoadIcon('Icon.ico'))
    form.show()
    app.exec_()

if __name__ == "__main__":

    main()