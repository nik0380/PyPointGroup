import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu, QAction
from pypointgroup.gui.tools import TryExcept

class ContextMenu(QMenu):

    def __init__(self, parent, ui) -> None:

        from pypointgroup.gl.pgoprview import PGOperatorListView
        from pypointgroup.gui.ui.pgMainForm_ui import Ui_MainWindow

        super().__init__(parent)

        self.ui:Ui_MainWindow = ui
        self.lv:PGOperatorListView = parent

        self.init_menu()

    def init_menu(self):
        self.addAction('Remove', self.OnRemoveItem)
        self.addAction('Clear', self.OnClear)
        self.addAction('Generate Group', self.OnGenerate)

    @TryExcept
    def OnRemoveItem(self):

        ixs = self.lv.selectedIndexes()

        if ixs:
            ix = ixs[0]
            i = ix.row()
            self.lv.removeOperator(i)

    @TryExcept
    def OnClear(self):
        self.lv.clearOperators()

    @TryExcept
    def OnGenerate(self):
        self.ui.bGenGroup.click()