class SkillBase:

    def respond(self, speech="", title=None, text=None, image=None):
        out = {
            'outputSpeech': {
                'type': 'PlainText',
                'text': speech
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': "Reprompt"
                }
            },
            'shouldEndSession': False
        }
        if text or title or image:
            out["card"] = {
                'type': 'Standard',
                'title': title or 'EE Testbench',
                'text': text or speech
            }
            if image:
                out["card"]["image"]={
            "smallImageUrl": image.replace("http://","https://"),
            "largeImageUrl": image.replace("http://","https://")
        }
        return self.build_response({},out)

    def build_response(self, session_attributes, speechlet_response):
        return {
            'version': '1.0',
            'sessionAttributes': session_attributes,
            'response': speechlet_response
        }

    def execute(self, intent, session):
        return self.respond("Base Skill")
