import asyncio

import httpx
import orjson
import logging
import pandas as pd
from authlib.integrations.httpx_client import OAuth1Auth

from settings import Settings
from utils import parse_tweet

EMPTY_CARRIAGE = "\n"

logging.basicConfig(level=Settings.LOG_LEVEL)
logger = logging.getLogger("twitter")

auth = OAuth1Auth(
    client_id=Settings.CLIENT_API_KEY,
    client_secret=Settings.CLIENT_SECRET_KEY,
    token=Settings.OAUTH_TOKEN,
    token_secret=Settings.OAUTH_TOKEN_SECRET,
)
queue: asyncio.Queue = asyncio.Queue(maxsize=Settings.MAX_TWEETS)


async def read_stream(max_time: int):
    try:
        await asyncio.wait_for(
            read_tweets(
                Settings.STREAM_URL,
                Settings.TRACK_TOPIC,
            ),
            max_time,
        )
    except asyncio.TimeoutError:
        logger.info(f"Stream read maximum time ({max_time}) reached.")
    except httpx.HTTPError as ex:
        logger.error(f"Could not establish stream connection: {str(ex)}")
    finally:
        await queue.put(None)


async def main():
    rows = []
    asyncio.create_task(read_stream(Settings.MAX_READ_TIME_SEC))
    while len(rows) < Settings.MAX_TWEETS:
        raw_tweet = await queue.get()
        if not raw_tweet:
            break
        try:
            tweet = orjson.loads(raw_tweet)
        except orjson.JSONDecodeError:
            logger.warning("Error on serializing tweet. Skip...")
            continue
        logger.debug(f"Got: {tweet}")
        rows.append(parse_tweet(tweet))

    if rows:
        df = pd.DataFrame(rows)
        df = df.sort_values(by=["user_created_at", "user_id", "created_at"])
        df.to_csv(
            f"{Settings.OUTPUT_PATH}/data.csv", sep=Settings.DELIMITER, index=False
        )
    logger.info(f"Completed. Got {len(rows)} tweets!")


async def read_tweets(
    stream_url: str,
    topic: str = None,
):
    params = None if not topic else {"track": topic}
    client = httpx.AsyncClient(auth=auth)
    async with client.stream("GET", stream_url, params=params) as r:
        logger.debug("Connection established. Reading tweets...")
        async for tweet in r.aiter_lines():
            if tweet == EMPTY_CARRIAGE:
                logger.warning(f" No tweets on: {topic} received. Wait...")
            else:
                await queue.put(tweet)


if __name__ == "__main__":
    asyncio.run(main())
