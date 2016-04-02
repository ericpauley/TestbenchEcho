from skills.skill import SkillBase
from skills.welcome import Welcome
from skills.help import Help, GuideToGalaxy
from skills.nullskill import NullSkill
from skills.resistor import Resistor, RevResistor
from skills.octopart import OctoSpec, OctoDescrip
from skills.oscope import OSCOPEAutoset, OSCOPEImage, OSCOPESetVdiv, OSCOPEMeasure, OSCOPESetHdiv
from skills.fgen import FGENDouble, FGENHalf, FGENTriple, FGENSetFrequency, FGENSetVoltage, FGENSetVoltageOffset
from skills.wolfram import Wolfram, WolframResistor, WolframDistance

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Help()
skillmap["Welcome"] = Welcome()
skillmap["NullSkill"] = NullSkill()
skillmap["Resistor"] = Resistor()
skillmap["OctoSpec"] = OctoSpec()
skillmap["OctoDescrip"] = OctoDescrip()
skillmap["RevResistor"] = RevResistor()
skillmap["OSCOPEImage"] = OSCOPEImage()
skillmap["OSCOPEAutoset"] = OSCOPEAutoset()
skillmap["OSCOPESetVdiv"] = OSCOPESetVdiv()
skillmap["OSCOPESetHdiv"] = OSCOPESetHdiv()
skillmap["OSCOPEMeasure"] = OSCOPEMeasure()
skillmap["FGENDouble"] = FGENDouble()
skillmap["FGENHalf"] = FGENHalf()
skillmap["FGENTriple"] = FGENTriple()
skillmap["FGENSetFrequency"] = FGENSetFrequency()
skillmap["FGENSetVoltage"] = FGENSetVoltage()
skillmap["FGENSetVoltageOffset"] = FGENSetVoltageOffset()
skillmap["GuideToGalaxy"] = GuideToGalaxy()
skillmap["Wolfram"] = Wolfram()
skillmap["WolframResistor"] = WolframResistor()
skillmap["WolframDistance"] = WolframDistance()
