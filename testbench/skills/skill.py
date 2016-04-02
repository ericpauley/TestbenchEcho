import util

class SkillBase:

    def execute(__self__, intent, session):
        session_attributes = {}
        card_title = "Base Skill"
        speech_output = ""
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = ""
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
