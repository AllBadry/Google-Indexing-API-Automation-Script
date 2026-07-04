import json
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
import google.auth.transport.requests
import google.auth.exceptions
import requests

# 1. Setup Authentication using the Service Account JSON file
SCOPES = ['https://www.googleapis.com/auth/indexing']
SERVICE_ACCOUNT_FILE = 'service_account.json'

try:
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Refresh the token for a secure API connection
    auth_request = google.auth.transport.requests.Request()
    credentials.refresh(auth_request)
    
except Exception as e:
    print(f"❌ Error in authentication file 'service_account.json': {str(e)}")
    exit()

endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# 2. Parse the local sitemap.xml and extract URLs dynamically
SITEMAP_FILE = 'sitemap.xml'
urls_to_index = []

try:
    tree = ET.parse(SITEMAP_FILE)
    root = tree.getroot()
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    for url_tag in root.findall('ns:url', namespace):
        loc_tag = url_tag.find('ns:loc', namespace)
        if loc_tag is not None and loc_tag.text:
            urls_to_index.append(loc_tag.text.strip())
            
    print(f"✅ Found {len(urls_to_index)} URLs inside '{SITEMAP_FILE}'.\n")

except FileNotFoundError:
    print(f"❌ Error: The file '{SITEMAP_FILE}' was not found in this directory.")
    exit()
except ET.ParseError:
    print(f"❌ Error: Failed to parse '{SITEMAP_FILE}'. Please verify the XML structure.")
    exit()

# 3. Send indexing requests using REST API with the Bearer Token
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {credentials.token}"
}

for url in urls_to_index:
    content = {
        "url": url,
        "type": "URL_UPDATED"
    }
    
    try:
        response = requests.post(endpoint, json=content, headers=headers)
        
        if response.status_code == 200:
            print(f"🚀 Success -> URL: {url} -> Status: {response.status_code}")
        else:
            print(f"⚠️ Failed -> URL: {url} -> Status: {response.status_code} | Response: {response.text}")
            
    except Exception as e:
        print(f"💥 Error processing URL {url}: {str(e)}")
