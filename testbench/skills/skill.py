from testbench import util

class SkillBase:

    def execute(__self__, intent, session):
        session_attributes = {}
        card_title = "Base Skill"
        speech_output = "I'm just a skill"
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "yeah"
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
