class Letter:
    """
    Класс для описания буквы
        __sym - символ
        __sign - степень (1 или -1)
    """

    def __init__(self, sym, sign=1):
        """
        Конструктор
            sym - символ
            sign - степень (1 или -1)
        """
        self.__sym = sym
        self.__sign = sign

    def Copy(self, other):
        """
        Копировать букву
            other - копируемая буква
            return скопированная буква
        """
        self.__sym = other.__sym
        self.__sign = other.__sing
        return self

    def __eq__(self, other):
        """
        Оператор ==
            other - сравниваемая буква
            return True, если буквы эквивалентны
                False в противном случае
        """
        return self.__sym == other.__sym and self.__sign == other.__sign

    def __ne__(self, other):
        """
        Оператор !=
            other - сравниваемая буква
            return True, если буквы не эквивалентны
                False в противном случае
        """
        return not (self == other)

    def __lt__(self, other):
        """
        Оператор <
        При сравнении приоритереным признаком является значение символа,
        второстепенный признак - степень буквы (обратная буква меньше)
            other - сравниваемая буква
            return self < other
        """
        if self.__sym == other.__sym:
            return (not self.IsInverse()) and other.IsInverse()
        return self.__sym < other.__sym

    def __hash__(self):
        return hash((self.__sym, self.__sign))

    def IsReductive(self, other):
        """
        Проверка на сократимость с буквой
            other - буква
            return True, если буквы сократимы
                False в противном случае
        """
        if self.__sym == other.__sym and self.__sign != other.__sign:
            return True
        return False

    def IsInverse(self):
        """
        Проверка на то, является ли буква обратной
            return True, если степень буквы -1 (буква обратная)
                False, если степень буквы 1 (буква не обратная)
        """
        return True if self.__sign < 0 else False

    def Reverse(self):
        """
        Возвращает букву с противоположной степенью
            return буква с противоположной степенью
        """
        return Letter(self.__sym, -self.__sign)

    def L2String(self):
        """
        Конвертировать Letter в строку
            return буква, конвертированная в строку
        """
        if self.__sign == 1:
            return "{0}".format(self.__sym)
        return "{0}^({1})".format(self.__sym, self.__sign)
