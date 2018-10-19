import re

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from tests.model.element import proportion
from tests.screens.base_screen import BaseScreen
from tests.utils.logs import log


class BaseChatScreen(BaseScreen):
    LOCATION_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_location_0')
    TEXT_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_text_0')
    TEXT_RECEIVED_MESSAGE_BOX = (By.ID, 'message_cell_opponent_regular_text_0')
    TRANSLATE_MESSAGE_BOX = (By.ID, 'message_cell_mine_convertion_regular_text_0')
    IMAGE_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_image_0')
    VOICE_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_audio_0')
    RECEIVED_VOICE_MESSAGE_BOX = (By.ID, 'message_cell_opponent_regular_audio_0')
    VIDEO_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_video_0')
    PLACE_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_place_0')
    STICKER_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_sticker_0')
    CONTACT_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_contact_0')
    CHAT_FIELD = (By.ID, 'input_bar_text_view')
    BUBBLE_VIEW_ID = 'bubble_view'
    FILE_MESSAGE_BOX = (By.ID, 'message_cell_mine_regular_file_0')
    FORWARD_MESSAGE_BOX = 'message_cell_mine_forward_text_0'
    VOICE_REPLY_BOX = 'message_cell_mine_reply_regular_audio_0'
    REPLY_MESSAGE_BOX = 'message_cell_mine_reply_regular_text_0'
    UNBLOCK_BTN = (By.ID, 'input_bar_action_button')
    STARED_MSG_ICON = (By.ID, 'ic_star')
    LINK = (By.ID, 'Copy Link')
    REPLAY_SCREEN_ID = 'REPLIES'
    LANGUAGE_CURTAIN = 'collapsed_view_button'
    TRANSLATE_ICON = 'Icons General ic translate'
    AUTOTRANSLATE_ON = 'translation_auto_view_titleLabel'
    AUTOTRANSLATE_ON_DESC = 'Auto-translate on sending'
    CHAT_AVATAR = '_loaded_image'
    HISTORY_REMOVED = 'History was removed'
    CHANNEL_CREATED = (By.ID, 'Channel created')
    STATIC_TEXT = '//XCUIElementTypeStaticText'
    TYPE_TEXT_XPATH = "//XCUIElementTypeTextView"

    SEND_STATUS = 'delivery_status_sent'
    READ_STATUS = 'delivery_status_read'
    DOWN_ARROW = (By.ID, 'ic bottom arrow')
    STICKER_REPLY_BOX = (By.ID, 'message_cell_mine_reply_regular_sticker_0')

    def is_image_displayed(self):
        log.debug("Find image message sent verification element")
        return self.driver.find_element(*self.IMAGE_MESSAGE_BOX)

    def is_compressed(self):
        log.debug("Get last image size")
        image_msgs = self.driver.find_elements(*self.IMAGE_MESSAGE_BOX)
        last_msg = image_msgs[-1]
        texts = last_msg.find_elements_by_xpath(self.STATIC_TEXT)
        for text in texts:
            if re.findall(r'kB', text.get_attribute('value')):
                size = text.get_attribute('value').split(' ')[0]
                if int(float(size.replace(',', '.'))) in range(100, 200):
                    return True
                log.error("Size equals '{}'".format(text.get_attribute('value')))
                return False

    def scroll_down_try(self):
        log.debug('Try find down arrow and tap')
        if self.driver.wait_till_element_is_displayed(self.DOWN_ARROW, timeout=3):
            self.driver.find_element(*self.DOWN_ARROW).click()

    def get_len_images(self):
        log.debug('Collect all images in chat')
        image_boxes = self.driver.find_elements(*self.IMAGE_MESSAGE_BOX)
        log.debug('Collected "{}" images'.format(str(len(image_boxes))))
        return len(image_boxes)

    def is_file_message_displayed(self):
        log.debug('Find file message sent')
        # TODO: add size check, when will bug fix
        return self.driver.wait_till_element_is_displayed(self.FILE_MESSAGE_BOX)

    def is_video_displayed(self):
        log.debug("Find video message sent verification element")
        return self.driver.wait_till_element_is_displayed(self.VIDEO_MESSAGE_BOX)

    def is_voice_displayed(self):
        log.debug("Find voice message sent verification element")
        return self.driver.wait_till_element_is_displayed(self.VOICE_MESSAGE_BOX)

    def is_received_voice_displayed(self):
        log.debug("Find voice message receive verification element")
        return self.driver.wait_till_element_is_displayed(self.RECEIVED_VOICE_MESSAGE_BOX)

    def is_location_displayed(self):
        log.debug("Find location message sent verification element")
        return self.driver.wait_till_element_is_displayed(self.LOCATION_MESSAGE_BOX)

    def is_link(self):
        log.debug("Find link message context menu")
        return self.driver.find_element(*self.LINK)

    def is_replay_displayed(self, message, replayed):
        log.debug("Find replayed messages")
        cell = self.driver.find_elements_by_id(self.REPLY_MESSAGE_BOX)
        try:
            cell[-1].find_element_by_id(message)
            cell[-1].find_element_by_id(replayed)
            return True
        except NoSuchElementException:
            return False

    def is_replay_screen(self):
        log.debug("Find replay screen verification element")
        return self.driver.find_element_by_id(self.REPLAY_SCREEN_ID)

    def open_lang_curtain(self):
        log.debug('Open language curtain')
        self.el.tap_btn_by_id(self.LANGUAGE_CURTAIN)

    def tap_on_language(self, lang_code):
        log.debug('Open choose language screen')
        self.el.tap_btn_by_id(lang_code)

    def tap_translate_icon(self):
        log.debug('Tap translate for outgoing message')
        self.el.tap_btn_by_id(self.TRANSLATE_ICON)

    def is_curtain_display(self):
        log.debug("Check language curtain present")
        try:
            self.driver.find_element_by_id(self.LANGUAGE_CURTAIN)
            return True
        except NoSuchElementException:
            return False

    def verify_lang_code(self, lang_code):
        log.debug('Check language code "{}" display'.format(lang_code))
        try:
            self.driver.find_element_by_id(lang_code)
            return True
        except NoSuchElementException:
            return False

    def is_autotranslate_on(self):
        log.debug('Check autotraslation description on curtain')
        result = self.driver.find_element_by_id(self.AUTOTRANSLATE_ON).get_attribute('value')
        if result == self.AUTOTRANSLATE_ON_DESC:
            return True
        else:
            return False

    def is_avatar_loaded(self):
        log.debug('Check group avatar is loaded')
        result = self.driver.find_elements_by_id(self.CHAT_AVATAR)
        if result:
            return True
        else:
            return False

    def is_history_removed(self):
        log.debug('Check history removed')
        result_boxes = self.driver.find_elements_by_id(self.TEXT_MESSAGE_BOX)
        result_alert = self.driver.find_elements_by_id(self.HISTORY_REMOVED)
        if result_alert != [] and result_boxes == []:
            return True
        else:
            return False

    def is_voice_reply(self, message):
        log.debug('Find voice reply cell')
        self.driver.page_source
        result = self.driver.find_elements_by_id(self.VOICE_REPLY_BOX)
        static_elems = result[-1].find_elements_by_xpath(self.STATIC_TEXT)
        cell_texts = []
        for i in static_elems:
            cell_texts.append(i.get_attribute('value'))
        if message in cell_texts:
            return True
        else:
            return False

    def is_mention_present(self):
        log.debug('Check that mentions present')
        self.driver.page_source
        msgs = self.driver.find_elements(*self.TEXT_MESSAGE_BOX)
        if self.driver.wait_till_element_is_displayed((By.ID, self.BUBBLE_VIEW_ID)):
            last_msg = msgs[-1].find_element_by_xpath(self.TYPE_TEXT_XPATH)
            last_msg_text = last_msg.get_attribute('name')
            if re.findall(r'\[/mention\]', last_msg_text):
                log.debug('Mention is present in {}'.format(last_msg_text))
                return True
            else:
                log.debug('Mention is not present in {}'.format(last_msg_text))
                return False

    def scroll_down(self):
        el = self.driver.find_element_by_xpath('//XCUIElementTypeApplication')
        action = TouchAction(self.driver)
        swipe_start = proportion(240, 655, self.driver.get_window_size()['width'],
                                 self.driver.get_window_size()['height'])

        swipe_end = proportion(360, 575, self.driver.get_window_size()['width'],
                               self.driver.get_window_size()['height'])

        action.press(el, swipe_start['x'], swipe_start['y']).wait(100).move_to(el, swipe_end['x'],
                                                                               swipe_end['y']).release()
        action.perform()

    def is_place_displayed(self, place):
        log.debug("Find place message")
        self.driver.page_source
        place_msgs = self.driver.find_elements(*self.PLACE_MESSAGE_BOX)
        text_cells = place_msgs[-1].find_elements_by_xpath(self.STATIC_TEXT)
        texts = []
        for cell in text_cells:
            texts.append(cell.get_attribute('value'))
        if place in texts:
            log.debug('{} in {}'.format(place, texts))
            return True
        else:
            log.debug('{} not in {}'.format(place, texts))
            return False

    def is_contact_share(self, name):
        log.debug("Find contact share message")
        self.driver.page_source
        contact_msgs = self.driver.find_elements(*self.CONTACT_MESSAGE_BOX)
        try:
            contact_msgs[-1].find_element_by_id(name)
            return True
        except NoSuchElementException:
            return False

    def is_forward_present(self, msg):
        log.debug('Find last forwarded message')
        self.scroll_down_try()
        self.driver.page_source
        forwarded_msgs = self.driver.find_elements_by_id(self.FORWARD_MESSAGE_BOX)
        last_msg_text = forwarded_msgs[-1].find_element_by_xpath(self.TYPE_TEXT_XPATH)
        if last_msg_text.get_attribute('name') == msg:
            return True
        else:
            log.debug('Actual: {}\nExpected: {}'.format(last_msg_text.get_attribute('name'), msg))
            return False

    def get_send_status(self, msg_type):
        msg_boxes = ''
        if msg_type == 'text':
            msg_boxes = self.driver.find_elements(*self.TEXT_MESSAGE_BOX)
        elif msg_type == 'voice':
            msg_boxes = self.driver.find_elements(*self.VOICE_MESSAGE_BOX)
        elif msg_type == 'image':
            msg_boxes = self.driver.find_elements(*self.IMAGE_MESSAGE_BOX)
        elif msg_type == 'location':
            msg_boxes = self.driver.find_elements(*self.LOCATION_MESSAGE_BOX)
        elif msg_type == 'contact':
            msg_boxes = self.driver.find_elements(*self.CONTACT_MESSAGE_BOX)
        elif msg_type == 'file':
            msg_boxes = self.driver.find_elements(*self.FILE_MESSAGE_BOX)
        elif msg_type == 'sticker':
            msg_boxes = self.driver.find_elements(*self.STICKER_MESSAGE_BOX)
        status = msg_boxes[-1].find_elements_by_id(self.SEND_STATUS)
        if status:
            return True
        else:
            return False

    def is_sticker_displayed(self):
        log.debug('Find Sticker in the chat')
        return self.driver.wait_till_element_is_displayed(self.STICKER_MESSAGE_BOX)

    def is_sticker_reply(self):
        log.debug("Find sticker reply box")
        return self.driver.wait_till_element_is_displayed(self.STICKER_REPLY_BOX)

    def get_sticker_count(self, before=0):
        log.debug('Collect all images in chat')
        sticker_boxes = self.driver.find_elements(*self.STICKER_MESSAGE_BOX)
        log.debug('Collected "{}" images'.format(str(len(sticker_boxes))))
        actual = len(sticker_boxes) - before
        return actual

    def is_channel_created(self):
        log.debug("Check channel creation sys message")
        return self.driver.wait_till_element_is_displayed(self.CHANNEL_CREATED)
