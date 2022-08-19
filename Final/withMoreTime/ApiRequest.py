import requests
import json
import pprint

class InfoRequest():
    def __init__(self):
        self.api_url = 'https://www.dnd5eapi.co'

    def get_background_json(self, background_name:str):
        background_response = requests.get(f'{self.api_url}/api/backgrounds/{background_name}')
        background_parse_json = json.loads(background_response.text)
        return background_parse_json

    def get_class_json(self, class_name:str):
        class_response = requests.get(f'{self.api_url}/api/classes/{class_name}')
        class_parse_json = json.loads(class_response.text)
        return class_parse_json

    def get_starting_equipment(self, se_name:str):
        se_parse_json = self.get_class_json(se_name)

        for items in se_parse_json['starting_equipment_options']: #todo still needs refinement
            print(f'Choose {items["choose"]}:')
            for item in items['from']:
                if 'equipment' in item.keys():
                    print(f'\t{item["equipment"]["name"]}')
                elif 'equipment_option' in item.keys():
                    if item['equipment_option']['choose'] == 1:
                        eo_response = requests.get(
                            f'{self.api_url}{item["equipment_option"]["from"]["equipment_category"]["url"]}')
                        eo_parse_json = json.loads(eo_response.text)
                        for options in eo_parse_json['equipment']:
                            print(f'\t{options["name"]}')
                    else:
                        print(f'\t{item["equipment_option"]}')
                elif 'equipment_category' in item.keys():
                    ec_response = requests.get(f'{self.api_url}{item["equipment_category"]["url"]}')
                    ec_parse_json = json.loads(ec_response.text)
                    for category in ec_parse_json['equipment']:
                        print(f'\t{category["name"]}')
                else:
                    print(f'\t{item}')




if __name__ == "__main__":
    info = InfoRequest()
    # print(info.get_background_info('acolyte'))
    print(json.dumps(info.get_class_json('bard'), indent=4))
    # info.get_starting_equipment('paladin')