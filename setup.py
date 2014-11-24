from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksScheduler',
    version='0.1.0',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Scheduler for Geobricks events, e.g. layers download.',
    install_requires=[
        'flask', 'APScheduler'
    ],
    url='http://pypi.python.org/pypi/GeobricksScheduler/'
)
