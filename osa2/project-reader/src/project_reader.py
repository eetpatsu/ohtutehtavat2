from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print("Content", content)

        sisalto = tomllib.loads(content)
        # print("Deserialisoitu", sisalto)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            sisalto['tool']['poetry']['name'],
            sisalto['tool']['poetry']['description'],
            sisalto['tool']['poetry']['license'],
            sisalto['tool']['poetry']['authors'],
            list(sisalto['tool']['poetry']['dependencies'].keys()),
            list(sisalto['tool']['poetry']['group']['dev']['dependencies'].keys())
        )
