from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

import enums
from common_tools.common_methods import CM
from enums import wheel_enums
from model.element import Element
from utils.logs import log


class WheelView:
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
    GALLERY = (By.ID, 'Select from gallery')
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

    FIRST_WHEEL = "wheel_0"
    SECOND_WHEEL = "wheel_1"
    ITEMS_ID = "wheel_item_title"
    GET_ITEM_TEXT = "//XCUIElementTypeStaticText"

    # LS - it's meaning to the "LEFT SIDE"
    # RS - it's meaning to the "RIGHT SIDE"
    FIRST_WHEEL_RS_IN_PERCENT = (0.869, 0.781, 0.594, 0.889)
    FIRST_WHEEL_LS_IN_PERCENT = (0.594, 0.889, 0.869, 0.781)
    SECOND_WHEEL_RS_IN_PERCENT = (0.715, 0.645, 0.352, 0.805)
    SECOND_WHEEL_LS_IN_PERCENT = (0.352, 0.805, 0.715, 0.645)

    def __init__(self, driver):
        self.driver = driver
        self.wenums = wheel_enums
        self.FIRST_WHEEL_RS = None
        self.FIRST_WHEEL_LS = None
        self.SECOND_WHEEL_RS = None
        self.SECOND_WHEEL_LS = None
        self.el = Element(self.driver)
        self.get_wheel()

    def tap_settings(self):
        log.debug("Tap '{}' button on wheel".format("Settings"))
        self.el.click_btn(self.SETTINGS_BTN)

    def tap_logout(self):
        log.debug("Tap '{}' button on wheel".format("Logout"))
        self.el.tap_btn(self.LOGOUT_BTN)

    def tap_myself_chat(self):
        log.debug("Tap first '{}' user".format("Added"))
        self.get_first_level_item(enums.wheel_enums.MYSELF, enums.wheel_enums.FIRST_LVL)

    def tap_contacts(self):
        log.debug("Tap '{}' button on wheel".format("Contacts"))
        self.get_first_level_item(enums.wheel_enums.CONTACTS, enums.wheel_enums.FIRST_LVL)

    def tap_new_contacts(self):
        log.debug("Tap '{}' button on wheel".format("New contact"))
        self.get_second_level_item(enums.wheel_enums.NEW_CONTACT, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.CONTACTS_LVL_ITEM_LIST)

    def tap_add_by_number(self):
        log.debug("Tap '{}' button on wheel".format("Add contact by number"))
        self.get_second_level_item(enums.wheel_enums.BY_NUMBER, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.CONTACTS_LVL_ITEM_LIST)

    def tap_add_by_username(self):
        log.debug("Tap '{}' button on wheel".format("Add contact by username"))
        self.get_second_level_item(enums.wheel_enums.BY_USERNAME, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.CONTACTS_LVL_ITEM_LIST)

    def tap_add_by_contacts(self):
        log.debug("Tap '{}' button on wheel".format("Add contact by phone book"))
        self.get_second_level_item(enums.wheel_enums.BY_CONTACTS, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.CONTACTS_LVL_ITEM_LIST)

    def tap_edit_profile(self):
        log.debug("Tap '{}' button on wheel".format("Edit profile"))
        self.get_second_level_item(enums.wheel_enums.EDIT_PROFILE, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.EDIT_PROFILE_ITEM_LIST)

    def tap_edit_username(self):
        log.debug("Tap '{}' button on wheel".format("Edit username"))
        self.get_second_level_item(enums.wheel_enums.MY_USERNAME, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.EDIT_PROFILE_ITEM_LIST)

    def tap_edit_name(self):
        log.debug("Tap '{}' button on wheel".format("Edit name"))
        self.get_second_level_item(enums.wheel_enums.MY_NAME, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.EDIT_PROFILE_ITEM_LIST)

    def tap_edit_photo(self):
        log.debug("Tap '{}' button on wheel".format("Edit photo"))
        self.get_second_level_item(enums.wheel_enums.MY_PHOTO, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.EDIT_PROFILE_ITEM_LIST)

    def tap_photo_form_gallery(self):
        log.debug("Tap '{}' button on wheel".format("Photo from gallery"))
        self.el.tap_btn(self.GALLERY)

    def tap_list(self):
        log.debug("Tap '{}' section on wheel".format("All"))
        self.el.tap_btn(self.LIST)

    def tap_media(self):
        log.debug("Tap '{}' button on wheel".format("Media"))
        self.get_second_level_item(enums.wheel_enums.MEDIA, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.CHAT_ACTIONS_LVL_ITEM_LIST)

    def tap_media_gallery(self):
        log.debug("Tap '{}' button from media section on wheel".format("Gallery"))
        self.el.tap_btn(self.MEDIA_GALLERY)

    def tap_first_media(self):
        log.debug("Tap first photo from '{}' section on wheel".format("Recents"))
        photos = self.driver.find_elements(*self.MEDIA_PHOTOS)
        self.el.tap_element(photos[0])

    def tap_camera_wheel(self):
        log.debug("Tap '{}' button on wheel".format("Camera"))
        self.get_second_level_item(enums.wheel_enums.CAMERA, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.CHAT_ACTIONS_LVL_ITEM_LIST)

    def tap_location(self):
        log.debug("Tap '{}' button on wheel".format("Location"))
        self.get_second_level_item(enums.wheel_enums.LOCATION, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.CHAT_ACTIONS_LVL_ITEM_LIST)

    def tap_send_locations(self):
        log.debug("Tap '{}' button on wheel".format("Send location"))
        self.el.tap_btn(self.SEND_LOCATION)

    def tap_groups(self):
        log.debug("Tap '{}' button on wheel".format("Groups"))
        self.get_first_level_item(enums.wheel_enums.GROUPS, enums.wheel_enums.FIRST_LVL)

    def tap_new_group(self):
        log.debug("Tap '{}' button on wheel".format("New group"))
        self.get_second_level_item(enums.wheel_enums.NEW_GROUP, enums.wheel_enums.SECOND_LVL,
                                   enums.wheel_enums.GROUPS_LVL_ITEM_LIST)

    def get_wheel(self):
        if self.FIRST_WHEEL_RS or self.FIRST_WHEEL_LS or self.SECOND_WHEEL_RS or self.SECOND_WHEEL_LS is None:
            width, height = self.get_screen()
            self.FIRST_WHEEL_RS = (CM.set_wheel_coordinates(width, height, self.FIRST_WHEEL_RS_IN_PERCENT))
            self.FIRST_WHEEL_LS = (CM.set_wheel_coordinates(width, height, self.FIRST_WHEEL_LS_IN_PERCENT))
            self.SECOND_WHEEL_RS = (CM.set_wheel_coordinates(width, height, self.SECOND_WHEEL_RS_IN_PERCENT))
            self.SECOND_WHEEL_LS = (CM.set_wheel_coordinates(width, height, self.SECOND_WHEEL_LS_IN_PERCENT))
        return self.FIRST_WHEEL_RS, self.FIRST_WHEEL_LS, self.SECOND_WHEEL_RS, self.SECOND_WHEEL_LS

    def get_screen(self):
        screen_size = self.driver.get_window_size()
        width = screen_size["width"]
        height = screen_size["height"]
        return width, height

    def get_visible_item_names(self, req_lvl):
        visible_item_names = []
        log.debug("Get visible items names")
        main_elem = self.driver.find_element_by_id(req_lvl)
        elems = main_elem.find_elements_by_id(self.ITEMS_ID)
        for elem in elems:
            visible_item_names.append(elem.get_attribute('value'))
        log.debug(visible_item_names)
        return visible_item_names

    def click_on_item(self, item_name, req_lvl):
        log.debug("Click on the {} item".format(item_name))
        main_elem = self.driver.find_element_by_id(req_lvl)
        elems = main_elem.find_elements_by_id(self.ITEMS_ID)
        for elem in elems:
            if elem.get_attribute('value') == item_name:
                el = Element(self.driver)
                el.tap_element(elem)
                # elem.click()
                break

    def get_counter(self, req_lvl):
        log.debug("Get visible items count")
        main_elem = self.driver.find_element_by_id(req_lvl)
        elems = main_elem.find_elements_by_id(self.ITEMS_ID)
        counter = len(elems)
        log.debug("Counter is " + str(counter))
        return counter

    def open_menu(self):
        log.debug("Open Menu")
        self.driver.find_element(*self.WHEEL_BTN).click()

    def close_menu(self):
        log.debug("Close Menu")
        self.driver.find_element(*self.WHEEL_BTN).click()

    def scroll_first_wheel(self, side, counter=1):
        """
        This method scrolling the first wheel
        :param side: (str) Scroll way: "Left" or "Right"
        :param counter: (int) How many times we need to use scroll
        :return:
        """
        log.debug("Scrolling to the {} side".format(side))
        if side == "Left":
            log.debug("left")
            for i in range(counter):
                self.driver.swipe_screen(*self.FIRST_WHEEL_LS)
        else:
            for i in range(counter):
                print(self.FIRST_WHEEL_RS)
                self.driver.swipe_screen(*self.FIRST_WHEEL_RS)

    def scroll_second_wheel(self, side, counter=1):
        """
        This method scrolling the second wheel
        :param side: (str) Scroll way: "Left" or "Right"
        :param counter: (int) How many times we need to use scroll
        :return:
        """
        log.debug("Scrolling to the {} side".format(side))
        if side == "Left":
            log.debug("left")
            for i in range(counter):
                self.driver.swipe_screen(*self.SECOND_WHEEL_LS)
        else:
            for i in range(counter):
                self.driver.swipe_screen(*self.SECOND_WHEEL_RS)

    def go_to_home_screen(self):
        """
        Long press on wheel button
        """
        self.open_menu()
        log.debug("Go to the Home page")
        elem = self.driver.find_element(*self.WHEEL_BTN)
        action = TouchAction(self.driver)
        action.long_press(el=elem, duration=3000).release().perform()

    # main control method
    def get_first_level_item(self, required_item_name, req_lvl):
        log.debug("Menu - select item '{}'".format(required_item_name))
        visible_item_names = self.get_visible_item_names(req_lvl)
        if visible_item_names.__contains__(required_item_name):
            log.debug("Click on item '{}'".format(required_item_name))
            self.click_on_item(required_item_name, wheel_enums.FIRST_LVL)
            # TODO: implement returning of the screen object
            # import some_screen
            # return some_screen
        else:
            # TODO: move 'existed_item_names' to the method's arguments
            log.debug("Search the item in the wheel")
            existed_item_names = wheel_enums.FIRST_LVL_ITEM_LIST
            required_wheel_position = self.get_required_position(existed_item_names, required_item_name)
            wheel_current_position = self.get_wheel_current_position(existed_item_names, visible_item_names)
            side, counter = self.get_swipe_counter(wheel_current_position, required_wheel_position)
            self.scroll_first_wheel(side, counter+1)
            self.click_on_item(required_item_name, wheel_enums.FIRST_LVL)

    # main control method
    def get_second_level_item(self, required_item_name, req_lvl, wheel_items=None):
        log.debug("Menu - select item '{}'".format(required_item_name))
        visible_item_names = self.get_visible_item_names(req_lvl)
        if visible_item_names.__contains__(required_item_name):
            log.debug("Click on item '{}'".format(required_item_name))
            self.click_on_item(required_item_name, req_lvl)
            # TODO: need to implement returning of the screen object
            # import some_screen
            # return some_screen
        else:
            log.debug("Search the item in the wheel")
            existed_item_names = wheel_items
            print(existed_item_names)
            required_wheel_position = self.get_required_position(existed_item_names, required_item_name)
            wheel_current_position = self.get_wheel_current_position(existed_item_names, visible_item_names)
            side, counter = self.get_swipe_counter(wheel_current_position, required_wheel_position)
            self.scroll_second_wheel(side, counter)
            self.click_on_item(required_item_name, req_lvl)

    # TODO: Use this implementation when android element IDs are added
    # def get_visible_item_names(self, items_locator):
    #     visible_item_names = []
    #     visible_items = self.driver.find_elements(*items_locator)
    #     for item in visible_items:
    #         visible_item_names.append(item.get_text())
    #     return visible_item_names

    @staticmethod
    def get_wheel_current_position(existed_items, visible_items):
        """
        This method measures the wheel's current position indexes
        :param existed_items: (list) Basic list with all existed items
        :param visible_items: (list) List with all visible item's names
        :return: (list) Wheel's current position indexes
        """
        log.debug("Init the current wheel position")
        current_position = []
        for item in visible_items:
            current_position.append(existed_items.index(item))
        log.debug(current_position)
        return current_position

    @staticmethod
    def get_required_position(existed_items, req_item):
        """
        This method measures the wheel's required position where the required item is visible.
        :param existed_items: (list) Basic list with all existed items
        :param req_item: (str) Required item name
        :return: (int) Wheel's required position index
        """
        log.debug("Search for required item index")
        index = existed_items.index(req_item)
        log.debug("Index is {}".format(index))
        return index

    @staticmethod
    def get_swipe_counter(cur_position, req_position):
        """
        This method measures the side to swipe
        :param cur_position: (list) Wheel's current position indexes
        :param req_position: (int) Wheel's required position index
        :return: (str) Side to swipe and (int) Swipe counter
        """
        log.debug("Get side swipe and swipe counter")
        cur_and_req_positions = cur_position
        cur_and_req_positions.append(req_position)
        log.debug(cur_and_req_positions)
        cur_and_req_positions.sort()
        req_position_index = cur_and_req_positions.index(req_position)
        # if left way
        if req_position_index == 0:
            side = "Left"
            position_difference = cur_and_req_positions[req_position_index + 1] - \
                cur_and_req_positions[req_position_index]
            counter = int(position_difference / 3 + 1)
            return side, counter
        # if right way
        else:
            side = "Right"
            position_difference = cur_and_req_positions[req_position_index] - \
                cur_and_req_positions[req_position_index - 1]
            counter = int(position_difference / 3 + 1)
            return side, counter
