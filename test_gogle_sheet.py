import gspread
from oauth2client.service_account import ServiceAccountCredentials

def test_write_to_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("phantombuster_config.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("LinkedIn Auto Posts").sheet1
    sheet.append_row(["🚀 Test post from my automation bot!"])

if __name__ == "__main__":
    test_write_to_sheet()
