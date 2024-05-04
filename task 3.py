class Tracks:
    All_tracks = []

    def __init__(self, name: str, duration: int, singer: str, year: int, album_name: str, genre: str):
        self.__name = name
        self.__duration = duration
        self.__singer = singer
        self.__year = year
        self.__album_name = album_name
        self.__genre = genre
        self.pause = False
        self.pause_time = None
        Tracks.All_tracks.append(self)

    name = property()
    album_name = property()
    singer = property()
    year = property()

    @year.setter
    def year(self, value):
        pass
    @year.getter
    def year(self):
        return self.__year

    @singer.setter
    def singer(self, value):
        pass

    @singer.getter
    def singer(self):
        return self.__singer

    @name.setter
    def name(self, value):
        pass

    @name.getter
    def name(self):
        return self.__name

    @album_name.setter
    def album_name(self, value):
        pass

    @album_name.getter
    def album_name(self):
        return self.__album_name

    def play_track(self, time=None):
        if time is None:
            dur = self.__duration
        else:
            dur = time

        while not self.pause:
            counter = 0
            print(self.__name)
            print(f'00:00 {5 * "-"} {Tracks.to_format(self.__duration)}')
            print(dur)
            while dur > 0:
                counter += 1
                dur -= 1
                if counter % 30 == 0:
                    print("1. Поставить на паузу.\n"
                          "2. Продолжить прослушивание.")
                    check = int(input(""))
                    if check == 1:
                        self.pause = True
                        self.pause_time = dur
                        break
            break

    @staticmethod
    def to_format(value):
        minutes = value // 60
        seconds = value % 60
        result = ''
        if 10 <= minutes <= 59:
            result += str(minutes) + ":"
        else:
            result += "0" + str(minutes) + ":"
        if 10 <= seconds <= 59:
            result += str(seconds)
        else:
            result += "0" + str(minutes)
        return result

    def __repr__(self):
        return self.__name


class Albums:
    All_Albums = []
    Album_names = []

    def __init__(self, name: str, singer: str, year: int):
        self.__name = name
        self.__singer = singer
        self.__year = year
        self.__tracks = self.fill_up()
        self.stop = False
        Albums.All_Albums.append(self)
        Albums.Album_names += [self.__name]

    name = property()
    tracks = property()

    @tracks.setter
    def tracks(self, value):
        pass

    @tracks.getter
    def tracks(self):
        return self.__tracks

    @name.setter
    def name(self, value):
        pass

    @name.getter
    def name(self):
        return self.__name

    def play_album(self):
        while not self.stop:
            for track in self.__tracks:
                track.play_track()
                if track.pause:
                    print("1. Возобновить прослушивание.\n"
                          "2. Остановить воспроизведение альбома.")
                    answer = int(input("Выбор: "))
                    if answer == 1:
                        track.pause = False
                        track.play_track(track.pause_time)
                    if answer == 2:
                        self.stop = True
                        break
        else:
            self.stop = False

    def fill_up(self):
        filling_up = []
        for element in Tracks.All_tracks:
            if element.singer == self.__singer and element.album_name == self.__name:
                filling_up += [element]
        return filling_up


MENU = f'Выберите действие: \n' \
       f'1. Список альбомов.\n' \
       f'2. Вопроизведение альбома.\n' \
       f'3. Выход.'

if __name__ == '__main__':
    with open('Tracks.txt', 'r', encoding='utf8') as f:
        data = f.readlines()

    for line in data:
        name, duration, singer, year, album_name, genre = line.split(',')
        new_object = Tracks(name, int(duration), singer, int(year), album_name, genre)

    for track in Tracks.All_tracks:
        if track.album_name not in Albums.Album_names:
            new_album = Albums(track.album_name, track.singer, track.year)

    while True:
        print(MENU)
        command = int(input("Выбор: "))
        if command == 1:
            for album in Albums.All_Albums:
                print(album.name)

        if command == 2:
            title = input("Введите название альбома: ")
            for album in Albums.All_Albums:
                if album.name == title:
                    album.play_album()

        if command == 3:
            break
