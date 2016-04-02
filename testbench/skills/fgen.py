import util
from skills.skill import SkillBase
import redis
import json
import random
import string

types = {"frequency":'frequency',"voltage":'voltage',"voltage offset":'voltageoffset'}
funits = {"Hertz":1,"kilohertz":1000,"megahertz":100000}
vunits = {"volts":1,"volt":1,"millivolts":.001,"millivolt":.001}

class FGENDouble(SkillBase):

    def execute(self, intent, session):
        t = types[intent['slots']['type']['value']]
        command = ['double', t]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('doubling the ' + t)

class FGENHalf(SkillBase):

    def execute(self, intent, session):
        t = types[intent['slots']['type']['value']]
        command = ['half', t]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('halving the ' + t)

class FGENTriple(SkillBase):

    def execute(self, intent, session):
        t = types[intent['slots']['type']['value']]
        command = ['triple', t]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('tripling the ' + t)

class FGENSetFrequency(SkillBase):

    def execute(self, intent, session):
        value = int(intent['slots']['value']['value']) * funits[intent['slots']['funits']['value']]
        command = ['frequency', str(value)]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('changing the frequency to ' + intent['slots']['value']['value'] + intent['slots']['funits']['value'])

class FGENSetVoltage(SkillBase):

    def execute(self, intent, session):
        value = int(intent['slots']['value']['value']) * vunits[intent['slots']['vunits']['value']]
        command = ['voltage', str(value)]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('changing the voltage to ' + intent['slots']['value']['value'] + intent['slots']['vunits']['value'])

class FGENSetVoltageOffset(SkillBase):

    def execute(self, intent, session):
        value = int(intent['slots']['value']['value']) * vunits[intent['slots']['vunits']['value']]
        command = ['voltageoffset', str(value)]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('changing the voltage offset to ' + intent['slots']['value']['value'] + intent['slots']['vunits']['value'])
