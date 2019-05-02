import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A simple Django app to conduct Web-based polls',
    long_description=README,
    url='https://www.parellelmemory.com',
    author='Your Name',
    author_email='questionmark@parellelmemory.com',
    classifiers=[
        'Environment :: Web Env',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Dev',
        'License :: OSI Approved :: BSD License',
        'OS : OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP'
    ],
)