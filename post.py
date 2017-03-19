class Post:
    def __init__(self, post):
        title = post.find('h5', attrs={'class': 'result-list-entry__brand-title'})
        self.title = title.text

        try:
            a = self.title.find("NEU")
            self.title = self.title[3:]
        except ValueError:
            donothing="here"

        link = post.find('a', attrs={'class': 'result-list-entry__brand-title-container'})
        self.link = link.get('href')


        addrContainer = post.find('div', attrs={'class': 'result-list-entry__address'})
        self.address = addrContainer.find('span').text


        criteria = post.find_all('dl', attrs={'class': 'result-list-entry__primary-criterion'})

        self.rent = trim(criteria[0].find('dd').text)
        self.area = trim(criteria[1].find('dd').text)
        self.rooms = trim(criteria[2].find('dd').text)

        print(self.title, self.rent, self.area, self.rooms, self.address, self.link)

    title = "title"
    rent = "47€"
    area = "qm"
    rooms = "2"
    address = "Sample Address Here"
    link = "link"


def trim(str):
    return str.replace("\r\n","").replace("\n","").replace(" ", "")