from setuptools import setup, find_packages

setup(
    name = 'ACE',
    version = '0.0.1',
    author = 'Karim Galal, Walid Chatt',
    author_email = 'karim.galal@analytics-club.org, walid.chatt@analytics-club.org',
    license = 'MIT',
    description = 'Analytics Club ETHZ helper package',
    packages = ['ACE'],
    url = '',
    keywords = ['ETHZ','ethz','eth','ai','artificial intelligence',
                'machine learning', 'data processing','chatbot',
                'education','ml'],
    install_requires = [
        'numpy','pandas','torch',
        'tensorflow','transformers','sklearn',
        'emoji',
        ],
    classifiers=[
        'Programming Language :: Python :: 3'
        ]
    )
