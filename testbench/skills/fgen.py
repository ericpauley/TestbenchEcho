import util
from skills.skill import SkillBase
import redis
import json
import random
import string

types = {"frequency":'frequency',"voltage":'voltage',"voltage offset":'voltageoffset'}

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

