class str():
    def __init__(self):
        self.lib = True
        self.quote = """\"\"\"this is a triple double-quoted triple double-quoted string\"\"\""""

    def print(self, thing):
        print(thing + "\n" + self.quote)
        return None