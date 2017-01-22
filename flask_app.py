from flask import Flask, request, redirect, render_template_string, url_for
import twilio.twiml
from sympy import symbols,preview,Symbol
import PIL
from PIL import Image
import requests
from io import BytesIO
from flask_images import resized_img_src
import os
import random
import string
import converter

dpiVal = 500

def formula_as_file( formula, file, negate=False ):
    tfile = file
    if negate:
        tfile = 'tmp.png'
    r = requests.get( 'http://latex.codecogs.com/png.latex?\dpi{dpiVal} %s' % formula )
    f = open( tfile, 'wb' )
    f.write( r.content )
    f.close()
    if negate:
        os.system( 'convert tmp.png -colorspace sRGB -type truecolor %s' %file )

app = Flask(__name__)

@app.route("/<path:path>")
def showfile(path):
    return url_for('static',filename=path)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    resp = twilio.twiml.Response()
    msg = resp.message("")
    if isinstance(request.values['Body'],str) & request.values['Body'][0] == "$":
        length = len(request.values['Body'])
        body = request.values['Body'][1:length-2]
        title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        formula_as_file( r"" + body, "static/" + title + ".png", True)
        img = Image.open('static/' + title + '.png','r')
        img_w,img_h = img.size
        background = Image.new('RGBA',(img_w+100,img_h+100),(255,255,255,255))
        bg_w,bg_h = background.size
        offset = ((bg_w - img_w)/2,(bg_h - img_h)/2)
        background.paste(img,offset)
        title2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        background.save('static/' + title2 + '.png')
        img = Image.open('static/' + title2 + '.png')
        msg.media(showfile(title2 + '.png'))

    elif NumMedia > 0:
        print "hello"
        code = converter.main(request.values['Media'])
        request.values['Body'] = code

    print(request.values['Body'])

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
