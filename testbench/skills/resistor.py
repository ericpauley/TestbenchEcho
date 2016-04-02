import util
from skills.skill import SkillBase

colormap = {"black":0,
"brown":1,
"red":2,
"orange":3,
"yellow":4,
"green":5,
"blue":6,
"purple":7,
"violet":7,
"grey":8,
"white":9}

revcolormap = {v: k for k, v in colormap.items()}

units = ["Ohms","KiloOhms","MegaOhms","GigaOhms"]

revunits = {"kiloohm":1000,"kiloohms":1000, "megaohm":1000000, "megaohms":1000000, "gigaohm":1000000000,"gigaohms":1000000000, "ohm":1, "ohms":1}

colorvars = ["ColorA", "ColorB", "ColorC", "ColorD"]

class Resistor(SkillBase):

    def execute(__self__, intent, session):
        session_attributes = {}
        val = 0
        colors = []
        for color in colorvars:
            if 'value' in intent['slots'][color]:
                colors.append(intent['slots'][color]['value'])
        print colors
        for color in colors[:-1]:
            val = val*10 + colormap[color]
        val = val*pow(10, colormap[colors[-1]])
        unit = 0
        while val > 1000:
            val /=1000.0
            unit += 1
        card_title = None
        speech_output = str(val)+" "+units[unit]
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class RevResistor(SkillBase):

    def execute(__self__, intent, session):
        session_attributes = {}
        card_title = None
        val = str(int(intent['slots']['value']['value']) * revunits[intent['slots']['units']['value']])
        colors = [revcolormap[int(v)] for v in val]
        while colors[-1] == "black":
            colors = colors[:-1]
        colors = colors[:3]
        colors += [revcolormap[len(val)-len(colors)]]
        speech_output = " ".join(colors)
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
