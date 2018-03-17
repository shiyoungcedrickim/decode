from setuptools import setup

setup(name='decode',
      version='0.1.0',
      packages=['decode'],
      entry_points={
          'console_scripts': [
              'decode = decode.__main__:main'
          ]
      },
      )