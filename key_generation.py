
from alphabet_generator import alphabet
from corepresentation import *
from random import randint, choice


def CreateKey(w, m, h, n):
    return (h ** n) * (w ** m) * (h ** -n)


def Hide(word, n_operations, corepresentation, n_letters):
    """
    n_letters - количество используемых букв
    """
    letters = []
    for _letter in alphabet(n_letters):
        letters.append(_letter)
        letters.append(_letter.Reverse())
    word = Word(word)

    for i in range(n_operations):
        k = randint(0, 10)
        m = randint(0, word.Size() - 1)
        if k < 2:
            """
            Вставка тривиального слова на m-й позиции
            """
            letter = choice(letters)
            trivial_word = Word([letter, letter.Reverse()])
            new_word = word.Insert(trivial_word, m)
        elif k < 5:
            """
            Вставка произвольного слова из множества определяющих соотношений на m-й позиции
            """
            relation = choice(corepresentation.Symmetrization())
            new_word = word.Insert(relation, m)
        elif k < 8:
            """
            R-удлинение на m-й позиции
            """
            new_word = word.R_elongated(corepresentation, m)
        elif k < 9:
            """
            Свободное сокращение
            """
            new_word = word.Reduced()
        else:
            """
            R-сокращение
            """
            new_word = word.R_reduced(corepresentation)

        word = new_word
    return word
