from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, SelectField
 
class UserSearchForm(Form):
  activity = SelectField(u'Activity', choices=[('hiking', 'Hiking'), ('kitesurfing', 'Kite-Surfing')])
  location = TextField("Location")
  submit = SubmitField("Send")