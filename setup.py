from setuptools import setup, find_packages
from setuptools import setup, find_packages
import codecs
import os
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
setup(
    name='poofpy',
    version='0.4',
    license='MIT',
    author="Tarook (Tarek)",
    author_email='tarekthedream@gmail.com',
    url='https://github.com/tarekturbo/poofpy',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=["poof","api wrapper","crypto","payments","crypto payments","crypto api","payment gateway","crypto payment gateway","free","payment","gateway","sellix","shoppy","poof.io"],
    install_requires=[
          'pydantic',
          'requests'
      ],

)