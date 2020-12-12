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
        self.tGodine= QtWidgets.QLineEdit()
        hbox1.addWidget(lGodine)
        hbox1.addWidget(self.tGodine)
        vbox.addLayout(hbox1)
        
        #vakcinacija
        hboxVak = QtWidgets.QHBoxLayout()
        lVakcinacija= QLabel("Da li ste vakcinisani: ")
        self.rVak1= QtWidgets.QRadioButton("Jesam od svih")
        self.rVak2= QtWidgets.QRadioButton("Nisam od svih vakcina koje su bile potrebne")
        self.rVak3= QtWidgets.QRadioButton("Nisam uopste")
        grVak = QtWidgets.QButtonGroup(self)
        grVak.addButton(self.rVak1)
        grVak.addButton(self.rVak2)
        grVak.addButton(self.rVak3)
        hboxVak.addWidget(lVakcinacija)
        hboxVak.addWidget(self.rVak1)
        hboxVak.addWidget(self.rVak2)
        hboxVak.addWidget(self.rVak3)
        vbox.addLayout(hboxVak)

        #alergija
        hboxAlergija = QtWidgets.QHBoxLayout()
        lAlergija= QLabel("Da li ste alergicni: ")
        self.rAlergija1= QtWidgets.QRadioButton("na neku vrstu hrane")
        self.rAlergija2= QtWidgets.QRadioButton("na neku vrstu leka")
        grAlergija1 = QtWidgets.QButtonGroup(self)
        grAlergija1.addButton(self.rAlergija1)
        grAlergija2 = QtWidgets.QButtonGroup(self)
        grAlergija2.addButton(self.rAlergija2)
        hboxAlergija.addWidget(lAlergija)
        hboxAlergija.addWidget(self.rAlergija1)
        hboxAlergija.addWidget(self.rAlergija2)
        vbox.addLayout(hboxAlergija)

        #teske infekcije
        hboxInfekcija = QtWidgets.QHBoxLayout()
        vboxInfekcija2= QtWidgets.QVBoxLayout()
        lInfekcije= QLabel("Da li ste imali neke od teskih infekcija: ")
        self.rInfekcija1= QtWidgets.QRadioButton("pneumonija (upala pluca)")
        self.rInfekcija2= QtWidgets.QRadioButton("meningitis (upala mozga)")
        self.rInfekcija3= QtWidgets.QRadioButton("endokarditis (upala srca)")
        grInfekcija1 = QtWidgets.QButtonGroup(self)
        grInfekcija1.addButton(self.rInfekcija1)
        grInfekcija2 = QtWidgets.QButtonGroup(self)
        grInfekcija2.addButton(self.rInfekcija2)
        grInfekcija3 = QtWidgets.QButtonGroup(self)
        grInfekcija3.addButton(self.rInfekcija3)
        hboxInfekcija.addWidget(lInfekcije)
        vboxInfekcija2.addWidget(self.rInfekcija1)
        vboxInfekcija2.addWidget(self.rInfekcija2)
        vboxInfekcija2.addWidget(self.rInfekcija3)
        hboxInfekcija.addLayout(vboxInfekcija2)
        vbox.addLayout(hboxInfekcija)

        #diabetes
        hboxDiabetes = QtWidgets.QHBoxLayout()
        lDiabetes= QLabel("Da li imate diabetes: ")
        self.rDiabetes1= QtWidgets.QRadioButton("Da")
        self.rDiabetes2= QtWidgets.QRadioButton("Ne")
        grDiabetes = QtWidgets.QButtonGroup(self)
        grDiabetes.addButton(self.rDiabetes1)
        grDiabetes.addButton(self.rDiabetes2)
        hboxDiabetes.addWidget(lDiabetes)
        hboxDiabetes.addWidget(self.rDiabetes1)
        hboxDiabetes.addWidget(self.rDiabetes2)
        vbox.addLayout(hboxDiabetes)

        #hipertenzija
        hboxHipertenzija = QtWidgets.QHBoxLayout()
        lHipertenzija= QLabel("Da li imate hipertenziju (povisen krvni pritisak): ")
        self.rHiper1= QtWidgets.QRadioButton("Da")
        self.rHiper2= QtWidgets.QRadioButton("Ne")
        grHiper = QtWidgets.QButtonGroup(self)
        grHiper.addButton(self.rHiper1)
        grHiper.addButton(self.rHiper2)
        hboxHipertenzija.addWidget(lHipertenzija)
        hboxHipertenzija.addWidget(self.rHiper1)
        hboxHipertenzija.addWidget(self.rHiper2)
        vbox.addLayout(hboxHipertenzija)

        #hipotenzija
        hboxHipotenzija = QtWidgets.QHBoxLayout()
        lHipotenzija= QLabel("Da li imate hipotenziju (snizen krvni pritisak): ")
        self.rHipo1= QtWidgets.QRadioButton("Da")
        self.rHipo2= QtWidgets.QRadioButton("Ne")
        grHipo = QtWidgets.QButtonGroup(self)
        grHipo.addButton(self.rHipo1)
        grHipo.addButton(self.rHipo2)
        hboxHipotenzija.addWidget(lHipotenzija)
        hboxHipotenzija.addWidget(self.rHipo1)
        hboxHipotenzija.addWidget(self.rHipo2)
        vbox.addLayout(hboxHipotenzija)

        #astma
        hboxAstma = QtWidgets.QHBoxLayout()
        vboxAstma2= QtWidgets.QVBoxLayout()
        lAstma= QLabel("Da li imate astmu (ako da, koliko cesto): ")
        self.rAstma1= QtWidgets.QRadioButton("dnevno vise puta")
        self.rAstma2= QtWidgets.QRadioButton("jednom dnevno")
        self.rAstma3= QtWidgets.QRadioButton("vise od jednom nedeljno")
        self.rAstma4= QtWidgets.QRadioButton("manje od jednom nedeljno")
        self.rAstma5= QtWidgets.QRadioButton("nemam uopste")
        grAstma = QtWidgets.QButtonGroup(self)
        grAstma.addButton(self.rAstma1)
        grAstma.addButton(self.rAstma2)
        grAstma.addButton(self.rAstma3)
        grAstma.addButton(self.rAstma4)
        grAstma.addButton(self.rAstma5)
        hboxAstma.addWidget(lAstma)
        vboxAstma2.addWidget(self.rAstma1)
        vboxAstma2.addWidget(self.rAstma2)
        vboxAstma2.addWidget(self.rAstma3)
        vboxAstma2.addWidget(self.rAstma4)
        vboxAstma2.addWidget(self.rAstma5)
        hboxAstma.addLayout(vboxAstma2)
        vbox.addLayout(hboxAstma)

        #cigarete
        hboxCigarete = QtWidgets.QHBoxLayout()
        vboxCigarete2= QtWidgets.QVBoxLayout()
        lCigarete= QLabel("Da li pusite cigarete (ako da, koliko cigareta dnevno): ")
        self.rCig1= QtWidgets.QRadioButton("ne")
        self.rCig2= QtWidgets.QRadioButton("od 1 do 5 dnevno")
        self.rCig3= QtWidgets.QRadioButton("od 5 do 10 dnevno")
        self.rCig4= QtWidgets.QRadioButton("od 10 do 20 dnevno")
        self.rCig5= QtWidgets.QRadioButton("vise od 20")
        grCig = QtWidgets.QButtonGroup(self)
        grCig.addButton(self.rCig1)
        grCig.addButton(self.rCig2)
        grCig.addButton(self.rCig3)
        grCig.addButton(self.rCig4)
        grCig.addButton(self.rCig5)
        hboxCigarete.addWidget(lCigarete)
        vboxCigarete2.addWidget(self.rCig1)
        vboxCigarete2.addWidget(self.rCig2)
        vboxCigarete2.addWidget(self.rCig3)
        vboxCigarete2.addWidget(self.rCig4)
        vboxCigarete2.addWidget(self.rCig5)
        hboxCigarete.addLayout(vboxCigarete2)
        vbox.addLayout(hboxCigarete)

        self.simptomi = QLabel("SIMPTOMI", self)  
        vbox.addWidget(self.simptomi)
        self.cesti = QLabel("Najcesci simptomi",self)
        vbox.addWidget(self.cesti) 

        #temperatura
        hboxT = QtWidgets.QHBoxLayout()
        ltemp= QLabel("Temperatura: ")
        self.rtemp1= QtWidgets.QRadioButton("manje od 37")
        self.rtemp2= QtWidgets.QRadioButton("od 37 do 38")
        self.rtemp3= QtWidgets.QRadioButton("vise od 38")
        bgT = QButtonGroup(self)
        bgT.addButton(self.rtemp1)
        bgT.addButton(self.rtemp2)
        bgT.addButton(self.rtemp3)
        hboxT.addWidget(ltemp)
        hboxT.addWidget(self.rtemp1)
        hboxT.addWidget(self.rtemp2)
        hboxT.addWidget(self.rtemp3)
        vbox.addLayout(hboxT)
        
        #suv kasalj
        hboxSK = QtWidgets.QHBoxLayout()
        lskasalj= QLabel("Suv kasalj: ")
        self.rskasalj1= QtWidgets.QRadioButton("Da")
        self.rskasalj2= QtWidgets.QRadioButton("Ne")
        bgSK = QButtonGroup(self)
        bgSK.addButton(self.rskasalj1)
        bgSK.addButton(self.rskasalj2)
        hboxSK.addWidget(lskasalj)
        hboxSK.addWidget(self.rskasalj1)
        hboxSK.addWidget(self.rskasalj2)
        vbox.addLayout(hboxSK)

        #umor
        hboxU = QtWidgets.QHBoxLayout()
        lumor= QLabel("Umor: ")
        self.rumor1= QtWidgets.QRadioButton("Da")
        self.rumor2= QtWidgets.QRadioButton("Ne")
        bgU = QButtonGroup(self)
        bgU.addButton(self.rumor1)
        bgU.addButton(self.rumor2)
        hboxU.addWidget(lumor)
        hboxU.addWidget(self.rumor1)
        hboxU.addWidget(self.rumor2)
        vbox.addLayout(hboxU)

        self.manje = QLabel("Manje cesti simptomi",self)
        vbox.addWidget(self.manje)

        #bol
        hboxB = QtWidgets.QHBoxLayout()
        lbol = QLabel("Bolovi u misicima: ")
        self.rbol1= QtWidgets.QRadioButton("Da")
        self.rbol2= QtWidgets.QRadioButton("Ne")
        bgB = QButtonGroup(self)
        bgB.addButton(self.rbol1)
        bgB.addButton(self.rbol2)
        hboxB.addWidget(lbol)
        hboxB.addWidget(self.rbol1)
        hboxB.addWidget(self.rbol2)
        vbox.addLayout(hboxB)

        #upaljeno grlo
        hboxUG = QtWidgets.QHBoxLayout()
        lugrlo = QLabel("Upaljeno grlo: ")
        self.rugrlo1= QtWidgets.QRadioButton("Da")
        self.rugrlo2= QtWidgets.QRadioButton("Ne")
        bgUG = QButtonGroup(self)
        bgUG.addButton(self.rugrlo1)
        bgUG.addButton(self.rugrlo2)
        hboxUG.addWidget(lugrlo)
        hboxUG.addWidget(self.rugrlo1)
        hboxUG.addWidget(self.rugrlo2)
        vbox.addLayout(hboxUG)

        #dijareja
        hboxD = QtWidgets.QHBoxLayout()
        ldijareja = QLabel("Dijareja (proliv): ")
        self.rdijareja1 = QtWidgets.QRadioButton("Da")
        self.rdijareja2 = QtWidgets.QRadioButton("Ne")
        bgD = QButtonGroup(self)
        bgD.addButton(self.rdijareja1)
        bgD.addButton(self.rdijareja2)
        hboxD.addWidget(ldijareja)
        hboxD.addWidget(self.rdijareja1)
        hboxD.addWidget(self.rdijareja2)
        vbox.addLayout(hboxD)

        #glavobolja
        hboxG = QtWidgets.QHBoxLayout()
        lglavobolja = QLabel("Glavobolja: ")
        self.rglavobolja1 = QtWidgets.QRadioButton("Da")
        self.rglavobolja2 = QtWidgets.QRadioButton("Ne")
        bgG = QButtonGroup(self)
        bgG.addButton(self.rglavobolja1)
        bgG.addButton(self.rglavobolja2)
        hboxG.addWidget(lglavobolja)
        hboxG.addWidget(self.rglavobolja1)
        hboxG.addWidget(self.rglavobolja2)
        vbox.addLayout(hboxG)
 
        #gubitak cula
        hboxC = QtWidgets.QHBoxLayout()
        lcula = QLabel("Gubitak cula mirisa ili ukusa: ")
        self.rcula1 = QtWidgets.QRadioButton("Cubitak cula mirisa")
        self.rcula2 = QtWidgets.QRadioButton("Gubitak cula ukusa")
        rcula3 = QtWidgets.QRadioButton("Nije doslo do gubitka cula mirisa ili ukusa")
        bgC1 = QButtonGroup(self)
        bgC1.addButton(self.rcula1)
        bgC2 = QButtonGroup(self)
        bgC2.addButton(self.rcula2)
        bgC3 = QButtonGroup(self)
        bgC3.addButton(self.rcula3)
        
        hboxC.addWidget(lcula)
        hboxC.addWidget(self.rcula1)
        hboxC.addWidget(self.rcula2)
        hboxC.addWidget(self.rcula3)
       # hboxC.addWidget(rgrupa)
        vbox.addLayout(hboxC)
        
        #teski simptomi
        lteski = QtWidgets.QLabel("Teski simptomi")
        vbox.addWidget(lteski)

        hboxDisanje = QtWidgets.QHBoxLayout()
        ldisanje = QtWidgets.QLabel("Teskoce pri disanju ili nedostatak daha: ")
        self.rbDisanje1 = QtWidgets.QRadioButton("Da")
        self.rbDisanje2 = QtWidgets.QRadioButton("Ne")
        grDisanje = QtWidgets.QButtonGroup(self)
        grDisanje.addButton(self.rbDisanje1)
        grDisanje.addButton(self.rbDisanje2)
        hboxDisanje.addWidget(ldisanje)
        hboxDisanje.addWidget(rbDisanje1)
        hboxDisanje.addWidget(rbDisanje2)
        vbox.addLayout(hboxDisanje)

        hboxPritisak = QtWidgets.QHBoxLayout()
        lpritisak = QtWidgets.QLabel("Bol ili pritisak u grudima: ")
        self.rbPritisak1 = QtWidgets.QRadioButton("Da")
        self.rbPritisak2 = QtWidgets.QRadioButton("Ne")
        grPritisak = QtWidgets.QButtonGroup(self)
        grPritisak.addButton(self.rbPritisak1)
        grPritisak.addButton(self.rbPritisak2)
        hboxPritisak.addWidget(lpritisak)
        hboxPritisak.addWidget(self.rbPritisak1)
        hboxPritisak.addWidget(self.rbPritisak2)
        vbox.addLayout(hboxPritisak)

        #kontakti
        lkont = QtWidgets.QLabel("KONTAKTI")
        vbox.addWidget(lkont)

        hboxPoz = QtWidgets.QHBoxLayout()
        lpoz = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja je pozitivna na Covid-19? ")
        self.rbPoz1 = QtWidgets.QRadioButton("Da")
        self.rbPoz2 = QtWidgets.QRadioButton("Ne")
        grPoz = QtWidgets.QButtonGroup(self)
        grPoz.addButton(self.rbPoz1)
        grPoz.addButton(self.rbPoz2)
        hboxPoz.addWidget(lpoz)
        hboxPoz.addWidget(self.rbPoz1)
        hboxPoz.addWidget(self.rbPoz2)
        vbox.addLayout(hboxPoz)

        hboxSim = QtWidgets.QHBoxLayout()
        lsim = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja\n ima simptome Covida-19 ali se nije testirala? ")
        self.rbSim1 = QtWidgets.QRadioButton("Da")
        self.rbSim2 = QtWidgets.QRadioButton("Ne")
        grSim = QtWidgets.QButtonGroup(self)
        grSim.addButton(self.rbSim1)
        grSim.addButton(self.rbSim2)
        hboxSim.addWidget(lsim)
        hboxSim.addWidget(self.rbSim1)
        hboxSim.addWidget(self.rbSim2)
        vbox.addLayout(hboxSim)

        #kraj
        hboxKraj = QtWidgets.QHBoxLayout()
        self.pbGotovo = QtWidgets.QPushButton("Gotovo")
        self.pbPonovo = QtWidgets.QPushButton("Pocni ispocetka")
        hboxKraj.addWidget(self.pbGotovo)
        hboxKraj.addWidget(self.pbPonovo)
        vbox.addLayout(hboxKraj)

        self.lprocena = QtWidgets.QLabel("Procena: ")
        self.leprocena = QtWidgets.QLineEdit()
        vbox.addWidget(self.lprocena)
        vbox.addWidget(self.leprocena)
        
        pbGotovo.clicked.connect(self.ukupno)
        
    def ukupno(self):
        n=0
        #godine
        try:
            broj=int(int(self.tgodine.text())/2)
            n+=broj
        except:
            self.greska()
        
        
        if self.rVak1.isChecked():
            n+=0
        elif self.rVak2.isChecked():
            n+=5
        elif self.rVak3.isChecked():
            n+=10
        else:
            self.greska()
        
        
        #alergija
        if self.rAlergija1.isChecked():
            n+=5
        elif self.rAlergija2.isChecked():
            n+=5
        #infekcija
        if self.rInfekcija1.isChecked():
            n+=50
        elif self.rInfekcija2.isChecked():
            n+=30
        elif self.rInfekcija3.isChecked():
            n+=30
        #diabetes
        if self.rDiabetes1.isChecked():
            n+=40
        elif self.rDiabetes2.isChecked():
            n+=0
        else: 
            self.greska()
        #hipertenzija
        if self.rHiper1.isChecked():
            n+=10
        elif self.rHiper2.isChecked():
            n+=0
        else: 
            self.greska()
        #hipotenzija
        if self.rHipo1.isChecked():
            n+=10
        elif self.rHipo2.isChecked():
            n+=0
        else: 
            self.greska()

        #astma
        if self.rAstma1.isChecked():
            n+=50
        elif self.rAstma2.isChecked():
            n+=40
        elif self.rAstma3.isChecked():
            n+=30
        elif self.rAstma4.isChecked():
            n+=10
        elif self.rAstma5.isChecked():
            n+=0
        else: 
            self.greska()
        
        #cigarete
        if self.rCig1.isChecked():
            n+=0
        elif self.rCig2.isChecked():
            n+=5
        elif self.rCig3.isChecked():
            n+=10
        elif self.rCig4.isChecked():
            n+=15
        elif self.rCig5.isChecked():
            n+=20
        else: 
            self.greska()
        
        
        
        if self.rtemp1.isChecked():
            n+=0
        elif self.rtemp2.isChecked():
            n+=100
        elif self.rtemp3.isChecked():
            n+=50
        else:
            self.greska()
            
        if self.rskasalj1.isChecked():
            n+=100
        elif self.rskasalj2.isChecked():
            n+=0
        else:
            self.greska()
            
        if self.rumor1.isChecked():
            n+=100
        elif self.rumor2.isChecked():
            n+=0
        else:
            self.greska()
            
        if self.rbol1.isChecked():
            n+=50
        elif self.rbol2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if self.rugrlo1.isChecked():
            n+=50
        elif self.rugrlo2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if self.rdijareja1.isChecked():
            n+=50
        elif self.rdijareja2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if self.rglavobolja1.isChecked():
            n+=30
        elif self.rglavobolja2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if self.rcula1.isChecked():
            n+=50
        elif self.rcula2.isChecked():
            n+=50
        elif self.rcula3.isChecked():
            n+=0 
        else:
            self.greska()
        #teski
        if self.rbDisanje1.isChecked():
            n+=150
        elif self.rbDisanje2.isChecked():
            n+=0
        else:
            self.greska()
        
        if self.rbPritisak1.isChecked():
            n+=150
        elif self.rbPritisak2.isChecked():
            n+=0
        else:
            self.greska()

        #kontakti
        if self.rbPoz1.isChecked():
            n+=200
        elif self.rbPoz2.isChecked():
            n+=0
        else:
            self.greska()

        if self.rbSim1.isChecked():
            n+=200
        elif self.rbSim2.isChecked():
            n+=0
        else:
            self.greska()

        if n>=300:
            self.leprocena.setText("Doktor")
        elif n>=70:
            self.leprocena.setText("Kucno")
        else:
            self.leprocena.setText("OK")
        
    
    def greska(self):
        alert=QtWidgets.QMessageBox()
        alert.setWindowTitle("Poruka")
        alert.setText("Neispravan unos")
        alert.move(250,250)
        alert.exec_()


app = QtWidgets.QApplication([])
window = Gui()
app.exec_()
