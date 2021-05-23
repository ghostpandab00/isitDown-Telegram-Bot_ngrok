import requests
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def status_responses(input_text):
    user_message = str(input_text).lower()
    r = requests.head("https://" + user_message)
    
    if (r.status_code == 200) or (r.status_code == 300) or (r.status_code == 301):
        return "datz workin' fine"
    
    return "dat shitz not workin'"

