import util
from skills.skill import SkillBase
import redis
import json
import random
import string
import time

#scale = [.002,.005,.01,.05,.1,.5,1,2,5]
vunits = {"volts":1,"volt":1,"millivolts":.001,"millivolt":.001}
tunits = {"nanoseconds":.000000001,"nanosecond":.000000001,"microseconds":.000001,"microsecond":.000001,"milliseconds":.001,"millisecond":.001,"seconds":1,"second":1}
measurements = {"frequency":['FREQuency','Hertz'],"mean":['MEAN','Volts'],"period":['period','seconds'],"peak to peak voltage":['PK2pk','volts'],"rms":['CRMs','volts'],"minimum":['MINImum','volts'],"maximum":['MAXImum',"volts"],"rise":['RISe','seconds'],"fall":['FALL','seconds'],"positive pulse width":['PWIdth','seconds'],"negative pulse width":['NWIdth','seconds']}

class OSCOPEAutoset(SkillBase):

    def execute(self, intent, session):
        command = ['AUTOSet']
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond("Auto scaling")


class OSCOPEImage(SkillBase):

    def execute(self, intent, session):
        name = "".join([random.choice(string.ascii_lowercase) for i in range(10)])
        command = ['copy', name]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond("Capturing screen to the alexa app", "New Oscilloscope Capture", "Your capture should appear shortly.", "https://authenticspokl.tk/"+name+".png")

class OSCOPESetVdiv(SkillBase):

    def execute(self, intent, session):
        vmult = vunits[intent['slots']['vunits']['value']]
        v = vmult * int(intent['slots']['value']['value'])
        if (v >= .002) and (v <= 5):
            value = ' ' + str(v) + 'E0'
            m = 0
            if v < 1:
                while (v < 1):
                    v = v*10
                    m = m + 1
                value = ' ' + str(v) + 'E-' + str(m)
        ch = intent['slots']['channel']['value']
        command = ['CH',ch,'SCALE',value]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('Setting channel ' + ch + ' scale')

class OSCOPESetHdiv(SkillBase):

    def execute(self, intent, session):
        tmult = tunits[intent['slots']['tunits']['value']]
        t = tmult * int(intent['slots']['value']['value'])
        value = ' ' + str(t) + 'E0'
        m = 0
        if t < 1:
            while (t < 1):
                t = t*10
                m = m + 1
            value = ' ' + str(t) + 'E-' + str(m)
        command = ['horizontal','SCALe',value]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        return self.respond('Changing the horizontal scale')

class OSCOPEMeasure(SkillBase):

    def execute(self, intent, session):
        t = measurements[intent['slots']['measurement']['value']]
        ch = 'CH' + intent['slots']['channel']['value']
        command = ['measurement', '1', ch,t[0]]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        pubsub = r.pubsub()
        pubsub.subscribe("results")
        next(pubsub.listen())
        resultData = next(pubsub.listen())
        tempresult = json.loads(resultData['data'])
        value = float(tempresult)
        result = str(value) + t[1]
        return self.respond(result)
