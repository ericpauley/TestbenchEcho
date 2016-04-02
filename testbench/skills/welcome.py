from testbench import util
from testbench.skills.skill import SkillBase

class Welcome(SkillBase):

    def execute(__self__, intent, session):
        session_attributes = {}
        card_title = "Welcome"
        speech_output = "Welcome to Double E testbench"
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "Ask me anything Double E"
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
