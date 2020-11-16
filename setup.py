from setuptools import setup, find_packages

setup(name='python-markdown-generator',
      version='0.1',
      description='Python library for dynamically generating HTML sanitized Markdown syntax.',
      long_description=open('README.md').read(),
      url='https://github.com/Nicceboy/python-markdown-generator',
      author='Niklas Saari',
      author_email='niklas.saari@oulu.fi',
      license='Apache-2.0',
      packages=find_packages(),
      zip_safe=False)
