from flask import Flask, request, redirect
import twilio.twiml
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
    msg.media("http://www.mathtran.org/cgi-bin/mathtran?D=15;tex=$x=1$")
    print(request.values['Body'])
    # 'http://www.mathtran.org/cgi-bin/mathtran?D=15;tex=$x=1$'
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)