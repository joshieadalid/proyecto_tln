import json
from typing import List, TypedDict


class User(TypedDict):
    name: str
    username: str
    profile_id: str
    avatar: str


class Stats(TypedDict):
    comments: int
    retweets: int
    quotes: int
    likes: int


class Tweet(TypedDict):
    link: str
    text: str
    user: User
    date: str
    is_retweet: bool
    is_pinned: bool
    external_link: str
    replying_to: List
    quoted_post: dict
    stats: Stats
    pictures: List[str]
    videos: List[str]
    gifs: List[str]


def cargar_tweets(filename: str) -> List[Tweet]:
    with open(filename, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    tweets = datos['tweets']
    return tweets
