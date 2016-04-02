import util
from skills.skill import SkillBase
import redis
import json
import random
import string

#scale = [.002,.005,.01,.05,.1,.5,1,2,5]
vunits = {"volts":1,"volt":1,"millivolts":.001,"millivolt":.001}

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
        name = "".join([random.choice(string.ascii_lowercase) for i in range(1)])
        command = ['copy', name]
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

class OSCOPESetVdiv(SkillBase):

    def execute(__self__, intent, session):
        vmult = vunits[intent['slots']['vunits']['value']]
        v = vmult * intent['slots']['value']['value']
        print v
        if (v >= .002) and (v <= 5):
            value = ' ' + str(v) + 'E0'
            m = 0
            if v < 1:
                while (v < 1):
                    v = v*10
                    m = m + 1
                value = ' ' + str(v) + 'E-' + str(m)
        ch = intent['slots']['channel']['value']
        command = ['CH',str(ch),'SCALE',value]
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
