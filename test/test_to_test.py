

#def test_1(app):
#    app.session.login("administrator", "root")
#    assert app.session.is_logged_in_as("administrator")

def test_2(app):
    #app.session.login("administrator", "root")
    l = app.pr.get_project_list()
    print(l)
