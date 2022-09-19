# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

# Пример

class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}