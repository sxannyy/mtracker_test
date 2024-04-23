from setuptools import setup

setup(
   name='mtraker',
   version='1.0',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   license='MIT',
   author='Sasha Sanzhitova',
   author_email='sxannyy@mail.ru',
   url='https://github.com/sxannyy/mtracker_test.git',
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
