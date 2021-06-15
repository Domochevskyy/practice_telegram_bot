# -*- coding: utf-8 -*-
import sys
import time
import pytest
import os
import telebot
from telebot import types

from config import TOKEN, CHAT_ID

TOKEN = TOKEN
CHAT_ID = CHAT_ID

should_skip = False if TOKEN is None or CHAT_ID is None else True


# @pytest.mark.skipif(should_skip, reason="No environment variables configured")
class TestTeleBot:
    def test_message_listener(self):
        msg_list = []
        for x in range(100):
            msg_list.append(self.create_text_message('Message ' + str(x)))

        def listener(messages):
            assert len(messages) == 100

        tb = telebot.TeleBot(token=TOKEN)
        tb.set_update_listener(listener)

    def test_message_handler_help(self):
        tb = telebot.TeleBot(token=TOKEN)
        msg = self.create_text_message('/help')

        @tb.message_handler(commands=['help'])
        def command_handler(message):
            message.text = 'Вас привестствует тестовый бот Николая Медного.'

        tb.process_new_messages([msg])
        time.sleep(1)
        assert msg.text == 'Вас привестствует тестовый бот Николая Медного.'

    def test_message_handler_about(self):
        tb = telebot.TeleBot(token=TOKEN)
        msg = self.create_text_message('/about')

        @tb.message_handler(commands=['about'])
        def command_handler(message):
            message.text = 'Бот определяет количество объектов на фотографии и детектирует эти объекты'

        tb.process_new_messages([msg])
        time.sleep(1)
        assert msg.text == 'Бот определяет количество объектов на фотографии и детектирует эти объекты'

    def test_message_handler_start(self):
        tb = telebot.TeleBot(token=TOKEN)
        msg = self.create_text_message('/start')

        @tb.message_handler(commands=['start'])
        def command_handler(message):
            message.text = 'Вас привестствует тестовый бот Николая Медного.'

        tb.process_new_messages([msg])
        time.sleep(1)
        assert msg.text == 'Вас привестствует тестовый бот Николая Медного.'

    def test_send_message(self):
        text = 'CI Test Message'
        tb = telebot.TeleBot(TOKEN)
        ret_msg = tb.send_message(CHAT_ID, text)
        assert ret_msg.message_id

    def test_edit_message_text(self):
        tb = telebot.TeleBot(TOKEN)
        msg = tb.send_message(CHAT_ID, 'Test')
        new_msg = tb.edit_message_text('Edit test', chat_id=CHAT_ID, message_id=msg.message_id)
        assert new_msg.text == 'Edit test'

    def test_reply_to(self):
        text = 'CI reply_to Test Message'
        tb = telebot.TeleBot(TOKEN)

        @tb.message_handler(content_types=['text'])
        def command_handler(message):
            msg = tb.send_message(CHAT_ID, text)
            ret_msg = tb.reply_to(message, 'Я пока не умею разговаривать с людьми, могу принимать только фотографии')
            assert ret_msg.reply_to_message.message_id == msg.message_id

    def test_send_photo(self):
        file_data = open('for_testing.jpg', 'rb')
        tb = telebot.TeleBot(TOKEN)
        ret_msg = tb.send_photo(CHAT_ID, file_data)
        assert ret_msg.message_id

        ret_msg = tb.send_photo(CHAT_ID, ret_msg.photo[0].file_id)
        assert ret_msg.message_id

    def test_chat(self):
        tb = telebot.TeleBot(TOKEN)
        me = tb.get_me()
        msg = tb.send_message(CHAT_ID, 'Test')
        assert me.id == msg.from_user.id
        assert msg.chat.id == int(CHAT_ID)


    @staticmethod
    def create_text_message(text):
        params = {'text': text}
        chat = types.User(11, False, 'test')
        return types.Message(1, None, None, chat, 'text', params, "")
