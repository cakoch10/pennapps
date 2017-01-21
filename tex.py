from __future__ import unicode_literals
from flask import Flask, request, redirect

import base64
import hashlib
import os
import shutil
import tempfile
import unittest

from PIL import Image
from webtest import TestApp

from latexrender import app

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def test_uses_previously_generated_file():
	latex = '$$ a + x = 2 $$'
	latex = base64.b64encode(latex.encode('utf-8'))
	ltx_hash = hashlib.md5(latex).hexdigest()
	file_path = os.path.join(self.output_dir, '{0}.png'.format(ltx_hash))
	img = Image.new('RGB', (5, 5))
	img.save(file_path, 'PNG')
	_, test_file = tempfile.mkstemp(prefix='latexrendertest', suffix='.png')
        img.save(test_file, 'PNG')
        try:
            resp = self.application.get(
                '/{0}/'.format(latex.decode('utf-8')), status=200)
            with open(test_file, 'rb') as f:
                self.assertEqual(resp.body, f.read())
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)

if __name__ == '__main__':
	app.run(debug=True)
