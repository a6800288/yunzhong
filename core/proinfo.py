from flask import make_response, request, render_template, Blueprint, url_for, redirect, session
proinfo = Blueprint('proinfo', __name__ , template_folder='../core_template/templates')
from core_module.dbmongo import User,Product
from core_module.form import loginForm , productForm
import ast

@proinfo.route('/', methods=['GET', 'POST'])
def porinfo():
    loginform = loginForm()
    return render_template('proinfo.html',**locals())

@proinfo.route('/bill', methods=['GET', 'POST'])
def porbill():
    if request.method == 'POST':
        loop1 = [1]
        buydict = request.cookies.get('buydict')
        allmoney = 0
        if buydict is None :
            buyinfo = []
        else:
            buydict = ast.literal_eval(str(buydict))
            buyinfo = []
            for x in buydict:
                title = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('name')
                price = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('cost')
                much = buydict.get(x)
                tempinfo = [title,price,much]
                buyinfo.append(tempinfo)
                allmoney = allmoney + (price*much)
            loginform = loginForm()
            pform = productForm()
        return render_template('proinfo-shop03.html',**locals())

@proinfo.route('/checkit', methods=['GET', 'POST'])
def checkit():
    if request.method == 'POST':
        loop1 = [1]
        buydict = request.cookies.get('buydict')
        allmoney = 0
        if buydict is None :
            buyinfo = []
        else:
            buydict = ast.literal_eval(str(buydict))
            buyinfo = []
            for x in buydict:
                title = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('name')
                price = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('cost')
                much = buydict.get(x)
                tempinfo = [title,price,much]
                buyinfo.append(tempinfo)
                allmoney = allmoney + (price*much)
            loginform = loginForm()
            pform = productForm()
        return render_template('proinfo-shop02.html',**locals())

@proinfo.route('/checked', methods=['GET', 'POST'])
def shop1():
    loop1 = [1]
    buydict = request.cookies.get('buydict')
    allmoney = 0
    if buydict is None :
        buyinfo = []
    else:
        buydict = ast.literal_eval(str(buydict))
        buyinfo = []
        for x in buydict:
            title = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('name')
            price = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('cost')
            much = buydict.get(x)
            tempinfo = [title,price,much]
            buyinfo.append(tempinfo)
            allmoney = allmoney + (price*much)
    loginform = loginForm()
    return render_template('proinfo-shop01.html',**locals())

@proinfo.route('/show/<url>', methods=['GET', 'POST'])
def showinfo(url):
    loginform = loginForm()
    data = Product.getdata(url)
    if Product.count(str(url)) == 0 :
        return render_template('404.html',**locals())
    return render_template('proinfo-show.html',**locals())

@proinfo.route('/clear', methods=['GET', 'POST'])
def delclr():
    response = make_response(redirect(url_for('main.index')))
    response.set_cookie('num','',expires=0)
    response.set_cookie('buydict','',expires=0)
    return response


@proinfo.route('/shop', methods=['GET', 'POST'])
def shop():
    loop1 = [1]
    buydict = request.cookies.get('buydict')
    allmoney = 0
    if buydict is None :
        buyinfo = []
    else:
        buydict = ast.literal_eval(str(buydict))
        buyinfo = []
        for x in buydict:
            title = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('name')
            price = Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('cost')
            much = buydict.get(x)
            tempinfo = [title,price,much]
            buyinfo.append(tempinfo)
            allmoney = allmoney + (price*much)
    loginform = loginForm()
    return render_template('proinfo-shop.html',**locals())

@proinfo.route('/addcart',methods=['POST'])
def addcart():
    loginform = loginForm()
    num = request.cookies.get('num')
    buydict = request.cookies.get('buydict')
    for x in request.form:
        response = make_response(redirect(url_for('proinfo.showinfo',url=str(x).rsplit('-',1)[0])))

    for x in request.form:
        if int(request.form[x]) <= int(Product.getdata(str(x).rsplit('-',1)[0]).get('orderdict')[int(str(x).rsplit('-',1)[1])].get('much')):
            if num is None :
                num = 0
            if buydict is None:
                buydict = str({})
            buydict = ast.literal_eval(str(buydict))
            num = str(int(num)+int(request.form[x]))
            if buydict.get(x) == None:
                buydict[x]=0
            buydict[x] = int(buydict.get(x)) + int(request.form[x])
            buydict = dict( (x,y) for x,y in buydict.items() if y!=0)

    response.set_cookie('num',num)
    print(buydict)
    response.set_cookie('buydict',str(buydict))
    return response
