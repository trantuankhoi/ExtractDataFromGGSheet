# from __future__ import print_function

import os
import io
from tqdm import tqdm

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from config import CREDENTIAL_PATH, SCOPES, SHEET_DIR, FOLDER_IDS


class DriveAPI:
    def __init__(self, cre_path, scopes):
        self.cre_path = cre_path
        self.scopes = scopes
        self.service = self.build_api()


    def build_api(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.cre_path, self.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        try:
            service = build('drive', 'v3', credentials=creds)
        except HttpError as error:
            print(f'An error occurred: {error}')

        return service

    def get_files_in_folder(self, folder_id):
        querry = f"parents in '{folder_id}' and trashed = false"
        results = self.service.files().list(supportsAllDrives=True, 
                                       includeItemsFromAllDrives=True, 
                                       q=querry, 
                                       fields = "nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        return items
    
    def download_file_by_id(self, file_id, file_name, des_path):
        request = self.service.files().export_media(fileId=file_id,
                                                 mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        pbar = tqdm(total=100, ncols=70, desc=file_name)
        while done is False:
            status, done = downloader.next_chunk()
            if status:
                pbar.update(int(status.progress() * 100) - pbar.n)
        pbar.close()

        with io.open(des_path, "wb") as f:
            file.seek(0)
            f.write(file.read())

# api = DriveAPI(cre_path=CREDENTIAL_PATH, scopes=SCOPES)
# items = api.get_files_in_folder("1Rt91uNYgtchCil5Zt53dK7S8ya0c5en_")

# for item in items:
#     id = item['id']
#     file_name = item['name']
#     file_path = os.path.join(SHEET_DIR, file_name + ".xlsx")
#     api.download_file_by_id(id, file_name, file_path)