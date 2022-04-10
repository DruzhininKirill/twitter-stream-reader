import asyncio

from settings import Settings

from authlib.integrations.httpx_client import AsyncOAuth1Client

base_authorization_url = "https://api.twitter.com/oauth/authorize"
request_token_url = "https://api.twitter.com/oauth/request_token"
access_token_url = "https://api.twitter.com/oauth/access_token"


async def main():
    client = AsyncOAuth1Client(Settings.CLIENT_API_KEY, Settings.CLIENT_SECRET_KEY)

    request_token = await client.fetch_request_token(request_token_url)
    print(request_token)
    token_url = client.create_authorization_url(
        base_authorization_url, request_token["oauth_token"], oauth_callback="oob"
    )
    print(token_url)
    verifier = input("verifier: ")
    access_token = await client.fetch_access_token(access_token_url, verifier=verifier)
    print(access_token)


if __name__ == "__main__":
    asyncio.run(main())
