from flask import Flask
from data import db_session
from data.users import User

from data.jobs import Jobs
import datetime
import sqlalchemy
from data.db_session import SqlAlchemyBase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'





def main():
    db_name = input()
    db_session.global_init(db_name)
    # captain = User()
    # captain.surname = 'Scott'
    # captain.name = "Ridley"
    # captain.age = 21
    # captain.position = 'captain'
    # captain.speciality = 'research engineer'
    # captain.address = 'module_1'
    # captain.email = "scott_chief@mars.org"
    #
    # user1 = User()
    # user1.surname = 'Ivanov'
    # user1.name = "Pavel"
    # user1.age = 27
    # user1.position = 'main engineer'
    # user1.speciality = 'spaceship engineer'
    # user1.address = 'module_2'
    # user1.email = "email1@email.ru"
    #
    # user2 = User()
    # user2.surname = 'Smit'
    # user2.name = "Jack"
    # user2.age = 19
    # user2.position = 'cleaner'
    # user2.speciality = 'poet'
    # user2.address = 'module_3'
    # user2.email = "email2@email.ru"
    #
    # user3 = User()
    # user3.surname = 'Green'
    # user3.name = "Anna"
    # user3.age = 30
    # user3.position = 'doctor'
    # user3.speciality = 'nurse'
    # user3.address = 'medical office'
    # user3.email = "email3@email.ru"
    #
    db_sess = db_session.create_session()
    # db_sess.add(captain)
    # db_sess.add(user1)
    # db_sess.add(user2)
    # db_sess.add(user3)
    # db_sess.commit()

    for user in db_sess.query(User).filter(User.address == 'module_1'):
        print(user)
    app.run()


if __name__ == '__main__':
    main()
