import util
from skills.skill import SkillBase

class NullSkill(SkillBase):

    def execute(self, intent, session):
        return self.respond("")
