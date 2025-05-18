from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    user.hashed_password = '123'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    main2()


def main2():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = 'Musk'
    user.name = 'Elon'
    user.age = 53
    user.position = 'captains right hand'
    user.speciality = 'research engineer'
    user.address = 'module_2'
    user.email = 'ElonTech@mars.org'
    user.hashed_password = '123'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    main3()


def main3():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = 'Bezos'
    user.name = 'Jeff'
    user.age = 61
    user.position = 'helper'
    user.speciality = 'research engineer'
    user.address = 'module_3'
    user.email = 'Bezos@mars.org'
    user.hashed_password = '123'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_session.global_init("db/mars_explorer.db")
    main4()


def main4():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = 'Straubel'
    user.name = 'Jeffrey'
    user.age = 49
    user.position = 'helper'
    user.speciality = 'research engineer'
    user.address = 'module_4'
    user.email = 'JBSTR@mars.org'
    user.hashed_password = '123'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_session.global_init("db/mars_explorer.db")


if __name__ == '__main__':
    main()
