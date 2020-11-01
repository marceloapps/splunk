import requests
from datetime import datetime
from st2common.runners.base_action import Action

class SendLogAction(Action):
    def run(self, splunk_url, index, token, event):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        event_headers = {'Authorization': 'Splunk ' + token}
        event_payload = {'event': event, 'sourcetype': '_json', 'index': index, 'time': timestamp}

        r = requests.post(
            url = splunk_url, 
            headers = event_headers, 
            data = event_payload,
            timeout = 60,
            verify = False
        )

        if r.status_code == 200:
            return (True, r.status_code)
        else:
            return (False, r.status_code + ' ' + r.reason)
