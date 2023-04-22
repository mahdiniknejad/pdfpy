from bs4 import BeautifulSoup


class Html:
    
    def __init__(self, file) -> None:
        with open(file, mode='r') as f:
            html = f.read()
        soup = BeautifulSoup(html, 'html5lib')
        self.soup = soup
    
    # def __iter__(self):
    #     self.a = 1
    #     return self

    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    def loop(self):
        pass
