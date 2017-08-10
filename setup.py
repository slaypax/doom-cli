from setuptools import setup

setup(
    name="doom-cli",
    version='0.1',
    py_modules=['doom-cli'],
    install_requires=[
        'Click',
        'Requests'
    ],
    entry_points='''
        [console_scripts]
        doom=doom:cli
    ''',
)