from setuptools import setup

setup (name = 'zgit',
       version = '1.0',
       packages = ['zgit'],
       entry_points = {
           'console_scripts' : [
               'zgit = zgit.cli:main'
           ]
       })
