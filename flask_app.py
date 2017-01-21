from flask import Flask, request, redirect, render_template_string, url_for
import twilio.twiml
from sympy import symbols,preview,Symbol
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from PIL import Image
import requests
from io import BytesIO

# import httplib, urllib, base64

#headers = {
#    # Request headers
#    'Content-Type': 'application/json',
#    'Ocp-Apim-Subscription-Key': '{subscription key}',
#}

#params = urllib.urlencode({
#})

#try:
#    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
#    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{body}", headers)
#    response = conn.getresponse()
#    data = response.read()
#    print(data)
#    conn.close()
#except Exception as e:
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))


app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}

@app.route("/<path:path>")
def showfile(path):
    return url_for('static',filename=path)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        mess = callers[from_number] + ", thanks for the message!"
    else:
        mess = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    msg = resp.message(mess)
    
    preview(r"$$\int_0^3 x^3 \,dx$$",viewer='file',filename='static/test.png',euler=False)
    #tempFileObj = NamedTemporaryFile(suffix='png')
    #pilImage = open('/home/linuxc/git-repos/pennapps/test.png','rb')
    #copyfileobj(pilImage,tempFileObj)
    #pilImage.close()
    

    #img = Image.open('test.png')
    #msg.media(img)
    #response = requests.get('http://www.mathtran.org/cgi-bin/mathtran?D=15;tex=$x=1$')
    #img = Image.open(BytesIO(response.content))
    msg.media(showfile('test.png'))
    print(request.values['Body'])
    # 'http://www.mathtran.org/cgi-bin/mathtran?D=15;tex=$x=1$'
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
