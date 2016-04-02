import json
import urllib
import util
from skills.skill import SkillBase



specMap = {"DC supply voltage": 'supply_voltage_dc'}

class OctopartTest(SkillBase):
    def execute(__self__, intent, session):
        session_attributes = {}
        val = ""
        url = 'http://octopart.com/api/v3/parts/match?'
        url += '&apikey=0c491965'
        url += '&pretty_print=false'
        url += '&queries=[{"mpn":"LF412CD"}]'
        url += '&include[]=specs'


        data = urllib.urlopen(url).read()
        response = json.loads(data)

        result = response['results'][0]
        item = result['items'][0]
        specs = item['specs']
        val = specs['supply_voltage_dc']['display_value']

        #val = response["results"][0]["items"][0]['specs'][specMap[intent['slots']['spec']['value']]]['display_value']

        speech_output = str(val)
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))



'''# print request time (in milliseconds)
print response['msec']

#print response
# print mpn's
for result in response['results']:
    for item in result['items']:
        #print item['offers'][0]['prices']
        try:
            print item['mpn']
            #print item['price']
            #print item['specs']
            print item['specs']['supply_voltage_dc']['display_value']
            print item['specs']['case_package']['display_value']
        except:
            print "this item doesn't have that attribute"
'''
