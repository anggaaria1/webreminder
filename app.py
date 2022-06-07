from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import mysql.connector

#from datbas import db, data

application=Flask(__name__)
application.config['DB_USER'] = "angga"
application.config ['DB_PASSWORD'] = 'anggaaria1'
application.config['DB_NAME'] = 'dbcuciac'
application.config['DB_HOST'] = 'localhost'

conn = cursor = None

def openDB():
    global conn, cursor
    conn = mysql.connector.connect(
        user = application.config['DB_USER'],
        password = application.config['DB_PASSWORD'],
        database = application.config['DB_NAME'],
        host= application.config['DB_HOST'],

    )
    cursor = conn.cursor()

def closeDB():
    global conn, cursor
    cursor.close()
    conn.close()


basedir = os.path.abspath(os.path.dirname(__file__))

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
@app.route("/")
def main():
    return render_template('index.html')

@app.route ('/tambah', methods=['GET','POST'])
def tambah():
    if request.method == 'POST':
        NO_LR = request.form['NO_LR']
        NAMA = request.form['NAMA']
        WA_NUMBER = request.form['WA_NUMBER']
        MODEL = request.form['MODEL']
        JENIS_PERAWATAN = request.form['JENIS_PERAWATAN']
        ALAMAT = request.form['ALAMAT']
        REQ_DATE = request.form['REQ_DATE']
        COMPLETION_DATE = request.form['COMPLETION_DATE'] 
        KETERANGAN = request.form['KETERANGAN']
        STATUS_LAPORAN = request.form['STATUS_LAPORAN']
        dataset = data(NO_LR, NAMA, WA_NUMBER, MODEL, JENIS_PERAWATAN, ALAMAT, REQ_DATE, COMPLETION_DATE, KETERANGAN, STATUS_LAPORAN)
        db.session.add(dataset)
        db.session.commit()
        return redirect(url_for('permintaan_kunjungan'))
    else:
        return render_template('/view/permintaan_kunjungan.html')


@app.route ('/ubah/<NO_LR>', methods=['GET','POST'])
def ubah(NO_LR):
    datax = data.query.filter_by(NO_LR = NO_LR).first()
    if request.method == 'POST':
        datax.NO_LR = request.form['NO_LR']
        datax.NAMA = request.form['NAMA']
        datax.WA_NUMBER = request.form['WA_NUMBER']
        datax.MODEL = request.form['MODEL']
        datax.JENIS_PERAWATAN = request.form['JENIS_PERAWATAN']
        datax.ALAMAT = request.form['ALAMAT']
        datax.REQ_DATE = request.form['REQ_DATE']
        datax.COMPLETION_DATE = request.form['COMPLETION_DATE'] 
        datax.KETERANGAN = request.form['KETERANGAN']
        datax.STATUS_LAPORAN = request.form['STATUS_LAPORAN']
        db.session.add(datax)
        db.session.commit()
        return redirect(url_for('permintaan_kunjungan'))
    else:
        return render_template('/view/permintaan_barang_update.html',data=datax)

@app.route ('/hapus/<NO_LR>', methods=['GET','POST'])
def hapus(NO_LR):
    datanya = data.query.filter_by(NO_LR= NO_LR).first()
    db.session.delete(datanya)
    db.session.commit()
    return redirect(url_for('permintaan_kunjungan'))

@app.route("/permintaan_kunjungan")
def permintaan_kunjungan():
    return render_template('/view/permintaan_kunjungan.html', menu ='master',  submenu='permintaan', container = data.query.all())

@app.route("/reminder")
def reminder():
    
    openDB()
    cursor.execute('SELECT Notification, DATE_FORMAT(Completn_date, "%d %M %Y"), List_name, Telephone FROM dbcucijaksel WHERE Completn_date BETWEEN SUBDATE(CURRENT_DATE(),INTERVAL 8 MONTH) AND NOW()')
    rows = cursor.fetchall()
    
    return render_template('/view/reminder.html', container = rows)

    #return render_template('/view/reminder.html', menu ='master', submenu='createapp')



if __name__ == "__main__":
    app.run(debug=True)


