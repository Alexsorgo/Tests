from configs import config
from screens.base_screen import BaseScreen
from utils.logs import log


class ParticipantsScreen(BaseScreen):
    PARTICIPANT_CELL = 'participants_contact_cell'
    PARTICIPANT_ALIAS = 'participant_title'
    PARTICIPANT_USER = config.AMERICA_USERNAME

    def is_participant_updated(self, alias):
        log.debug('Collect participants alias')
        aliases = self.driver.find_elements_by_id(self.PARTICIPANT_ALIAS)
        names = []
        for al in aliases:
            names.append(al.get_attribute('value'))
        if alias in names:
            return True
        else:
            return False

    def open_participant(self):
        log.debug('Open participant: "{}"'.format(self.PARTICIPANT_USER))
        aliases = self.driver.find_elements_by_id(self.PARTICIPANT_ALIAS)
        for alias in aliases:
            if alias.get_attribute('value') == self.PARTICIPANT_USER:
                self.el.tap_element(alias)
                break
