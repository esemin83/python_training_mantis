import random
import string


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*2
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])


def test_sing_up_new_account(app):
    app.session.login("administrator", "root")
    username = random_name("user_", 10)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.singup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()


def test_sing_up_new_account_soap(app):
    #app.session.login("administrator", "root")
    username = random_name("user_", 15)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.singup.new_user(username, email, password)
    assert app.soap.can_login(username, password)
