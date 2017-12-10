from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, ValidationError, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange

from .models import Contact, User, Location, Task
from lupon import db

from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField(
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ]
    )
    password = PasswordField(validators=[DataRequired(), Length(max=255)])


class UserForm(FlaskForm):
    email = StringField(
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ],
        render_kw={"placeholder": "e@ma.il", "type": "email"}
    )
    password = PasswordField('Password', validators=[DataRequired(), Length(max=255)])
    password_repeat = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=255), EqualTo('password', message='Passwords must match')])
    username = StringField('Username',validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Username"})
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City',validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State',validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = StringField('Street No.',validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = StringField('Zip',validators=[Length(max=255)], render_kw={"placeholder": "Zip"})

    eula = BooleanField('Accept License Agreement')
    submit = SubmitField('Signup!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first() is not None:
            raise ValidationError(u'This username is taken')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is not None:
            raise ValidationError(u'This email is taken')
    
 
class UserProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State',validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = StringField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = StringField('Zip', validators=[Length(max=255)], render_kw={"placeholder": "Zip"})
    submit = SubmitField('Update Profile')


class LocationForm(FlaskForm):
    pass


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ContactForm(FlaskForm):
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname = StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    email = StringField('Email', validators=[Email()], render_kw={"placeholder": "Email", "type": "email"})
    phone = StringField('Phone', validators=[Email()], render_kw={"placeholder": "Phone", "type": "tel"})
    mobile = StringField('Mobile', validators=[Email()], render_kw={"placeholder": "Mobile", "type": "tel"})
    fax = StringField('Fax', validators=[Email()], render_kw={"placeholder": "Fax", "type": "tel"})
    title = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    sex = SelectField('Sex', choices=[('m', 'Male'),('f', 'Female'),('n', 'None')], render_kw={"placeholder": "Sex"})
    add_task = SubmitField('Create')
    # homepage
    # company
    # discount
    # user_id
    # addresses

class AddressForm(FlaskForm):
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State', validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = StringField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = StringField('Zip', validators=[Length(max=255)], render_kw={"placeholder": "Zip"})


class TaskForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Name"})
    amount = FloatField('Amount', render_kw={"placeholder": "Amount"})
    value = FloatField('Value', render_kw={"placeholder": "Value"})
    unit = StringField('Unit', validators=[Length(max=255)], render_kw={"placeholder": "Unit"})
    description = StringField('Description', render_kw={"placeholder": "Description"})
    add_task = SubmitField('Add')
    update_task = SubmitField('Update')
    del_task = SubmitField('Delete')

    #def validate_name(self, field):
    #    if Task.query.filter_by(name=field.data, user_id=current_user.get_id()).first() is not None:
    #        raise ValidationError(u'This name is taken')