from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QButtonGroup
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
        
        #goidne
        hbox1 = QtWidgets.QHBoxLayout()
        lGodine= QLabel("Uneti broj godina: ")
        tGodine= QtWidgets.QLineEdit()
        hbox1.addWidget(lGodine)
        hbox1.addWidget(tGodine)
        vbox.addLayout(hbox1)
        
        #vakcinacija
        hboxVak = QtWidgets.QHBoxLayout()
        lVakcinacija= QLabel("Da li ste vakcinisani: ")
        rVak1= QtWidgets.QRadioButton("Jesam od svih")
        rVak2= QtWidgets.QRadioButton("Nisam od svih vakcina koje su bile potrebne")
        rVak3= QtWidgets.QRadioButton("Nisam uopste")
        hboxVak.addWidget(lVakcinacija)
        hboxVak.addWidget(rVak1)
        hboxVak.addWidget(rVak2)
        hboxVak.addWidget(rVak3)
        vbox.addLayout(hboxVak)

        #alergija
        hboxAlergija = QtWidgets.QHBoxLayout()
        lAlergija= QLabel("Da li ste alergicni: ")
        rAlergija1= QtWidgets.QRadioButton("na neku vrstu hrane")
        rAlergija2= QtWidgets.QRadioButton("na neku vrstu leka")
        hboxAlergija.addWidget(lAlergija)
        hboxAlergija.addWidget(rAlergija1)
        hboxAlergija.addWidget(rAlergija2)
        vbox.addLayout(hboxAlergija)

        #teske infekcije
        hboxInfekcija = QtWidgets.QHBoxLayout()
        vboxInfekcija2= QtWidgets.QVBoxLayout()
        lInfekcije= QLabel("Da li ste imali neke od teskih infekcija: ")
        rInfekcija1= QtWidgets.QRadioButton("pneumonija (upala pluca)")
        rInfekcija2= QtWidgets.QRadioButton("meningitis (upala mozga)")
        rInfekcija3= QtWidgets.QRadioButton("endokarditis (upala srca)")
        hboxInfekcija.addWidget(lInfekcije)
        vboxInfekcija2.addWidget(rInfekcija1)
        vboxInfekcija2.addWidget(rInfekcija2)
        vboxInfekcija2.addWidget(rInfekcija3)
        hboxInfekcija.addLayout(vboxInfekcija2)
        vbox.addLayout(hboxInfekcija)

        #diabetes
        hboxDiabetes = QtWidgets.QHBoxLayout()
        lDiabetes= QLabel("Da li imate diabetes: ")
        rDiabetes1= QtWidgets.QRadioButton("Da")
        rDiabetes2= QtWidgets.QRadioButton("Ne")
        hboxDiabetes.addWidget(lDiabetes)
        hboxDiabetes.addWidget(rDiabetes1)
        hboxDiabetes.addWidget(rDiabetes2)
        vbox.addLayout(hboxDiabetes)

        #hipertenzija
        hboxHipertenzija = QtWidgets.QHBoxLayout()
        lHipertenzija= QLabel("Da li imate hipertenziju (povisen krvni pritisak): ")
        rHiper1= QtWidgets.QRadioButton("Da")
        rHiper2= QtWidgets.QRadioButton("Ne")
        hboxHipertenzija.addWidget(lHipertenzija)
        hboxHipertenzija.addWidget(rHiper1)
        hboxHipertenzija.addWidget(rHiper2)
        vbox.addLayout(hboxHipertenzija)

        #hipotenzija
        hboxHipotenzija = QtWidgets.QHBoxLayout()
        lHipotenzija= QLabel("Da li imate hipotenziju (snizen krvni pritisak): ")
        rHipo1= QtWidgets.QRadioButton("Da")
        rHipo2= QtWidgets.QRadioButton("Ne")
        hboxHipotenzija.addWidget(lHipotenzija)
        hboxHipotenzija.addWidget(rHipo1)
        hboxHipotenzija.addWidget(rHipo2)
        vbox.addLayout(hboxHipotenzija)

        #astma
        hboxAstma = QtWidgets.QHBoxLayout()
        vboxAstma2= QtWidgets.QVBoxLayout()
        lAstma= QLabel("Da li imate astmu (ako da, koliko cesto): ")
        rAstma1= QtWidgets.QRadioButton("dnevno vise puta")
        rAstma2= QtWidgets.QRadioButton("jednom dnevno")
        rAstma3= QtWidgets.QRadioButton("vise od jednom nedeljno")
        rAstma4= QtWidgets.QRadioButton("manje od jednom nedeljno")
        rAstma5= QtWidgets.QRadioButton("nemam uopste")
        hboxAstma.addWidget(lAstma)
        vboxAstma2.addWidget(rAstma1)
        vboxAstma2.addWidget(rAstma2)
        vboxAstma2.addWidget(rAstma3)
        vboxAstma2.addWidget(rAstma4)
        vboxAstma2.addWidget(rAstma5)
        hboxAstma.addLayout(vboxAstma2)
        vbox.addLayout(hboxAstma)

        #cigarete
        hboxCigarete = QtWidgets.QHBoxLayout()
        vboxCigarete2= QtWidgets.QVBoxLayout()
        lCigarete= QLabel("Da li pusite cigarete (ako da, koliko cigareta dnevno): ")
        rCig1= QtWidgets.QRadioButton("ne")
        rCig2= QtWidgets.QRadioButton("od 1 do 5 dnevno")
        rCig3= QtWidgets.QRadioButton("od 5 do 10 dnevno")
        rCig4= QtWidgets.QRadioButton("od 10 do 20 dnevno")
        rCig5= QtWidgets.QRadioButton("vise od 20")
        hboxCigarete.addWidget(lCigarete)
        vboxCigarete2.addWidget(rCig1)
        vboxCigarete2.addWidget(rCig2)
        vboxCigarete2.addWidget(rCig3)
        vboxCigarete2.addWidget(rCig4)
        vboxCigarete2.addWidget(rCig5)
        hboxCigarete.addLayout(vboxCigarete2)
        vbox.addLayout(hboxCigarete)

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
        bgT = QButtonGroup(self)
        bgT.addButton(rtemp1)
        bgT.addButton(rtemp2)
        bgT.addButton(rtemp3)
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
        bgSK = QButtonGroup(self)
        bgSK.addButton(rskasalj1)
        bgSK.addButton(rskasalj2)
        hboxSK.addWidget(lskasalj)
        hboxSK.addWidget(rskasalj1)
        hboxSK.addWidget(rskasalj2)
        vbox.addLayout(hboxSK)

        #umor
        hboxU = QtWidgets.QHBoxLayout()
        lumor= QLabel("Umor: ")
        rumor1= QtWidgets.QRadioButton("Da")
        rumor2= QtWidgets.QRadioButton("Ne")
        bgU = QButtonGroup(self)
        bgU.addButton(rumor1)
        bgU.addButton(rumor2)
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
        bgB = QButtonGroup(self)
        bgB.addButton(rbol1)
        bgB.addButton(rbol2)
        hboxB.addWidget(lbol)
        hboxB.addWidget(rbol1)
        hboxB.addWidget(rbol2)
        vbox.addLayout(hboxB)

        #upaljeno grlo
        hboxUG = QtWidgets.QHBoxLayout()
        lugrlo = QLabel("Upaljeno grlo: ")
        rugrlo1= QtWidgets.QRadioButton("Da")
        rugrlo2= QtWidgets.QRadioButton("Ne")
        bgUG = QButtonGroup(self)
        bgUG.addButton(rugrlo1)
        bgUG.addButton(rugrlo2)
        hboxUG.addWidget(lugrlo)
        hboxUG.addWidget(rugrlo1)
        hboxUG.addWidget(rugrlo2)
        vbox.addLayout(hboxUG)

        #dijareja
        hboxD = QtWidgets.QHBoxLayout()
        ldijareja = QLabel("Dijareja (proliv): ")
        rdijareja1 = QtWidgets.QRadioButton("Da")
        rdijareja2 = QtWidgets.QRadioButton("Ne")
        bgD = QButtonGroup(self)
        bgD.addButton(rdijareja1)
        bgD.addButton(rdijareja2)
        hboxD.addWidget(ldijareja)
        hboxD.addWidget(rdijareja1)
        hboxD.addWidget(rdijareja2)
        vbox.addLayout(hboxD)

        #glavobolja
        hboxG = QtWidgets.QHBoxLayout()
        lglavobolja = QLabel("Glavobolja: ")
        rglavobolja1 = QtWidgets.QRadioButton("Da")
        rglavobolja2 = QtWidgets.QRadioButton("Ne")
        bgG = QButtonGroup(self)
        bgG.addButton(rglavobolja1)
        bgG.addButton(rglavobolja2)
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
        bgC1 = QButtonGroup(self)
        bgC1.addButton(rcula1)
        bgC2 = QButtonGroup(self)
        bgC2.addButton(rcula2)
        bgC3 = QButtonGroup(self)
        bgC3.addButton(rcula3)
        
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
        rbDisanje1 = QtWidgets.QRadioButton("Da")
        rbDisanje2 = QtWidgets.QRadioButton("Ne")
        hboxDisanje.addWidget(ldisanje)
        hboxDisanje.addWidget(rbDisanje1)
        hboxDisanje.addWidget(rbDisanje2)
        vbox.addLayout(hboxDisanje)

        hboxPritisak = QtWidgets.QHBoxLayout()
        lpritisak = QtWidgets.QLabel("Bol ili pritisak u grudima: ")
        rbPritisak1 = QtWidgets.QRadioButton("Da")
        rbPritisak2 = QtWidgets.QRadioButton("Ne")
        hboxPritisak.addWidget(lpritisak)
        hboxPritisak.addWidget(rbPritisak1)
        hboxPritisak.addWidget(rbPritisak2)
        vbox.addLayout(hboxPritisak)

        #kontakti
        lkont = QtWidgets.QLabel("KONTAKTI")
        vbox.addWidget(lkont)

        hboxPoz = QtWidgets.QHBoxLayout()
        lpoz = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja je pozitivna na Covid-19? ")
        rbPoz1 = QtWidgets.QRadioButton("Da")
        rbPoz2 = QtWidgets.QRadioButton("Ne")
        hboxPoz.addWidget(lpoz)
        hboxPoz.addWidget(rbPoz1)
        hboxPoz.addWidget(rbPoz2)
        vbox.addLayout(hboxPoz)

        hboxSim = QtWidgets.QHBoxLayout()
        lsim = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja\n ima simptome Covida-19 ali se nije testirala? ")
        rbSim1 = QtWidgets.QRadioButton("Da")
        rbSim2 = QtWidgets.QRadioButton("Ne")
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
