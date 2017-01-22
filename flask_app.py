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

def formula_as_file( formula, file, negate=False ):
    tfile = file
    if negate:
        tfile = 'tmp.png'
    r = requests.get( 'http://latex.codecogs.com/png.latex?\dpi{500} %s' % formula )
    f = open( tfile, 'wb' )
    f.write( r.content )
    f.close()
    if negate:
        os.system( 'convert tmp.png -colorspace sRGB -type truecolor %s' %file )
        #os.system( 'convert tmp.png -colorspace rgb %s' %file ) <-Is grey then black
	#os.system( 'convert tmp.png -negate -colorspace (255,255,255,255) %s' %file )
        #os.system( 'convert tmp.png -channel RGB -negate -colorspace rgb %s' %file )

app = Flask(__name__)
#app.config['IMAGES_PATH']='static'


@app.route("/<path:path>")
def showfile(path):
    return url_for('static',filename=path)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    resp = twilio.twiml.Response()
    msg = resp.message("")
    
    title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    #preview(r"" + request.values['Body'] + "",viewer='file',filename='static/test.png',euler=False)
    #formula_as_file( r"\Gamma_{Levin}(x) = \| \nabla p(x) \|_2^{0.8} + \sum_i |\frac{\partial^2 p(x)}{\partial x_i^2}|^{0.8}", "static/" + title + ".png", True)
    formula_as_file( r"" + request.values['Body'], "static/" + title + ".png", True)
    
    
    img = Image.open('static/' + title + '.png','r')
    img_w,img_h = img.size
    background = Image.new('RGBA',(img_w+100,img_h+100),(255,255,255,255))
    bg_w,bg_h = background.size
    offset = ((bg_w - img_w)/2,(bg_h - img_h)/2)
    background.paste(img,offset)
   
    title2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
   
    background.save('static/' + title2 + '.png')
    basewidth = 80
    #wpercent = (basewidth/float(img.size[0]))
    #hsize = float(img.size[1]*float(wpercent))
    
    #img = img.resize((80,40),PIL.Image.ANTIALIAS)
    #img.save('static/test2.png', 'PNG', quality=90)
    
    img = Image.open('static/' + title2 + '.png')
    
    #msg.media(img)
    #response = requests.get('http://www.mathtran.org/cgi-bin/mathtran?D=15;tex=$x=1$')
    #img = Image.open(BytesIO(response.content))
    #msg.media(resized_img_src(showfile('test.png'),width=50,height=50))..
    msg.media(showfile(title2 + '.png'))
    #msg.media(resized_img_src('test.png',width=50,height=50))
    print(request.values['Body'])
    # 'http://www.mathtran.org/cgi-bin/mathtran?D=15;tex=$x=1$'
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
