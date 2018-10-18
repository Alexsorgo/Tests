from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from model.element import center
from screens.chats.base_chat_screen import BaseChatScreen
from utils.logs import log


class ChatScreen(BaseChatScreen):
    STICKER_BTN_ID = 'text_input_bar_emoji_button'
    MICROPHONE_BTN = (By.ID, 'input_bar_voice_button')
    SEND_BTN = (By.ID, 'input_bar_send_button')
    NEXT_ARROW = (By.ID, 'contextMenuNext')
    MSG_FORWARD = (By.ID, 'Forward')
    MSG_COPY = (By.ID, 'Copy')
    MSG_REPLY = (By.ID, 'Reply')
    MSG_STAR = (By.ID, 'Star')
    MSG_TRANSLATE_ID = 'Translate with Google'
    MSG_EDIT = (By.ID, 'Edit')
    MSG_DELETE = (By.ID, 'Delete')
    MSG_UNTRANSLATE = (By.ID, 'Untranslate')
    MSG_CLOSE_ID = 'Cancel'
    MESSAGE_EDITED_ID = 'edited'
    MESSAGE_OUTDATED_ID = 'Outdated'
    BLOCK_BTN = (By.ID, 'default_input_view_action_button')
    OPEN_PROFILE = (By.ID, 'chat_title')
    DELETE_FOR_ME = (By.ID, 'Delete for me')
    DELETE_FOR_ALL = (By.ID, 'Delete for all')
    DELETE_FOR_BOTH = (By.ID, 'Delete for both')
    DELETE = (By.ID, 'Delete')
    STOP_SENDING = (By.ID, 'ic btn stop download')
    MENTION_TITLE_ID = 'username_label'
    REPLAY_CURTAIN_ID = 'reply_preview'
    TRANSLATED_CONTENT_ID = 'conversion_content_label'
    MENTION_ID = '@'
    TRANSLATE_STATUS = (By.ID, 'Translating...')
    STICKER_ID = 'sticker_cell'
    STICKER_NAVIGATION_BOARD = (By.ID, 'menu_collection_view')
    STICKER_MENU_CELL = (By.ID, 'sticker_menu_package_cell')
    COLLECT_VIEW = (By.XPATH, '//XCUIElementTypeCollectionView')
    CONTEXT_ITEM = (By.ID, 'context_menu_item')
    CONTEXT_VOICE_MESSAGE = (By.ID, 'ic_mic_dark_gray')

    def record_voice_msg(self):
        log.debug("Long press to '{}' button".format("Microphone"))
        mic = self.driver.find_element(*self.MICROPHONE_BTN)
        action = TouchAction(self.driver)
        action.long_press(x=center(mic)['XCentr'], y=center(mic)['YCentr'], duration=3000).release().perform()

    def set_chat_msg(self, msg_text):
        log.debug("Set '{}' to chat field".format(msg_text))
        self.el.set_text_clear(self.CHAT_FIELD, msg_text)

    def tap_send_btn(self):
        log.debug("Tap '{}' button".format("Send"))
        self.el.tap_btn(self.SEND_BTN)

    def create_scheduled_message(self):
        log.debug("Long press and swipe up send button")
        send_btn = self.driver.find_element(*self.SEND_BTN)
        coordinates = center(send_btn)
        self.driver.execute_script('mobile: dragFromToForDuration',
                                   {"duration": 1.0, "fromX": coordinates['XCentr'], "fromY": coordinates['YCentr'],
                                    "toX": coordinates['XCentr'], "toY": (coordinates['YCentr'] - 100)})

    def open_context_menu(self, msg_text):
        log.debug("Long press to message: '{}'".format(msg_text))
        self.scroll_down_try()
        self.driver.page_source
        message = self.driver.find_element_by_id(msg_text)
        coordinates = center(message)
        action = TouchAction(self.driver)
        action.long_press(x=coordinates['XCentr'], y=coordinates['YCentr'], duration=3500).release().perform()

    def open_sticker_context_menu(self):
        log.debug("Long press to sticker message")
        self.scroll_down_try()
        self.driver.page_source
        messages = self.driver.find_elements(*self.STICKER_MESSAGE_BOX)
        # TODO: Update locator, when it will be make
        message = messages[-1].find_element_by_id(self.CHAT_AVATAR)
        coordinates = center(message)
        action = TouchAction(self.driver)
        action.long_press(x=coordinates['XCentr'], y=coordinates['YCentr'], duration=3500).release().perform()

    def open_translation_context_menu(self):
        log.debug("Long press to sticker message")
        self.scroll_down_try()
        self.driver.page_source
        messages = self.driver.find_elements_by_id(self.TRANSLATED_CONTENT_ID)
        coordinates = center(messages[-1])
        action = TouchAction(self.driver)
        action.long_press(x=coordinates['XCentr'], y=coordinates['YCentr'], duration=3500).release().perform()

    def open_context_menu_last_bubble(self):
        log.debug("Long press to sticker message")
        self.scroll_down_try()
        self.driver.page_source
        messages = self.driver.find_elements_by_id(self.BUBBLE_VIEW_ID)
        coordinates = center(messages[-1])
        action = TouchAction(self.driver)
        action.long_press(x=coordinates['XCentr'], y=coordinates['YCentr'], duration=3500).release().perform()

    def tap_context_edit(self):
        log.debug("Tap on '{}' in context menu".format("Edit"))
        self.el.tap_btn(self.MSG_EDIT)

    def tap_context_star(self):
        log.debug("Tap on '{}' in context menu".format("Stared"))
        self.el.tap_btn(self.MSG_STAR)

    def tap_context_option(self, option):
        log.debug("Tap on context '{}'".format(option))
        self.el.tap_btn_by_id(option)

    def tap_context_translate(self):
        log.debug("Tap on '{}' in context menu".format("Translate"))
        translate = self.driver.find_element_by_id(self.MSG_TRANSLATE_ID)
        translate.click()
        self.driver.wait_till_element_disappear(self.TRANSLATE_STATUS)

    def tap_context_delete(self):
        log.debug("Tap on '{}' in context menu".format("Delete"))
        self.el.tap_btn(self.MSG_DELETE)

    def tap_context_untranslate(self):
        log.debug("Tap on Untraslate in context menu")
        self.el.tap_btn(self.MSG_UNTRANSLATE)

    def tap_context_reply(self):
        log.debug("Tap on '{}' in context menu".format("Reply"))
        self.el.tap_btn(self.MSG_REPLY)

    def tap_context_forward(self):
        log.debug("Tap on forward in context menu")
        self.el.tap_btn(self.MSG_FORWARD)

    def tap_delete_for_me(self):
        log.debug("Tap on '{}' button".format("Delete for me"))
        self.el.click_btn(self.DELETE_FOR_ME)

    def tap_delete_for_all(self):
        log.debug("Tap on '{}' button".format("Delete for all"))
        self.el.click_btn(self.DELETE_FOR_ALL)

    def tap_delete_for_both(self):
        log.debug("Tap on '{}' button".format("Delete for all"))
        self.el.click_btn(self.DELETE_FOR_BOTH)

    def tap_delete(self):
        log.debug("Tap on '{}' button".format("Delete"))
        self.el.click_btn(self.DELETE)

    def tap_open_profile(self):
        log.debug("Tap on '{}' for open profile".format("Placeholder"))
        self.el.tap_btn(self.OPEN_PROFILE)

    def tap_record_send(self):
        log.debug("Tap on '{}' on voice record".format("Send"))
        self.el.tap_btn(self.SEND_BTN)

    def get_text_msg(self):
        log.debug("Get text message")
        self.driver.page_source
        text = []
        text_msg_boxes = self.driver.find_elements(*self.TEXT_MESSAGE_BOX)
        names = text_msg_boxes[-1].find_elements_by_xpath(self.TYPE_TEXT_XPATH)
        for name in names:
            text.append(name.get_attribute('name'))
        return text

    def get_received_text_msg(self):
        log.debug("Get received text message")
        self.driver.page_source
        text = []
        text_msg_boxes = self.driver.find_elements(*self.TEXT_RECEIVED_MESSAGE_BOX)
        names = text_msg_boxes[-1].find_elements_by_xpath(self.TYPE_TEXT_XPATH)
        for name in names:
            text.append(name.get_attribute('name'))
        return text

    def get_last_text_msg(self):
        log.debug("Get last text message element")
        text_msg_boxes = self.driver.find_elements(*self.TEXT_MESSAGE_BOX)
        name = text_msg_boxes[-1]
        return name

    def close_context(self):
        log.debug("Tap cancel button on context menu")
        self.el.tap_btn_by_id(self.MSG_CLOSE_ID)

    def is_message_deleted(self, msg):
        log.debug("Find elemets with id: '{}'".format(msg))
        return self.driver.find_elements_by_id(msg) == []

    def unblock_btn(self):
        log.debug('Find Unblock button')
        return self.driver.wait_till_element_is_displayed(self.UNBLOCK_BTN)

    def tap_unblock_btn(self):
        log.debug('Tap Unblock button')
        self.el.click_btn(self.UNBLOCK_BTN)

    def input_present(self):
        log.debug('Find text input')
        return self.driver.find_element(*self.CHAT_FIELD)

    def open_keyboard(self):
        log.debug('Find text input')
        self.driver.find_element(*self.CHAT_FIELD).click()

    def stared_present(self):
        log.debug("Find stared message image")
        self.scroll_down_try()
        last_msg = self.get_last_text_msg()
        try:
            last_msg.find_element(*self.STARED_MSG_ICON)
            return True
        except NoSuchElementException:
            return False

    def open_replay(self, replay_count):
        log.debug("Open message replayed '{}' times".format(str(replay_count)))
        self.scroll_down_try()
        replayed_msg = self.driver.find_element_by_id(str(replay_count))
        replayed_msg.click()

    def get_translated_msg(self):
        log.debug("Get translated message")
        self.driver.page_source
        translated = []
        text_msg_boxes = self.driver.find_elements(*self.TRANSLATE_MESSAGE_BOX)
        init_msgs = text_msg_boxes[-1].find_elements_by_xpath(self.TYPE_TEXT_XPATH)
        for msg in init_msgs:
            translated.append(msg.get_attribute('name'))
        translated_texts = self.driver.find_elements(*self.TRANSLATE_MESSAGE_BOX)
        init_translated = translated_texts[-1].find_elements_by_id(self.TRANSLATED_CONTENT_ID)
        for text in init_translated:
            translated.append(text.get_attribute('value'))
        return translated

    def is_outdated(self):
        log.debug("Check is translated message outdated")
        last_message = self.driver.find_elements(*self.TRANSLATE_MESSAGE_BOX)
        try:
            last_message[-1].find_element_by_id(self.MESSAGE_OUTDATED_ID)
            return True
        except NoSuchElementException:
            return False

    def tap_first_mention(self):
        log.debug('Tap first mention')
        self.set_chat_msg(self.MENTION_ID)
        self.driver.find_element_by_id(self.MENTION_TITLE_ID).click()

    def is_reply_curtain_present(self):
        log.debug('Check is replay preview present')
        curtain = self.driver.find_elements_by_id(self.REPLAY_CURTAIN_ID)
        if curtain:
            return True
        else:
            return False

    def set_msg_without_clear(self, msg_text):
        log.debug("Set '{}' to chat field".format(msg_text))
        self.el.set_text(self.CHAT_FIELD, msg_text)

    def tap_sticker_btn(self):
        self.driver.page_source
        log.debug("Tap emoji button")
        self.el.tap_btn_by_id(self.STICKER_BTN_ID)

    def send_first_sticker(self):
        log.debug("Tap emoji button")
        self.el.tap_btn_by_id(self.STICKER_ID)

    def is_sticker_board_display(self):
        log.debug("Check sticker board open")
        return self.driver.wait_till_element_is_displayed(self.STICKER_MENU_CELL)

    def close_keyboard(self):
        log.debug("Close keyboard")
        self.el.tap_btn(self.COLLECT_VIEW)

    def get_context_options(self):
        log.debug("Collect all context options")
        options = self.driver.find_elements(*self.CONTEXT_ITEM)
        options_text = [[i.get_attribute('value') for i in option.find_elements_by_xpath(self.STATIC_TEXT)]
                        for option in options]
        return options_text
