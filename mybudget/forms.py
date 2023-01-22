from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[('groceries','Groceries'), ('transportation','Transportation'), ('entertainment','Entertainment'), ('other','Other')])
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    account = SelectField('Account', choices=[('cash','Cash'), ('credit_card','Credit Card'), ('bank_account','Bank Account')])

class IncomeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[('salary','Salary'), ('investment','Investment'), ('other','Other')])
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    account = SelectField('Account', choices=[('cash','Cash'), ('credit_card','Credit Card'), ('bank_account','Bank Account')])
