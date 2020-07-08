class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.current_page = 0
        self.next_page = True
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label):
        if not self.next_page:
            return 'No more free spots'
        if len(self.photos[self.current_page]) == 4:
            self.current_page += 1
            if len(self.photos) < self.current_page + 1:
                self.next_page = False
                return 'No more free spots'
        self.photos[self.current_page].append(label)
        return f'{label} photo added successfully on page {self.current_page+1} slot {len(self.photos[self.current_page])}'

    def display(self):
        result = ''
        for p in self.photos:
            result += f'{"-" * 11}\n'
            for pic in range(len(p)):
                if pic == len(p) - 1:
                    result += '[]'
                else:
                    result += '[] '
            result += '\n'
        result += f'{"-" * 11}\n'
        return result


album = PhotoAlbum(1)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
