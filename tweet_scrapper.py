import json
from typing import Any, List

from ntscraper import Nitter

from tweetT import Tweet


def main() -> None:
    tweets: List[Tweet] = Nitter().get_tweets("c4jimenez", mode='user', number=10)

    # Export the data in json format
    with open("datos/tweets2.json", "w") as file:
        json.dump(tweets, file, indent=4)


if __name__ == '__main__':
    main()
