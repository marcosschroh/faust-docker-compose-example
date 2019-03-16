import configparser
import os


class Settings(configparser.ConfigParser):
    # Environment variable settings overrides
    class EnvironmentInterpolation(configparser.BasicInterpolation):
        def before_get(self, parser, section, option, value, defaults):
            return os.environ.get(self._env_name(section, option), os.path.expandvars(value))

        @classmethod
        def _env_name(cls, section, option):
            def munge(name):
                return name.upper().replace('.', '_')

            return '%s_%s' % (munge(section), munge(option))

    def __init__(self):
        super(Settings, self).__init__(interpolation=Settings.EnvironmentInterpolation())

        self.read(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
                               os.environ.get('PROJECT_SETTINGS', 'local.ini')))


SETTINGS = Settings()
