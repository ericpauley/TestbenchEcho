import json
import urllib
import util
from skills.skill import SkillBase



specMap = {
"access time": 'access_time',
"actuator length": 'actuator_length',
"actuator type": 'actuator_type',
"antenna connection":'antenna_connection',
"architecture": 'architecture',
"available channels": 'available_channels',
"bandwidth": 'bandwitdth',
"bits": 'bits',
"breakdown voltage": 'breakdown_voltage',
"drain to source breakdown voltage": 'breakdown_voltage_drain_to_source',
"collector to base breakdown voltage": 'breakdown_voltage_collector_to_base',
"collector to emitter breakdown voltage": 'breakdown_voltage_collector_to_emitter',
"gate to source breakdown voltage":'breakdown_voltage_gate_to_source',
"cable length": 'cable_length',
"capacitance": 'capacitance',
"capactiance tolerance": 'capacitance_tolerance',
"capacitance per foot": 'capacitance_per_foot',
"carry current": 'carry_current',
"SI case package": 'case_package_si',
"case package": 'case_package',
"character height": 'character_size_height',
"character width": 'character_size_width',
"china ROHS": 'china_rohs',
"clock speed": 'clock_speed',
"coil current": 'coil_current',
"AC coil power": 'coil_power_ac',
"DC coil power": 'coil_power_dc',
"coil resistance": 'coil_resistance',
"coil voltage": 'coil_voltage',
"AC coil voltage": 'coil_voltage_ac',
"color": 'color',
"common mode rejection ratio": 'cmrr',
"conductor material": 'conductor_material',
"contact current rating": 'contact_current_rating',
"contact material": 'contact_material',
"contact plating": 'contact_plating',
"contact resistance": 'contact_resistance',
"contact syle": 'contact_style',
"DC contact voltage rating": 'contact_voltage_rating_dc',
"contacts type": 'contacts_type',
"continuous drain current": 'id_continuous_drain_current',
"cord length": 'cord_length',
"core": 'core',
"core architecture": 'core_architecture',
"core size": 'core_size',
"core sub architecture": 'core_subarchitecture',
"current rating": 'current_rating',
"data rate": 'data_rate',
"dielectric characteristic": 'dialectric_characteristic',
"dielectric material": 'dialectric_material',
"dielectric strength": 'dialectric_strength',
"dielectric withstanding voltage": 'dialectric_withstanding_voltage',
"digital logic level": 'logic_type',
"drain to gate voltage": 'vdg_drain_to_gate_voltage',
"drain to source resistance": 'rds_drain_to_source_resistance_on',
"drain to source voltage": 'vds_drain_to_source_voltage',
"drivers per package": 'drivers_per_package',
"dropout voltage": 'dropout_voltage',
"ELV compliant": 'elv_compliant',
"equivalent series resistance": 'equivalent_series_resistance_esr',
"flash memory size": 'flash_memory_bytes',
"fram memory size": 'fram_memory_bytes',
"flammability rating": 'flammability_rating',
"forward current": 'forward_current',
"forward voltage": 'forward_voltage',
"frequency": 'frequency',
"frequency stability": 'frequency_stability',
"frequency tolerance": 'frequency_tolerance',
"gain": 'gain',
"gain bandwidth product": 'gbw',
"gate charge": 'gate_charge',
"gate to source threshold voltage": 'gate_to_source_threshold_voltage',
"gender": 'gender',
"glow wire compliant": 'glow_wire_compliant',
"halogen free status": 'halogen_free_status',
"holding current": 'holding_current',
"housing color": 'housing_color',
"housing material": 'housing_material',
"housing type": 'housing_type',
"inductance": 'inductance',
"inductance tolerance": 'inductance_tolerance',
"input bias current": 'input_bias_current',
"input capacitance": 'input_capacitance',
"input current": 'input_current',
"input impedance": 'input_impedance',
"input offset drift": 'input_offset_drift',
"input offset voltage": 'input_offset_voltage',
"input power": 'input_power',
"DC input voltage": 'input_voltage_dc',
"insulation material": 'insulation_material',
"insulation resistance": 'insulation_resistance',
"isolation voltage": 'isolation_voltage',
"jacket material": 'jacket_material',
"lead length": 'lead_length',
"lead free status": 'lead_free_status',
"lens color": 'lens_color',
"lens type": 'lens_type',
"lifecycle status": 'lifecycle_status',
"load capacitance": 'load_capacitance',
"load current": 'load_current',
"luminous intensity": 'luminous_intensity',
"mated height": 'mated_height',
"material": 'material',
"memory size": 'memory_size',
"mil spec": 'mil_spec',
"mounting angle": 'moutning_angle',
"mounting type": 'mounting_type',
"negative supply voltage": 'negative_supply_voltage',
"number of ADCs": 'number_of_adcs',
"number of bits": 'number_of_bits',
"number of channels": 'number_of_channels',
"number of circuits": 'number_of_circuits',
"number of conductors": 'number_of_conductors',
"number of contacts": 'number_of_contacts',
"number of DACs": 'number_of_dacs',
"number of detents": 'number_of_detents',
"number of fibers": 'number_of_fibers',
"number of gates": 'number_of_gates',
"number of I oh pins": 'number_of_i_o_pins',
"number of mating cycles": 'number_of_mating_cycles',
"number of outlets": 'number_of_outlets',
"number of outputs": 'number_of_outputs',
"number of pins": 'number_of_pins',
"number of positions": 'number_of_positions',
"number of regulated outputs": 'number_of_regulated_outputs',
"number of rows": 'number_of_rows',
"number of slots": 'number_of_slots',
"number of UARTs": 'number_of_uart',
"operating force": 'operating_force',
"operating temperature": 'operating_temperature',
"operating voltage": 'operating_voltage',
"orientation": 'orientation',
"oscillator type": 'oscillator_type',
"output capacitor capacitance": 'output_capacitor_capacitance',
"output capacitor type": 'output_capacitor_type',
"output current": 'output_current',
"output current drive": 'output_current_drive',
"output power": 'output_current',
"output type": 'output_type',
"output voltage": 'output_voltage',
"packaging": 'packaging',
"part family": 'part_family',
"peak wavelength": 'peak_wavelength',
"pin pitch": 'pin_pitch',
"polarity": 'polarity',
"positive supply voltage": 'positive_supply_voltgae',
"power consumption": 'power_cosumption',
"power dissipation": 'power_dissipation',
"power rating": 'power_rating',
"power supply rejection ratio": 'psrr',
"processor type":'processor_type',
"propogation delay max": 'propagation_delay_max',
"Q factor": 'q_factor',
"quiescent current": 'quiescent_current',
"ram memory size":'ram_bytes',
"reach SVHC compliance": 'reach_svhc_compliance',
"release force": 'release_force',
"resistance": 'resistance',
"resistance tolerance": 'resistance_tolerance',
"resolution in bits": 'resolution_bits',
"resolution in pulses per revolution": 'resolution_bits_revlution',
"resonant frequency": 'resonant_frequency',
"rise time": 'rise_time',
"rise fall time": 'rise_fall_time',
"ROHS": 'rohs',
"sample rate": 'sample_rate',
"seal": 'seal',
"self resonant frequency": 'self_resonant_frequency',
"settling time": 'settling_time',
"shielding": 'shielding',
"shielding type": 'shielding_type',
"shrouded": 'shrouded',
"size diameter": 'size_diameter',
"size height": 'size_height',
"size inner diameter": 'size_inner_diameter',
"size length": 'size_length',
"size thickness": 'size_thickness',
"size width": 'size_width',
"slew rate": 'slew_rate',
"standby current": 'standby_current',
"static current": 'static_current',
"supply current": 'supply_current',
"supply current per channel": 'supply_current_per_channel',
"AC supply voltage": 'supply_voltage_ac',
"DC supply voltage": 'supply_voltage_dc',
"switching current": 'switching_current',
"switching frequency": 'switching_frequency',
"switching voltage": 'switching_voltage',
"temperature coefficient": 'temperature_coefficient',
"termination style": 'termination_style',
"test text attribute": 'test_text_attribute',
"thermal resistance": 'thermal_resistance',
"thermal shutdown": 'thermal_shutdown',
"threshold voltage": 'threshold_voltage',
"time to trip": 'time_to_trip',
"topology": 'topology',
"tripping current": 'tripping_current',
"viewing angle": 'viewing_angle',
"voltage nodes": 'voltage_nodes',
"AC voltage rating": 'voltage_rating_ac',
"DC voltage rating": 'voltage_rating_dc',
"transient voltage rating": 'voltage_rating_transient',
"wavelength": 'wavelength',
"weight": 'weight',
"wire guage": 'wire_guage'
}

units = [
  "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
  "nine"
]

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


class OctoSpec(SkillBase):
    def execute(__self__, intent, session):
        session_attributes = {}

        mpnpre = intent['slots']['mpn']['value']

        splitArray = mpnpre.split(' ')
        for index in range(len(splitArray)):
            for unit in units:
                if splitArray[index].count(unit) >= 1:
                    splitArray[index] = str(text2int(splitArray[index]))
                    break


        mpn = ''.join(splitArray)

        val = ""
        url = "http://octopart.com/api/v3/parts/search"

# NOTE: Use your API key here (https://octopart.com/api/register)
        url += "?apikey=0c491965"

        args = [
            ('q', mpn),
            ('start', 0),
            ('limit', 10)
            ]

        url += '&' + urllib.urlencode(args)
        url += '&include[]=specs'

        data = urllib.urlopen(url).read()
        response = json.loads(data)

        result = response['results'][0]
        item = result['item']
        specs = item['specs']
        outputSpecMap = specMap[intent['slots']['spec']['value']]
        val = specs[outputSpecMap]['display_value']


        #val = response["results"][0]["items"][0]['specs'][specMap[intent['slots']['spec']['value']]]['display_value']

        speech_output = str(val)
        card_title = None
        reprompt_text = None
        should_end_session = False
        return util.build_response(session_attributes, util.build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))

class OctoDescrip(SkillBase):
    def execute(__self__, intent, session):
        session_attributes={}

        mpnpre = intent['slots']['mpn']['value']

        splitArray = mpnpre.split(' ')
        for index in range(len(splitArray)):
            for unit in units:
                if splitArray[index].count(unit) >= 1:
                    splitArray[index] = str(text2int(splitArray[index]))
                    break


        mpn = ''.join(splitArray)
        url = "http://octopart.com/api/v3/parts/search"
        url += "?apikey=0c491965"
        args = [
            ('q', mpn),
            ('start', 0),
            ('limit', 10)
            ]

        url += '&' + urllib.urlencode(args)
        url += '&include[]=description'

        data = urllib.urlopen(url).read()
        response = json.loads(data)

        result = response['results'][0]
        item = result ['item']
        descrip = item['descriptions'][0]
        value = descrip['value']

        try:
            speech_output = "It is a " + str(value)
        except:
            try:
                descrip = item['descriptions'][1]
                value = descrip['value']
                speech_output = "It is a " + str(value)
            except:
                descrip = item['descriptions'][2]
                value = descrip['value']
                speech_output = "It is a " + str(value)



        card_title = None
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
