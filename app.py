from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from calculateCar import carnumber, percarnumber
from calculateDay import calculateday
from calculateHouse import calculatehouse
from calculatePhone import phonenumber
import pandas as pd
import numpy as np
import requests

app = Flask(__name__)
cred = credentials.Certificate("webgoodnumber-firebase-adminsdk-jzi22-8258ba1e45.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://webgoodnumber-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
database = db.reference('')
database = database.child('User')
commentU = db.reference('')
commentU = commentU.child('Comment')
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

def splitdata(data):
    data = data[:len(data ) - 1].split(",")
    return data

@app.route("/addUser", methods=['POST'])
def addUser():
    name = request.form["name"]
    password = request.form["password"]
    file = request.form["image"]
    if len(name) == 0 or len(password) == 0:
        mes = "กรุณากรอกข้อมูลชื่อผู้ใช้หรือรหัสผ่านให้ครบถ้วน"
        color = "danger"
        return render_template("singup.html", mes=mes, color=color)
    imgefile = file
    imgefile_che = requests.get(file)
    if str(imgefile_che) != '<Response [200]>':
        profile = ['astronaut.jpg', 'charizard.jpg', 'pngtree.jpg', 'shiba.jpg', 'ninja.jpg', 'lufy.jpg', 'pan.jpg', 'pika.jpg', 'tttttt.jpg', 'pikaju.jpg']
        filename = np.random.choice(profile, 1, p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
        imgefile = '../static/profile_image/' + filename[0]
    add_database = database.push()
    add_database.set({
        'name': name, 'password':password, 'image':imgefile, 'phone':'', 'car':'', 
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

@app.route("/showData/<string:id>", methods=['GET' ,'POST'])
def showData(id):
    data = database.get()
    account = data[id]
    name = account['name']
    image = account['image']
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
    try:
        com = request.form["description"]
        if len(com) != 0:
            comment = commentU.push()
            comment.set({'name':name, 'image':image, 'com':com})
    except:
        pass
    comment = commentU.get()
    sort_com = []
    for num in comment:
        sort_com.append(comment[num])
    comment = sort_com[::-1]
    return render_template("showData.html", comment=comment, account=account, data=datatop, unit=unit, id=id)

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