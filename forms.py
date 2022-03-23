from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    name = StringField("Please enter a username: ", validators=[DataRequired()])
    email = StringField("Please enter an email address: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CategoryForm(FlaskForm):
    nhl = SubmitField("NHL Teams")
    countries = SubmitField("Countries")
    animals = SubmitField("Animals")

class ChooseLetter(FlaskForm):
    letter = StringField("Please enter a letter: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

