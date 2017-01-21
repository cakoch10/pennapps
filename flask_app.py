from flask import Flask, request, redirect
import twilio.twiml
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
    msg.media("https://chart.googleapis.com/chart?cht=tx&chl=" + request.values['Body'])
    print(request.values['Body'])
    # 'http://www.mathtran.org/cgi-bin/mathtran?D=15;tex=$x=1$'
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)