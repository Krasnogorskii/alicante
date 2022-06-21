
from setuptools import setup

APP_NAME = 'CITA'
APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'packages': ['selenium'],
    'iconfile': 'spain.icns',
    'argv_emulation': True,

}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
