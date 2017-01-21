import os
from urlparse import urlparse
from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP

from twilio.rest import TwilioRestClient

host, port = urlparse(os.environ["http_proxy"]).netloc.split(":")
Connection.set_proxy_info(
    host,
    int(port),
    proxy_type=PROXY_TYPE_HTTP,
)

# put your own credentials here
ACCOUNT_SID = "AC514060b3911159eb3a64f82778c386d8"
AUTH_TOKEN = "2a7547e5c0424fa28a3f14bf83f3f9b7"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+17328060305",
    from_="+17322534903",
    body="LaTeX",
    media_url="http://www.forkosh.com/mathtex.cgi?c=\sqrt{a^2+b^2}",
)
