class Media():
    def __init__(self, name, headers, url, params):
        self.name = name
        self.headers = headers
        self.url = url
        self.params = params

    def parse_url(self, text):
        return text
