import util
from skills.skill import SkillBase

class Help(SkillBase):

    def execute(self, intent, session):
        return self.respond("You can ask me anything about double E.")


class GuideToGalaxy(SkillBase):

    def execute(self, intent, session):
        return self.respond("42")
