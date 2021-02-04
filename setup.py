import os
from setuptools import setup
from scan import version


setup(name='syrahsearch',
      version=version,
      description='Command-line search engine with some cool machine learning solutions.',
      url='https://github.com/syrahsearch/syrah',
      author='Kamil Boberek',
      packages=['modules', 'AI'],
      author_email='notimportant@protonmail.com',
      license='MIT',
      entry_points={
          'console_scripts': [
              'syrahsearch = scan:main'
          ]
      },      
      install_requires=[
          'validators',
          'tensorflow',
          'termcolor',
          'requests',
          'numpy',
          'scipy',
          'PyMySQL',
          'beautifulsoup4',
          'dropbox',
      ],      
      zip_safe=False      
)