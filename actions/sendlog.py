import requests
from st2common.runners.base_action import Action

class SendLogAction(Action):
    def run(self, splunk_url, index, token, event):
        event_headers = 'Authorization: Splunk ' + token
        event_payload = {'event': event}

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
