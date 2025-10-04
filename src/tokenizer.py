"""
Модуль для токенизации выражений.
"""
import re
from typing import List
from constants import TOKEN

class Tokenizer:
    """ Класс для токенов """

    def __init__(self) -> None:
        """Инициализация токенизатора"""

        self._token_pattern = TOKEN
    def tokenize(self, mathematical_expression: str) -> List[str]:
        """
        Функция разбивает выражение на токены.
        Получает mathematical_expression: Математическое выражение строка
        Возвращает писок токенов
        Ошибка: Если выражение пустое или не является строкой
        """
        #Проверяем
        if not isinstance(mathematical_expression, str):
            raise ValueError("Математическое выражение должно быть строкой")
        mathematical_expression = mathematical_expression.strip()
        if not mathematical_expression:
            raise ValueError("Пустое выражение")
        #Если прошло проверку, то удаляем пробелы и токенизируем
        mathematical_expression = mathematical_expression.replace(' ', '')
        tokens = re.findall(self._token_pattern, mathematical_expression)
        #возвращаем токен
        return tokens
    def is_digit_token(token: str) -> bool:
        """ Проверка, что токен число
        Получаем Токен строку
        ВОзвращаем True если токен является числом, если не число False
        """
        if not isinstance(token, str):
            return False
        return token.replace('.', '').isdigit()
    def is_identifier(token: str) -> bool:
        """
        Проверка, что токен является идентификатором
        Получаем Токен
        Возращаем True если токен является идентификатором,если не False
        """
        if not isinstance(token, str):
            return False
        return bool(re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', token))
