from setuptools import setup

setup(
   name='mtraker',
   version='1.0',
   description='My first library.',
   license='MIT',
   author='Danny1234561111',
   author_email='shornikovdaniil1111@gmail.com',
   url='https://github.com/Danny1234561111/kekorik.git',
   packages=['mtracker'],
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
