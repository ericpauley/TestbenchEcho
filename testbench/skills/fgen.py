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

    def execute(__self__, intent, session):
        t = types[intent['slots']['type']['value']]
        command = ['double', t]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = 'doubling the ' + t
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class FGENHalf(SkillBase):

    def execute(__self__, intent, session):
        t = types[intent['slots']['type']['value']]
        command = ['half', t]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = 'halving the ' + t
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class FGENTriple(SkillBase):

    def execute(__self__, intent, session):
        t = types[intent['slots']['type']['value']]
        command = ['triple', t]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = 'tripling the ' + t
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class FGENSetFrequency(SkillBase):

    def execute(__self__, intent, session):
        value = int(intent['slots']['value']['value']) * funits[intent['slots']['funits']['value']]
        command = ['frequency', str(value)]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = 'changing the frequency to ' + intent['slots']['value']['value'] + intent['slots']['funits']['value']
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class FGENSetVoltage(SkillBase):

    def execute(__self__, intent, session):
        value = int(intent['slots']['value']['value']) * vunits[intent['slots']['vunits']['value']]
        command = ['voltage', str(value)]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = 'changing the voltage to ' + intent['slots']['value']['value'] + intent['slots']['vunits']['value']
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class FGENSetVoltageOffset(SkillBase):

    def execute(__self__, intent, session):
        value = int(intent['slots']['value']['value']) * vunits[intent['slots']['vunits']['value']]
        command = ['voltageoffset', str(value)]
        r = redis.Redis("104.236.205.31")
        r.publish("boss",json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = 'changing the voltage offset to ' + intent['slots']['value']['value'] + intent['slots']['vunits']['value']
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

