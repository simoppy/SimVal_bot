import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from cfg.config_load import FOLDER_ID

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_creds():
    creds = None
    if os.path.exists('cfg/token.json'):
        try:
            creds = Credentials.from_authorized_user_file('cfg/token.json', SCOPES)
        except Exception:
            os.remove('cfg/token.json')
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('cfg/token.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def upload_to_drive(file_path):
    try:
        service = build('drive', 'v3', credentials=get_creds())        
        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [FOLDER_ID]
        }
        
        media = MediaFileUpload(file_path, resumable=False)
        
        print(f"--- [Drive] Загрузка файла {os.path.basename(file_path)}... ---")
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()
        print(file.get('webViewLink'))
        
        return file.get('webViewLink')
        
    except Exception as e:
        print(f"--- [Drive] Ошибка: {e} ---")
        return None