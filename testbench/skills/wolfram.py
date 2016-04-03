import xml.etree.ElementTree as ET
import urllib
import util
from skills.skill import SkillBase
import xmltodict
import base64

class Wolfram(SkillBase):

    def execute(self, intent, session):
        image = "https://www.wolframalpha.com/images/press/photos/logos/wa-logo-stacked1-large.jpg"
        session_attributes = {}
        card_title = "Wolfram"
        query = intent['slots']['query']['value']
        query.replace(' ','%20')
        url = "http://api.wolframalpha.com/v2/query?"
        url += "appid=238HJV-7G3G7G8VYU&input="
        url += query
        url += "&format=image,plaintext"
        data = urllib.urlopen(url).read()
        response = ET.fromstring(data)

        #xml_data=urllib.urlopen(url).read()
        #incomingDictData = xmltodict.parse(xml_data)
        #print incomingDictData

        speech = ""
        for pod in response.findall('.//pod'):
            if pod.attrib['title'] == 'Result' or pod.attrib['title'] == 'Circuit diagram':
                for im in pod.findall('.//img'):
                    image = im.attrib['src']
            if pod.attrib['title'] == 'Result' or pod.attrib['title'] == 'Definition' or pod.attrib['title'] == 'Equation':
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech += pt.text

        image = "https://alexasslisbogusandlame.tk/pngify/"+base64.b32encode(image)+".png"

        return util.respond(speech, "Wolfram Alpha", speech, image)

class WolframResistor(SkillBase):

    def execute(self, intent, session):
        image = "https://www.wolframalpha.com/images/press/photos/logos/wa-logo-stacked1-large.jpg"
        session_attributes = {}
        card_title = "Wolfram Resistor"
        r1 = intent['slots']['resistorA']['value']
        u1 = intent['slots']['runitA']['value']
        r2 = intent['slots']['resistorB']['value']
        u2 = intent['slots']['runitB']['value']
        op = intent['slots']['operation']['value']
        query = r1+'%20'+u1+'%20' +'in%20'+op+'%20'+r2+'%20'+u2
        url = "http://api.wolframalpha.com/v2/query?"
        url += "appid=238HJV-7G3G7G8VYU&input="
        url += query
        url += "&format=image,plaintext"
        data = urllib.urlopen(url).read()
        response = ET.fromstring(data)

        #xml_data=urllib.urlopen(url).read()
        #incomingDictData = xmltodict.parse(xml_data)
        #print incomingDictData

        speech = ""
        for pod in response.findall('.//pod'):
            if pod.attrib['title'] == 'Equation':
                for im in pod.findall('.//img'):
                    image = im.attrib['src']
            elif pod.attrib['title'] == 'Result':
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech += pt.text

        image = "https://alexasslisbogusandlame.tk/pngify/"+base64.b32encode(image)+".png"

        return util.respond(speech, "Wolfram Alpha", speech, image)

class WolframDistance(SkillBase):

    def execute(self, intent, session):
        image = "https://www.wolframalpha.com/images/press/photos/logos/wa-logo-stacked1-large.jpg"
        session_attributes = {}
        card_title = "Wolfram Distance"
        o1 = intent['slots']['objectA']['value']
        o2 = intent['slots']['objectB']['value']
        query = 'distance'+'%20'+'between%20'+o1+'%20'+'and%20'+o2
        url = "http://api.wolframalpha.com/v2/query?"
        url += "appid=238HJV-7G3G7G8VYU&input="
        url += query
        url += "&format=image,plaintext"
        data = urllib.urlopen(url).read()
        response = ET.fromstring(data)

        #xml_data=urllib.urlopen(url).read()
        #incomingDictData = xmltodict.parse(xml_data)
        #print incomingDictData

        speech = ""
        for pod in response.findall('.//pod'):
            if pod.attrib['title'] == 'History' or pod.attrib['title'] == 'Map':
                for im in pod.findall('.//img'):
                    image = im.attrib['src']
            if pod.attrib['title'] == 'Current result' or pod.attrib['title'] == 'Result':
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech = pt.text

        image = "https://alexasslisbogusandlame.tk/pngify/"+base64.b32encode(image)+".png"

        return util.respond(speech, "Wolfram Alpha", speech, image)

class WolframCompute(SkillBase):

    def execute(__self__, intent, session):
        image = "https://www.wolframalpha.com/images/press/photos/logos/wa-logo-stacked1-large.jpg"
        session_attributes = {}
        card_title = "Wolfram Computation"
        n1 = intent['slots']['numA']['value']
        n2 = intent['slots']['numB']['value']
        op = intent['slots']['operation']['value']
        query = n1+'%20'+op+'%20'+n2
        print query
        print query.replace(' ','%20')
        url = "http://api.wolframalpha.com/v2/query?"
        url += "appid=238HJV-7G3G7G8VYU&input="
        url += query.replace(' ','%20')
        url += "&format=image,plaintext"
        data = urllib.urlopen(url).read()
        response = ET.fromstring(data)

        #xml_data=urllib.urlopen(url).read()
        #incomingDictData = xmltodict.parse(xml_data)
        #print incomingDictData
        if op == 'divided by':
            speech = str(float(n1)/float(n2))
        elif:
            speech = ""
        for pod in response.findall('.//pod'):
            if pod.attrib['title'] == 'Result' or pod.attrib['title'] == 'Exact Result':
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech = pt.text

        image = "https://alexasslisbogusandlame.tk/pngify/"+base64.b32encode(image)+".png"

        return util.respond(speech, "Wolfram Alpha", speech, image)

class WolframConvert(SkillBase):

    def execute(__self__, intent, session):
        image = "https://www.wolframalpha.com/images/press/photos/logos/wa-logo-stacked1-large.jpg"
        session_attributes = {}
        card_title = "Wolfram Computation"
        n = intent['slots']['num']['value']
        u1 = intent['slots']['unitA']['value']
        u2 = intent['slots']['unitB']['value']
        query = n+'%20'+u1+'%20'+'in'+'%20'+u2
        print query
        url = "http://api.wolframalpha.com/v2/query?"
        url += "appid=238HJV-7G3G7G8VYU&input="
        url += query
        url += "&format=image,plaintext"
        data = urllib.urlopen(url).read()
        response = ET.fromstring(data)

        #xml_data=urllib.urlopen(url).read()
        #incomingDictData = xmltodict.parse(xml_data)
        #print incomingDictData

        speech = ""
        for pod in response.findall('.//pod'):
            if pod.attrib['title'] == 'Result':
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech = pt.text

        image = "https://alexasslisbogusandlame.tk/pngify/"+base64.b32encode(image)+".png"

        return util.respond(speech, "Wolfram Alpha", speech, image)

