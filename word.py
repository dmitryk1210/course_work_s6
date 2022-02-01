import copy


class Word:
    """
    Класс для описания слова
        __letters - список букв
    """

    def __init__(self, let_list):
        """
        Конструктор
            let_list - список букв, из которых составляется слово
        """
        if type(let_list) == Word:
            self.__letters = copy.deepcopy(let_list.__letters)
        else:
            self.__letters = copy.deepcopy(list(let_list))

    def Copy(self):
        """
        Копировать слово
            return скопированное слово
        """
        return Word(self.__letters)

    def __eq__(self, other):
        """
        Оператор ==
            other - сравниваемое слово
            return True, если слова эквивалентны
                False в противном случае
        """
        if self.Size() != other.Size():
            return False
        for i in range(self.Size()):
            if self.__letters[i] != other.__letters[i]:
                return False
        return True

    def __ne__(self, other):
        """
         Оператор !=
             other - сравниваемое слово
             return True, если слова не эквивалентны
                 False в противном случае
         """
        return not (self == other)

    def __lt__(self, other):
        """
        Оператор <
        При сравнении приоритетным признаком считается длина слова,
        при одинаковой длине слова сравниваются побуквенно
            other - сравниваемое слово
            return self < other
        """
        if self.Size() != other.Size():
            return self.Size() < other.Size()
        for i in range(self.Size()):
            if self.__letters[i] != other.__letters[i]:
                return self.__letters[i] < other.__letters[i]
        return False

    def __mul__(self, other):
        """
        Оператор *
        Возвращает объединение слов self и other
            other - второе слово
            return слово, состоящее из объединения self и other
        """
        return Word(self.__letters + other.__letters)

    def __pow__(self, power):
        """
        Оператор **
        Возвращает слово self в степени power.
        Если power < 0, то возвращается обратное к self в степени abs(power)
            power - показатель степени
            return self ** power
        """
        word_foo = self.Reverse() if power < 0 else self
        result = Word(word_foo)
        for i in range(abs(power) - 1):
            result = result * word_foo
        return result

    def __hash__(self):
        return hash(tuple(self.__letters))

    def __iter__(self):
        return iter(self.__letters)

    def __next__(self):
        return next(self.__letters)

    def __getitem__(self, key):
        return self.__letters[key]

    def __setitem__(self, key, value):
        self.__letters[key] = value
        return self.__letters[key]

    def Reverse(self):
        """
         Возвращает слово, обратное исходному
             return обратное слово
         """
        foo = Word(self)
        foo.__letters.reverse()
        for i in range(len(foo.__letters)):
            foo.__letters[i] = foo.__letters[i].Reverse()
        return foo

    def IsSimple(self):
        """
        Проверить, является ли данное слово простым (т.е. все возможные сокращения букв произведены)
            return True, если слово простое
                False в противном случае
        """
        for i in range(self.Size() - 1):
            if self.__letters[i].IsReductive(self.__letters[i + 1]):
                return False
        return True

    def IsReductive(self):
        """
        Проверить, есть ли в данном слове сократимые пары букв
            return True, если такие пары есть
                False в противном случае
        """
        return not self.IsSimple()

    def IsSimpleCyclically(self):
        """
        Проверить, является ли данное слово циклически простым
            return True, если слово циклически простое
                False в противном случае
        """
        if self.IsSimple() and not self.__letters[0].IsReductive(self.__letters[-1]):
            return True
        return False

    def IsReductiveCyclically(self):
        """
        Проверить, есть ли в данном слове сократимые пары букв (в том числе - циклические)
            return True, если такие пары есть
                False в противном случае
        """
        return not self.IsSimpleCyclically()

    def CyclicPermutation(self, k=1):
        """
        Произвести циклическую перестановку букв в слове.
        Последняя буква перемещается в начало слова, остальные смещаются на 1 ближе к концу
            k - количество сдвигов
            return измененное слово
        """
        foo = Word(self)
        for i in range(k % self.Size()):
            foo.__letters.insert(0, foo.__letters.pop())
        return foo

    def Size(self):
        """
        Возвращает длину слова
            return длина слова
        """
        return len(self.__letters)

    def IsEmpty(self):
        """
        Проверка, является ли слово пустым
            return True, если длина слова равна 0
                False в противном случае
        """
        if self.Size() == 0:
            return True
        return False

    def Reduced(self, cyclic=False):
        """
        Возвращает слово, в котором произведены все возможные сокращения
            cyclic - флаг проверки, требуется ли циклическое сокращение слова
            return измененное слово
        """
        i = 0
        foo = Word(self)
        while i < foo.Size() - 1:
            if foo.__letters[i].IsReductive(foo.__letters[i + 1]):
                del foo.__letters[i:i + 2]
                if i > 0:
                    i -= 1
            else:
                i += 1
        if cyclic:
            while foo.__letters[0].IsReductive(foo.__letters[-1]):
                foo.__letters = foo.__letters[1:-1]
        return foo

    def W2String(self):
        """
        Конвертировать Word в строку
            return слово, конвертированное в строку
        """
        word_str = ''
        for letter in self.__letters:
            word_str += letter.L2String() + ' '
        return word_str.strip()

    def __str__(self):
        """
        Перегрузка функции str()
            return слово, конвертированное в строку
        """
        return self.W2String()

    def print(self):
        """
        Вывести слово на экран консоли
        """
        print(self.W2String())

    def GetSubword(self, subword_len):
        """
        Получить из данного слово подслово заданное длины
            subword_len - длина извлекаемого подслова
            return извлеченное подслово
        """
        return Word(self.__letters[:subword_len])

    def DeleteSubword(self, subword_len):
        """
        Удалить из данного слово подслово заданное длины
            subword_len - длина удаляемого подслова
            return слово без удаленной части
        """
        return Word(self.__letters[subword_len:])

    def IsSuperword(self, other):
        """
        Проверить, включает ли слово заданный кусок (подслово)
            other - предполагаемый кусок (подслово)
            return True, если other является куском слова (self)
        """
        if other.Size() > self.Size():
            return False
        for i in range(other.Size()):
            if self.__letters[i] != other.__letters[i]:
                return False
        return True

    def Insert(self, inserted_word, position):
        """
        Вставить в исходное слово другое слово на заданную позицию
            inserted_word - вставляемое слово
            position - позиция, на которую вставляется слово
            return новое слово
        """
        if position == 0:
            return Word(inserted_word.__letters + self.__letters)
        if position < self.Size():
            return Word(self.__letters[:position] + inserted_word.__letters + self.__letters[position:])
        return Word(self.__letters + inserted_word.__letters)

    def R_reduced(self, corepresentation):
        """
        Возвращает слово, в котором произведены все возможные R-сокращения
            corepresentation - копредставление R
            return слово, в котором произведены все сокращения
        """
        word = Word(self)
        simplified = False
        r_min_size = corepresentation.Symmetrization()[0].Size()
        while not simplified:
            k = 0
            simplified = True
            while k < word.Size() - r_min_size + 1:
                for r in corepresentation.Symmetrization():
                    if r.Size() >= word.Size() - k - 1:
                        continue
                    for i in range(r.Size() - 1):
                        if r[i] != word[k + i]:
                            break
                    else:
                        if r[-1] == word[k + r.Size() - 1]:
                            word = Word(word.__letters[:k] + word.__letters[k + r.Size():])
                        else:
                            word = Word(word.__letters[:k] + [r[-1].Reverse()] + word.__letters[k + r.Size() - 1:])
                        simplified = False
                word = word.Reduced()
                if simplified:
                    break
                k += 1
        return word

    def R_elongated(self, corepresentation, position):
        """
        Возвращает слово, в котором произведено R-удлинение
            corepresentation - копредставление R
            position - индекс элемента, который заменяется на удлинение
            return удлиненное слово
        """
        word = Word(self)
        for r in corepresentation.Symmetrization():
            if r.Size() > 1 and r[0] == word[position]:
                if position == word.Size() - 1:
                    word = Word(word.__letters[:position]) * Word(r[1:]).Reverse()
                else:
                    word = Word(word.__letters[:position]) * Word(r[1:]).Reverse() * Word(word.__letters[position + 1:])
                break
        return word
