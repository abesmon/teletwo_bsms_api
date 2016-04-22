#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import logging

import requests

class RecipNumberError(Exception):
    pass

class TeleTwoReqError(Exception):
    pass

class TeleTwoAPI:
    def __init__(self, partner_login, partner_password, sender_name):
        self.TELE_TWO_API_HOST = 'http://bsms.tele2.ru/api/' # initial

        self.PARTNER_LOGIN = partner_login
        self.PARTNER_PASSWORD = partner_password
        self.SENDER_NAME = sender_name.decode('ascii')

    def send_message(self, recipient_number, message):
        # привести номер телефона к типизированному виду
        recipient_number = str(recipient_number)
        recipient_number = re.sub('[^\d]+', '', recipient_number) # чистим все, что не является символом

        # проверка на то, что номер телефона 11 цифр в длинну
        if len(recipient_number) <> 11:
            raise RecipNumberError('Recipient phone number must be 11 digits long')

        # привести сообщение к типизированному виду
        message = message.decode("utf-8")

        payload = {
            'operation': 'send',
            'login': self.PARTNER_LOGIN,
            'password': self.PARTNER_PASSWORD,
            'msisdn': recipient_number,
            'shortcode': self.SENDER_NAME,
            'text': message
        }

        r = requests.get(self.TELE_TWO_API_HOST, params=payload)

        logging.info(r.status_code, r.text)

        if r.status_code != requests.codes.ok:
            raise TeleTwoReqError('Error occurs while request to TeleTwo')

        if r.text.find('ERROR') <> -1:
            raise TeleTwoReqError(r.text.split(': ')[1])

        return r.text
