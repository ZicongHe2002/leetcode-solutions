class Codec:
    def __init__(self):
        self.links = {}

    def encode(self, longUrl):
        short = f'http://tinyurl.com/{len(self.links):x}'
        self.links[short] = longUrl
        return short

    def decode(self, shortUrl):
        return self.links[shortUrl]
