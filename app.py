from flask import Flask, render_template, request, redirect, url_for
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from calculateCar import carnumber, percarnumber
from calculateDay import calculateday
from calculateHouse import calculatehouse
from calculatePhone import phonenumber
import pandas as pd
import numpy as np

app = Flask(__name__)
cred = credentials.Certificate("webgoodnumber-firebase-adminsdk-jzi22-8258ba1e45.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://webgoodnumber-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
database = db.reference('')
database = database.child('User')
app.app_context().push()

@app.route("/")
def singup():
    return render_template("singup.html", mes="", color="light")

@app.route("/login")
def login():
    return render_template("login.html", mes="", color="light")

@app.route("/sendphone/<string:id>", methods=['POST'])
def sendphone(id):
    numberphone = request.form["numberphone"]
    try:
        sumphone, mesphone, positive_resultphone, negative_resultphone, double_num, mean_duo_af, category = phonenumber(numberphone)
        data = database.child('{0}'.format(id))
        data.update({
            'phone':numberphone, 'sumphone':sumphone, 'mesphone':mesphone, 'positive_resultphone':positive_resultphone, 
            'negative_resultphone':negative_resultphone, 'double_num':double_num, 'mean_duo_af':mean_duo_af, 'category':category
            })
        return redirect("/predictPhone/{0}".format(id))
    except:
        return redirect("/index/{0}".format(id))

@app.route("/sendcar/<string:id>", methods=['POST'])
def sendcar(id):
    numbercar = request.form["numbercar"]
    try:
        mescar = carnumber(numbercar)
        positive_resultcar, negative_resultcar = percarnumber(numbercar)
        data = database.child('{0}'.format(id))
        data.update({
            'mescar':mescar, 'car':numbercar, 'positive_resultcar':positive_resultcar, 'negative_resultcar':negative_resultcar
            })
        return redirect("/predictCar/{0}".format(id))
    except:
        return redirect("/index/{0}".format(id))

@app.route("/senddate/<string:id>", methods=['POST'])
def senddate(id):
    numberdate = request.form["numberdate"]
    try:
        mesday, mesmonth = calculateday.daynumber(numberdate)
        data = database.child('{0}'.format(id))
        data.update({
            'date':numberdate, 'mesday':mesday, 'mesmonth':mesmonth
            })
        return redirect("/predictDate/{0}".format(id))
    except:
        return redirect("/index/{0}".format(id))

@app.route("/sendhouse/<string:id>", methods=['POST'])
def sendhouse(id):
    numberhouse = request.form["numberhouse"]
    try:
        sumhouse, meshouse = calculatehouse.housenumber(numberhouse)
        data = database.child('{0}'.format(id))
        data.update({
            'house':numberhouse, 'sumhouse':sumhouse, 'meshouse':meshouse
            })
        return redirect("/predictHouse/{0}".format(id))
    except:
        return redirect("/index/{0}".format(id))

def save_image(image_file):
    image_name = image_file.filename
    image_path = os.path.join(app.root_path, "static/profile_image", image_name)
    image_file.save(image_path)
    return image_name

def splitdata(data):
    data = data[:len(data ) - 1].split(",")
    return data

@app.route("/addUser", methods=['POST'])
def addUser():
    name = request.form["name"]
    password = request.form["password"]
    file = request.files["image"]
    if len(name) == 0 or len(password) == 0:
        mes = "กรุณากรอกข้อมูลชื่อผู้ใช้หรือรหัสผ่านให้ครบถ้วน"
        color = "danger"
        return render_template("singup.html", mes=mes, color=color)
    try:
        image_file = save_image(file)
        url_for("static", filename="profile_image/"+image_file)
    except:
        profile = ['astronaut.jpg', 'charizard.jpg', 'pngtree.jpg', 'shiba.jpg', 'ninja.jpg']
        file.filename = np.random.choice(profile, 1, p=[0.2, 0.2, 0.2, 0.2, 0.2])
    add_database = database.push()
    add_database.set({
        'name': name, 'password':password, 'image':file.filename[0], 'phone':'', 'price':'', 'car':'', 
        'date':'', 'house':'', 'sumphone':'', 'sumhouse':'', 'mesphone':'', 'mescar':'', 'mesday':'', 
        'mesmonth':'', 'meshouse':'', 'double_num':'', 'mean_duo_af':'', 'category':'', 'positive_resultphone':0,
        'negative_resultphone':0, 'positive_resultcar':0, 'negative_resultcar':0, 'total_positive':0})
    data = database.get()
    for item in data:
        if name == data[item]['name'] and password == data[item]['password']:
            return redirect("/index/{0}".format(item))

@app.route("/intoUser", methods=['POST'])
def intoUser():
    name = request.form["name"]
    password = request.form["password"]
    data = database.get()
    for item in data:
        if name == data[item]['name'] and password == data[item]['password']:
            return redirect("/index/{0}".format(item))
        else:
            mes = "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"
            color = "danger"
            return render_template("login.html", mes=mes, color=color)

@app.route("/index/<string:id>")
def index(id):
    data = database.get()
    account = data[id]
    return render_template("index.html", account=account, id=id)

@app.route("/predictPhone/<string:id>")
def predictPhone(id):
    data = database.get()
    account = data[id]
    double_num = account['double_num']
    mean_duo_af = account['mean_duo_af']
    category = category = account['category']
    double_num = splitdata(double_num)
    mean_duo_af = splitdata(mean_duo_af)
    category = splitdata(category)
    data2D = []
    for loop in range(len(double_num)):
        data = {'double_num':double_num[loop], 'mean_duo_af':mean_duo_af[loop]}
        data2D.append(data)
    return render_template("predictPhone.html", account=account, data=data2D, categories=category, id=id)

@app.route("/predictCar/<string:id>")
def predictCar(id):
    data = database.get()
    account = data[id]
    return render_template("predictCar.html", account=account, id=id)

@app.route("/predictDate/<string:id>")
def predictDate(id):
    data = database.get()
    account = data[id]
    return render_template("predictDate.html", account=account, id=id)

@app.route("/predictHouse/<string:id>")
def predictHouse(id):
    data = database.get()
    account = data[id]
    return render_template("predictHouse.html", account=account, id=id)

@app.route("/dataDeveloper/<string:id>")
def dataDeveloper(id):
    data = database.get()
    account = data[id]
    return render_template("dataDeveloper.html", account=account, id=id)

@app.route("/showData/<string:id>")
def showData(id):
    data = database.get()
    account = data[id]
    total = (account['positive_resultphone'] + account['positive_resultcar']) / 2
    updata = database.child('{0}'.format(id))
    updata.update({'total_positive':total})
    number = []
    top = 0
    data = database.get().copy()
    datatop = []
    for num in data:
        number.append(data[num]['total_positive'])
    number.sort(reverse=True)
    for che in number:
        newdata = []
        top += 1
        for num in data:
            if data[num]['total_positive'] == che:
                value = data.pop(num)
                if num == id:
                    unit = top
                newdata.append(value)
                newdata.append(top)
                break
        datatop.append(newdata)
    return render_template("showData.html", account=account, data=datatop, unit=unit, id=id)

@app.route("/relationship/<string:id>")
def relationship(id):
    data = database.get()
    account = data[id]
    data_category = pd.read_csv('datacsv/counts_category.csv')
    data_double = pd.read_csv('datacsv/counts_double.csv')
    name_category = ''
    num_category = []
    price_category = []
    for loop_category in range(len(data_category.counts)):
        name_category += data_category.category[loop_category] + ","
        num_category.append(data_category.counts[loop_category])
        price_category.append(data_category.price[loop_category] // data_category.counts[loop_category])
    name_double = ''
    num_double = []
    price_double = []
    for loop_double in range(len(data_double.counts)):
        name_double += str(data_double.double[loop_double]) + ","
        num_double.append(data_double.counts[loop_double])
        price_double.append(data_double.price[loop_double] // data_double.counts[loop_double])
    return render_template("relationship.html", account=account, name_category=name_category, num_category=num_category, price_category=price_category, name_double=name_double, price_double=price_double, id=id)

if __name__ == "__main__":
    app.run(debug=True)