import util
from skills.skill import SkillBase
import redis
import json
import random
import string
import time

#scale = [.002,.005,.01,.05,.1,.5,1,2,5]
vunits = {"volts":1,"volt":1,"millivolts":.001,"millivolt":.001}
measurements = {"frequency":['FREQuency','Hertz'],"mean":['MEAN','Volts'],"period":['period','seconds'],"peak to peak voltage":['PK2pk','volts'],"rms":['CRMs','volts'],"minimum":['MINImum','volts'],"maximum":['MAXImum',"volts"],"rise":['RISe','seconds'],"fall":['FALL','seconds'],"positive pulse width":['PWIdth','seconds'],"negative pulse width":['NWIdth','seconds']}

class OSCOPEAutoset(SkillBase):

    def execute(__self__, intent, session):
        command = ['AUTOSet']
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = None
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))


class OSCOPEImage(SkillBase):

    def execute(__self__, intent, session):
        name = "".join([random.choice(string.ascii_lowercase) for i in range(10)])
        command = ['copy', name]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = "New Oscilloscope Capture"
        speech_output = "Capturing screen to the alexa app"
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        out= util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session, "https://alexasslisbogusandlame.tk/"+name+".bmp"))
        print out
        return out

class OSCOPESetVdiv(SkillBase):

    def execute(__self__, intent, session):
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
        session_attributes = {}
        card_title = None
        speech_output = None
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class OSCOPEMeasure(SkillBase):

    def execute(__self__, intent, session):
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
        session_attributes = {}
        card_title = None
        speech_output = result
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
