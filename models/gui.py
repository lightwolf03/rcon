# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rconui.ui'
#
# Created: Fri Apr 12 19:47:27 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from models.const import MAPS, GAMETYPES
from models.threads import Daemon
from models.log import log
from models.connection import RconConnection


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 480))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.tab_7)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 410, 631, 31))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.verticalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.listGAMETYPES = QtGui.QComboBox(self.verticalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listGAMETYPES.sizePolicy().hasHeightForWidth())
        self.listGAMETYPES.setSizePolicy(sizePolicy)
        self.listGAMETYPES.setObjectName("listGAMETYPES")
        self.horizontalLayout_7.addWidget(self.listGAMETYPES)
        self.pushButtonCHANGEGT = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.pushButtonCHANGEGT.setObjectName("pushButtonCHANGEGT")
        self.horizontalLayout_7.addWidget(self.pushButtonCHANGEGT)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.listMAPS = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.listMAPS.setObjectName("listMAPS")
        self.horizontalLayout_4.addWidget(self.listMAPS)
        self.pushButtonCHANGEMAP = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.pushButtonCHANGEMAP.setObjectName("pushButtonCHANGEMAP")
        self.horizontalLayout_4.addWidget(self.pushButtonCHANGEMAP)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab_7)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 0, 481, 391))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tablePLAYERS = QtGui.QTableWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablePLAYERS.sizePolicy().hasHeightForWidth())
        self.tablePLAYERS.setSizePolicy(sizePolicy)
        self.tablePLAYERS.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablePLAYERS.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tablePLAYERS.setShowGrid(True)
        self.tablePLAYERS.setGridStyle(QtCore.Qt.DotLine)
        self.tablePLAYERS.setRowCount(18)
        self.tablePLAYERS.setColumnCount(5)
        self.tablePLAYERS.setObjectName("tablePLAYERS")
        self.tablePLAYERS.setColumnCount(5)
        self.tablePLAYERS.setRowCount(18)
        item = QtGui.QTableWidgetItem()
        self.tablePLAYERS.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablePLAYERS.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablePLAYERS.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablePLAYERS.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablePLAYERS.setHorizontalHeaderItem(4, item)
        self.tablePLAYERS.horizontalHeader().setDefaultSectionSize(89)
        self.tablePLAYERS.horizontalHeader().setMinimumSectionSize(40)
        self.tablePLAYERS.verticalHeader().setDefaultSectionSize(20)
        self.tablePLAYERS.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_2.addWidget(self.tablePLAYERS)
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_7)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 161, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditIP = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditIP.setObjectName("lineEditIP")
        self.verticalLayout.addWidget(self.lineEditIP)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditPORT = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPORT.setObjectName("lineEditPORT")
        self.verticalLayout.addWidget(self.lineEditPORT)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEditPSWD = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPSWD.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPSWD.setObjectName("lineEditPSWD")
        self.verticalLayout.addWidget(self.lineEditPSWD)
        self.pushButtonCONNECT = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonCONNECT.setObjectName("pushButtonCONNECT")
        self.verticalLayout.addWidget(self.pushButtonCONNECT)
        self.pushButtonDISCONNECT = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonDISCONNECT.setObjectName("pushButtonDISCONNECT")
        self.verticalLayout.addWidget(self.pushButtonDISCONNECT)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab_7)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 230, 165, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.labelMAP = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelMAP.setFont(font)
        self.labelMAP.setObjectName("labelMAP")
        self.horizontalLayout.addWidget(self.labelMAP)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.labelCOUNT = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelCOUNT.setFont(font)
        self.labelCOUNT.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCOUNT.setObjectName("labelCOUNT")
        self.horizontalLayout_2.addWidget(self.labelCOUNT)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.labelGT = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelGT.setFont(font)
        self.labelGT.setObjectName("labelGT")
        self.horizontalLayout_3.addWidget(self.labelGT)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.listWidget = QtGui.QListWidget(self.tab_8)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 181, 451))
        self.listWidget.setObjectName("listWidget")
        self.buttonKICK = QtGui.QPushButton(self.tab_8)
        self.buttonKICK.setGeometry(QtCore.QRect(190, 170, 98, 27))
        self.buttonKICK.setObjectName("buttonKICK")
        self.buttonBAN = QtGui.QPushButton(self.tab_8)
        self.buttonBAN.setGeometry(QtCore.QRect(190, 210, 98, 27))
        self.buttonBAN.setObjectName("buttonBAN")
        self.buttonSAY = QtGui.QPushButton(self.tab_8)
        self.buttonSAY.setGeometry(QtCore.QRect(190, 250, 98, 27))
        self.buttonSAY.setObjectName("buttonSAY")
        self.textEditSAY = QtGui.QTextEdit(self.tab_8)
        self.textEditSAY.setGeometry(QtCore.QRect(320, 120, 291, 211))
        self.textEditSAY.setObjectName("textEditSAY")
        self.tabWidget.addTab(self.tab_8, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "Change gt:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCHANGEGT.setText(QtGui.QApplication.translate("Form", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Change map:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCHANGEMAP.setText(QtGui.QApplication.translate("Form", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePLAYERS.setSortingEnabled(False)
        self.tablePLAYERS.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePLAYERS.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePLAYERS.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Score", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePLAYERS.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "GUID", None, QtGui.QApplication.UnicodeUTF8))
        self.tablePLAYERS.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "Ping", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCONNECT.setText(QtGui.QApplication.translate("Form", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDISCONNECT.setText(QtGui.QApplication.translate("Form", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Map:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMAP.setText(QtGui.QApplication.translate("Form", "Not connected", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Players: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCOUNT.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "/   18", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Gametype:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGT.setText(QtGui.QApplication.translate("Form", "Not connected", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("Form", "Main Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonKICK.setText(QtGui.QApplication.translate("Form", "Kick", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBAN.setText(QtGui.QApplication.translate("Form", "Ban", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSAY.setText(QtGui.QApplication.translate("Form", "Say", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QtGui.QApplication.translate("Form", "Kick/Ban Tab", None, QtGui.QApplication.UnicodeUTF8))

class MainWindow(QtGui.QWidget, Ui_Form):
    def __init__(self):
        from models.const import VARS
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyRCON MW2 v 0.0.1")
        VARS.worker.setDaemon(True)
        VARS.worker.start()
        for mp in MAPS.values():
            self.listMAPS.addItem(mp)
        for gt in GAMETYPES.values():
            self.listGAMETYPES.addItem(gt)
        ################
        self.lineEditIP.setText('192.168.0.101')
        self.lineEditPORT.setText('28960')
        self.lineEditPSWD.setText('04101963')
        ################
        self.pushButtonCONNECT.clicked.connect(lambda: self.connectRCON(self.lineEditIP.text(), self.lineEditPORT.text(), self.lineEditPSWD.text()))
        self.pushButtonDISCONNECT.clicked.connect(lambda: self.disconnectRCON())
        self.pushButtonCHANGEMAP.clicked.connect(lambda: VARS.worker.do(lambda: self.changeMap(self.listMAPS.currentText())))
        self.pushButtonCHANGEGT.clicked.connect(lambda: VARS.worker.do(lambda: self.changeGT(self.listGAMETYPES.currentText())))
        self.buttonKICK.clicked.connect(lambda: VARS.worker.do(self.kickPlayer(self.listWidget.currentItem().text())))
        self.buttonBAN.clicked.connect(lambda: VARS.worker.do(self.banPlayer(self.listWidget.currentItem().text())))
        self.buttonSAY.clicked.connect(lambda: VARS.worker.do(self.sayPlayer(self.listWidget.currentItem().text(), self.textEditSAY.toPlainText())))


    def __del__(self):
        log("PyRCON stopped")

    def connectRCON(self, ip, port, pswd):
        from models.const import VARS
        VARS.connection = RconConnection(ip, port, pswd)
        VARS.daemon = Daemon()
        VARS.daemon.setDaemon(True)
        VARS.connection.connect()
        self.lineEditIP.setEnabled(False)
        self.lineEditPORT.setEnabled(False)
        self.lineEditPSWD.setEnabled(False)
        self.pushButtonCONNECT.setEnabled(False)
        self.pushButtonDISCONNECT.setEnabled(True)
        log("socket connected, daemon started")
        VARS.daemon.start()


    def disconnectRCON(self):
        from models.const import VARS
        VARS.connection.closeConnect()
        self.lineEditIP.setEnabled(True)
        self.lineEditPORT.setEnabled(True)
        self.lineEditPSWD.setEnabled(True)
        self.pushButtonCONNECT.setEnabled(True)
        self.pushButtonDISCONNECT.setEnabled(False)
        self.labelMAP.setText("not connected")
        self.labelGT.setText("not connected")
        VARS.daemon.stop()

    def changeMap(self, mp):
        from models.const import VARS
        for k,v in MAPS.items():
            if v == mp:
                VARS.connection.send("map %s" % (k))


    def changeGT(self, gt):
        from models.const import VARS
        for k,v in GAMETYPES.items():
            if v == gt:
                VARS.connection.changeGameType(k)

    def kickPlayer(self, nick):
        from models.const import VARS
        for player in VARS.players:
            if player.name == nick:
                VARS.connection.send("clientkick %s" %  (player.num))
                print("KICK ", player.name, player.num)

    def banPlayer(self, nick):
        from models.const import VARS
        for player in VARS.players:
            if player.name == nick:
                VARS.connection.send("banClient %s" %  (player.num))
                print("BAN ", player.name, player.num)

    def sayPlayer(self, nick, text):
        from models.const import VARS
        for player in VARS.players:
            if player.name == nick:
                VARS.connection.send("tell %s %s" % (player.num, text))
        self.textEditSAY.clear()