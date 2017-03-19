import random
from model.project import Project


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.pr.get_project_list()) == 0:
        app.pr.add_new_project(Project('name1', 'description1'))
    old_list = app.pr.get_project_list()
    project_to_delete = random.choice(old_list)
    app.pr.delete_random_project(project_to_delete)
    new_list = app.pr.get_project_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project_to_delete)
    assert sorted(old_list) == sorted(new_list)
    print('old = ', old_list)
    print('new = ', new_list)


