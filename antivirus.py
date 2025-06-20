import os
import time
import requests

API_KEY = "3c756b6c49e7ad34a70ccd9569e7753cf281218a8ae19ef09f63c3d2419aeacd"
VIRUS_TOTAL_FILE_UPLOAD_URL = "https://www.virustotal.com/api/v3/files"
HEADERS = {
    "x-apikey": API_KEY
}

def scan_file(file_path):
    print(f"Scanning file: {file_path}")
    with open(file_path, 'rb') as f:
        files = {"file": (os.path.basename(file_path), f)}
        response = requests.post(VIRUS_TOTAL_FILE_UPLOAD_URL, headers=HEADERS, files=files)

    if response.status_code == 200:
        data = response.json()
        analysis_id = data['data']['id']
        get_report(analysis_id)
    else:
        print(f"Error scanning {file_path}: {response.status_code}")
        print(response.text)

def get_report(analysis_id):
    report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    
    while True:
        response = requests.get(report_url, headers=HEADERS)
        if response.status_code == 200:
            result = response.json()
            status = result["data"]["attributes"]["status"]
            if status == "completed":
                stats = result["data"]["attributes"]["stats"]
                print(f"Scan complete. Results: {stats}")
                break
            else:
                print("Scan in progress, waiting...")
                time.sleep(5)
        else:
            print(f"Failed to get report for {analysis_id}: {response.status_code}")
            break

def iterate_files(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isdir(full_path):
            iterate_files(full_path)
        else:
            scan_file(full_path)

# כאן זה שורה שמורה לסרוק את התיקייה שבה הסקריפט נמצא
iterate_files("IODtest")