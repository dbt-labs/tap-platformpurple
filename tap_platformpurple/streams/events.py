from tap_platformpurple.streams.base import BaseDatePaginatedPlatformPurpleStream


class EventsStream(BaseDatePaginatedPlatformPurpleStream):
    TABLE = "events"
    KEY_PROPERTIES = ["docID"]
    API_METHOD = "POST"

    def get_url(self):
        return "https://api-v4.platformpurple.com/api/stats/events4Environment"

    def get_filters(self):
        return {"environment": self.config.get("environment")}
