from .skill import SkillBase
from .welcome import Welcome

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Welcome()
