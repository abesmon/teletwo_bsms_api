#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='teletwo_bsms_api',
    version='0.0.1',
    description='Не официальная библиотека для работы с API TELE2 для отправки смс сообщений через HTTP протокол',
    url='https://github.com/abesmon/teletwo_bsms_api.git',
    author='Alexey Lysenko [abesmon]',
    author_email='abesmon@gmail.com',
    license='MIT',

    # Dependent packages (distributions)
    install_requires=["requests"],

    packages=['teletwo_bsms_api'],
    zip_safe=False)
