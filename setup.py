from setuptools import setup, find_packages

setup(
      description = 'A package to pull fantasy football projections.',
      name = 'ff_stats',
      version = '0.1.0',
      packages = find_packages(include = ['ff_stats', 'ff_stats.*'],
      install_requires = ['numpy',
                          'pandas',
                          'requests',
                          'time',
                          'random',
                          'json'])