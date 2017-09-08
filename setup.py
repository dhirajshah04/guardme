try:
   from setuptools import setup
except ImportError:
   from distutils.core import setup

classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]
requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

setup(name='guardme',
      version='1.0',
      description="To save username and password",
      author='Dhiraj Shah',
      author_email='dhiraj.shah04@gmail.com',
      url='https://github.com/dhirajshah04/guardme',
      scripts=['src/guardme'],
      install_requires=requirements,
      packages=['guard_me'],
      package_dir={'guard_me': 'src/guard_me'},
      classifiers=classifiers
)