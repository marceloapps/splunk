# Copyright 2020 The StackStorm Authors.
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import paramiko
import requests

from st2common.runners.base_action import Action

__all__ = [
    'SendLog'
]

class SendLogAction(Action):
    def run(self, splunk_url, index, token, event, timeout):
        event_headers = 'Authorization: Splunk ' + token
        event_payload = {'event': event}

        r = requests.post(
            url = splunk_url, 
            headers = event_headers, 
            data = event_payload,
            timeout = timeout,
            verify = False
        )

        if r.status_code == 200:
            return 0
        else:
            return 1