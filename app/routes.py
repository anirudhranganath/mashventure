import os
import sys
sys.path.append('../')
from flask import Flask, render_template, request
from forms import UserSearchForm
import config
 
app = Flask(__name__) 
app.secret_key = config.MV_FORM_SECRET_KEY
 
@app.route('/',methods=['GET', 'POST'])
def home():
  form = UserSearchForm()
  if request.method == 'POST':
    return 'Form posted.'
  elif request.method == 'GET':
    return render_template('home.html',form=form)
 
if __name__ == '__main__':
  app.run(debug=True)