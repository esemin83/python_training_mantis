

class Project:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href^="/mantisbt-1.2.19/manage_overview_page.php"]').click()
        wd.find_element_by_css_selector('a[href^="/mantisbt-1.2.19/manage_proj_page.php"]').click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        l = []
        for row in wd.find_elements_by_css_selector('a[href^="manage_proj_edit_page.php"]'):
            name = row.text
            l.append(name)
        return list(l)

    def delete_random_project(self, name):
        wd = self.app.wd
        self.open_project_page()
        self.select_project(name)
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_css_selector("input.button").click()

    def select_project(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()

#    def add_new_project(self, name, description):
#        wd = self.app.wd
#        self.open_project_page()
#        wd.find_element_by_css_selector('input[value= "Create New Project"]').click()
#        wd.find_element_by_name("name").click()
#        wd.find_element_by_name("name").clear()
#        wd.find_element_by_name("name").send_keys("%s" % name)
#        wd.find_element_by_name("description").click()
#        wd.find_element_by_name("description").clear()
#        wd.find_element_by_name("description").send_keys("%s" %description)
#        wd.find_element_by_css_selector("input.button").click()

    def add_new_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector('input[value= "Create New Project"]').click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("%s" % project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("%s" % project.description)
        wd.find_element_by_css_selector("input.button").click()

