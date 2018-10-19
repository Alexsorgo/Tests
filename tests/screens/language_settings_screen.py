from tests.screens.base_screen import BaseScreen
from tests.utils.logs import log


class LanguageSettingsScreen(BaseScreen):
    IS_LANGUAGE_SETTINGS_ID = 'LANGUAGE SETTINGS'
    LANGUAGE_ON_SENDING_ID = 'translation_directable_action_cell'
    AUTO_ON_SENDING_ID = 'translation_switchable_action_cell'
    ALERT_ONCE_ID = 'Once'
    ALERT_ALWAYS_ID = 'Always'

    def is_language_screen(self):
        log.debug('Check is language screen display')
        self.el.tap_btn_by_id(self.IS_LANGUAGE_SETTINGS_ID)

    def open_on_sending(self):
        log.debug('Open section: language on sending')
        self.el.tap_btn_by_id(self.LANGUAGE_ON_SENDING_ID)

    def set_autotranslate_on_sending(self):
        log.debug('Switch on autotranslate on sending')
        self.el.tap_btn_by_id(self.AUTO_ON_SENDING_ID)

    def tap_alert_once(self):
        log.debug('Choose language for once')
        self.el.tap_btn_by_id(self.ALERT_ONCE_ID)
