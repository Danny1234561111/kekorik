from setuptools import setup, find_packages

setup(
   name='hello',
   version='1',
   description='hello',
   license='MIT',
   author = 'Danny1234561111',
   author_email = 'shornikovdaniil1111@gmail.com',
   url = 'https://github.com/Danny1234561111/kekorik',
   packages=find_packages(exclude=['test']),
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
