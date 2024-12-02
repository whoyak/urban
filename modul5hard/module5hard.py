import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):

        hashed_password = hash(password)


        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"User '{nickname}' logged in successfully.")
                return


        print("Invalid nickname or password.")

    def log_out(self):

        if self.current_user is None:
            print("No user is currently logged in.")
        else:
            print(f"User '{self.current_user.nickname}' logged out.")
            self.current_user = None  # Сбрасываем текущего пользователя на None

    def register(self, nickname: str, password: str, age: int):

        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return


        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def add(self, *videos):

        for video in videos:
            if not any(existing_video.title == video.title for existing_video in self.videos):
                self.videos.append(video)  # Если такого видео нет, добавляем
                print(f"Video '{video.title}' added successfully.")
            else:
                print(f"Video '{video.title}' already exists, not added.")

    def get_videos(self, search_term: str):

        search_term = search_term.lower()
        result = [video.title for video in self.videos if search_term in video.title.lower()]
        return result

    def watch_video(self, title: str):

        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return


        video = next((v for v in self.videos if v.title == title), None)

        if video is None:
            print("Видео не найдено")
            return


        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return


        print(f"Воспроизведение видео '{video.title}':")
        while video.time_now < video.duration:
            time.sleep(1)
            video.time_now += 1
            print(f"Секунда: {video.time_now}")

        print("Конец видео")
        video.time_now = 0




if __name__ == "__main__":
    ur = UrTube()


    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    ur.add(v1, v2)


    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')


    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user.nickname)

    ur.watch_video('Лучший язык программирования 2024 года!')

