from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datbas import db, data

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
           'mysql://angga:anggaaria1@localhost/dbsubsitusi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)


@app.route("/")
def main():
    return render_template('index.html')

@app.route ('/tambah', methods=['GET','POST'])
def tambah():
    if request.method == 'POST':
        notifikasi = request.form['notifikasi']
        customer_name = request.form['customer_name']
        date_request = request.form['date_request']
        kerusakan = request.form['kerusakan']
        parts = request.form['parts']
        reason = request.form['reason']
        status = request.form['status']
        status_barang = request.form['status_barang'] 
        OLD_MODEL =  request.form['OLD_MODEL']
        SN_OLD =  request.form['SN_OLD']
        dataset = data(notifikasi, customer_name, date_request, kerusakan, parts, reason, status, status_barang, OLD_MODEL, SN_OLD)
        db.session.add(dataset)
        db.session.commit()
        return redirect(url_for('permintaan_barang'))
    else:
        return render_template('/view/permintaan_barang.html')

@app.route("/permintaan_barang")
def permintaan_barang():
    return render_template('/view/permintaan_barang.html', menu ='master', submenu='permintaan', container = data.query.all() )

@app.route("/create_approval")
def create_approval():
    return render_template('/view/create_approval.html', menu ='master', submenu='createapp')

@app.route("/approval_complete")
def approval_complete():
    return render_template('/view/approval_complete.html', menu ='master', submenu='appcomp')

@app.route("/ambil_barang")
def ambil_barang():
    return render_template('/view/ambil_barang.html', menu ='master', submenu='ambilbar')

@app.route("/approval_cut_budget")
def approval_cut_budget():
    return render_template('/view/approval_cut_budget.html', menu ='master', submenu='appcut')

@app.route("/jadwal_antar")
def jadwal_antar():
    return render_template('/view/jadwal_antar.html', menu ='master', submenu='jadwal')

@app.route("/cek_unit")
def cek_unit():
    return render_template('/view/cek_unit.html', menu ='master', submenu='pengecekan')

@app.route("/exchange")
def exchange():
    return render_template('/view/exchange.html', menu ='master', submenu='exchange')

@app.route("/status_repair")
def status_repair():
    return render_template('/view/status_repair.html', menu ='master', submenu='statusrep')

@app.route("/kirim_unit")
def kirim_unit():
    return render_template('/view/kirim_unit.html', menu ='master', submenu='kirim')

if __name__ == "__main__":
    app.run(debug=True)


