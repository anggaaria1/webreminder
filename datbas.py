from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
           'mysql://angga:anggaaria1@localhost/dbcuciac'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

class data(db.Model):
    __tablename__ = "tb_customer"
    NO_LR = db.Column(db.Integer, primary_key=True)
    NAMA = db.Column(db.String(20))
    WA_NUMBER = db.Column(db.String(15))
    MODEL = db.Column(db.String(20))
    JENIS_PERAWATAN = db.Column(db.String(20))
    ALAMAT = db.Column(db.String(20))
    REQ_DATE =  db.Column(db.Date)
    COMPLETION_DATE =  db.Column(db.Date) 
    KETERANGAN = db.Column(db.String(30))
    STATUS_LAPORAN = db.Column(db.String(2))
    
    def __init__(self, NO_LR, NAMA, WA_NUMBER, MODEL, JENIS_PERAWATAN, ALAMAT, REQ_DATE, COMPLETION_DATE, KETERANGAN, STATUS_LAPORAN):
        self.NO_LR = NO_LR
        self.NAMA = NAMA
        self.WA_NUMBER = WA_NUMBER
        self.MODEL = MODEL
        self.JENIS_PERAWATAN = JENIS_PERAWATAN
        self.ALAMAT = ALAMAT
        self.REQ_DATE = REQ_DATE
        self.COMPLETION_DATE = COMPLETION_DATE
        self.KETERANGAN = KETERANGAN
        self.STATUS_LAPORAN = STATUS_LAPORAN

    def __repr__(self):
        return '[%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,]' % \
            (self.NO_LR, self.NAMA, self.WA_NUMBER, self.MODEL, self.JENIS_PERAWATAN ,self.ALAMAT, self.REQ_DATE, self.COMPLETION_DATE,self.KETERANGAN,self.STATUS_LAPORAN)