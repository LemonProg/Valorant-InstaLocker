from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl 
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import pyautogui
import keyboard
import time

Agents = [
    "Jett", "Raze", "Breach", "Omen", "Brimstone", "Phoenix", "Sage", "Sova", "Viper", 
    "Cypher", "Reyna", "Killjoy", "Skye", "Yoru", "Astra", "KAY/O", "Chamber", "Neon", "Fade"
]


agentChoose = "empty"

# Position of 1440x1080 Agents/Confirm Button
def StretchedAgentPick():
    lockbtn = 724, 819
    
    #Agents coordinates
    astra = 322, 911
    breach = 411, 911
    brimstone = 507, 911
    chamber = 592, 911
    cypher = 660, 911
    fade = 760, 911
    jett = 842, 911
    kayo = 920, 911
    killjoy = 995, 911
    neon = 1090, 911
    omen = 333, 1000
    phoenix = 418, 1000
    raze = 528, 1000
    reyna = 590, 1000
    sage = 646, 1000
    skye = 750, 1000
    sova = 810, 1000
    viper = 920, 1000
    yoru = 990, 1000
    
    if agentChoose == Agents[0]:
        pyautogui.moveTo(jett)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[1]:
        pyautogui.moveTo(raze)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[2]:
        pyautogui.moveTo(breach)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[3]:
        pyautogui.moveTo(omen)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[4]:
        pyautogui.moveTo(brimstone)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[5]:
        pyautogui.moveTo(phoenix)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[6]:
        pyautogui.moveTo(sage)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[7]:
        pyautogui.moveTo(sova)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[8]:
        pyautogui.moveTo(viper)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[9]:
        pyautogui.moveTo(cypher)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[10]:
        pyautogui.moveTo(reyna)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[11]:
        pyautogui.moveTo(killjoy)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[12]:
        pyautogui.moveTo(skye)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[13]:
        pyautogui.moveTo(yoru)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[14]:
        pyautogui.moveTo(astra)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[15]:
        pyautogui.moveTo(kayo)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[16]:
        pyautogui.moveTo(chamber)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[17]:
        pyautogui.moveTo(neon)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[18]:
        pyautogui.moveTo(fade)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()

# Position of 1920x1080 Agents/Confirm Button
def NotStretchedAgentPick(): 
        lockbtn = 930, 810
        
        #Agents coordinates
        astra = 561, 911
        breach = 647, 911
        brimstone = 733, 911
        chamber = 821, 911
        cypher = 898, 911
        fade = 991, 911
        jett = 1073, 911
        kayo = 1167, 911
        killjoy = 1234, 911
        neon = 1319, 911
        omen = 554, 980
        phoenix = 647, 980
        raze = 737, 980
        reyna = 820, 980
        sage = 902, 980
        skye = 982, 980
        sova = 1072, 980
        viper = 1154, 980
        yoru = 1249, 980
        
        if agentChoose == Agents[0]:
            pyautogui.moveTo(jett)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[1]:
            pyautogui.moveTo(raze)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[2]:
            pyautogui.moveTo(breach)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[3]:
            pyautogui.moveTo(omen)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[4]:
            pyautogui.moveTo(brimstone)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[5]:
            pyautogui.moveTo(phoenix)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[6]:
            pyautogui.moveTo(sage)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[7]:
            pyautogui.moveTo(sova)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[8]:
            pyautogui.moveTo(viper)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[9]:
            pyautogui.moveTo(cypher)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[10]:
            pyautogui.moveTo(reyna)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[11]:
            pyautogui.moveTo(killjoy)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[12]:
            pyautogui.moveTo(skye)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[13]:
            pyautogui.moveTo(yoru)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[14]:
            pyautogui.moveTo(astra)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[15]:
            pyautogui.moveTo(kayo)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[16]:
            pyautogui.moveTo(chamber)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[17]:
            pyautogui.moveTo(neon)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()
        if agentChoose == Agents[18]:
            pyautogui.moveTo(fade)
            pyautogui.click()
            pyautogui.moveTo(lockbtn)
            pyautogui.click()

# GUI, you don't have to touch it
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(516, 423)
        MainWindow.setFixedSize(516, 426)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 261, 61))
        font = QtGui.QFont()
        font.setFamily("VALORANT")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 141, 21))
        font = QtGui.QFont()
        font.setFamily("VALORANT")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.resolutionLabel = QtWidgets.QLabel(self.centralwidget)
        self.resolutionLabel.setEnabled(True)
        self.resolutionLabel.setGeometry(QtCore.QRect(-10, 130, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.resolutionLabel.setFont(font)
        self.resolutionLabel.setTextFormat(QtCore.Qt.AutoText)
        self.resolutionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.btnStretch = QtWidgets.QPushButton(self.centralwidget)
        self.btnStretch.setGeometry(QtCore.QRect(360, 130, 131, 31))
        self.btnStretch.setObjectName("btnStretch")
        self.btnNotStretch = QtWidgets.QPushButton(self.centralwidget)
        self.btnNotStretch.setGeometry(QtCore.QRect(200, 130, 131, 31))
        self.btnNotStretch.setObjectName("btnNotStretch")
        self.comboAgents = QtWidgets.QComboBox(self.centralwidget)
        self.comboAgents.setGeometry(QtCore.QRect(170, 230, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboAgents.setFont(font)
        self.comboAgents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboAgents.setEditable(True)
        self.comboAgents.setObjectName("comboAgents")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.comboAgents.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-23, 170, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 100, 621, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.agentLabel = QtWidgets.QLabel(self.centralwidget)
        self.agentLabel.setEnabled(True)
        self.agentLabel.setGeometry(QtCore.QRect(150, 200, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.agentLabel.setFont(font)
        self.agentLabel.setTextFormat(QtCore.Qt.AutoText)
        self.agentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.agentLabel.setObjectName("agentLabel")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-10, 300, 621, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.agentBtn = QtWidgets.QPushButton(self.centralwidget)
        self.agentBtn.setGeometry(QtCore.QRect(220, 270, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.agentBtn.setFont(font)
        self.agentBtn.setObjectName("agentBtn")
        self.f2Label = QtWidgets.QLabel(self.centralwidget)
        self.f2Label.setGeometry(QtCore.QRect(56, 330, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.f2Label.setFont(font)
        self.f2Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.f2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.f2Label.setObjectName("f2Label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.comboAgents.setEditable(False)
        
        self.agentBtn.clicked.connect(self.AgentButtonPressed)
        self.btnNotStretch.clicked.connect(self.ifnotStretched)
        self.btnStretch.clicked.connect(self.ifStretched)
    
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "InstaLocker"))
        self.label.setText(_translate("MainWindow", "vAlorant"))
        self.label_2.setText(_translate("MainWindow", "INSTalocker"))
        self.resolutionLabel.setText(_translate("MainWindow", "Select your resolution :"))
        self.btnStretch.setText(_translate("MainWindow", "1440x1080"))
        self.btnNotStretch.setText(_translate("MainWindow", "1920x1080"))
        self.comboAgents.setCurrentText(_translate("MainWindow", "Jett"))
        self.comboAgents.setItemText(0, _translate("MainWindow", "Jett"))
        self.comboAgents.setItemText(1, _translate("MainWindow", "Raze"))
        self.comboAgents.setItemText(2, _translate("MainWindow", "Breach"))
        self.comboAgents.setItemText(3, _translate("MainWindow", "Omen"))
        self.comboAgents.setItemText(4, _translate("MainWindow", "Brimstone"))
        self.comboAgents.setItemText(5, _translate("MainWindow", "Phoenix"))
        self.comboAgents.setItemText(6, _translate("MainWindow", "Sage"))
        self.comboAgents.setItemText(7, _translate("MainWindow", "Sova"))
        self.comboAgents.setItemText(8, _translate("MainWindow", "Viper"))
        self.comboAgents.setItemText(9, _translate("MainWindow", "Cypher"))
        self.comboAgents.setItemText(10, _translate("MainWindow", "Reyna"))
        self.comboAgents.setItemText(11, _translate("MainWindow", "Killjoy"))
        self.comboAgents.setItemText(12, _translate("MainWindow", "Skye"))
        self.comboAgents.setItemText(13, _translate("MainWindow", "Yoru"))
        self.comboAgents.setItemText(14, _translate("MainWindow", "Astra"))
        self.comboAgents.setItemText(15, _translate("MainWindow", "KAY/O"))
        self.comboAgents.setItemText(16, _translate("MainWindow", "Chamber"))
        self.comboAgents.setItemText(17, _translate("MainWindow", "Neon"))
        self.comboAgents.setItemText(18, _translate("MainWindow", "Fade"))
        self.agentLabel.setText(_translate("MainWindow", "Select your Agent :"))
        self.agentBtn.setText(_translate("MainWindow", "OK"))
        self.f2Label.setText(_translate("MainWindow", "<html><head/><body><p>Press <span style=\" font-weight:600;\">F2</span> in game / Hold <span style=\" font-weight:600;\">F3</span> to exit. </p></body></html>"))
        self.player = QMediaPlayer()
        
    # When i click the 'OK' Button
    def AgentButtonPressed(self):
        self.ClickSound()
        global agentChoose 
        agentChoose = self.comboAgents.currentText()
        if notStretched == True:
            if agentChoose in Agents:
                keyboardLoop = True
                instaLoop = True
                count = 0
                keyboard.wait("F2")
                while instaLoop:
                    if count < 100:
                        NotStretchedAgentPick()
                        count =  count + 1
                        time.sleep(0.05)
                        print(count)
                        if keyboard.is_pressed('F3'):
                            keyboardLoop = False
                            instaLoop = False
                            print("Exit")
                        
                        
        if Stretched == True:
            if agentChoose in Agents:
                keyboardLoop = True
                instaLoop = True
                while keyboardLoop:
                    if keyboard.is_pressed('F2'):
                        while instaLoop:
                            StretchedAgentPick()
                            if keyboard.is_pressed('F3'):
                                keyboardLoop = False
                                instaLoop = False
                                print("Exit")
                        
    # When i click the 1920x1080 Button
    def ifnotStretched(self):
        self.ClickSound()
        global notStretched
        global Stretched
        notStretched = True
        Stretched = False
    
    # When i click the 1440x1080 Button
    def ifStretched(self):
        self.ClickSound()
        global Stretched
        global notStretched
        Stretched = True
        notStretched = False

    # The Function To play "UwU" when you click one any button in the app
    def ClickSound(self):
        ''' 
            If you want to change the sound, 
            - download any sound in "MP3"
            - Use my website to upload your sound : https://online-hoster.000webhostapp.com/ (i wrote in french but i will explain in english here)
            - Click on "Videos", add your sound, then click on "Envoyer"
            - Press "Copie" to copy it (you can lisen it as well)
            - Then replace the older by paste it in the variable "path" just under
            - That will work now !
            (sorry my website is a ugly but it work so...) 
        '''
        path = "https://online-hoster.000webhostapp.com/Images/../uploads/166197982313474472601852417475.mp3"
        url = QUrl.fromLocalFile(path)
        content = QMediaContent(url)
        
        self.player.setMedia(content)
        self.player.play()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
