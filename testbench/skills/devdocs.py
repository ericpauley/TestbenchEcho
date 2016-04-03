import json
import urllib
import util
import base64
from skills.skill import SkillBase


class DevDocs(SkillBase):
    def execute(self, intent, session):

        api = str(intent['slots']['api']['value'])


        response = api
        return self.respond(response)

class DevMethods(SkillBase):
    def execute(self, intent, session):

        api = str(intent['slots']['api']['value'])
        method = str(intent['slots']['method']['value'])

        response = api + method
        return self.respond(response)
