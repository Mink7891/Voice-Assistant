import speech_recognition
import os
import random
import sys
import webbrowser as wb

# Команды
commands_dict = {
    'commands': {
        'create_task': ['добавь заметку', 'добавить заметку'],
        'delete_task': ['удали заметку', 'удалить заметку'],
        'play_music': ['включи музыку', 'включить музыку', 'туса', 'музыку', 'музыка'],
        'vk': ['открыть vk', 'открой vk', 'открыть вк', 'открой вк', 'вк', 'открыть вконтакте', 'открой вконтакте', 'вконтакте', 'открыть в контакте', 'открой в контакте', 'в контакте'],
        'telegram': ['открыть telegram', 'открой telegram', 'открыть tg', 'открой tg', 'открыть тг', 'открой тг', 'открыть телеграм', 'открой телеграм', 'тг', 'телеграм', 'telegramm', 'tg'],
        'search_in_wb': ['найти', 'найди'],
        'get_weather_forecast': ["weather", "forecast", "погода", "прогноз"],
        'stop': ['стоп'],
    }
}

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


# Распознование голоса
def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU')
            query = str(query).lower()
        return query
    except speech_recognition.UnknownValueError:
        query = listen_command()


# Создание заметки
def create_task():
    print("Что добавим в список дел?")

    query = listen_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'Задача {query} добавлена в заметки'


# Удаление заметки
def delete_task():
    print("Что удалим из списка дел?")

    query = listen_command()

    with open("todo-list.txt", "r") as file:
        lines = file.readlines()
    with open("todo-list.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != query:
                file.write(line)
    return f'Задача {query} удалена из заметок'


# Проигрывание рандомной песни
def play_music():

    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'start {random_file}')

    return f'Танцуй под {random_file.split("/")[-1]}'

# Остановить
def stop():
    sys.exit()

# Открыть вк
def vk():
    wb.open('https://vk.com/al_feed.php')

# Открыть telegram
def telegram():
    wb.open('https://web.telegram.org/')

# Поиск в браузере
def search_in_wb():
    print("Что хотите найти?")

    query = listen_command()
    wb.open('https://yandex.ru/yandsearch?clid=2028026&text={}&lr=11373'.format(query))

# Погода
def get_weather_forecast():
    print("Где хотите узнать погоду?")

    query = listen_command()
    wb.open('https://yandex.ru/search/?text=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+{}&clid=2411726&lr=10716'.format(query))

def main():
    query = listen_command()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())


if __name__ == '__main__':
    while True:
        main()
