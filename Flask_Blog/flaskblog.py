from flask import Flask, flash, redirect, render_template, url_for
from forms import Loginform, Registrationform

app = Flask(__name__)

app.config['SECRET_KEY']='5c2d06c9304afa76925b4b82ab092102'

posts=[
    {
        'author': 'Tuba Tosunoglu',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
    },
    {
        'author': 'Amine Asrih',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2019',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form=Registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form=Loginform()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)