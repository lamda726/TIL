

# telegram



### 1.2 가상환경 진입 및 설정

* 가상환경 진입

  ``` bash
  $ source venv/Scripts/activate
  ```

* VScode 자동 가상환경 진입 설정
  
  * 이 옵션을 설정하는 경우, 반드시 .vscode 



### 1.3 Flask 개발용 서버 실행

 #### 1.3.1 Flask 공식 문서로 시작하기





#### 1.3.2 서버 실행을 간편하게

공식문서에 있는대로 Flask run 명령어를 수행하면 서버가 실행된다.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 여기가 핵심!반드시 파일 최하단에 위치시킬 것!
if __name__ == '__main__':
    app.run(debug=True)
```





### 2. Telegram

* 요청

  `getMe` method를 사용해서 내 봇에 대한 정보를 받아온다.

  ```html
  https://api.telegram.org/bot<token>/getMe
  ```

* 결과값

```json
{
    "ok": true,
    "result": {
    "id": 821566613,
    "is_bot": true,
    "first_name": "wanda",
    "username": "pepawan_bot"
    }
}
```

### 3. 사용자에게 메시지 보내기

#### 3.1 사용자의 ID값 알아내기

> 사용자에게 메시지를 보내려면 사용자의 ID값을 알아야 한다.

* `gitUpdates`

  



#### 3.2 메시지 보내기



#### 3.3 Flask로 메시지 보내기



```python


```

### 4. ngrok

> 우리의 Flask서버는 현재 로컬환경에서 개발용 서버로 작동하고 있다. 그래서 텔레그램 측에 웹훅을 적용하기  위해 주소를 알려주더라도 텔레그램 측에서 우리 서버 주소로 접근을 할 수 가없다. 이를 해결하기 위해 로컬 서버 주소를 임시로 public하게 열어주는 툴인 엔그록(ngrok)을 사용해보자

#### 4.1 설치 및 파일 배치

* [ngrok공식 홈페이지](https://ngrok.com/)
* 압축 풀기 > ngrok.exe

#### 4.2 서버 실행



