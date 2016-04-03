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

vunits = {"volts":1,"volt":1,"millivolts":.001,"millivolt":.001}

class Resistor(SkillBase):

    def execute(self, intent, session):
        val = 0
        colors = []
        for color in colorvars:
            if 'value' in intent['slots'][color]:
                colors.append(intent['slots'][color]['value'])
        for color in colors[:-1]:
            val = val*10 + colormap[color]
        val = val*pow(10, colormap[colors[-1]])
        unit = 0
        while val > 1000:
            val /=1000.0
            unit += 1
        return self.respond(str(val)+" "+units[unit])

class RevResistor(SkillBase):

    def execute(self, intent, session):
        val = str(int(intent['slots']['value']['value']) * revunits[intent['slots']['units']['value']])
        colors = [revcolormap[int(v)] for v in val]
        while colors[-1] == "black":
            colors = colors[:-1]
        colors = colors[:3]
        colors += [revcolormap[len(val)-len(colors)]]
        return self.respond(" ".join(colors))

class VoltageDivider(SkillBase):

    def execute(self, intent, session):
        image = "http://web.mit.edu/rec/www/workshop/voltage-divider.gif"+base64.b32encode(image)+".png"
        v = int(intent['slots']['vin']['value'])
        u = intent['slots']['vunits']['value']
        r1 = int(intent['slots']['resistorA']['value']) * revunits[intent['slots']['runitsA']['value']]
        r2 = int(intent['slots']['resistorB']['value']) * revunits[intent['slots']['runitsB']['value']]
        vo = v*r2/(r1 + r2)
        result = str(vo) + u
        return self.respond(result, "Voltage Divider", result, image)
