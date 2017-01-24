#!/usr/bin/env python
import sys
import requests
import json
import urllib
from urlparse import urlparse

def main(med):

    #file_path = sys.argv[1]
    med = url.get()
    urllib.urlretrieve(med, "ABC.jpg")

    r = requests.post('http://api.mathpix.com/v2/latex',
        files={'file': open(ABC.jpg, 'rb')},
        headers={"app_id": "4985f625", "app_key": "4423301b832793e217d04bc44eb041d3"})
    text = r.text
    return json.dumps(json.loads(text), indent=4, sort_keys=True)
