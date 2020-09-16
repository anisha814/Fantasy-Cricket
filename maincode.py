# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maincode.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from pointscalculation import PlayerPoints
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from openteam import Ui_MainWindow as Open
from newteam import Ui_MainWindow as New
from evaluateteam import Ui_MainWindow as Evaluate

import sqlite3
fancr=sqlite3.connect("FantasyCricket.db")
curcricket=fancr.cursor()


class Ui_MainWindow(object):
     def __init__(self):
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Evaluate()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)
     def file_open (self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.pushButton.clicked.connect(self.openteam)

    
     def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()
 
     def setupUi(self, MainWindow):
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        
        self.a = [] 
        self.b = []  
        self.c = []   
        self.d = [] 
        self.list1 = []  
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 726)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 85, 255);\n"
"background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 130, 821, 47))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(85, 0, 0);\n"
"background-color: rgb(0, 255, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(85, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 821, 91))
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-color: rgb(85, 0, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 260, 821, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)#listwidget2
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)#listwidget
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 190, 401, 61))
        self.frame_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        self.radioButton.setFont(font)#radiobutton
        self.radioButton.setEnabled(False)
        self.radioButton.setAcceptDrops(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_3)
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        self.radioButton_3.setFont(font)#radiobutton3
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        self.radioButton_2.setFont(font)#rab2
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()#rab4
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(440, 180, 401, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)#menu
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 31))
        self.menubar.setObjectName("menubar")
        
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_TEAM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        
        self.actionNEW_TEAM.setFont(font)#newteam
        self.actionNEW_TEAM.setObjectName("actionNEW_TEAM")
        self.actionOPEN_TEAM = QtWidgets.QAction(MainWindow)
        self.actionNEW_TEAM.setVisible(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        
        self.actionOPEN_TEAM.setFont(font)#open
        self.actionOPEN_TEAM.setObjectName("actionOPEN_TEAM")
        self.actionSAVE_TEAM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        
        self.actionSAVE_TEAM.setFont(font)#save
        self.actionSAVE_TEAM.setObjectName("actionSAVE_TEAM")
        
        self.actionEVALUATE_TEAM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionEVALUATE_TEAM.setFont(font)#evaluate
        self.actionEVALUATE_TEAM.setObjectName("actionEVALUATE_TEAM")

        self.actionQuit = QtWidgets.QAction(MainWindow)# Quit
        self.actionQuit.setObjectName("actionQuit") 
        self.actionQuit.triggered.connect(self.quit)
        
        self.menuManage_Team.addAction(self.actionNEW_TEAM)
        self.menuManage_Team.addAction(self.actionOPEN_TEAM)
        self.menuManage_Team.addAction(self.actionSAVE_TEAM)
        self.menuManage_Team.addAction(self.actionEVALUATE_TEAM)
        self.menuManage_Team.addAction(self.actionQuit)
        self.menubar.addAction(self.menuManage_Team.menuAction())

        self.actionNEW_TEAM.triggered.connect(self.file_new)
        self.actionOPEN_TEAM.triggered.connect(self.file_open)
        self.actionSAVE_TEAM.triggered.connect(self.file_save)
        self.actionEVALUATE_TEAM.triggered.connect(self.file_evaluate)
        self.actionQuit.triggered.connect(self.quit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2)

        
        self.Stats = {}

        self.new_screen.pushButton.clicked.connect(self.namechange)

        # RADIOBUTTONS  CLICK
        self.radioButton.clicked.connect(self.load_names)
        self.radioButton_2.clicked.connect(self.load_names)
        self.radioButton_3.clicked.connect(self.load_names)
        self.radioButton_4.clicked.connect(self.load_names)
        

     def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Points available"))
        self.label_11.setText(_translate("MainWindow", "##"))
        self.label_12.setText(_translate("MainWindow", "Points used"))
        self.label_13.setText(_translate("MainWindow", "##"))
        self.label_2.setText(_translate("MainWindow", "Batsaman(BAT)"))
        self.label_3.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.label_5.setText(_translate("MainWindow", "##"))
        self.label_6.setText(_translate("MainWindow", "All Rounder"))
        self.label_8.setText(_translate("MainWindow", "Wicket Keeper"))
        self.label_9.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Your Selection"))
        self.label_7.setText(_translate("MainWindow", "##"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_3.setText(_translate("MainWindow", "BOW"))
        self.radioButton_2.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team Name :"))
        self.label_14.setText(_translate("MainWindow", "Displayed Here"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNEW_TEAM.setText(_translate("MainWindow", "NEW TEAM"))
        self.actionOPEN_TEAM.setText(_translate("MainWindow", "OPEN TEAM"))
        self.actionSAVE_TEAM.setText(_translate("MainWindow", "SAVE TEAM"))
        self.actionEVALUATE_TEAM.setText(_translate("MainWindow", "EVALUATE TEAM"))
        self.actionQuit.setText(_translate("MainWindow","Quit"))

     def file_new(self):
        self.newDialog.show()

     def namechange(self):
        teamname = self.new_screen.label_14.text()
        curcricket.execute("SELECT DISTINCT name FROM teams")
        l = curcricket.fetchall()
        for i in l:
            if i[0] == teamname:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.tname = self.new_screen.label_14.text()
            self.label_14.setText(str('    '+self.tname))
            self.newDialog.close()


     def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.label_11.setText(str(self.avail_points))
        self.label_13.setText(str(self.used_points))
        self.label_5.setText(str(self.bowlerscount))
        self.label_3.setText(str(self.batsmencount))
        self.label_7.setText(str(self.alrdscount))
        self.label_9.setText(str(self.wicketerscount))
        self.listWidget.clear()
        self.load_names()
        self.listWidget_2.clear()


     def file_save(self):
        if not self.error():  
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Critical)
             msg.setInformativeText(' Inufficient Players OR Points !!')
             msg.setWindowTitle("Fantasy Cricket")
             msg.exec_()
        elif self.error():  
             try:
                curcricket.execute("SELECT DISTINCT Name FROM Teams;")
                x = curcricket.fetchall()
                for i in x:
                    if self.label_14.text() == i[0]:   
                           print('Updating already there')
                           curcricket.execute("DELETE  FROM Teams WHERE Name='" + self.label_14.text() + "';") 
             except:
                print('error')
             for i in range(self.listWidget.count()):
                
                try:
                    #print(PlayerPoints[self.list1[i]])
                    curcricket.execute("INSERT INTO Teams (Name,Players,Value) VALUES (?,?,?)",
                    (self.label_14.text(), self.list1[i], PlayerPoints[self.list1[i]]))

                     
                except:
                    print('error in operation!')
             fancr.commit()
        else:
             print('---error in operation')

 
     def quit(self):
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Critical)
         msg.setInformativeText(' Bye Bye')
         msg.setWindowTitle("Fantasy Cricket")
         msg.exec_()
        
         sys.exit()




     def load_names(self):

          Batsman = 'BAT'
          WicketKeeper = 'WK'
          Allrounder = 'AR'
          Bowler = 'BOW'
          sql1 = "SELECT Player,Value from stats WHERE ctg = '" + Batsman + "';"
          sql2 = "SELECT Player,Value from Stats WHERE ctg = '" + WicketKeeper + "';"
          sql3 = "SELECT Player,Value from Stats WHERE ctg ='" + Allrounder + "';"
          sql4 = "SELECT Player,Value from Stats WHERE ctg = '" + Bowler + "';"

          curcricket.execute(sql1)
          x = curcricket.fetchall()
          curcricket.execute(sql4)
          y = curcricket.fetchall()
          curcricket.execute(sql3)
          z = curcricket.fetchall()
          curcricket.execute(sql2)
          w = curcricket.fetchall()

          batsmen = []
          bowlers = []
          allrounders = []
          wcktkeepers = []

          for k in x:
               batsmen.append(k[0])
               self.b.append(k[0])
               self.Stats[k[0]] = k[1]
          for k in y:
               bowlers.append(k[0])
               self.Stats[k[0]] = k[1]
               self.a.append(k[0])
          for k in w:
               wcktkeepers.append(k[0])
               self.Stats[k[0]] = k[1]
               self.d.append(k[0])
          for k in z:
               allrounders.append(k[0])
               self.Stats[k[0]] = k[1]
               self.c.append(k[0])
          for i in self.list1:
               if i in allrounders:
                    allrounders.remove(i)
               elif i in batsmen:
                    batsmen.remove(i)
               elif i in bowlers:
                    bowlers.remove(i)
               elif i in wcktkeepers:
                    wcktkeepers.remove(i)

          if self.radioButton.isChecked() == True:
               self.listWidget_2.clear()
               for i in range(len(batsmen)):
                    item = QtWidgets.QListWidgetItem(batsmen[i])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.listWidget_2.addItem(item)
          elif self.radioButton_2.isChecked() == True:
               self.listWidget_2.clear()
               for i in range(len(bowlers)):
                    item = QtWidgets.QListWidgetItem(bowlers[i])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.listWidget_2.addItem(item)
          elif self.radioButton_3.isChecked() == True:
               self.listWidget_2.clear()
               for i in range(len(allrounders)):
                    item = QtWidgets.QListWidgetItem(allrounders[i])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.listWidget_2.addItem(item)

          elif self.radioButton_4.isChecked() == True:
               self.listWidget_2.clear()
               for i in range(len(wcktkeepers)):
                    item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.listWidget_2.addItem(item)


     def removelist1(self, item):   
        self.conditions_1(item.text())
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.listWidget.addItem(item.text())
        self.totalcount = self.listWidget.count()
        self.list1.append(item.text())
        self.error()


     def conditions_1(self, cat):   
        self.avail_points -= self.Stats[cat]
        self.used_points += self.Stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.label_11.setText(str(self.avail_points))
        self.label_13.setText(str(self.used_points))
        self.label_5.setText(str(self.bowlerscount))
        self.label_3.setText(str(self.batsmencount))
        self.label_7.setText(str(self.alrdscount))
        self.label_9.setText(str(self.wicketerscount))


     def conditions_2(self, cat):   
        self.avail_points += self.Stats[cat]
        self.used_points -= self.Stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.label_11.setText(str(self.avail_points))
        self.label_13.setText(str(self.used_points))
        self.label_5.setText(str(self.bowlerscount))
        self.label_3.setText(str(self.batsmencount))
        self.label_7.setText(str(self.alrdscount))
        self.label_9.setText(str(self.wicketerscount))


     def removelist2(self, item):
        self.listWidget.takeItem(self.listWidget.row(item))
        self.listWidget_2.addItem(item.text())
        self.list1.remove(item.text())
        self.totalcount = self.listWidget.count()
        self.conditions_2(item.text())



     def openteam(self): 
        self.reset()
        teamname = self.open_screen.comboBox.currentText()
        self.label_14.setText(teamname)
        self.enablebuttons()
        curcricket.execute("SELECT Players from Teams WHERE Name= '" + teamname + "';")
        x=curcricket.fetchall()
        score=[]
        for i in x:
            curcricket.execute("SELECT Value from Stats WHERE Player='"+i[0]+"';")
            y=curcricket.fetchone()
            score.append(y[0])
        
        sum=0
        for i in score:
            sum+=i
        self.listWidget.clear()
        self.load_names()
        for i in x:
            self.listWidget.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.label_11.setText(str(self.avail_points))
        self.label_13.setText(str(self.used_points))
        self.openDialog.close()



     def enablebuttons(self):
        self.radioButton.setEnabled(True)
        self.radioButton_3.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.radioButton_4.setEnabled(True)
        
     def disablebuttons(self):
        self.radioButton.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_4.setEnabled(False)


               
     def error(self):
        msg = QMessageBox()
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            
            msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        elif self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No more than 11 players allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            return 0
        elif self.totalcount < 11 :
            return 0
        elif self.wicketerscount < 1:
            return 0
        elif self.avail_points <= -1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough points!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0

        return 1



           
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
