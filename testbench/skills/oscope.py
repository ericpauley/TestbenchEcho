import util
from skills.skill import SkillBase
import redis
import json

class OSCOPEAutoset(SkillBase)

    def execute(__self__, intent, session):
        command = ['AUTOSet']
        r = redis.Redis("104.236.205.31")
        r.publish("boss", json.dumps(command))
        session_attributes = {}
        card_title = None
        speech_output = None
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
        
