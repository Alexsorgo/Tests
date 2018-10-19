from tests.screens.chats.base_chat_screen import BaseChatScreen
from tests.utils.logs import log


class CreateGroupScreen(BaseChatScreen):
    SET_GROUP_AVATAR = 'image_view'
    OPEN_ALIAS = 'change_alias_view'

    def set_group_avatar(self):
        log.debug("Set group avatar")
        self.el.tap_btn_by_id(self.SET_GROUP_AVATAR)

    def set_alias(self, alias):
        log.debug('Open alias screen')
        self.el.tap_btn_by_id(self.OPEN_ALIAS)
        from tests.screens.group import AliasScreen
        al = AliasScreen(self.driver)
        al.set_alias(alias)

