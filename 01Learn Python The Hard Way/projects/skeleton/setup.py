try:
 from setuptools import setup
except ImportError:
 from distutils.core import setup

config={
    'description': 'Abel Project',
    'author': 'Abel',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'awan@movoto.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'abelProjet'

}

setup(**config)
