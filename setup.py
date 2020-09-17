import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='monnify',
    version='1.0.0',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    license='MIT License',  # example license
    description='A Library created for ease of using monnify\'s API to create unique account numbers for your users/members, verify user transaction, generate Bearer Token etc..',
    long_description_content_type='text/plain',
    long_description=README,
    url='https://github.com/ldonjibson/monnify',
    author='Olayanju A. Ajibola',
    author_email='ajibolaolayanju@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
