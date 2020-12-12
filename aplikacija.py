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
        grVak = QtWidgets.QButtonGroup(self)
        grVak.addButton(rVak1)
        grVak.addButton(rVak2)
        grVak.addButton(rVak3)
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
        grAlergija1 = QtWidgets.QButtonGroup(self)
        grAlergija1.addButton(rAlergija1)
        grAlergija2 = QtWidgets.QButtonGroup(self)
        grAlergija2.addButton(rAlergija2)
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
        grInfekcija1 = QtWidgets.QButtonGroup(self)
        grInfekcija1.addButton(rInfekcija1)
        grInfekcija2 = QtWidgets.QButtonGroup(self)
        grInfekcija2.addButton(rInfekcija2)
        grInfekcija3 = QtWidgets.QButtonGroup(self)
        grInfekcija3.addButton(rInfekcija3)
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
        grDiabetes = QtWidgets.QButtonGroup(self)
        grDiabetes.addButton(rDiabetes1)
        grDiabetes.addButton(rDiabetes2)
        hboxDiabetes.addWidget(lDiabetes)
        hboxDiabetes.addWidget(rDiabetes1)
        hboxDiabetes.addWidget(rDiabetes2)
        vbox.addLayout(hboxDiabetes)

        #hipertenzija
        hboxHipertenzija = QtWidgets.QHBoxLayout()
        lHipertenzija= QLabel("Da li imate hipertenziju (povisen krvni pritisak): ")
        rHiper1= QtWidgets.QRadioButton("Da")
        rHiper2= QtWidgets.QRadioButton("Ne")
        grHiper = QtWidgets.QButtonGroup(self)
        grHiper.addButton(rHiper1)
        grHiper.addButton(rHiper2)
        hboxHipertenzija.addWidget(lHipertenzija)
        hboxHipertenzija.addWidget(rHiper1)
        hboxHipertenzija.addWidget(rHiper2)
        vbox.addLayout(hboxHipertenzija)

        #hipotenzija
        hboxHipotenzija = QtWidgets.QHBoxLayout()
        lHipotenzija= QLabel("Da li imate hipotenziju (snizen krvni pritisak): ")
        rHipo1= QtWidgets.QRadioButton("Da")
        rHipo2= QtWidgets.QRadioButton("Ne")
        grHipo = QtWidgets.QButtonGroup(self)
        grHipo.addButton(rHipo1)
        grHipo.addButton(rHipo2)
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
        grAstma = QtWidgets.QButtonGroup(self)
        grAstma.addButton(rAstma1)
        grAstma.addButton(rAstma2)
        grAstma.addButton(rAstma3)
        grAstma.addButton(rAstma4)
        grAstma.addButton(rAstma5)
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
        grCig = QtWidgets.QButtonGroup(self)
        grCig.addButton(rCig1)
        grCig.addButton(rCig2)
        grCig.addButton(rCig3)
        grCig.addButton(rCig4)
        grCig.addButton(rCig5)
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
        if rVak1.isChecked():
            n+=0
        elif rVak2.isChecked():
            n+=5
        elif rVak3.isChecked():
            n+=10
        else:
            self.greska()
        
        
        #alergija
        if rAlergija1.isChecked():
            n+=5
        elif rAlergija2.isChecked():
            n+=5
        #infekcija
        if rInfekcija1.isChecked():
            n+=50
        elif rInfekcija2.isChecked():
            n+=30
        elif rInfekcija3.isChecked():
            n+=30
        #diabetes
        if rDiabetes1.isChecked():
            n+=40
        elif rDiabetes2.isChecked():
            n+=0
        else: 
            self.greska()
        #hipertenzija
        if rHiper1.isChecked():
            n+=10
        elif rHiper2.isChecked():
            n+=0
        else: 
            self.greska()
        #hipotenzija
        if rHipo1.isChecked():
            n+=10
        elif rHipo2.isChecked():
            n+=0
        else: 
            self.greska()

        #astma
        if rAstma1.isChecked():
            n+=50
        elif rAstma2.isChecked():
            n+=40
        elif rAstma3.isChecked():
            n+=30
        elif rAstma4.isChecked():
            n+=10
        elif rAstma5.isChecked():
            n+=0
        else: 
            self.greska()
        
        #cigarete
        if rCig1.isChecked():
            n+=0
        elif rCig2.isChecked():
            n+=5
        elif rCig3.isChecked():
            n+=10
        elif rCig4.isChecked():
            n+=15
        elif rCig5.isChecked():
            n+=20
        else: 
            self.greska()
        
        
        
         if rtemp1.isChecked():
            n+=0
        elif rtemp2.isChecked():
            n+=100
        elif rtemp3.isChecked():
            n+=50
        else:
            self.greska()
            
        if rskasalj1.isChecked():
            n+=100
        elif rskasalj2.isChecked():
            n+=0
        else:
            self.greska()
            
        if rumor1.isChecked():
            n+=100
        elif rumor2.isChecked():
            n+=0
        else:
            self.greska()
            
        if rbol1.isChecked():
            n+=50
        elif rbol2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if rugrlo1.isChecked():
            n+=50
        elif rugrlo2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if rdijareja1.isChecked():
            n+=50
        elif rdijareja2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if rglavobolja1.isChecked():
            n+=30
        elif rglavobolja2.isChecked():
            n+=0 
        else:
            self.greska()
        
        if rcula1.isChecked():
            n+=50
        elif rcula2.isChecked():
            n+=50
        elif rcula3.isChecked():
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
