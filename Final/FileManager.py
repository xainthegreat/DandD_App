import json


class FileManager:
    '''
    this class allows the saving and loading of .json files related to D&D character creation
    '''
    @staticmethod
    def save_to_json(data_dict):
        '''
        saves a .json file using the character data sent from the gui
        :param data_dict:
        dictionary - all the information from the gui about the character
        :return:
        none
        '''
        with open(f'{data_dict["Player Info"]["Character Name"]}.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)

    @staticmethod
    def load_from_json(path):
        '''
        loads data from a .json file and returns it
        :param path:
        string - the path of the file to be opened
        :return:
        dictionary - data retrieved from .json
        '''
        try:
            with open(path, 'r') as json_file:
                data = json.load(json_file)
            return data
        except:
            print('failed to open file and return data')
