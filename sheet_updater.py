import gspread
from oauth2client.service_account import ServiceAccountCredentials

def push_to_sheet(content):
  
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('/home/multi-sy-9/Desktop/Onetab/Ln_Automation/phantombuster_config.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("LinkedIn Auto Posts").sheet1 
    sheet.append_row([content])
    sheet.delete_rows(2)  # Use 1 if there are no headers
