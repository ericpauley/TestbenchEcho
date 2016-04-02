from skills.skill import SkillBase

class Welcome(SkillBase):

    def execute(self, intent, session):
        return self.respond("Welcome to Double E testbench")
