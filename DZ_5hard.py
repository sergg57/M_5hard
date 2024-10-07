from time import sleep


# class DataBaseUser:
#     def __init__(self):
#         self.data = {}
#
#     def add_user(self, user):
#         self.data[user.name] = [user.password, user.age]
#         print(self.data)
#         print(self.data.values())


class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    #database_user = DataBaseUser()
    users = []
    videos = []
    current_user = None

    def log_in(self, name, password):
        user_logged = False
        for user in self.users:
            if user.name == name and user.password == hash(password):
                self.current_user = user
                user_logged = True
                print(f'Вы вошли как: {user.name}.'
                      f'Теперь вы - {self.current_user.name} текущий пользователь')
                break
        if not user_logged:
            print('Неверное имя или пароль. Попробуйте ещё раз или зарегистрируйтесь.')


    def register(self, name, password, age):
        user = User(name, hash(password), age)
        #print(f'Пароль для пользователя {user.name} - {password} = {hash(password)}')
        user_logged = False
        for item in self.users:
            if item.name in user.name:
                print(f'Пользователь {user.name} уже существует.')
                user_logged = True
                break
        if not user_logged:
            self.users.append(user)
            self.current_user = user
        return user


    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта')


    def add(self, *args):
        self.videos.append(args)
        return  self.videos


    def get_videos(self, word):
        list_of_videos = []
        for item in self.videos:
            for video in item:
                if word.lower() in video.title.lower():
                    list_of_videos.append(video.title)
        return list_of_videos


    def watch_video(self, video_title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
        else:
            video_logged = False
            for item in self.videos:
                for video in item:
                    if video_title in video.title:
                        video_logged = True
                        if self.current_user.age < 18 and video.adult_mode == True:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                        else:
                            for i in range(video.duration):
                                print( i+1, end=' ')
                                sleep(1)
                            print('Конец видео')
            if  video_logged == False:
                    print('Видео не найдено')






if __name__ == '__main__':
    """
    #database_user = DataBaseUser()
    ur = UrTube()
    users = []
    
    while True:
        choice = input("Приветствую! Выберите действие: \n1. - Вход\n2. - Регистрация\n")
        if choice == '1':
            name = input('Ваше имя: ')
            password = input('Ваш пароль: ')
            ur.log_in(name, password)
            continue
        if choice == '2':
            name = input('Ваше имя: ')
            password = input('Ваш пароль: ')
            age = int(input('Ваш возраст: '))
            user = User(name, password, age)
            UrTube.register(self=ur, name=name, password=password, age = age)

            continue
   """





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.name)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

