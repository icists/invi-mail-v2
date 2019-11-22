from __future__ import print_function

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os.path

from email.mime.text import MIMEText
import base64
from time import sleep

import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from core.parser import ContentParser
from core.Invitation import Invitation

#스프레드시트의 url을 쓰세요.
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1XJYZxwkuoVx3y7QIfYku36puTGJAz8rCDSZRems5ozE/edit#gid=0'

#디버깅 여부를 적으세요.
#True일 때는 메일이 전송되지 않습니다.
DEBUG = True

def sheet_auth():
    
    """
    Google Spreadsheet과 연동하는 함수입니다.
    다음 링크를 참조하세요.
    http://hleecaster.com/python-google-drive-spreadsheet-api/
    """

    print("Preparing Sheets API...")
    scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
    ]
    creds_file = 'sheet_credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    gc = gspread.authorize(credentials)
    doc = gc.open_by_url(spreadsheet_url)
    return doc.worksheet('시트1')


def gmail_auth():

    """
    Gmail과 연동하는 함수입니다.
    다음 링크를 참조하세요.
    https://developers.google.com/gmail/api/quickstart/python
    """

    print("Preparing Gmail API...")
    SCOPES = [
            'https://www.googleapis.com/auth/gmail.send',
            'https://www.googleapis.com/auth/gmail.metadata',
    ]
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds_file = os.path.dirname(os.path.realpath(__file__)) + \
                '/gmail_credentials.json'
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def send_invi_msg(invi, service, user_id='me'):

    """
    이메일을 보내는 함수입니다.
    """

    if invi.is_eng():
        template = os.path.dirname(os.path.realpath(__file__)) + '/data/eng.json'
    else:
        template = os.path.dirname(os.path.realpath(__file__)) + '/data/kor.json'
    
    val = {
        'name': invi.name,
        'sender': invi.sender,
        'field': invi.field,
        'date': invi.date,
        'one_sen': invi.one_sen,
        'leul': invi.postposition_leul(invi.finalResonance(invi.name)),
        'yi': invi.postposition_yi(invi.finalResonance(invi.sender))
    }
    parser = ContentParser(template = template, values = val)

    subject = parser.get_title()
    print("To: {:30}\nTitle: {:40}\n".format(str(invi), parser.get_title()))

    # build msg
    msg_txt = parser.get_content()
    message = MIMEText(msg_txt, _charset = 'utf-8')
    message['subject'] = subject
    message['from'] = user_id
    message['to'] = invi.mail

    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    msg_body = {'raw': raw}

    # send message
    if not DEBUG:
        sleep(2)
        print(msg_txt)
        message = (service.users().messages().send(userId=user_id, body=msg_body).execute())
    else:
        print("[!] DEBUG Mode, mails are not sent!")
    print('--------------------------------------------------------') #divider

def main():
    #initializing
    worksheet = sheet_auth()
    gmail_credentials = gmail_auth()
    service = build('gmail', 'v1', credentials=gmail_credentials)
    print("Complete")
    print()

    data = worksheet.get_all_values()
    for i, row in enumerate(data):
        if not i: continue
        invi = Invitation(row)
        if not invi.done:
            send_invi_msg(invi, service)
            if not DEBUG:
                worksheet.update_cell(i+1, 9, 'O')


if __name__ == "__main__":
    main()