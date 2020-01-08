from tap_platformpurple.streams.base import BasePlatformPurpleStream


class UserReferralsStream(BasePlatformPurpleStream):
    TABLE = "user_referrals"
    KEY_PROPERTIES = ["id"]
    API_METHOD = "POST"

    def get_stream_data(self, data):
        return [self.transform_record(item) for item in data.get("data")]

    def get_url(self):
        return "https://api-v4-staging.platformpurple.com/api/stats/creditedReferralsForOrg"

    def get_filters(self):
        return {"environment": self.config.get("environment")}
