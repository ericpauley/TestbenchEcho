# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session, image=None):
    out = {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': "Reprompt"
            }
        },
        'shouldEndSession': should_end_session
    }
    if title is not None:
        out["card"] = {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        }
        if image is not None:
            out["card"]['type']="Standard"
            out["card"]["image"]={
        "smallImageUrl": image,
        "largeImageUrl": image
      }
    return out


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
