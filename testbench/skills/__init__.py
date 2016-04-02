from skills.skill import SkillBase
from skills.welcome import Welcome
from skills.help import Help

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Help()
skillmap["Welcome"] = Help()
