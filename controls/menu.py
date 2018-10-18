from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from common_tools.common_methods import CM
from enums import wheel_enums
from model.element import Element, center
from utils.logs import log


class Menu:
    WHEEL_BTN = (By.ID, "wheel_open_button")
    MEDIA_PHOTOS = (By.ID, 'wheel_2_item_image')
    GALLERY = (By.ID, 'Select from Gallery')
    # TODO: update var "FIRST_LVL_ITEMS"
    FIRST_LVL_WHEEL = (By.ID, "wheel_0")
    SECOND_LVL_WHEEL = (By.ID, "wheel_1")
    THIRST_LVL_WHEEL = (By.ID, "wheel_2")

    ITEMS_TEXT = "wheel_item_title"

    # LS - it's meaning to the "LEFT SIDE"
    # RS - it's meaning to the "RIGHT SIDE"
    FIRST_WHEEL_RS_IN_PERCENT = (0.869, 0.781, 0.594, 0.889)
    FIRST_WHEEL_LS_IN_PERCENT = (0.594, 0.889, 0.869, 0.781)
    SECOND_WHEEL_RS_IN_PERCENT = (0.715, 0.645, 0.352, 0.805)
    SECOND_WHEEL_LS_IN_PERCENT = (0.390, 0.820, 0.715, 0.645)

    def __init__(self, driver):
        self.driver = driver
        self.wenums = wheel_enums
        self.FIRST_WHEEL_RS = None
        self.FIRST_WHEEL_LS = None
        self.SECOND_WHEEL_RS = None
        self.SECOND_WHEEL_LS = None
        self.el = Element(self.driver)
        self.get_wheel()

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

    def go_to(self, first_lvl_item, second_lvl_items=None, screen_name=None, third_lvl_item=None):
        log.debug("Open Menu and select first lvl item: '{}'".format(first_lvl_item))
        self.open_menu()
        self.wheel_executor(self.FIRST_LVL_WHEEL, first_lvl_item, self.wenums.FIRST_LVL_ITEM_LIST)
        if second_lvl_items is not None:
            for item in second_lvl_items:
                log.debug("Select second lvl item: '{}'".format(item))
                second_lvl_item_list = self.get_second_level_item_list(first_lvl_item, screen_name)
                self.wheel_executor(self.SECOND_LVL_WHEEL, item, second_lvl_item_list)
            if third_lvl_item is not None:
                # TODO: Update or replace wenums for THIRST_LVL_WHEEL
                self.wheel_executor(self.THIRST_LVL_WHEEL, third_lvl_item, self.wenums.THIRD_LVL_ITEM_LIST)

    def get_second_level_item_list(self, first_lvl_item, which_action=None):
        if first_lvl_item == self.wenums.ACTIONS:
            return self.wenums.SECOND_LVL_MANAGER[first_lvl_item][which_action]
        return self.wenums.SECOND_LVL_MANAGER[first_lvl_item]

    def wheel_executor(self, wheel_location, item_name, existed_item_list):
        is_elem_hunted, counter, visible_items, visible_item_names = self.wheel_hunter(wheel_location, item_name)
        if is_elem_hunted is False:
            wheel_lvl = wheel_location[1]
            self.wheel_inspector(wheel_lvl, existed_item_list, item_name, visible_item_names)
            self.wheel_hunter(wheel_location, item_name)

    def wheel_inspector(self, wheel_lvl, existed_item_names, item_name, visible_item_names):
        log.debug("Search the item in the wheel")
        required_wheel_position = self.get_required_position(existed_item_names, item_name)
        wheel_current_position = self.get_wheel_current_position(existed_item_names, visible_item_names)
        self.scroll_wheel(wheel_lvl, *self.get_swipe_counter(wheel_current_position, required_wheel_position))

    def wheel_hunter(self, wheel_location, req_item_name):
        log.debug("Get wheel")
        wheel = self.driver.find_element(*wheel_location)
        log.debug("Get visible items count")
        real_first_lvl_elems = wheel.find_elements_by_id(self.ITEMS_TEXT)
        counter = len(real_first_lvl_elems)
        log.debug("Counter is " + str(counter))
        visible_item_names = []
        log.debug("Get visible item names")
        for elem in real_first_lvl_elems:
            elem_name = elem.get_attribute('value')
            if elem_name == req_item_name:
                try:
                    log.debug("Try click on: {}".format(req_item_name))
                    # TODO: Remove "if req_item_name == "Contacts":" when bug is fixed
                    # if req_item_name == "Contacts":
                    #     self.scroll_wheel("wheel_0", "Right", counter=1)
                    elem.click()
                    log.debug("Element has been hunted")
                    return True, None, None, None
                # TODO: Replace "Exception"!!!
                except Exception as msg:
                    log.debug("Exception occurred. Element: '{}'".format(elem_name))
                    log.debug(msg)
                    visible_item_names.append(elem_name)
            else:
                log.debug("Add '{}' to list".format(elem_name))
                visible_item_names.append(elem_name)
        log.debug("RETURN END")
        return False, counter, real_first_lvl_elems, visible_item_names

    def open_menu(self):
        log.debug("Open Menu")
        self.driver.find_element(*self.WHEEL_BTN).click()

    def close_menu(self):
        log.debug("Close Menu")
        self.driver.find_element(*self.WHEEL_BTN).click()

    def get_required_locators(self, req_lvl):
        if req_lvl == 'wheel_0':
            log.debug("First level locators prepared")
            return self.FIRST_WHEEL_LS, self.FIRST_WHEEL_RS
        elif req_lvl == "wheel_1":
            log.debug("Second level locators prepared")
            return self.SECOND_WHEEL_LS, self.SECOND_WHEEL_RS
        elif req_lvl == "wheel_2":
            log.debug("The feature is not implemented")
            # TODO: implement third level wheel
        else:
            log.error("Could not get required locators")
            raise IndexError

    def scroll_wheel(self, wheel_lvl, side, counter=1):
        """
        This method scrolling the wheel
        :param wheel_lvl: (str) Wheel level: "first", "second" or "third"
        :param side: (str) Scroll way: "Left" or "Right"
        :param counter: (int) How many times we need to use scroll
        :return:
        """
        counter += 1
        left_side, right_side = self.get_required_locators(wheel_lvl)
        log.debug("Scrolling to the {} side".format(side))
        if side == "Left":
            log.debug("left")
            for i in range(counter):
                self.driver.swipe_screen(*left_side)
        else:
            for i in range(counter):
                self.driver.swipe_screen(*right_side)

    def go_to_home_screen(self):
        """
        Long press on wheel button
        """
        self.open_menu()
        log.debug("Go to the Home page")
        elem = self.driver.find_element(*self.WHEEL_BTN)
        action = TouchAction(self.driver)
        action.long_press(el=elem, duration=3000).release().perform()

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

    # TODO: "Implement these features as part third level wheel"
    def tap_first_media(self):
        log.debug("Tap first photo from '{}' section on wheel".format("Recents"))
        photos = self.driver.find_elements(*self.MEDIA_PHOTOS)
        self.el.tap_element(photos[0])

    def long_press_wheel(self):
        log.debug("LOng press tp '{}' for got home page".format("Edit"))
        menu = Menu(self.driver)
        wheel_btn = self.driver.find_element(*menu.WHEEL_BTN)
        action = TouchAction(self.driver)
        action.press(x=center(wheel_btn)['XCentr'], y=center(wheel_btn)['YCentr']).wait(2000).release().perform()
