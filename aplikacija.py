from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush


class Gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()
        self.show()

    def initGui(self):
        self.setGeometry(0,0,1000,1000)
        self.setWindowTitle('Covid-19')
        
        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)
        
        #dodajemo sliku u pozadini
        oImage = QImage("2.jpeg")
        sImage = oImage.scaled(QSize(500,500))                   
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.licni = QLabel("LICNI PODACI", self)  
        vbox.addWidget(self.licni)

        hbox1 = QtWidgets.QHBoxLayout()
        lGodine= QLabel("Uneti broj godina: ")
        tGodine= QtWidgets.QLineEdit()
        hbox1.addWidget(lGodine)
        hbox1.addWidget(tGodine)
        vbox.addLayout(hbox1)

        self.simptomi = QLabel("SIMPTOMI", self)  
        vbox.addWidget(self.simptomi)
        self.cesti = QLabel("Najcesci simptomi",self)
        vbox.addWidget(self.cesti) 

        #temperatura
        hboxT = QtWidgets.QHBoxLayout()
        ltemp= QLabel("Temperatura: ")
        rtemp1= QtWidgets.QRadioButton("manje od 37")
        rtemp2= QtWidgets.QRadioButton("od 37 do 38")
        rtemp3= QtWidgets.QRadioButton("vise od 38")
        hboxT.addWidget(ltemp)
        hboxT.addWidget(rtemp1)
        hboxT.addWidget(rtemp2)
        hboxT.addWidget(rtemp3)
        vbox.addLayout(hboxT)
        
        #suv kasalj
        hboxSK = QtWidgets.QHBoxLayout()
        lskasalj= QLabel("Suv kasalj: ")
        rskasalj1= QtWidgets.QRadioButton("Da")
        rskasalj2= QtWidgets.QRadioButton("Ne")
        hboxSK.addWidget(lskasalj)
        hboxSK.addWidget(rskasalj1)
        hboxSK.addWidget(rskasalj2)
        vbox.addLayout(hboxSK)

        #umor
        hboxU = QtWidgets.QHBoxLayout()
        lumor= QLabel("Umor: ")
        rumor1= QtWidgets.QRadioButton("Da")
        rumor2= QtWidgets.QRadioButton("Ne")
        hboxU.addWidget(lumor)
        hboxU.addWidget(rumor1)
        hboxU.addWidget(rumor2)
        vbox.addLayout(hboxU)

        self.manje = QLabel("Manje cesti simptomi",self)
        vbox.addWidget(self.manje)

        #bol
        hboxB = QtWidgets.QHBoxLayout()
        lbol = QLabel("Bolovi u misicima: ")
        rbol1= QtWidgets.QRadioButton("Da")
        rbol2= QtWidgets.QRadioButton("Ne")
        hboxB.addWidget(lbol)
        hboxB.addWidget(rbol1)
        hboxB.addWidget(rbol2)
        vbox.addLayout(hboxB)

        #upaljeno grlo
        hboxUG = QtWidgets.QHBoxLayout()
        lugrlo = QLabel("Upaljeno grlo: ")
        rugrlo1= QtWidgets.QRadioButton("Da")
        rugrlo2= QtWidgets.QRadioButton("Ne")
        hboxUG.addWidget(lugrlo)
        hboxUG.addWidget(rugrlo1)
        hboxUG.addWidget(rugrlo2)
        vbox.addLayout(hboxUG)

        #dijareja
        hboxD = QtWidgets.QHBoxLayout()
        ldijareja = QLabel("Dijareja (proliv): ")
        rdijareja1 = QtWidgets.QRadioButton("Da")
        rdijareja2 = QtWidgets.QRadioButton("Ne")
        hboxD.addWidget(ldijareja)
        hboxD.addWidget(rdijareja1)
        hboxD.addWidget(rdijareja2)
        vbox.addLayout(hboxD)

        #glavobolja
        hboxG = QtWidgets.QHBoxLayout()
        lglavobolja = QLabel("Glavobolja: ")
        rglavobolja1 = QtWidgets.QRadioButton("Da")
        rglavobolja2 = QtWidgets.QRadioButton("Ne")
        hboxG.addWidget(lglavobolja)
        hboxG.addWidget(rglavobolja1)
        hboxG.addWidget(rglavobolja2)
        vbox.addLayout(hboxG)
 
        #gubitak cula
        hboxC = QtWidgets.QHBoxLayout()
        lcula = QLabel("Gubitak cula mirisa ili ukusa: ")
        rcula1 = QtWidgets.QRadioButton("Cubitak cula mirisa")
        rcula2 = QtWidgets.QRadioButton("Gubitak cula ukusa")
        rcula3 = QtWidgets.QRadioButton("Nije doslo do gubitka cula mirisa ili ukusa")
        #grupa = QtGui.QButtonGroup()
        #rgrupa.addButton(rcula1)
        #rgrupa.addButton(rcula2)
        #rgrupa.addButton(rcula3)
        
        hboxC.addWidget(lcula)
        hboxC.addWidget(rcula1)
        hboxC.addWidget(rcula2)
        hboxC.addWidget(rcula3)
       # hboxC.addWidget(rgrupa)
        vbox.addLayout(hboxC)
        
        #teski simptomi
        lteski = QtWidgets.QLabel("Teski simptomi")
        vbox.addWidget(lteski)

        hboxDisanje = QtWidgets.QHBoxLayout()
        ldisanje = QtWidgets.QLabel("Teskoce pri disanju ili nedostatak daha: ")
        rbDisanje1 = QtWidgets.QRadioButton("da")
        rbDisanje2 = QtWidgets.QRadioButton("ne")
        hboxDisanje.addWidget(ldisanje)
        hboxDisanje.addWidget(rbDisanje1)
        hboxDisanje.addWidget(rbDisanje2)
        vbox.addLayout(hboxDisanje)

        hboxPritisak = QtWidgets.QHBoxLayout()
        lpritisak = QtWidgets.QLabel("Bol ili pritisak u grudima: ")
        rbPritisak1 = QtWidgets.QRadioButton("da")
        rbPritisak2 = QtWidgets.QRadioButton("ne")
        hboxPritisak.addWidget(lpritisak)
        hboxPritisak.addWidget(rbPritisak1)
        hboxPritisak.addWidget(rbPritisak2)
        vbox.addLayout(hboxPritisak)

        #kontakti
        lkont = QtWidgets.QLabel("KONTAKTI")
        vbox.addWidget(lkont)

        hboxPoz = QtWidgets.QHBoxLayout()
        lpoz = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja je pozitivna na Covid-19? ")
        rbPoz1 = QtWidgets.QRadioButton("da")
        rbPoz2 = QtWidgets.QRadioButton("ne")
        hboxPoz.addWidget(lpoz)
        hboxPoz.addWidget(rbPoz1)
        hboxPoz.addWidget(rbPoz2)
        vbox.addLayout(hboxPoz)

        hboxSim = QtWidgets.QHBoxLayout()
        lsim = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja\n ima simptome Covida-19 ali se nije testirala? ")
        rbSim1 = QtWidgets.QRadioButton("da")
        rbSim2 = QtWidgets.QRadioButton("ne")
        hboxSim.addWidget(lsim)
        hboxSim.addWidget(rbSim1)
        hboxSim.addWidget(rbSim2)
        vbox.addLayout(hboxSim)

        #kraj
        hboxKraj = QtWidgets.QHBoxLayout()
        pbGotovo = QtWidgets.QPushButton("Gotovo")
        pbPonovo = QtWidgets.QPushButton("Pocni ispocetka")
        hboxKraj.addWidget(pbGotovo)
        hboxKraj.addWidget(pbPonovo)
        vbox.addLayout(hboxKraj)

        lprocena = QtWidgets.QLabel("Procena: ")
        leprocena = QtWidgets.QLineEdit()
        leprocena.resize(900,100)
        vbox.addWidget(lprocena)
        vbox.addWidget(leprocena)


app = QtWidgets.QApplication([])
window = Gui()
app.exec_()
