import os


CATEGORIES_FILENAME = os.environ.get('CATEGORIES_FILENAME', 'categories.json')
DATA_FILES_DIRECTORY = os.environ.get('DATA_FILES_DIRECTORY',
                                      os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data_files'))


DEFAULT_SETTINGS = {
    'app': {
        'DEBUG': True,
        'SECRET_KEY': 'ecret-key-goes-here',
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite'
    },
    'data_files_directory': DATA_FILES_DIRECTORY,
    'categories_file': os.path.join(DATA_FILES_DIRECTORY, CATEGORIES_FILENAME),
    'gunicorn': {
        'reload': True,
        'accesslog': "-",
        'bind_port': os.environ.get("GUNICORN_PORT", 8001),
        'app_dir': os.environ.get('APP_DIR', '/home/vault'),
        'bind_host': os.environ.get("GUNICORN_HOST", '0.0.0.0'),
        'access_log_format': '%(t)s %(h)s "%(r)s" %(s)s "%(a)s"',
        'configured_workers': os.environ.get("GUNICORN_WORKER_COUNT", 4),
    }
}

class Settings(dict):
    """
    A dict that allows access of its keys through '.' notation.
    This will automatically convert any nested dicts into `Settings` instances as well, so you can access nested items
    with dots. e.g. `settings.gunicorn.reload`
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__convert_dicts()

    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, item, value):
        if isinstance(value, dict) and not isinstance(value, Settings):
            self[item] = Settings(value)
        else:
            self[item] = value

    def __convert_dicts(self):
        """ update all dicts within this dict to be `Settings` dicts recursively """
        for k in self.keys():
            if isinstance(self[k], dict):
                if not isinstance(self[k], Settings):
                    self[k] = Settings(self[k])
                self[k].__convert_dicts()

    def load_settings_file(self):
        # TODO: a placeholder to remind me to implement parsing a settings file, YAML format maybe?
        pass


settings = Settings(DEFAULT_SETTINGS)
