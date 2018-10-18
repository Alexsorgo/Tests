from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class GroupScreen(BaseScreen):
    DONE_BTN = (By.ID, 'DONE')
    GROUP_NAME = (By.ID, 'change_group_view')
    ALIAS = (By.ID, 'change_alias_view')
    PARTICIPANTS = (By.ID, 'update_participants_view')
    GROUP_NAME_FIELD = (By.ID, 'name_field_input')
    CANCEL = (By.ID, 'cancel_button')
    ALIAS_FIELD = (By.ID, 'alias_field_input')
    CREATE_GROUP = (By.ID, 'create_button')
    GROUP_FROM_LIST = (By.ID, 'message_cell')
    DELETE_PARTICIPANTS = (By.ID, 'Delete Participants')
    PARTICIPANT_CELL = (By.ID, 'participants_contact_cell')
    PARTICIPANT_TITLE = 'participant_title'
    GROUP_CREATED = (By.ID, 'You created the group')
    
    def add_user(self, user):
        log.debug("Add '{}' to group".format(user))
        table = self.driver.find_elements(*self.PARTICIPANT_CELL)
        for cell in table:
            name = cell.find_element_by_id(self.PARTICIPANT_TITLE).get_attribute('value')
            if name == user:
                self.el.tap_element(cell)
                break
        else:
            log.error('No {} in list'.format(user))
            raise NoSuchElementException

    def tap_done(self):
        log.debug("Tap '{}' button".format("Done"))
        self.el.tap_btn(self.DONE_BTN)

    def tap_group_name(self):
        log.debug("Open '{}' screen".format("Group name"))
        self.el.click_btn(self.GROUP_NAME)

    def tap_alias(self):
        log.debug("Open '{}' screen".format("Alias"))
        self.el.click_btn(self.ALIAS)

    def tap_participants(self):
        log.debug("Open '{}' screen".format("Participants"))
        self.el.click_btn(self.PARTICIPANTS)

    def set_group_name(self, name):
        log.debug("Set '{}' in group name field".format(name))
        self.el.set_text_clear(self.GROUP_NAME_FIELD, name)

    def tap_cancel(self):
        log.debug("Tap '{}' button".format("Cancel"))
        self.el.click_btn(self.CANCEL)

    def set_alias(self, alias):
        log.debug("Set '{}' in alias field".format(alias))
        self.el.set_text_clear(self.ALIAS_FIELD, alias)

    def tap_create(self):
        log.debug("Tap '{}' button".format("Create"))
        self.el.click_btn(self.CREATE_GROUP)

    def input_value(self):
        log.debug("Get set '{}' value".format("Group name"))
        el = self.driver.find_element(*self.GROUP_NAME_FIELD)
        return el.get_attribute('value')

    def open_group(self):
        log.debug("Open first '{}' from list".format("Group"))
        self.el.click_btn(self.GROUP_FROM_LIST)

    def delete_participant(self):
        log.debug("Open '{}' list".format("Participants"))
        self.el.click_btn(self.DELETE_PARTICIPANTS)

    def mark_participants(self):
        log.debug("Mark all '{}' to delete them".format("Participants"))
        for part in self.driver.find_elements(*self.PARTICIPANT_CELL):
            part.click()

    def is_group_created(self):
        log.debug('Find create group verification element')
        return self.driver.find_element(*self.GROUP_CREATED)

    def default_alias(self, alias):
        log.debug('Check default alias')
        result = self.driver.find_elements_by_id(alias)
        if result:
            return True
        else:
            return False
