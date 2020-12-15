# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pgMainForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 708)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.glView = PGView(self.splitter)
        self.glView.setObjectName("glView")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tabGroups = QtWidgets.QWidget()
        self.tabGroups.setObjectName("tabGroups")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabGroups)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lvGroups = QtWidgets.QListWidget(self.tabGroups)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lvGroups.setFont(font)
        self.lvGroups.setObjectName("lvGroups")
        self.gridLayout_2.addWidget(self.lvGroups, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabGroups, "")
        self.tabOperators = QtWidgets.QWidget()
        self.tabOperators.setObjectName("tabOperators")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabOperators)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lvOperators = PGOperatorListView(self.tabOperators)
        self.lvOperators.setMinimumSize(QtCore.QSize(0, 191))
        self.lvOperators.setObjectName("lvOperators")
        self.verticalLayout_4.addWidget(self.lvOperators)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbOperators = QtWidgets.QComboBox(self.tabOperators)
        self.cbOperators.setObjectName("cbOperators")
        self.verticalLayout_3.addWidget(self.cbOperators)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tabOperators)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tbOperName = QtWidgets.QLineEdit(self.tabOperators)
        self.tbOperName.setObjectName("tbOperName")
        self.verticalLayout.addWidget(self.tbOperName)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tbQ11 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ11.setObjectName("tbQ11")
        self.horizontalLayout.addWidget(self.tbQ11)
        self.tbQ12 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ12.setObjectName("tbQ12")
        self.horizontalLayout.addWidget(self.tbQ12)
        self.tbQ13 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ13.setObjectName("tbQ13")
        self.horizontalLayout.addWidget(self.tbQ13)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tbQ21 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ21.setObjectName("tbQ21")
        self.horizontalLayout_2.addWidget(self.tbQ21)
        self.tbQ22 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ22.setObjectName("tbQ22")
        self.horizontalLayout_2.addWidget(self.tbQ22)
        self.tbQ23 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ23.setObjectName("tbQ23")
        self.horizontalLayout_2.addWidget(self.tbQ23)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tbQ31 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ31.setObjectName("tbQ31")
        self.horizontalLayout_3.addWidget(self.tbQ31)
        self.tbQ32 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ32.setObjectName("tbQ32")
        self.horizontalLayout_3.addWidget(self.tbQ32)
        self.tbQ33 = QtWidgets.QLineEdit(self.tabOperators)
        self.tbQ33.setObjectName("tbQ33")
        self.horizontalLayout_3.addWidget(self.tbQ33)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.bGenGroup = QtWidgets.QPushButton(self.tabOperators)
        self.bGenGroup.setEnabled(False)
        self.bGenGroup.setCheckable(False)
        self.bGenGroup.setObjectName("bGenGroup")
        self.horizontalLayout_4.addWidget(self.bGenGroup)
        self.bAddOperator = QtWidgets.QPushButton(self.tabOperators)
        self.bAddOperator.setObjectName("bAddOperator")
        self.horizontalLayout_4.addWidget(self.bAddOperator)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabOperators, "")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_PointGroup = QtWidgets.QAction(MainWindow)
        self.actionAbout_PointGroup.setObjectName("actionAbout_PointGroup")
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_PointGroup)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGroups), _translate("MainWindow", "Groups"))
        self.label.setText(_translate("MainWindow", "Operator name:"))
        self.tbOperName.setText(_translate("MainWindow", "INV"))
        self.tbQ11.setText(_translate("MainWindow", "-1"))
        self.tbQ12.setText(_translate("MainWindow", "0"))
        self.tbQ13.setText(_translate("MainWindow", "0"))
        self.tbQ21.setText(_translate("MainWindow", "0"))
        self.tbQ22.setText(_translate("MainWindow", "-1"))
        self.tbQ23.setText(_translate("MainWindow", "0"))
        self.tbQ31.setText(_translate("MainWindow", "0"))
        self.tbQ32.setText(_translate("MainWindow", "0"))
        self.tbQ33.setText(_translate("MainWindow", "-1"))
        self.bGenGroup.setText(_translate("MainWindow", "Generate"))
        self.bAddOperator.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOperators), _translate("MainWindow", "Operators"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "?"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_PointGroup.setText(_translate("MainWindow", "About PointGroup..."))
from pypointgroup.gl.pgoprview import PGOperatorListView
from pypointgroup.gl.pgview import PGView
