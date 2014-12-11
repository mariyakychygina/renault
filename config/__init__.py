import importlib

import settings_default


class Config(object):

    db_config = None

    def __init__(self):
        self.default_settings = settings_default
        self.default_settings_keys = dir(self.default_settings)
        try:
            self.settings = importlib.import_module('settings')
        except ImportError:
            self.settings = None
        self.settings_keys = dir(self.settings) if self.settings else []

    def get(self, key):
        if key in self.settings_keys:
            return getattr(self.settings, key)
        elif key in self.default_settings_keys:
            return getattr(self.default_settings, key)
        else:
            raise KeyError('%s not found in settings' % (key))

    def __getattribute__(self, name):
        try:
            return super(Config, self).__getattribute__(name)
        except AttributeError:
            return self.get(name.upper())


config = Config()