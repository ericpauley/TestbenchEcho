import json
import urllib
import util
import base64
from skills.skill import SkillBase
from string import ascii_uppercase,ascii_lowercase


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
"si case package": 'case_package_si',
"case package": 'case_package',
"character height": 'character_size_height',
"character width": 'character_size_width',
"china ROHS": 'china_rohs',
"clock speed": 'clock_speed',
"coil current": 'coil_current',
"ac coil power": 'coil_power_ac',
"dc coil power": 'coil_power_dc',
"coil resistance": 'coil_resistance',
"coil voltage": 'coil_voltage',
"ac coil voltage": 'coil_voltage_ac',
"color": 'color',
"common mode rejection ratio": 'cmrr',
"conductor material": 'conductor_material',
"contact current rating": 'contact_current_rating',
"contact material": 'contact_material',
"contact plating": 'contact_plating',
"contact resistance": 'contact_resistance',
"contact syle": 'contact_style',
"dc contact voltage rating": 'contact_voltage_rating_dc',
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
"elv compliant": 'elv_compliant',
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
"dc input voltage": 'input_voltage_dc',
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
"number of adcs": 'number_of_adcs',
"number of bits": 'number_of_bits',
"number of channels": 'number_of_channels',
"number of circuits": 'number_of_circuits',
"number of conductors": 'number_of_conductors',
"number of contacts": 'number_of_contacts',
"number of dacs": 'number_of_dacs',
"number of detents": 'number_of_detents',
"number of fibers": 'number_of_fibers',
"number of gates": 'number_of_gates',
"number of i oh pins": 'number_of_i_o_pins',
"number of mating cycles": 'number_of_mating_cycles',
"number of outlets": 'number_of_outlets',
"number of outputs": 'number_of_outputs',
"number of pins": 'number_of_pins',
"number of positions": 'number_of_positions',
"number of regulated outputs": 'number_of_regulated_outputs',
"number of rows": 'number_of_rows',
"number of slots": 'number_of_slots',
"number of uarts": 'number_of_uart',
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
"q factor": 'q_factor',
"quiescent current": 'quiescent_current',
"ram memory size":'ram_bytes',
"reach svhc compliance": 'reach_svhc_compliance',
"release force": 'release_force',
"resistance": 'resistance',
"resistance tolerance": 'resistance_tolerance',
"resolution in bits": 'resolution_bits',
"resolution in pulses per revolution": 'resolution_bits_revlution',
"resonant frequency": 'resonant_frequency',
"rise time": 'rise_time',
"rise fall time": 'rise_fall_time',
"rohs": 'rohs',
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
"ac supply voltage": 'supply_voltage_ac',
"dc supply voltage": 'supply_voltage_dc',
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
"ac voltage rating": 'voltage_rating_ac',
"dc voltage rating": 'voltage_rating_dc',
"transient voltage rating": 'voltage_rating_transient',
"wavelength": 'wavelength',
"weight": 'weight',
"wire guage": 'wire_guage'
}


class OctoSpec(SkillBase):
    def execute(self, intent, session):

        digits = ""
        for i in ascii_uppercase:
            if i in intent['slots'] and 'value' in intent['slots'][i]:
                digit = intent['slots'][i]['value'].replace(".","")
                digits += digit
        digits = digits.replace(" ", "")
        digits = digits.replace(".","")
        digits.upper()

        val = ""
        url = "http://octopart.com/api/v3/parts/search"
        url += "?apikey=0c491965"
        args = [
            ('q', digits),
            ('start', 0),
            ('limit', 10)
            ]
        url += '&' + urllib.urlencode(args)
        url += '&include[]=specs'
        url += '&include[]=imagesets'

        data = urllib.urlopen(url).read()
        response = json.loads(data)

        try:
            result = response['results'][0]
            item = result['item']
            specs = item['specs']
            outputSpecMap = specMap[intent['slots']['spec']['value']]
            val = specs[outputSpecMap]['display_value']

            result = response['results'][0]
            item = result ['item']
            imagesets = item['imagesets'][0]
            try:
                image = imagesets['large_image']['url']
            except:
                try:
                    image = imagesets['small_image']['url']
                except:
                    image = None
            image = "https://alexasslisbogusandlame.tk/pngify/"+base64.b32encode(image)+".png"
            response = str("The " + intent['slots']['spec']['value'] + " is " + val)
            #val = response["results"][0]["items"][0]['specs'][specMap[intent['slots']['spec']['value']]]['display_value']
        except:
            response = "I cannot find that part specification"
            image = None
        return self.respond(response, "Technical specification: " + intent['slots']['spec']['value'], response, image)

class OctoDescrip(SkillBase):
    def execute(self, intent, session):

        digits = ""
        for i in ascii_uppercase:
            if i in intent['slots'] and 'value' in intent['slots'][i]:
                digit = intent['slots'][i]['value'].replace(".","")
                digits += digit
        digits = digits.replace(" ", "")
        digits = digits.replace(".","")
        digits.upper()
        url = "http://octopart.com/api/v3/parts/search"
        url += "?apikey=0c491965"
        args = [
            ('q', digits),
            ('start', 0),
            ('limit', 10)
            ]
        url += '&' + urllib.urlencode(args)
        url += '&include[]=descriptions'
        url += '&include[]=imagesets'

        data = urllib.urlopen(url).read()
        response = json.loads(data)
        partT = ""
        try:
            result = response['results'][0]
            item = result ['item']
            descrip = item['descriptions'][0]
            value = descrip['value']
            partT = item['mpn']

        except:
            speech_output = "I cannot find that part"
            image = None
            partT = "Could not find part"

        imagesets = item['imagesets'][0]
        try:
            image = imagesets['large_image']['url']
        except:
            try:
                image = imagesets['small_image']['url']
            except:
                image = None
        image = "https://alexasslisbogusandlame.tk/pngify/"+base64.b32encode(image)+".png"

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

        return self.respond(speech_output, partT, speech_output[8:], image)


class OctoPrice(SkillBase):
    def execute(self, intent, session):

        digits = ""
        for i in ascii_uppercase:
            if i in intent['slots'] and 'value' in intent['slots'][i]:
                digit = intent['slots'][i]['value'].replace(".","")
                digits += digit
        #for i in ascii_lowercase:
            #digits = digits.replace(i,"")
            digits = digits.replace(" ", "")
            digits = digits.replace(".","")
            digits.upper()
        url = "http://octopart.com/api/v3/parts/search"
        url += "?apikey=0c491965"
        args = [
            ('q', digits),
            ('start', 0),
            ('limit', 10)
            ]

        url += '&' + urllib.urlencode(args)

        data = urllib.urlopen(url).read()
        response = json.loads(data)
        try:
            result = response['results'][0]
            item = result ['item']
            offers = item['offers'][0]
            prices = offers['prices']

            price_data = json.dumps(prices)
            prices_dict = json.loads(price_data)

            minPrice = str(prices['USD'][0][1])
            maxPrice = str(prices['USD'][len(prices_dict['USD'])-1][1])
            minPrice = minPrice[:-3];
            maxPrice = maxPrice[:-3];
            response = "The price ranges from " + maxPrice + "$"  " to " + minPrice + "$"
        except:
            response = "I cannot gather price information for that part"

        return self.respond(response)
