from screens.gallery.base_gallery_screen import BaseGalleryScreen
from utils.logs import log


class GalleryScreen(BaseGalleryScreen):
    TITLE_SCREEN_ID = 'title_label'
    CELL = '//XCUIElementTypeCell'
    DATE_ID = 'section_header_title'
    IMAGE_ID = 'image_view'
    ALL_BUTTON_ID = 'all_button'
    PHOTO_BUTTON_ID = 'photo_button'
    VIDEO_BUTTON_ID = 'video_button'
    BY_FOLDER_ID = 'BY FOLDER'
    BY_DATE_ID = 'BY DATE'

    def open_preview_image(self):
        log.debug('Open first preview image')
        self.tap_filter_photo()
        self.driver.find_element_by_xpath(self.CELL).click()

    def tap_filter_photo(self):
        log.debug('Tap photo button in filter')
        self.driver.find_element_by_id(self.PHOTO_BUTTON_ID).click()

    def tap_filter_video(self):
        log.debug('Tap video button in filter')
        self.driver.find_element_by_id(self.VIDEO_BUTTON_ID).click()

    def is_gallery_screen(self):
        log.debug('Gallery screen displayed')
        title = self.driver.find_element_by_id(self.TITLE_SCREEN_ID)
        if title.get_attribute('value') == 'GALLERY':
            return True
        else:
            log.error('Find screen "{}"'.format(title.get_attribute('value')))
            return False

    def multiselect(self, number):
        log.debug('Select "{}" images'.format(str(number)))
        selects = self.driver.find_elements_by_id(self.SELECT_ID)
        headers = self.driver.find_elements_by_id(self.DATE_ID)
        visible_count = len(selects)
        log.debug("Collected {} image cells".format(str(visible_count)))
        if visible_count < number:
            for select in selects[:visible_count]:
                select.click()
            self.driver.swipe(headers[2].location['x'], headers[2].location['y'], headers[0].location['x'],
                              headers[0].location['y'], 1500)
            selects = self.driver.find_elements_by_id(self.SELECT_ID)
            for select in selects[visible_count:int(number)]:
                select.click()
        elif visible_count >= number:
            for select in selects[:number]:
                select.click()

    def select_several_images(self, images_count=11):
        log.debug("Select '{}' images".format(images_count))
        self.tap_filter_photo()
        selected_for_now = 0
        while selected_for_now < images_count:
            log.debug("Get visible check boxes")
            elems = self.driver.find_elements_by_id(self.SELECT_ID)
            log.debug("Select all visible images {}".format(len(elems)))
            for elem in elems:
                if not selected_for_now < images_count:
                    log.debug("{} images were selected".format(selected_for_now))
                    break
                log.debug("Select current image")
                elem.click()
                log.debug("Increase selected image counter")
                selected_for_now += 1
                log.debug("Counter increased")
            elem_loc = elems[-1].location
            self.driver.swipe_screen(elem_loc["x"], elem_loc["y"], elem_loc["x"], elem_loc["y"] - 1100, duration=500)

    def select_avatar(self):
        log.debug('Open first preview image')
        self.driver.find_element_by_xpath(self.CELL).click()

    def open_preview_video(self):
        log.debug('Open first preview image')
        self.tap_filter_video()
        self.driver.find_element_by_xpath(self.CELL).click()
