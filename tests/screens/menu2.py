from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from tests.common_tools import CM
from tests.enums import wheel_enums
from tests.model.element import Element, center
from tests.utils.logs import log


class Menu:
    WHEEL_BTN = (By.ID, "wheel_open_button")
    MEDIA_PHOTOS = (By.ID, 'wheel_2_item_image')
    GALLERY = (By.ID, 'Select from Gallery')
    # TODO: update var "FIRST_LVL_ITEMS"
    FIRST_LVL_WHEEL = "wheel_0"
    SECOND_LVL_WHEEL = (By.ID, "wheel_1")
    THIRST_LVL_WHEEL = (By.ID, "wheel_2")

    ITEMS_TEXT = "wheel_item_title"

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

    def get_wheel(self):
        if self.FIRST_WHEEL_RS or self.FIRST_WHEEL_LS or self.SECOND_WHEEL_RS or self.SECOND_WHEEL_LS is None:
            width, height = self.driver.get_window_size().values()
            self.FIRST_WHEEL_RS = (CM.set_wheel_coordinates(width, height, self.FIRST_WHEEL_RS_IN_PERCENT))
            self.FIRST_WHEEL_LS = (CM.set_wheel_coordinates(width, height, self.FIRST_WHEEL_LS_IN_PERCENT))
            self.SECOND_WHEEL_RS = (CM.set_wheel_coordinates(width, height, self.SECOND_WHEEL_RS_IN_PERCENT))
            self.SECOND_WHEEL_LS = (CM.set_wheel_coordinates(width, height, self.SECOND_WHEEL_LS_IN_PERCENT))
        return self.FIRST_WHEEL_RS, self.FIRST_WHEEL_LS, self.SECOND_WHEEL_RS, self.SECOND_WHEEL_LS

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

    def get_second_level_item_list(self, first_lvl_item, screen_name=None):
        if first_lvl_item == self.wenums.ACTIONS:
            return self.wenums.SECOND_LVL_MANAGER[first_lvl_item][screen_name]
        return self.wenums.SECOND_LVL_MANAGER[first_lvl_item]

    def wheel_executor(self, wheel_location, item_name, existed_item_list):
        status, current_visible = self.visible_items(wheel_location, item_name)
        if status is False:
            req_index = existed_item_list.index(item_name)
            current_position = []
            for item in current_visible:
                current_position.append(existed_item_list.index(item))
            self.scroll_wheel(wheel_location, *self.get_swipe_counter(current_position, req_index))
            self.visible_items(wheel_location, item_name)

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

    def get_required_locators(self, req_lvl):
        print(req_lvl)
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

    def visible_items(self, wheel_location, item_name):
        wheel = self.driver.find_element_by_id(wheel_location)
        real_first_lvl_elems = wheel.find_elements_by_id(self.ITEMS_TEXT)
        visible_item_names = []
        log.debug("Get visible item names")
        for elem in real_first_lvl_elems:
            elem_name = elem.get_attribute('value')
            visible_item_names.append(elem_name)
        if item_name in visible_item_names:
            self.el.tap_btn_by_id(item_name)
            return True, visible_item_names
        else:
            return False, visible_item_names

    def open_menu(self):
        log.debug("Open Menu")
        self.driver.find_element(*self.WHEEL_BTN).click()

    def long_press_wheel(self):
        log.debug("LOng press tp '{}' for got home page".format("Edit"))
        menu = Menu(self.driver)
        wheel_btn = self.driver.find_element(*menu.WHEEL_BTN)
        action = TouchAction(self.driver)
        action.press(x=center(wheel_btn)['XCentr'], y=center(wheel_btn)['YCentr']).wait(2000).release().perform()
