from utils.logs import log


class CM:
    """
    Common methods.
    """

    @staticmethod
    def set_wheel_coordinates(width, height, perc):
        log.debug("Get wheel coordinates")
        x, y, x1, y1 = [perc[0]*width, perc[1]*height, perc[2]*width, perc[3]*height]
        return int(x), int(y), int(x1), int(y1)
