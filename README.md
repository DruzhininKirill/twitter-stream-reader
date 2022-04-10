# twitter-stream-reader

Twitter-stream-reader is a simple python script that allows dumping tweets from Twitter Streaming API to csv.


## Usage

local
```bash
pipenv run python main.py
```
docker
```bash
docker build -t . app
docker run --env-file .env app
```

## Env

| Key | Description | Values |
| ------ | ------ | ------ |
| CLIENT_API_KEY | App key retrieved from Twitter Dev Platform | str |
| CLIENT_SECRET_KEY | Secret key retrieved from Twitter Dev Platform | str |
| TRACK_TOPIC | Filtering keyword | str |
| STREAM_URL | Twitter stream URL | https://addr |
| LOG_LEVEL | Logging level | INFO/DEBUG/WARNING... |
| MAX_READ_TIME_SEC | Time to consume stream | int |
| MAX_TWEETS | Max number of messages to consume | int |
| OUTPUT_PATH | Path to save result csv | path/to/output.csv |
| OAUTH_TOKEN | OAuth1 parameter to authorize request | str |
| OAUTH_TOKEN_SECRET | OAuth1 parameter to authorize request | str |

## Auth

To retrieve OAUTH_TOKEN and OAUTH_TOKEN_SECRET simply:
1) Run:
```bash
pipenv python run auth.py
```
2) Follow the auth link in stdout to get authorization PIN.
3) Paste the PIN from the browser and click ENTER.
4) Copy OAUTH_TOKEN and OAUTH_TOKEN_SECRET from stdout to .env file.

## License
[MIT](https://choosealicense.com/licenses/mit/)