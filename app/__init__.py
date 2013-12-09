import os
import sys
sys.path.append('../')
from flask import Flask, render_template, request
from forms import UserSearchForm
import config
import urllib
from modules.Search import PageInfoSearch,UserFormSearch

app = Flask(__name__) 
app.secret_key = config.MV_FORM_SECRET_KEY
 
@app.route('/',methods=['GET', 'POST'])
def home():
  form = UserSearchForm()
  if request.method == 'POST':
    return 'Form posted.'
  elif request.method == 'GET':
    return render_template('home.html',form=form)

@app.route('/search',methods=['GET'])
def search():
    location = request.args.get('location')
    activity = request.args.get('activity')
    results = UserFormSearch.user_form_search_activity_location(activity,location)
    return render_template('search.html',query = activity + location,results = results,urllib=urllib)

@app.route('/page',methods=['GET'])
def page():
    site = request.args.get('site')
    siteinfo = PageInfoSearch.page_info(urllib.unquote(site).decode())
    return render_template('page.html',siteinfo = siteinfo)

if __name__ == '__main__':
  app.run(debug=True)