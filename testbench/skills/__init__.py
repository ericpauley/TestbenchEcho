from skills.skill import SkillBase
from skills.welcome import Welcome
from skills.help import Help
from skills.nullskill import NullSkill

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Help()
skillmap["Welcome"] = Welcome()
skillmap["NullSkill"] = NullSkill()
