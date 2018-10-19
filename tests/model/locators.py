# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    NEXT_BUTTON = (By.ID, 'NEXT')
    PHONE_FIELD = (By.ID, 'phone_field_input')
    CONFIRM_BUTTON = (By.ID, 'Confirm')
    SMS_CODE_FILED = (By.ID, 'code_field_input')
    COUNTRY_CODE = (By.ID, 'phone_field_code_input')
    TERMS = (By.ID, 'Terms of Service')
    LOGO = (By.ID, 'auth_light_logo')


class RegistrationPageLocators(object):
    FIRSTNAME_FIELD = (By.ID, 'first_name_field_input')
    LASTNAME_FIELD = (By.ID, 'last_name_field')
    DONE_BUTTON = (By.ID, 'DONE')
    CHECK_PAGE = (By.ID, 'How would you like to be called?')


class MainPageLocators(object):
    QR = (By.ID, 'ic qr code')
    WHEEL_BTN = (By.ID, 'btn wheel inactive')
    CONTACT_LIST = (By.ID, 'Go to history')
    ADDED_USER = (By.XPATH, '//XCUIElementTypeStaticText[@name="Added"]')
    OTHER_PROFILES = (By.XPATH, '//XCUIElementTypeCell[@name="contact_request_profile_contact_cell"]'
                                '/XCUIElementTypeButton')


class WheelLocators(object):
    FULL_SCREEN = (By.XPATH, '//XCUIElementTypeApplication')
    SETTINGS_BTN = (By.ID, 'ic_options')
    LOGOUT_BTN = (By.ID, 'LOG OUT')
    CONTACTS_BTN = (By.ID, 'ic_contacts')
    NEW_CONTACT = (By.ID, 'New Contact')
    BY_NUMBER = (By.ID, 'ic_by_number')
    BY_USERNAME = (By.ID, 'ic_by_username')
    BY_CONTACTS = (By.ID, 'ic_by_contacts')
    EDIT_PROFILE_BTN = (By.ID, 'ic_edit_profile')
    EDIT_USERNAME = (By.ID, 'My Username')
    EDIT_NAME = (By.ID, 'My Name')
    EDIT_PHOTO = (By.ID, 'My Photo')
    GALLERY = (By.ID, 'Select from Gallery')
    WHEEL_BTN = (By.ID, 'wheel_open_button')
    LIST = (By.ID, 'ic_list')
    MEDIA = (By.ID, 'ic_gallery')
    MEDIA_GALLERY = (By.ID, 'wheel_1_item_wheel_item_gallery')
    MEDIA_PHOTOS = (By.ID, 'wheel_2_item_image')
    CAMERA = (By.ID, 'ic_camera')
    LOCATION = (By.ID, 'ic_location')
    SEND_LOCATION = (By.ID, 'Send Locations')
    GROUPS = (By.ID, 'ic_groups')
    GROUPS_RECENTS = (By.ID, 'ic_recents')
    GROUPS_FAMILY = (By.ID, 'ic_family')
    GROUPS_NEW = (By.ID, 'ic_new_group')


class AddContactLocators(object):
    SEARCH = (By.ID, 'SEARCH')
    CONTACT_PHONE_FIELD = (By.ID, 'phone_field_input')
    ADD_BTN = (By.ID, 'ADD TO CONTACTS')
    CONTACT_USERNAME_FIELD = (By.ID, 'username_field_input')
    CELL = (By.XPATH, '//XCUIElementTypeCell')
    ADD_CONTACT = (By.ID, 'Add')
    STATIC_TEXT = (By.XPATH, 'XCUIElementTypeStaticText')
    BTN = (By.XPATH, '//XCUIElementTypeButton')
    REQUESTED = (By.ID, 'Requested')
    COUNTRY_FILED = (By.ID, 'phone_field_code_input')


class ProfilePageLocators(object):
    USERNAME_FIELD = (By.ID, 'username_field_input')
    FIRSTNAME_FIELD = (By.ID, 'first_name_field_input')
    LASTNAME_FIELD = (By.ID, 'last_name_field_input')
    DONE_BTN = (By.ID, 'DONE')
    KEEP_BTN = (By.ID, 'keep_button')
    ACCEPT_PHOTO = (By.ID, 'btn wheel done')


class ChatPageLocators(object):
    KEYBOARD_BTN = (By.ID, 'default_input_view_keyboard_button')
    MICROPHONE_BTN = (By.ID, 'default_input_view_microphone_button')
    SEND_BTN = (By.ID, 'text_input_bar_send_button')
    RECORD_SEND_BTN = (By.ID, 'record_input_view_send_button')
    CHAT_FIELD = (By.ID, 'text_input_bar_text_view')
    NEXT_ARROW = (By.ID, 'contextMenuNext')
    MSG_FORWARD = (By.ID, 'Forward')
    MSG_COPY = (By.ID, 'Copy')
    MSG_REPLY = (By.ID, 'Reply')
    MSG_STAR = (By.ID, 'contextMenuStar')
    MSG_TRANSLATE = (By.ID, 'Translate')
    MSG_EDIT = (By.ID, 'Edit')
    MSG_DELETE = (By.ID, 'Delete')
    BLOCK_BTN = (By.ID, 'default_input_view_action_button')
    OPEN_PROFILE = (By.ID, 'placeholder_image')
    DELETE_FOR_ME = (By.ID, 'Delete for me')
    STOP_SENDING = (By.ID, 'ic btn stop download')


class OtherProfilePageLocators(object):
    BLOCK_USER = (By.ID, 'Block user')
    ACCEPT_ALLERT = (By.ID, 'Yes')
    UNBLOCK_USER = (By.ID, 'Unblock user')
    SEND_A_MESSAGE = (By.ID, 'SEND A MESSAGE')
    CONTACT_USER = (By.ID, 'America Mishchenko')
    BANNED_USER = (By.ID, 'Banned')


class CameraPageLocators(object):
    TAKE_PHOTO = (By.ID, 'btn take photo default')
    CANCEL_PHOTO = (By.ID, 'close_button')
    CHANGE_CAMERA = (By.ID, 'ic change camera ios')
    VIDEO_CAMERA = (By.ID, 'Video')
    PHOTO_CAMERA = (By.ID, 'Photo')
    USE_PHOTO = (By.ID, 'Use photo')
    RETAKE = (By.ID, 'Retake')
    TAKE_VIDEO = (By.ID, 'btn record default')
    STOP_VIDEO = (By.ID, 'btn stop recording')
    USE_VIDEO = (By.ID, 'Use video')


class LocationPageLocators(object):
    CLOSE_LOCATION = (By.ID, 'close_button')
    MAP_MODE = (By.ID, 'ic map mode')
    CURRENT_LOCATION = (By.ID, 'ic map current')
    SEARCH = (By.ID, 'ic map search')
    SEND_LOCATION = (By.ID, 'send')


class GroupPageLocators(object):
    ADDED_LIST = (By.XPATH, '//XCUIElementTypeCell')
    DONE_BTN = (By.ID, 'DONE')
    GROUP_NAME = (By.ID, 'change_group_view')
    ALIAS = (By.ID, 'change_alias_view')
    PARTICIPANTS = (By.ID, 'update_participants_view')
    GROUP_NAME_FIELD = (By.ID, 'name_field_input')
    CANCEL = (By.ID, 'cancel_button')
    SAVE_BTN = (By.ID, 'save_button')
    ALIAS_FIELD = (By.ID, 'alias_field_input')
    CREATE_GROUP = (By.ID, 'create_button')
    GROUP_FROM_LIST = (By.ID, 'message_cell')
    DELETE_PARTICIPANTS = (By.ID, 'Delete Participants')
    PARTICIPANT_CELL = (By.ID, 'participants_contact_cell')
    DELETE_BTN = (By.ID, 'delete_button')
