from suds.client import Client
from suds import WebFault
from model.project import Project
import time


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_client(self):
        client = Client(self.app.config['soap']['wsdl'])
        return client

    def can_login(self, username, password):
        client = self.get_client()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_version(self):
        client = self.get_client()
        try:
            ver = client.service.mc_version()
            return ver
        except WebFault:
            return "Fault"

    def get_projects(self):
        #client = Client(self.app.config['soap']['wsdl'])
        client = self.get_client()
        projects = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
                                                                  self.app.config['webadmin']['password'])
        project_list = []
        for project in projects:
            id = str(project.id)
            name = str(project.name)
            project_list.append(Project(id=id, name=name))
        time.sleep(0)
        return list(project_list)

# mc_enum_project_view_states
# mc_projects_get_user_accessible
