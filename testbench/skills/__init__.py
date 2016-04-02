from skills.skill import SkillBase
from skills.welcome import Welcome
from skills.help import Help
from skills.nullskill import NullSkill
from skills.resistor import Resistor, RevResistor
from skills.OctopartTest import OctopartTest
from skills.oscope import OSCOPEAutoset, OSCOPEImage

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Help()
skillmap["Welcome"] = Welcome()
skillmap["NullSkill"] = NullSkill()
skillmap["Resistor"] = Resistor()
skillmap["OctopartTest"] = OctopartTest()
skillmap["RevResistor"] = RevResistor()
skillmap["OSCOPEImage"] = OSCOPEImage()
skillmap["OSCOPEAutoset"] = OSCOPEAutoset()
