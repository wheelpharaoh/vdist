import sys
# The ConfigParser module has been renamed to configparser in Python 3
if sys.version_info[0] == 3:
    import configparser
else:
    import ConfigParser as configparser


class Configuration(object):

    def __init__(self, arguments):
        self.output_folder = arguments.get("output_folder", None)
        self.builder_parameters = {key: value for key, value in arguments.items()
                                   if key != "output_folder"}
        print(self.builder_parameters)


def read(configuration_file):
    # Should return a dict whose keys should be configfile sections
    # (except DEFAULT) and values a dict with parameter:value pairs.
    pass

