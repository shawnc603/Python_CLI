from setuptools import setup
setup(
    name = 'Python_CLI',
    version = '0.1.0',
    packages = ['Python_CLI'],
    entry_points = {
        'console_scripts': [
            'Python_CLI = Tools.run:main'
        ]
    })