from flask import Flask, flash, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from helper import usernames, emails, nhl_teams, countries, animals
from forms import Form, CategoryForm, ChooseLetter
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A_Top_Secret_Key_For_Me'

lives = 5

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    register = Form()
    if request.method == "POST":
        new_id = len(usernames)+1
        usernames[new_id] = register.name.data
        emails[new_id] = register.email.data
        
        return redirect(url_for("index"))
    return render_template("register.html", register=register)

@app.route('/signIn', methods=["GET", "POST"])
def signIn():
    signIn = Form()
    if request.method == "POST":
        name = signIn.name.data
        email = signIn.email.data
        while name not in usernames.values() or email not in emails.values():
            flash("The username or email address is incorrect. Please try again!")
            return render_template("signIn.html", signIn=signIn)
        for id, username in usernames.items():
            if username == name:
                id = id
                name = username
                choice = CategoryForm()
        return render_template("setup.html", name=name, id=id, choice=choice)
    return render_template("signIn.html", signIn=signIn)

# Sets up the game variables

@app.route('/setup', methods=["GET", "POST"])
def players():
    choice = CategoryForm()
    if choice.validate_on_submit():
        global name
        if "nhl" in request.form:
            name = 'NHL Teams'
            lst = nhl_teams
        elif "countries" in request.form:
            name = "Countries"
            lst = countries
        elif "animals" in request.form:
            name = "Animals"
            lst = animals
        global word
        word = random.choice(lst)
        global hidden_word
        hidden_word = []
        for char in word:
            if char == " ":
                hidden_word.append(" /// ")
            else:
                hidden_word.append("_")
        global lives        
        lives = ["I", "I", "I", "I", "I"]
        global incorrect_letters
        incorrect_letters = []
        form = ChooseLetter()
        return render_template("game.html", category=name, form=form, lst=lst, word=word, hidden_word=hidden_word, lives=lives, incorrect_letters=incorrect_letters)
    return render_template("setup.html", choice=choice)

# Game code

@app.route('/game', methods=["GET", "POST"])
def game():
    
    message_string = ""
    form = ChooseLetter()
    
    if form.validate_on_submit():     
        letter = form.letter.data
        letter = str(letter).lower()

        # check letter against word and modify lives if necessary
        if letter not in word.lower() and letter not in incorrect_letters:
            incorrect_letters.append(letter) 
            if len(lives) == 1:
                message_string = "Too bad you lost!"
                return render_template("game_end.html", word=word, message_string=message_string)
            else:
                lives.pop()
        else:
            for i, char in enumerate(word):
                if char.lower() == letter:       
                    hidden_word[i] = char
            
        for i, char in enumerate(word):
            if char != hidden_word[i]:
                if char == " ":
                    continue
                return redirect(url_for("game", lives=lives, incorrect_letters=incorrect_letters)) 
            
        message_string = "Congrats you won!"
        return render_template("game_end.html", word=word, message_string=message_string)





    return render_template('game.html', form=form, word=word, hidden_word=hidden_word, lives=lives, category=name, incorrect_letters=incorrect_letters)


@app.route('/userChecks')
def userChecks():

    
    return render_template("userChecks.html", usernames=usernames, emails = emails )

