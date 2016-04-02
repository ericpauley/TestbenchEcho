from skills.skill import SkillBase
from skills.welcome import Welcome
from skills.help import Help
from skills.nullskill import NullSkill
from skills.resistor import Resistor, RevResistor
from skills.octospec import OctoSpec
from skills.oscope import OSCOPEAutoset, OSCOPEImage, OSCOPESetVdiv, OSCOPEMeasure
from skills.fgen import FGENDouble, FGENHalf, FGENTriple

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Help()
skillmap["Welcome"] = Welcome()
skillmap["NullSkill"] = NullSkill()
skillmap["Resistor"] = Resistor()
skillmap["OctoSpec"] = OctoSpec()
skillmap["RevResistor"] = RevResistor()
skillmap["OSCOPEImage"] = OSCOPEImage()
skillmap["OSCOPEAutoset"] = OSCOPEAutoset()
skillmap["OSCOPESetVdiv"] = OSCOPESetVdiv()
skillmap["OSCOPEMeasure"] = OSCOPEMeasure()
skillmap["FGENDouble"] = FGENDouble()
skillmap["FGENHalf"] = FGENHalf()
skillmap["FGENTriple"] = FGENTriple()