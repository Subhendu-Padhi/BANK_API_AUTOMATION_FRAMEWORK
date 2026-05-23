from configparser import ConfigParser

config = ConfigParser()
config.read("config/config.ini")


class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get("API", "base_url")