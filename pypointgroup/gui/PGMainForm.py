from .ui.pgMainForm_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QImage, QIcon
from pypointgroup.core.pgroupsgen import POINT_GROUPS_GENETATORS, POINT_GROUPS_LIST
from pypointgroup.core.symmetry import Symmetry, Operator, np
from pypointgroup.gui.tools import TryExcept, LoadIcon


class PGMainForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_controls()
        self.init_events()

    @TryExcept
    def init_events(self):
        gui = self.ui
        gui.lvGroups.clicked.connect(self.OnGroupClick)
        gui.actionExit.triggered.connect(self.OnClose)
        gui.actionSave_Image.triggered.connect(self.OnSaveImage)
        gui.actionAbout_PointGroup.triggered.connect(self.OnAbout)
        gui.cbOperators.currentTextChanged.connect(self.OnChangeOperator)
        gui.bAddOperator.clicked.connect(self.OnAddOperator)
        gui.bGenGroup.clicked.connect(self.OnGenerateClick)

    @TryExcept
    def init_controls(self):

        self.setWindowTitle('PointGroup')
        icon = LoadIcon('Icon.ico')
        self.setWindowIcon(icon)

        gui = self.ui
        gui.lvGroups.addItems(POINT_GROUPS_LIST)

        self.sym = Symmetry()
        gui.cbOperators.addItems(self.sym.keys())

        self.QM = (
            (gui.tbQ11, gui.tbQ12, gui.tbQ13),
            (gui.tbQ21, gui.tbQ22, gui.tbQ23),
            (gui.tbQ31, gui.tbQ32, gui.tbQ33),
        )

        gui.lvOperators.setUI(gui)

        gui.tabWidget.setCurrentIndex(0)


    @TryExcept
    def OnGroupClick(self):

        gui = self.ui
        ix = gui.lvGroups.currentIndex()
        if ix:
            i = ix.row()
            ng, g = self.sym.GenGroup(POINT_GROUPS_GENETATORS[i])
            gui.glView.setPointGroup(ng)

    def OnClose(self):
        self.close()

    @TryExcept
    def OnSaveImage(self):
        img = self.ui.glView.grabFramebuffer()
        path, fl = QFileDialog.getSaveFileName(self,
                    "Save Image", filter='JPG files (*.jpg);;All files (*.*)')
        if path:
            img.save(path)

    def OnAbout(self):
        QMessageBox.about(self, "About PointGroup",
                          'PointGroup v. 2.0\n(C) 2020. Nikolay V. Somov\ne-mail: somov@phys.unn.ru')

    @TryExcept
    def OnChangeOperator(self):
        gui = self.ui
        opr = gui.cbOperators.currentText()
        q = self.sym.GetOperator(opr)

        gui.tbOperName.setText(q.name)

        for i, row in enumerate(self.QM):
            for j, tb in enumerate(row):
                tb.setText(str(q.m[i,j]))

    @TryExcept
    def OnAddOperator(self):
        gui = self.ui
        m = [[int(tb.text()) for tb in row] for row in self.QM]
        opr = Operator(gui.tbOperName.text(), np.array(m))
        gui.lvOperators.addOperator(opr)

    @TryExcept
    def OnGenerateClick(self):
        gui = self.ui
        ng, g = self.sym.GenGroup(gui.lvOperators.getOperators())
        gui.glView.setPointGroup(ng)