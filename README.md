# invi-mail-v2
Google 스프레드시트와 Gmail과 연동한 자동 메일 매크로

### 사용법
Windows CMD 환경 기준으로 작성되었습니다.

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
$ Scripts\activate.bat
```

이제 패키지를 설치합니다.
```bash
$ pip install -r requirements.txt
```

#### Credentials
프로젝트 폴더에 다음 두 개의 json 파일이 있어야 합니다.
```bash
sheet_credentials.json
gmail_credentials.json
```
```sheet_credentials.json```은 Google Sheet API와,
```gmail_credentials.json```은 Gmail API와 연동하는 credentials입니다.
Google에서 credentials를 생성하고 이름을 위와 같이 바꾸세요.


#### Google 스프레드시트와 연동
본 프로그램은 Google 스프레드시트의 URL으로 해당 시트에 접근합니다.

우선 ```mail.py```에서 URL을 지정하세요.
```python
spreadsheet_url = 'your_spreadsheet_url'
```

이제, 본 매크로가 해당 시트에 접근할 수 있도록 권한을 주어야 합니다.
이를 위해, 해당 시트를 본 매크로와 공유해야 합니다.
```sheet_credentials.json```에서 ```"client_email"```에 해당하는 값을 복사해서 공유하시면 됩니다.

#### 스프레드시트의 구성

#### 실행
우선 Debug 모드가 활성화되어 있는지 확인하세요. Debug 모드에서는 메일이 전송되지 않습니다.
Debug 모드가 기본값이기 때문에, 이를 해제해주어야 합니다.
```python
DEBUG = False
```

모든 과정이 끝났다면, 이제 다음 명령어로 실행할 수 있습니다.
```$ python mail.py```

이후 다시 실행하기 위해서는 가상환경에 진입해야 합니다.
```bash
$ Scripts\activate.bat
$ python mail.py
```
