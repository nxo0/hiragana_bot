import json
import config
import random
import time
from requests_oauthlib import OAuth1Session

def tweet(content):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    AS = config.ACCESS_TOKEN_SECRET

    twitter = OAuth1Session(CK, CS, AT, AS)
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status" : content}

    req = twitter.post(url, params = params)

def main():
    str = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん！？がぎぐげござじずぜぞだぢづでどっぁぃぅぇぉ"
    char_list = list(str)
#(char_list, 6)の6の部分が文字数なのでここを好きな文字数に。
    output = random.sample(char_list, 6)
    sta = "".join(output)
    return sta

if __name__ == "__main__":
    print(main())
