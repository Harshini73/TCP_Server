from setuptools import setup,find_packages

setup(name='TCP_Server',
      version='1.0',
      packages=find_packages(exclude=['docs', '*.pyc']),
      url='https://github.com/Harshini73/TCP_Server',
      author='Harshini Komali',
      author_email='harshinikomali73@gmail.com',
      long_description=open('README.md').read(),
      description='Mutithreaded TCP Server',
      test_suite='nose.collector',
     )
