import os
import configparser

APP_ENV = os.environ.get('APP_ENV') or 'dev'

INI_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), f'{APP_ENV}.ini')

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

POSTGRES = CONFIG['postgres']

if APP_ENV == 'dev' or APP_ENV == 'test' or APP_ENV == 'docker':
    DB_CONFIG = (POSTGRES['user'], POSTGRES['password'], POSTGRES['host'], POSTGRES['database'])
    DATABASE_URL = f'postgresql+psycopg2://%s:%s@%s/%s' % DB_CONFIG
else:
    DB_CONFIG = (POSTGRES['host'], POSTGRES['database'])
    DATABASE_URL = "postgresql+psycopg2://%s/%s" % DB_CONFIG

DB_SCHEMA = POSTGRES['schema'] or ''
DB_ECHO = True if CONFIG['database']['echo'] == 'yes' else False
DB_AUTOCOMMIT = True

LOG_LEVEL = CONFIG['logging']['level']