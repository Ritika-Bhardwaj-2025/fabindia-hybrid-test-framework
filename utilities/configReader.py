import configparser

class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('C:/Users/10835846/PycharmProjects/ProjectGladiator/config/config.properties')

    def get_property(self, section, key):
        try:
            return self.config[section][key]
        except KeyError:
            print(f"Missing section '{section}' or key '{key}' in config file.")
            return None

    def get_website(self, section='LINK'):
        return self.get_property(section, 'url')



