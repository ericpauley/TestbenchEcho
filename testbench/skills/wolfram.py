import xml.etree.ElementTree as ET
import urllib
import util
from skills.skill import SkillBase
import skills.xmltodict as xmltodict

image = "https://www.wolframalpha.com/images/press/photos/logos/wa-logo-stacked1-large.jpg"

class Wolfram(SkillBase):

    def execute(__self__, intent, session):
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
            for pt in pod.findall('.//plaintext'):
                if pt.text:
                    speech += pt.text

        card_image = {"smallImageUrl":image,"largeImageUrl":image}
        card_text = speech
        print speech

        speech_output = speech
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
