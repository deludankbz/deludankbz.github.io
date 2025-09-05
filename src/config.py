import json

class Config:
    def __init__(self) -> None:
        with open('config.json', 'r', encoding='utf-8') as fs:
            config = json.loads(fs.read())

        self.config = config
        self.article = config['sourceArticle']
        self.index = config['index']
        pass

 
    def getIndex(self) -> str:
        with open(self.index, 'r', encoding='utf-8') as fs:
            return fs.read()


    def getArticle(self) -> str:
        with open(self.article, 'r', encoding='utf-8') as fs:
            return fs.read()


    def updateIndex(self, content) -> None:
        with open(self.index, 'w', encoding='utf-8') as fs:
            fs.writelines(content)
