from skills.skill import SkillBase
from skills.welcome import Welcome
from skills.help import Help, GuideToGalaxy
from skills.nullskill import NullSkill
from skills.resistor import Resistor, RevResistor, VoltageDivider
from skills.octopart import OctoSpec, OctoDescrip, OctoPrice
from skills.oscope import OSCOPEAutoset, OSCOPEImage, OSCOPESetVdiv, OSCOPEMeasure, OSCOPESetHdiv
from skills.fgen import FGENDouble, FGENHalf, FGENTriple, FGENSetFrequency, FGENSetVoltage, FGENSetVoltageOffset
from skills.wolfram import Wolfram, WolframResistor, WolframDistance, WolframCompute, WolframConvert, WolframFunction, WolframTest
from skills.devdocs import DevDocs, DevMethods

skillmap = {}
skillmap["AMAZON.HelpIntent"] = Help()
skillmap["Welcome"] = Welcome()
skillmap["NullSkill"] = NullSkill()
skillmap["Resistor"] = Resistor()
skillmap["VoltageDivider"] = VoltageDivider()
skillmap["OctoSpec"] = OctoSpec()
skillmap["OctoDescrip"] = OctoDescrip()
skillmap["OctoPrice"] = OctoPrice()
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
skillmap["WolframCompute"] = WolframCompute()
skillmap["WolframConvert"] = WolframConvert()
skillmap["WolframFunction"] = WolframFunction()
skillmap["WolframTest"] = WolframTest()
