import random
import string
from model.project import Project


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*2
    return "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])

project = Project(random_string(15), random_string(15))


def test_add_new_project(app):
    #app.session.login("administrator", "root")
    old_list = app.pr.get_project_list()
    app.pr.add_new_project(project)
    new_list = app.pr.get_project_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(project.name)
    print('old = ', old_list)
    print('new = ', new_list)
    assert sorted(new_list) == sorted(old_list)


def test_add_new_project_soap(app):
    #app.session.login("administrator", "root")
    old_list = app.soap.get_projects()
    app.pr.add_new_project(project)
    new_list = app.soap.get_projects()
    pr_id = sorted(new_list, key=Project.id_or_max)[-1].id
    assert len(old_list) + 1 == len(new_list)
    old_list.append(Project(name=project.name, id=pr_id))
    print('\n' 'old = ', sorted(old_list, key=Project.id_or_max))
    print('new = ', sorted(new_list, key=Project.id_or_max))
    assert sorted(new_list, key=Project.id_or_max) == sorted(old_list, key=Project.id_or_max)
