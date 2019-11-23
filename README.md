# invi-mail-v2
Google 스프레드시트와 Gmail과 연동한 자동 메일 매크로

### 사용법

#### 설치
우선 이 저장소를 clone하세요.
```bash
$ git clone https://github.com/icists/invi-mail-v2.git
```

그 다음 해당 디렉토리로 이동하고
```bash
$ cd invi-mail-v2
```
가상환경을 실행하세요.
```bash
$ python -m venv .
$ cd Scripts
$ activate.bat
```

이제 패키지를 설치합니다.
```bash
$ cd ..
$ pip install -r requirements.txt
```

#### 기본 설정
프로젝트 폴더에 다음 두 개의 json 파일이 있어야 합니다.
```bash
sheet_credentials.json
gmail_credentials.json
```
```sheet_credentials.json```은 Google Sheet API와,
```gmail_credentials.json```은 Gmail API와 연동하는 credentials입니다.
Google에서 credentials를 생성하고 이름을 위와 같이 바꾸세요.

```mail.py```에서 다음 두 변수를 설정하세요.
```python
spreadsheet_url = 'your_spreadsheet_url'
DEBUG = False
```

```sheet_credentials.json```에서 ```"client_email"```에 해당하는 값을 복사하세요.
연동할 스프레드시트에서 해당 이메일로 공유하세요.

#### 실행
다음 명령어로 실행할 수 있습니다.
```$ python mail.py```

이후 다시 실행하기 위해서는 가상환경에 진입해야 합니다.
```bash
$ cd Scripts
$ activate.bat
$ cd ..
$ python mail.py
```
