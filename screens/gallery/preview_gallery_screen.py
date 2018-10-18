from screens.gallery.base_gallery_screen import BaseGalleryScreen
from utils.logs import log


class PreviewGalleryScreen(BaseGalleryScreen):
    # TODO: add id, when implement
    FULL_VIEW_ID = 'image_view'

    def is_full_view_open(self):
        log.debug('Is full view image opened')
        full_view = self.driver.find_elements_by_id(self.FULL_VIEW_ID)
        if full_view:
            return True
        else:
            log.error('Full view not find')
            return False
