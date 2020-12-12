from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QButtonGroup
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont


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
        self.licni.setFont(QFont("Comic Sans MS",weight=QFont.Bold))
        
        #ime i prezime
        hboxIme = QtWidgets.QHBoxLayout()
        lime= QLabel("Uneti ime i prezime: ")
        self.time= QtWidgets.QLineEdit()
        hboxIme.addWidget(lime)
        hboxIme.addWidget(self.time)
        vbox.addLayout(hboxIme)
        
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
        self.grVak = QtWidgets.QButtonGroup(self)
        self.grVak.addButton(self.rVak1)
        self.grVak.addButton(self.rVak2)
        self.grVak.addButton(self.rVak3)
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
        self.grAlergija1 = QtWidgets.QButtonGroup(self)
        self.grAlergija1.addButton(self.rAlergija1)
        self.grAlergija2 = QtWidgets.QButtonGroup(self)
        self.grAlergija2.addButton(self.rAlergija2)
        hboxAlergija.addWidget(lAlergija)
        hboxAlergija.addWidget(self.rAlergija1)
        hboxAlergija.addWidget(self.rAlergija2)
        vbox.addLayout(hboxAlergija)

        #teske infekcije
        hboxInfekcija = QtWidgets.QHBoxLayout()
        lInfekcije= QLabel("Da li ste imali neke od teskih infekcija: ")
        self.rInfekcija1= QtWidgets.QRadioButton("pneumonija (upala pluca)")
        self.rInfekcija2= QtWidgets.QRadioButton("meningitis (upala mozga)")
        self.rInfekcija3= QtWidgets.QRadioButton("endokarditis (upala srca)")
        self.grInfekcija1 = QtWidgets.QButtonGroup(self)
        self.grInfekcija1.addButton(self.rInfekcija1)
        self.grInfekcija2 = QtWidgets.QButtonGroup(self)
        self.grInfekcija2.addButton(self.rInfekcija2)
        self.grInfekcija3 = QtWidgets.QButtonGroup(self)
        self.grInfekcija3.addButton(self.rInfekcija3)
        hboxInfekcija.addWidget(lInfekcije)
        hboxInfekcija.addWidget(self.rInfekcija1)
        hboxInfekcija.addWidget(self.rInfekcija2)
        hboxInfekcija.addWidget(self.rInfekcija3)
        vbox.addLayout(hboxInfekcija)

        #diabetes
        hboxDiabetes = QtWidgets.QHBoxLayout()
        lDiabetes= QLabel("Da li imate diabetes: ")
        self.rDiabetes1= QtWidgets.QRadioButton("Da")
        self.rDiabetes2= QtWidgets.QRadioButton("Ne")
        self.grDiabetes = QtWidgets.QButtonGroup(self)
        self.grDiabetes.addButton(self.rDiabetes1)
        self.grDiabetes.addButton(self.rDiabetes2)
        hboxDiabetes.addWidget(lDiabetes)
        hboxDiabetes.addWidget(self.rDiabetes1)
        hboxDiabetes.addWidget(self.rDiabetes2)
        vbox.addLayout(hboxDiabetes)

        #hipertenzija
        hboxHipertenzija = QtWidgets.QHBoxLayout()
        lHipertenzija= QLabel("Da li imate hipertenziju (povisen krvni pritisak): ")
        self.rHiper1= QtWidgets.QRadioButton("Da")
        self.rHiper2= QtWidgets.QRadioButton("Ne")
        self.grHiper = QtWidgets.QButtonGroup(self)
        self.grHiper.addButton(self.rHiper1)
        self.grHiper.addButton(self.rHiper2)
        hboxHipertenzija.addWidget(lHipertenzija)
        hboxHipertenzija.addWidget(self.rHiper1)
        hboxHipertenzija.addWidget(self.rHiper2)
        vbox.addLayout(hboxHipertenzija)

        #hipotenzija
        hboxHipotenzija = QtWidgets.QHBoxLayout()
        lHipotenzija= QLabel("Da li imate hipotenziju (snizen krvni pritisak): ")
        self.rHipo1= QtWidgets.QRadioButton("Da")
        self.rHipo2= QtWidgets.QRadioButton("Ne")
        self.grHipo = QtWidgets.QButtonGroup(self)
        self.grHipo.addButton(self.rHipo1)
        self.grHipo.addButton(self.rHipo2)
        hboxHipotenzija.addWidget(lHipotenzija)
        hboxHipotenzija.addWidget(self.rHipo1)
        hboxHipotenzija.addWidget(self.rHipo2)
        vbox.addLayout(hboxHipotenzija)

        #astma
        hboxAstma = QtWidgets.QHBoxLayout()
        lAstma= QLabel("Da li imate astmu (ako da, koliko cesto): ")
        self.rAstma1= QtWidgets.QRadioButton("dnevno vise puta")
        self.rAstma2= QtWidgets.QRadioButton("jednom dnevno")
        self.rAstma3= QtWidgets.QRadioButton("vise od jednom nedeljno")
        self.rAstma4= QtWidgets.QRadioButton("manje od jednom nedeljno")
        self.rAstma5= QtWidgets.QRadioButton("nemam uopste")
        self.grAstma = QtWidgets.QButtonGroup(self)
        self.grAstma.addButton(self.rAstma1)
        self.grAstma.addButton(self.rAstma2)
        self.grAstma.addButton(self.rAstma3)
        self.grAstma.addButton(self.rAstma4)
        self.grAstma.addButton(self.rAstma5)
        hboxAstma.addWidget(lAstma)
        hboxAstma.addWidget(self.rAstma1)
        hboxAstma.addWidget(self.rAstma2)
        hboxAstma.addWidget(self.rAstma3)
        hboxAstma.addWidget(self.rAstma4)
        hboxAstma.addWidget(self.rAstma5)
        vbox.addLayout(hboxAstma)

        #cigarete
        hboxCigarete = QtWidgets.QHBoxLayout()
        lCigarete= QLabel("Da li pusite cigarete (ako da, koliko cigareta dnevno): ")
        self.rCig1= QtWidgets.QRadioButton("ne")
        self.rCig2= QtWidgets.QRadioButton("od 1 do 5 dnevno")
        self.rCig3= QtWidgets.QRadioButton("od 5 do 10 dnevno")
        self.rCig4= QtWidgets.QRadioButton("od 10 do 20 dnevno")
        self.rCig5= QtWidgets.QRadioButton("vise od 20")
        self.grCig = QtWidgets.QButtonGroup(self)
        self.grCig.addButton(self.rCig1)
        self.grCig.addButton(self.rCig2)
        self.grCig.addButton(self.rCig3)
        self.grCig.addButton(self.rCig4)
        self.grCig.addButton(self.rCig5)
        hboxCigarete.addWidget(lCigarete)
        hboxCigarete.addWidget(self.rCig1)
        hboxCigarete.addWidget(self.rCig2)
        hboxCigarete.addWidget(self.rCig3)
        hboxCigarete.addWidget(self.rCig4)
        hboxCigarete.addWidget(self.rCig5)
        vbox.addLayout(hboxCigarete)

        self.simptomi = QLabel("SIMPTOMI", self)  
        vbox.addWidget(self.simptomi)
        self.simptomi.setFont(QFont("Comic Sans MS",weight=QFont.Bold))
        self.cesti = QLabel("Najcesci simptomi",self)
        vbox.addWidget(self.cesti)
        self.cesti.setFont(QFont("Arial",weight=QFont.Bold))

        #temperatura
        hboxT = QtWidgets.QHBoxLayout()
        ltemp= QLabel("Temperatura: ")
        self.rtemp1= QtWidgets.QRadioButton("manje od 37")
        self.rtemp2= QtWidgets.QRadioButton("od 37 do 38")
        self.rtemp3= QtWidgets.QRadioButton("vise od 38")
        self.bgT = QButtonGroup(self)
        self.bgT.addButton(self.rtemp1)
        self.bgT.addButton(self.rtemp2)
        self.bgT.addButton(self.rtemp3)
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
        self.bgSK = QButtonGroup(self)
        self.bgSK.addButton(self.rskasalj1)
        self.bgSK.addButton(self.rskasalj2)
        hboxSK.addWidget(lskasalj)
        hboxSK.addWidget(self.rskasalj1)
        hboxSK.addWidget(self.rskasalj2)
        vbox.addLayout(hboxSK)

        #umor
        hboxU = QtWidgets.QHBoxLayout()
        lumor= QLabel("Umor: ")
        self.rumor1= QtWidgets.QRadioButton("Da")
        self.rumor2= QtWidgets.QRadioButton("Ne")
        self.bgU = QButtonGroup(self)
        self.bgU.addButton(self.rumor1)
        self.bgU.addButton(self.rumor2)
        hboxU.addWidget(lumor)
        hboxU.addWidget(self.rumor1)
        hboxU.addWidget(self.rumor2)
        vbox.addLayout(hboxU)

        self.manje = QLabel("Manje cesti simptomi",self)
        vbox.addWidget(self.manje)
        self.manje.setFont(QFont("Arial",weight=QFont.Bold))

        #bol
        hboxB = QtWidgets.QHBoxLayout()
        lbol = QLabel("Bolovi u misicima: ")
        self.rbol1= QtWidgets.QRadioButton("Da")
        self.rbol2= QtWidgets.QRadioButton("Ne")
        self.bgB = QButtonGroup(self)
        self.bgB.addButton(self.rbol1)
        self.bgB.addButton(self.rbol2)
        hboxB.addWidget(lbol)
        hboxB.addWidget(self.rbol1)
        hboxB.addWidget(self.rbol2)
        vbox.addLayout(hboxB)

        #upaljeno grlo
        hboxUG = QtWidgets.QHBoxLayout()
        lugrlo = QLabel("Upaljeno grlo: ")
        self.rugrlo1= QtWidgets.QRadioButton("Da")
        self.rugrlo2= QtWidgets.QRadioButton("Ne")
        self.bgUG = QButtonGroup(self)
        self.bgUG.addButton(self.rugrlo1)
        self.bgUG.addButton(self.rugrlo2)
        hboxUG.addWidget(lugrlo)
        hboxUG.addWidget(self.rugrlo1)
        hboxUG.addWidget(self.rugrlo2)
        vbox.addLayout(hboxUG)

        #dijareja
        hboxD = QtWidgets.QHBoxLayout()
        ldijareja = QLabel("Dijareja (proliv): ")
        self.rdijareja1 = QtWidgets.QRadioButton("Da")
        self.rdijareja2 = QtWidgets.QRadioButton("Ne")
        self.bgD = QButtonGroup(self)
        self.bgD.addButton(self.rdijareja1)
        self.bgD.addButton(self.rdijareja2)
        hboxD.addWidget(ldijareja)
        hboxD.addWidget(self.rdijareja1)
        hboxD.addWidget(self.rdijareja2)
        vbox.addLayout(hboxD)

        #glavobolja
        hboxG = QtWidgets.QHBoxLayout()
        lglavobolja = QLabel("Glavobolja: ")
        self.rglavobolja1 = QtWidgets.QRadioButton("Da")
        self.rglavobolja2 = QtWidgets.QRadioButton("Ne")
        self.bgG = QButtonGroup(self)
        self.bgG.addButton(self.rglavobolja1)
        self.bgG.addButton(self.rglavobolja2)
        hboxG.addWidget(lglavobolja)
        hboxG.addWidget(self.rglavobolja1)
        hboxG.addWidget(self.rglavobolja2)
        vbox.addLayout(hboxG)
 
        #gubitak cula
        hboxC = QtWidgets.QHBoxLayout()
        lcula = QLabel("Gubitak cula mirisa ili ukusa: ")
        self.rcula1 = QtWidgets.QRadioButton("Cubitak cula mirisa")
        self.rcula2 = QtWidgets.QRadioButton("Gubitak cula ukusa")
        self.rcula3 = QtWidgets.QRadioButton("Nije doslo do gubitka cula mirisa ili ukusa")
        self.bgC1 = QButtonGroup(self)
        self.bgC1.addButton(self.rcula1)
        self.bgC2 = QButtonGroup(self)
        self.bgC2.addButton(self.rcula2)
        self.bgC3 = QButtonGroup(self)
        self.bgC3.addButton(self.rcula3)
        
        hboxC.addWidget(lcula)
        hboxC.addWidget(self.rcula1)
        hboxC.addWidget(self.rcula2)
        hboxC.addWidget(self.rcula3)
       # hboxC.addWidget(rgrupa)
        vbox.addLayout(hboxC)
        
        #teski simptomi
        lteski = QtWidgets.QLabel("Teski simptomi")
        vbox.addWidget(lteski)
        lteski.setFont(QFont("Arial",weight=QFont.Bold))

        hboxDisanje = QtWidgets.QHBoxLayout()
        ldisanje = QtWidgets.QLabel("Teskoce pri disanju ili nedostatak daha: ")
        self.rbDisanje1 = QtWidgets.QRadioButton("Da")
        self.rbDisanje2 = QtWidgets.QRadioButton("Ne")
        self.grDisanje = QtWidgets.QButtonGroup(self)
        self.grDisanje.addButton(self.rbDisanje1)
        self.grDisanje.addButton(self.rbDisanje2)
        hboxDisanje.addWidget(ldisanje)
        hboxDisanje.addWidget(self.rbDisanje1)
        hboxDisanje.addWidget(self.rbDisanje2)
        vbox.addLayout(hboxDisanje)

        hboxPritisak = QtWidgets.QHBoxLayout()
        lpritisak = QtWidgets.QLabel("Bol ili pritisak u grudima: ")
        self.rbPritisak1 = QtWidgets.QRadioButton("Da")
        self.rbPritisak2 = QtWidgets.QRadioButton("Ne")
        self.grPritisak = QtWidgets.QButtonGroup(self)
        self.grPritisak.addButton(self.rbPritisak1)
        self.grPritisak.addButton(self.rbPritisak2)
        hboxPritisak.addWidget(lpritisak)
        hboxPritisak.addWidget(self.rbPritisak1)
        hboxPritisak.addWidget(self.rbPritisak2)
        vbox.addLayout(hboxPritisak)

        #kontakti
        lkont = QtWidgets.QLabel("KONTAKTI")
        vbox.addWidget(lkont)
        lkont.setFont(QFont("Comic Sans MS",weight=QFont.Bold))

        hboxPoz = QtWidgets.QHBoxLayout()
        lpoz = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja je pozitivna na Covid-19? ")
        self.rbPoz1 = QtWidgets.QRadioButton("Da")
        self.rbPoz2 = QtWidgets.QRadioButton("Ne")
        self.grPoz = QtWidgets.QButtonGroup(self)
        self.grPoz.addButton(self.rbPoz1)
        self.grPoz.addButton(self.rbPoz2)
        hboxPoz.addWidget(lpoz)
        hboxPoz.addWidget(self.rbPoz1)
        hboxPoz.addWidget(self.rbPoz2)
        vbox.addLayout(hboxPoz)

        hboxSim = QtWidgets.QHBoxLayout()
        lsim = QtWidgets.QLabel("Da li ste bili u kontaktu sa osobom koja\n ima simptome Covida-19 ali se nije testirala? ")
        self.rbSim1 = QtWidgets.QRadioButton("Da")
        self.rbSim2 = QtWidgets.QRadioButton("Ne")
        self.grSim = QtWidgets.QButtonGroup(self)
        self.grSim.addButton(self.rbSim1)
        self.grSim.addButton(self.rbSim2)
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
        
        self.pbGotovo.clicked.connect(self.ukupno)
        self.pbPonovo.clicked.connect(self.brisi)
        
    def ukupno(self):
        n=0
        #godine
        try:
            broj=int(self.tGodine.text())/2
            n+=broj
        except:
            self.greska("niste uneli godine")
        
        
        if self.rVak1.isChecked():
            n+=0
        elif self.rVak2.isChecked():
            n+=5
        elif self.rVak3.isChecked():
            n+=10
        else:
            self.greska("niste uneli da li ste vakcinisani")
        
        
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
            self.greska("diabetes")
        #hipertenzija
        if self.rHiper1.isChecked():
            n+=10
        elif self.rHiper2.isChecked():
            n+=0
        else: 
            self.greska("hipertenzija")
        #hipotenzija
        if self.rHipo1.isChecked():
            n+=10
        elif self.rHipo2.isChecked():
            n+=0
        else: 
            self.greska("hipotenzija")

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
            self.greska("astma")
        
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
            self.greska("cigarete")
        
        
        
        if self.rtemp1.isChecked():
            n+=0
        elif self.rtemp2.isChecked():
            n+=100
        elif self.rtemp3.isChecked():
            n+=50
        else:
            self.greska("temper")
            
        if self.rskasalj1.isChecked():
            n+=100
        elif self.rskasalj2.isChecked():
            n+=0
        else:
            self.greska("kasalj")
            
        if self.rumor1.isChecked():
            n+=100
        elif self.rumor2.isChecked():
            n+=0
        else:
            self.greska("umor")
            
        if self.rbol1.isChecked():
            n+=50
        elif self.rbol2.isChecked():
            n+=0 
        else:
            self.greska("bol")
        
        if self.rugrlo1.isChecked():
            n+=50
        elif self.rugrlo2.isChecked():
            n+=0 
        else:
            self.greska("grlo")
        
        if self.rdijareja1.isChecked():
            n+=50
        elif self.rdijareja2.isChecked():
            n+=0 
        else:
            self.greska("dijare")
        
        if self.rglavobolja1.isChecked():
            n+=30
        elif self.rglavobolja2.isChecked():
            n+=0 
        else:
            self.greska("glavob")
        
        if self.rcula1.isChecked():
            n+=50
        elif self.rcula2.isChecked():
            n+=50
        elif self.rcula3.isChecked():
            n+=0 
        else:
            self.greska("cula")
        #teski
        if self.rbDisanje1.isChecked():
            n+=150
        elif self.rbDisanje2.isChecked():
            n+=0
        else:
            self.greska("disanje")
        
        if self.rbPritisak1.isChecked():
            n+=150
        elif self.rbPritisak2.isChecked():
            n+=0
        else:
            self.greska("pritisak")

        #kontakti
        if self.rbPoz1.isChecked():
            n+=200
        elif self.rbPoz2.isChecked():
            n+=0
        else:
            self.greska("kontakti")

        if self.rbSim1.isChecked():
            n+=200
        elif self.rbSim2.isChecked():
            n+=0
        else:
            self.greska("simptomi")

        if n>=300:
            self.preporucujemo("Na osnovu licnih podataka, bolesti od kojih bolujete i simptoma koje ste uneli, savetujemo Vam da se javite lekaru radi dalje kontrole i lecenja jer postoje indicije da ste zarazeni virusom COVID-19!")
        elif n>=70:
            self.preporucujemo("Na osnovu licnih podataka, bolesti od kojih bolujete i simptoma koje ste uneli, nije neophodno obracanje lekaru radi daljeg lecenja, vec je dovoljno da ostanete kod kuce, uzimate vitamine, cuvate svoje zdravlje i izbegavate kontakt sa drugim ljudima.")
        else:
            self.preporucujemo("Na osnovu licnih podataka, bolesti od kojih bolujete i simptoma koje ste uneli, ne postoje indicije da ste zarazeni virusom COVID-19, zdravlje Vam je stabilno, ali zarad sigurnosti Vas i ljudi u Vasem okruzenju, cuvajte svoje zdravlje i budite odgovorni! ")
        
    def brisi(self):
        self.tGodine.setText("")
        self.time.setText("")

        self.grVak.setExclusive(False)
        self.rVak1.setChecked(False)
        self.rVak2.setChecked(False)
        self.rVak3.setChecked(False)
        self.grVak.setExclusive(True)

        self.grAlergija1.setExclusive(False)
        self.rAlergija1.setChecked(False)
        self.grAlergija1.setExclusive(True)
        self.grAlergija2.setExclusive(False)
        self.rAlergija2.setChecked(False)
        self.grAlergija2(True)

        self.grInfekcija1.setExclusive(False)
        self.rInfekcija1.setChecked(False)
        self.grInfekcija1.setExclusive(True)
        self.grInfekcija2.setExclusive(False)
        self.rInfekcija2.setChecked(False)
        self.grInfekcija2.setExclusive(True)
        self.grInfekcija3.setExclusive(False)
        self.rInfekcija3.setChecked(False)
        self.grInfekcija3.setExclusive(True)

        self.grDiabetes.setExclusive(False)
        self.rDiabetes1.setChecked(False)
        self.rDiabetes2.setChecked(False)
        self.grDiabetes.setExclusive(True)

        self.grHipertenzija.setExclusive(False)
        self.rHiper1.setChecked(False)
        self.rHiper2.setChecked(False)
        self.grHipertenzija.setExclusive(True)

        self.grHipotenzija.setExclusive(False)
        self.rHipo1.setChecked(False)
        self.rHipo2.setChecked(False)
        self.grHipotenzija.setExclusive(True)

        self.grAstma.setExclusive(False)
        self.rAstma1.setChecked(False)
        self.rAstma2.setChecked(False)
        self.rAstma3.setChecked(False)
        self.rAstma4.setChecked(False)
        self.rAstma5.setChecked(False)
        self.grAstma.setExclusive(True)

        self.grCig.setExclusive(False)
        self.rCig1.setChecked(False)
        self.rCig2.setChecked(False)
        self.rCig3.setChecked(False)
        self.rCig4.setChecked(False)
        self.rCig5.setChecked(False)
        self.grCig.setExclusive(True)
        
        #ovde dodati Jovanin deo

        self.grDisanje.setExclusive(False)
        self.rbDisanje1.setChecked(False)
        self.rbDisanje2.setChecked(False)
        self.grDisanje.setExclusive(True)

        self.grPritisak.setExclusive(False)
        self.rbPritisak1.setChecked(False)
        self.rbPritisak2.setChecked(False)
        self.grPritisak.setExclusive(True)

        self.grPoz.setExclusive(False)
        self.rbPoz1.setChecked(False)
        self.rbPoz2.setChecked(False)
        self.grPoz.setExclusive(True)

        self.grSim.setExclusive(False)
        self.rbSim1.setChecked(False)
        self.rbSim2.setChecked(False)
        self.grSim.setExclusive(True)
    
    def greska(self, naziv):
        alert=QtWidgets.QMessageBox()
        alert.setWindowTitle("Poruka")
        alert.setText(naziv)
        alert.move(250,250)
        alert.exec_()
        
    def preporucujemo(self, naziv):
        alert=QtWidgets.QMessageBox()
        alert.setWindowTitle("Preporucujemo")
        alert.setText(naziv)
        alert.move(450,450)
        alert.exec_()


app = QtWidgets.QApplication([])
window = Gui()
app.exec_()
