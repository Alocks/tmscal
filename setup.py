# coding: utf-8
import codecs
from setuptools import setup, find_packages


setup(
    name='Midgard Shard Calculator',
    version=1.0,
    packages=find_packages(),

    author="Sakura",
    description='Midgard Shard Calculator for Tibia',
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'tmscal = calculator.cmdline:main',
        ]
    },
    license='MIT',
)
