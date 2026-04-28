from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def found_click():
    seph.tot=seph.tot+50
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 Foundation (50DT)")
    seph.list.itemClicked.connect(delete)
def blu_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 blush (20dt)")
    seph.list.itemClicked.connect(delete)

def setp_click():
    seph.tot += 30
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 setting-powder (30dt)")
    seph.list.itemClicked.connect(delete)

def bron_click():
    seph.tot += 22
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 bronzer (22dt)")
    seph.list.itemClicked.connect(delete)

def con_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 concealer (20dt)")
    seph.list.itemClicked.connect(delete)

def cont_click():
    seph.tot += 22
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 contour (22dt)")
    seph.list.itemClicked.connect(delete)

def high_click():
    seph.tot += 21
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 highlighter (21dt)")
    seph.list.itemClicked.connect(delete)

def pri_click():
    seph.tot += 25
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 primer (25dt)")
    seph.list.itemClicked.connect(delete)

def sets_click():
    seph.tot += 40
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 setting-spray (40dt)")
    seph.list.itemClicked.connect(delete)

def eyes_click():
    seph.tot += 50
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 eye-shadow (50dt)")
    seph.list.itemClicked.connect(delete)

def mas_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 mascara (20dt)")
    seph.list.itemClicked.connect(delete)

def eyel_click():
    seph.tot += 25
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 eyeliner (25dt)")
    seph.list.itemClicked.connect(delete)

def correc_click():
    seph.tot += 35
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 corrector (35dt)")
    seph.list.itemClicked.connect(delete)

def fake_click():
    seph.tot += 15
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 fake-lashes (15dt)")
    seph.list.itemClicked.connect(delete)

def brows_click():
    seph.tot += 10
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 brow-pencil (10dt)")
    seph.list.itemClicked.connect(delete)

def jew_click():
    seph.tot += 10
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 eye-jewels (10dt)")
    seph.list.itemClicked.connect(delete)

def cur_click():
    seph.tot += 12
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lash-curler (12dt)")
    seph.list.itemClicked.connect(delete)

def brushes_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 brushes (20dt)")
    seph.list.itemClicked.connect(delete)

def stick_click():
    seph.tot += 35
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lipstick (35dt)")
    seph.list.itemClicked.connect(delete)

def tint_click():
    seph.tot += 15
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-tint (15dt)")
    seph.list.itemClicked.connect(delete)

def mask_click():
    seph.tot += 25
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-mask (25dt)")
    seph.list.itemClicked.connect(delete)

def gloss_click():
    seph.tot += 25
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-gloss (25dt)")
    seph.list.itemClicked.connect(delete)

def liner_click():
    seph.tot += 10
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-liner (10dt)")
    seph.list.itemClicked.connect(delete)

def scrub_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-scrubber (20dt)")
    seph.list.itemClicked.connect(delete)

def oil_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-oil (20dt)")
    seph.list.itemClicked.connect(delete)

def therapy_click():
    seph.tot += 10
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-therapy (10dt)")
    seph.list.itemClicked.connect(delete)

def liprimer_click():
    seph.tot += 32
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 lip-primer (32dt)")
    seph.list.itemClicked.connect(delete)

def toner_click():
    seph.tot += 35
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 toner (35dt)")
    seph.list.itemClicked.connect(delete)

def clean_click():
    seph.tot += 40
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 cleanser (40dt)")
    seph.list.itemClicked.connect(delete)

def moist_click():
    seph.tot += 50
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 moisturizer (50dt)")
    seph.list.itemClicked.connect(delete)

def serum_click():
    seph.tot += 70
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 serum (70dt)")
    seph.list.itemClicked.connect(delete)

def eyec_click():
    seph.tot += 55
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 eye-cream (55dt)")
    seph.list.itemClicked.connect(delete)

def suns_click():
    seph.tot += 60
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 sunscreen (60dt)")
    seph.list.itemClicked.connect(delete)

def faceo_click():
    seph.tot += 45
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 face-oil (45dt)")
    seph.list.itemClicked.connect(delete)

def facem_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 face-mask (20dt)")
    seph.list.itemClicked.connect(delete)

def mic_click():
    seph.tot += 20
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 eau-micellar (20dt)")
    seph.list.itemClicked.connect(delete)

def shampo_click():
    seph.tot += 35
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 shampoo (35dt)")
    seph.list.itemClicked.connect(delete)

def shampod_click():
    seph.tot += 45
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 dry-shampoo (45dt)")
    seph.list.itemClicked.connect(delete)

def hairsp_click():
    seph.tot += 35
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 hairspray (35dt)")
    seph.list.itemClicked.connect(delete)

def hairm_click():
    seph.tot += 55
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 hair-mask (55dt)")
    seph.list.itemClicked.connect(delete)

def haircon_click():
    seph.tot += 35
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 conditioner (35dt)")
    seph.list.itemClicked.connect(delete)

def hairo_click():
    seph.tot += 50
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 hair-oil (50dt)")
    seph.list.itemClicked.connect(delete)

def scalp_click():
    seph.tot += 50
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 scalp-scrub (50dt)")
    seph.list.itemClicked.connect(delete)

def hairb_click():
    seph.tot += 15
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 hairbrush (15dt)")
    seph.list.itemClicked.connect(delete)

def bcurl_click():
    seph.tot += 35
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 heatless-curls (35dt)")
    seph.list.itemClicked.connect(delete)

def mystery_click():
    seph.tot += 80
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 mystery box (80dt)")
    seph.list.itemClicked.connect(delete)

def full_click():
    seph.tot += 150
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 full-glam box (150dt)")
    seph.list.itemClicked.connect(delete)

def bride_click():
    seph.tot += 300
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 bride-to-be box (300dt)")
    seph.list.itemClicked.connect(delete)

def gift_click():
    seph.tot += 60
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 gift box (60dt)")
    seph.list.itemClicked.connect(delete)

def night_click():
    seph.tot += 80
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 night kit (80dt)")
    seph.list.itemClicked.connect(delete)

def mini_click():
    seph.tot += 50
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 mini set (50dt)")
    seph.list.itemClicked.connect(delete)

def custom_click():
    seph.tot += 100
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 custom kit (100dt)")
    seph.list.itemClicked.connect(delete)

def conslt_click():
    seph.tot += 60
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 consultation (60dt)")
    seph.list.itemClicked.connect(delete)

def session_click():
    seph.tot += 100
    seph.lcd.display(seph.tot)
    seph.list.addItem("-1 makeup-session (100dt)")
    seph.list.itemClicked.connect(delete)
def delete(item):

    nom = item.text()
    if nom =="-1 Foundation (50DT)":
        seph.tot-=50
    elif nom == "-1 blush (20dt)":
        seph.tot -= 20
    elif nom == "-1 setting-powder (30dt)":
        seph.tot -= 30
    elif nom == "-1 bronzer (22dt)":
        seph.tot -= 22
    elif nom == "-1 concealer (20dt)":
        seph.tot -= 20
    elif nom == "-1 contour (22dt)":
        seph.tot -= 22
    elif nom == "-1 highlighter (21dt)":
        seph.tot -= 21
    elif nom == "-1 primer (25dt)":
        seph.tot -= 25
    elif nom == "-1 setting-spray (40dt)":
        seph.tot -= 40
    elif nom == "-1 eyeshadow (50dt)":
        seph.tot -= 50
    elif nom == "-1 mascara (20dt)":
        seph.tot -= 20
    elif nom == "-1 eyeliner (25dt)":
        seph.tot -= 25
    elif nom == "-1 corrector (35dt)":
        seph.tot -= 35
    elif nom == "-1 fake-lashes (15dt)":
        seph.tot -= 15
    elif nom == "-1 brow-pencil (10dt)":
        seph.tot -= 10
    elif nom == "-1 eye-jewels (10dt)":
        seph.tot -= 10
    elif nom == "-1 lash-curler (12dt)":
        seph.tot -= 12
    elif nom == "-1 brushes (20dt)":
        seph.tot -= 20
    elif nom == "-1 lipstick (35dt)":
        seph.tot -= 35
    elif nom == "-1 lip-tint (15dt)":
        seph.tot -= 15
    elif nom == "-1 lip-mask (25dt)":
        seph.tot -= 25
    elif nom == "-1 lip-gloss (25dt)":
        seph.tot -= 25
    elif nom == "-1 lip-liner (10dt)":
        seph.tot -= 10
    elif nom == "-1 lip-scrubber (20dt)":
        seph.tot -= 20
    elif nom == "-1 lip-oil (20dt)":
        seph.tot -= 20
    elif nom == "-1 lip-therapy (10dt)":
        seph.tot -= 10
    elif nom == "-1 lip-primer (32dt)":
        seph.tot -= 32
    elif nom == "-1 toner (35dt)":
        seph.tot -= 35
    elif nom == "-1 cleanser (40dt)":
        seph.tot -= 40
    elif nom == "-1 moisturizer (50dt)":
        seph.tot -= 50
    elif nom == "-1 serum (70dt)":
        seph.tot -= 70
    elif nom == "-1 eye-cream (55dt)":
        seph.tot -= 55
    elif nom == "-1 sunscreen (60dt)":
        seph.tot -= 60
    elif nom == "-1 face-oil (45dt)":
        seph.tot -= 45
    elif nom == "-1 face-mask (20dt)":
        seph.tot -= 30
    elif nom == "-1 eau-micellar (30dt)":
        seph.tot -= 30
    elif nom == "-1 shampoo (35dt)":
        seph.tot -= 35
    elif nom == "-1 dry-shampoo (45dt)":
        seph.tot -= 45
    elif nom == "-1 hairspray (35dt)":
        seph.tot -= 35
    elif nom == "-1 hair-mask (55dt)":
        seph.tot -= 55
    elif nom == "-1 conditioner (35dt)":
        seph.tot -= 35
    elif nom == "-1 hair-oil (50dt)":
        seph.tot -= 50
    elif nom == "-1 scalp-scrub (50dt)":
        seph.tot -= 50
    elif nom == "-1 hairbrush (15dt)":
        seph.tot -= 15
    elif nom == "-1 heatless-curls (35dt)":
        seph.tot -= 35
    elif nom == "-1 mystery-box (80dt)":
        seph.tot -= 80
    elif nom == "-1 full-glam box (150dt)":
        seph.tot -= 150
    elif nom == "-1 bride-to-be box (300dt)":
        seph.tot -= 300
    elif nom == "-1 giftbox (60dt)":
        seph.tot -= 60
    elif nom == "-1 night kit (80dt)":
        seph.tot -= 80
    elif nom == "-1 mini set (50dt)":
        seph.tot -= 50
    elif nom == "-1 custom kit (100dt)":
        seph.tot -= 100
    elif nom == "-1 consultation (60dt)":
        seph.tot -= 60
    elif nom=="-1 makeup-session (100dt)":
        seph.tot -= 100
    seph.lcd.display(seph.tot)
    row=seph.list.row(item)
    seph.list.takeItem(row)
  
def clear_click():
    seph.list.clear()
    seph.tot = 0
    seph.lcd.display(seph.tot)
def DIS_click():
    if seph.tot > 150:  
        discount_amount = seph.tot * 0.1   
        seph.tot = seph.tot - discount_amount  
        seph.list.addItem(f"DISCOUNT APPLIED ({(discount_amount)}DT)")
    seph.lcd.display(seph.tot)
     
app = QApplication([])
seph = loadUi ("C:/PROJECT/SEPHORA.ui") 
seph.show()
seph.tot=0
seph.found.clicked.connect ( found_click )
seph.blu.clicked.connect ( blu_click )
seph.sets.clicked.connect ( sets_click )
seph.cont.clicked.connect ( cont_click )
seph.high.clicked.connect ( high_click )
seph.con.clicked.connect ( con_click )
seph.setp.clicked.connect ( setp_click )
seph.bron.clicked.connect ( bron_click )
seph.pri.clicked.connect ( pri_click )
seph.eyes.clicked.connect ( eyes_click )
seph.eyel.clicked.connect ( eyel_click )
seph.correc.clicked.connect ( correc_click )
seph.brows.clicked.connect ( brows_click )
seph.jew.clicked.connect ( jew_click )
seph.brushes.clicked.connect ( brushes_click )
seph.mas.clicked.connect ( mas_click )
seph.cur.clicked.connect ( cur_click )
seph.fake.clicked.connect ( fake_click )
seph.stick.clicked.connect ( stick_click )
seph.scrub.clicked.connect ( scrub_click )
seph.liprimer.clicked.connect ( liprimer_click )
seph.gloss.clicked.connect ( gloss_click )
seph.mask.clicked.connect ( mask_click )
seph.oil.clicked.connect ( oil_click )
seph.tint.clicked.connect ( tint_click )
seph.liner.clicked.connect ( liner_click )
seph.therapy.clicked.connect ( therapy_click )
seph.facem.clicked.connect ( facem_click )
seph.faceo.clicked.connect ( faceo_click )
seph.mic.clicked.connect ( mic_click )
seph.serum.clicked.connect ( serum_click )
seph.toner.clicked.connect ( toner_click )
seph.clean.clicked.connect ( clean_click )
seph.suns.clicked.connect ( suns_click )
seph.moist.clicked.connect ( moist_click )
seph.eyec.clicked.connect ( eyec_click )
seph.shampod.clicked.connect ( shampod_click )
seph.hairb.clicked.connect ( hairb_click )
seph.scalp.clicked.connect ( scalp_click )
seph.haircon.clicked.connect ( haircon_click )
seph.hairsp.clicked.connect ( hairsp_click )
seph.shampo.clicked.connect ( shampo_click )
seph.hairm.clicked.connect ( hairm_click )
seph.hairo.clicked.connect ( hairo_click )
seph.bcurl.clicked.connect ( bcurl_click )
seph.mystery.clicked.connect ( mystery_click )
seph.custom.clicked.connect ( custom_click )
seph.session.clicked.connect ( session_click )
seph.bride.clicked.connect ( bride_click )
seph.full.clicked.connect ( full_click )
seph.night.clicked.connect ( night_click )
seph.gift.clicked.connect ( gift_click )
seph.mini.clicked.connect ( mini_click )
seph.conslt.clicked.connect ( conslt_click )
seph.clear.clicked.connect ( clear_click )
seph.DIS.clicked.connect ( DIS_click )

app.exec_()