from flask import Flask, redirect, render_template, request, jsonify
from data import db_session, job_api
from data.users import User
from flask_login import *
from  flask_wtf import FlaskForm
from wtforms import *
from flask import make_response
from wtforms.validators import DataRequired
from data.jobs import Jobs
import datetime
import sqlalchemy
from data.db_session import SqlAlchemyBase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init('db/mars_explorer.db')

@app.route('/')
def base_web():
    return render_template('base.html')
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        for i in db_sess.query(User):
            print(i.email, i.hashed_password)
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        print(form.email.data, user)
        if user:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                           message="Неправильный логин или пароль",
                           form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

def main():
    pass
    # db_name = input()
    # db_session.global_init(db_name)
    # # captain = User()
    # # captain.surname = 'Scott'
    # # captain.name = "Ridley"
    # # captain.age = 21
    # # captain.position = 'captain'
    # # captain.speciality = 'research engineer'
    # # captain.address = 'module_1'
    # # captain.email = "scott_chief@mars.org"
    # #
    # # user1 = User()
    # # user1.surname = 'Ivanov'
    # # user1.name = "Pavel"
    # # user1.age = 27
    # # user1.position = 'main engineer'
    # # user1.speciality = 'spaceship engineer'
    # # user1.address = 'module_2'
    # # user1.email = "email1@email.ru"
    # #
    # # user2 = User()
    # # user2.surname = 'Smit'
    # # user2.name = "Jack"
    # # user2.age = 19
    # # user2.position = 'cleaner'
    # # user2.speciality = 'poet'
    # # user2.address = 'module_3'
    # # user2.email = "email2@email.ru"
    # #
    # # user3 = User()
    # # user3.surname = 'Green'
    # # user3.name = "Anna"
    # # user3.age = 30
    # # user3.position = 'doctor'
    # # user3.speciality = 'nurse'
    # # user3.address = 'medical office'
    # # user3.email = "email3@email.ru"
    # #
    # db_sess = db_session.create_session()
    # # db_sess.add(captain)
    # # db_sess.add(user1)
    # # db_sess.add(user2)
    # # db_sess.add(user3)
    # # db_sess.commit()
    #
    # for user in db_sess.query(User).filter(User.address == 'module_1'):
    #     print(user)



if __name__ == '__main__':
    app.register_blueprint(job_api.blueprint)
    # db_sess = db_session.create_session()
    # jobs = db_sess.query(Jobs).all()
    # for i in jobs:
    #     print(i.to_dict())
    app.run()
