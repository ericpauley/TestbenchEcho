from skills.skill import SkillBase
from skills.welcome import Welcome
from skills.help import Help
from skills.nullskill import NullSkill
from skills.resistor import Resistor, RevResistor

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Help()
skillmap["Welcome"] = Welcome()
skillmap["NullSkill"] = NullSkill()
skillmap["Resistor"] = Resistor()
<<<<<<< Updated upstream
skillmap["OctopartTest"] = OctopartTest()
=======
skillmap["RevResistor"] = RevResistor()
>>>>>>> Stashed changes
