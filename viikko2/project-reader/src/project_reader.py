from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        name = data['tool']['poetry']['name']

        desc = data['tool']['poetry']['description']

        lic = data['tool']['poetry']['license']

        authors = data['tool']['poetry']['authors']

        deps = data['tool']['poetry']['dependencies'].keys()

        devdeps = data['tool']['poetry']['group']['dev']['dependencies'].keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, lic, authors, deps, devdeps)
