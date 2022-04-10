from datetime import datetime

TWITTER_DT_FORMAT = "%a %b %d %H:%M:%S +0000 %Y"


def twitter_dt_to_timestamp(dt: str) -> int:
    return int(datetime.strptime(dt, TWITTER_DT_FORMAT).timestamp())


def parse_tweet(data: dict):
    return dict(
        id=data["id"],
        created_at=data["timestamp_ms"],
        text=data["text"],
        user_id=data["user"]["id"],
        name=data["user"]["name"],
        screen_name=data["user"]["screen_name"],
        user_created_at=twitter_dt_to_timestamp(data["user"]["created_at"]),
    )
