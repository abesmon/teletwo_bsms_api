#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import TeleTwoAPI

TeleTwoAPI('testlogin', 'testpass', 'testname').send_message('7 903 999 99 99', 'Немного мессаджа')
