from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, SelectField
 
class UserSearchForm(Form):
  activity = SelectField(u'Activity', choices=[('','Any'),('CAMPING', 'Camping'),('PHOTOGRAPHY', 'Photography'),('HIKING', 'Hiking'), ('AUTO TOURING', 'Auto Touring'), ('BIKING', 'Biking'), ('CLIMBING', 'Climbing')])
  location = TextField("Location")
  submit = SubmitField("Send")