import gspread
from oauth2client.service_account import ServiceAccountCredentials

def push_to_sheet(content):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("phantombuster_config.json", scope)
    client = gspread.authorize(creds)
    
    sheet = client.open("LinkedIn Auto Posts").sheet1
    sheet.append_row([content])
