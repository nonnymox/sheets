sheet_id = "1TNXMEqEoD2yWTJK4qCIE-VFaQud6CSZ13DSCJckVVX4"

import os
from google.oauth2.service_account import Credentials

from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = "C:/Users/knonx/Documents/Projects 2025/sheets/recruiter.json"


credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()

range = 'A1:A10'

sheet_read = sheet.values().get(spreadsheetId=sheet_id, range=range).execute()

values= sheet_read.get('values', [])
for row in values:
    print(row)