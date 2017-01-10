from datetime import datetime, timedelta


class DaysDiff:

    def diff(self, start, end):

        diff = end - start

        return diff.days
