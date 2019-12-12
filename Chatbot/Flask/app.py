import random
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '어서와^^'
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mulcam')
def mulcam():
    return '20층 스카이라운지 뷰맛집!'

@app.route('/dday')
def dday():
    today = datetime.now()
    new_year = datetime(2020,1,1)
    result = new_year - today
    return f'<h1>더 성숙해지기까지 {result.days}일 남았습니다!</h1>'

@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'반갑습니다, {name}님!:)'
    # return render_template('greeting.html',html_name=name)
    return render_template('greeting.html',html_name=name)

@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    #return f'{number}의 세제곱의 값은 {number**3}입니다!:)'
    return render_template('cube.html', number=number,
    result=result)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['아이스크림','피자','쫄면','샐러드','라떼','냉채족발']
    order = random.sample(menu, people)
    return str(order)

@app.route('/movie')
def movie():
    movies = ['나이브스아웃','조커','엔드게임']
    return render_template('movie.html',
    movie_list=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template("google.html")

# 사용자로부터 입력 받을 페이지를 랜더링해줌
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/myresult')
def myresult():
    name = request.args.get('name')
    # 데이터 리스트
    option_one = ['잘생김','아름다움','귀여움','씩씩함','못생김']
    option_two = ['자상함','친절함','싸가지','당당함','소심함']
    option_three = ['체력','똑똑함','허당','잠만보','식욕']
    # 각 데이터 리스트 별로 요소를 하나씩 무작위로 뽑음
    # sample 사용할 경우(list 형태로 들어옴)
    # result1 = random.sample(option_one,1)
    # result2 = random.sample(option_two,1)
    # result3 = random.sample(option_three,1)
    
    # choice 사용할 경우(str 형태로 들어옴)
    result1 = random.choice(option_one)
    result2 = random.choice(option_two)
    result3 = random.choice(option_three)
    # 뽑은 데이터를 템플릿에 넘겨줌
    return render_template('myresult.html', name=name, result1=result1, result2=result2, result3=result3)

# app.py 가장 하단에 위치
# 1. 앞으로 flask run으로 서버를 켜는게 아니라 pythonapp.py로 서버를 실행한다.
# 2. 내용이 바뀌어도 서버를 껐다 켜지 않아도 된다.
if __name__=="__main__":
    app.run(debug=True)