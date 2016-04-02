import xml.etree.ElementTree as ET
import urllib
import util
from skills.skill import SkillBase
import skills.xmltodict as xmltodict


class Wolfram(SkillBase):

    def execute(__self__, intent, session):
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
            speech += pod.attrib['title']
            if pod.attrib['title'] == 'Result' or pod.attrib['title'] == 'Circuit diagram':
                for im in pod.findall('.//img'):
                    image = im.attrib['src']
            if pod.attrib['title'] == 'Result' or pod.attrib['title'] == 'Definition' or pod.attrib['title'] == 'Equation':
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech += pt.text

        
        card_text = speech
        card_image = {"smallImageUrl":image,"largeImageUrl":image}
        print speech

        speech_output = speech
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class WolframResistor(SkillBase):

    def execute(__self__, intent, session):
        image = "https://www.wolframalpha.com/images/press/photos/logos/wa-logo-stacked1-large.jpg"
        session_attributes = {}
        card_title = "Wolfram Resistor"
        r1 = intent['slots']['resistorA']['value']
        u1 = intent['slots']['unitA']['value']
        r2 = intent['slots']['resistorB']['value']
        u2 = intent['slots']['unitB']['value']
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
            speech += pod.attrib['title']
            if pod.attrib['title'] == 'Equation':
                for im in pod.findall('.//img'):
                    image = im.attrib['src']
            elif pod.attrib['title'] == 'Result':
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech += pt.text

        card_text = speech
        card_image = {"smallImageUrl":image,"largeImageUrl":image}
        print speech
        print image

        speech_output = speech
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class WolframDistance(SkillBase):

    def execute(__self__, intent, session):
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
            speech += pod.attrib['title']
            if pod.attrib['title'] == 'Current result':
                for im in pod.findall('.//img'):
                    image = im.attrib['src']
                for pt in pod.findall('.//plaintext'):
                    if pt.text:
                        speech += pt.text

        card_text = speech
        card_image = {"smallImageUrl":image,"largeImageUrl":image}
        print speech
        print image

        speech_output = speech
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

