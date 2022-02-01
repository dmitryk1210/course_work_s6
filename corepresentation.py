from word import Word
from alphabet_generator import alphabet
import itertools
from copy import deepcopy


class Corepresentation:
    """
    Класс для описания копредставления
        __def_relations ( = set of defining relations) - множество определяющих соотношений
    """

    def __init__(self, word_list):
        """
        Конструктор
            word_list - список слов, представляющих собой множество определяющих соотношений
        """
        self.__def_relations = set()
        self.__alphabet = set()
        for word in word_list:
            word_reduced = word.Reduced(cyclic=True)
            if word_reduced.Size() > 0:
                self.__def_relations.add(word_reduced)
                for letter in word_reduced:
                    self.__alphabet.add(letter if not letter.IsInverse() else letter.Reverse())
        if len(self.__def_relations) == 0:
            raise ValueError('Множество определяющих соотношений пусто')
        self.__symmetrization = None
        self.__pieces = self.Pieces()

    def Symmetrization(self):
        if self.__symmetrization is not None:
            return self.__symmetrization
        result = set()
        for word in self.__def_relations:
            spam = Word(word)
            for i in range(word.Size()):
                result.add(spam)
                result.add(spam.Reverse())
                spam = spam.CyclicPermutation()
        self.__symmetrization = sorted(result)
        return self.__symmetrization

    def Size(self):
        return len(self.__def_relations)

    def Pieces(self):
        pieces = set()
        symmetrizated_relations = self.Symmetrization()
        for relation in symmetrizated_relations:
            for k in range(relation.Size()):
                subword = relation.GetSubword(k + 1)
                found = False
                for other_relation in symmetrizated_relations:
                    if other_relation != relation and other_relation.IsSuperword(subword):
                        pieces.add(subword)
                        found = True
                if not found:
                    break
        return pieces

    def C(self, p):
        """
        Проверка условия C(p)
            p - параметр
            return True, если C(p) выполняется
                False в остальных случаях
        """
        def C4Word(word, k):
            if word.Size() == 0:
                return False
            if k == 0:
                return True
            for piece in self.__pieces:
                if word.IsSuperword(piece):
                    word_tail = word.DeleteSubword(piece.Size())
                    if not C4Word(word_tail, k - 1):
                        return False
            return True

        for relation in self.__def_relations:
            if not C4Word(relation, p - 1):
                return False
        return True

    def GetRelators(self):
        return list(deepcopy(self.__def_relations))


def GenerateRelators(n, l_min, l_max):
    letters = set()
    for _letter in alphabet(n):
        letters.add(_letter)
        letters.add(_letter.Reverse())
    result = set()
    for length in range(l_min, l_max + 1):
        for combination in itertools.combinations_with_replacement(letters, length):
            for replacement in itertools.permutations(combination):
                relator = Word(replacement)
                reduced_relator = relator.Reduced(cyclic=True)
                if reduced_relator.Size() >= l_min:
                    result.add(reduced_relator)
    return result


def GenerateCorepresentation(n, l, r, p):
    """
    Генератор копредставлений
        n - количество используемых букв из группового алфавита
        l - длина слов из множества определяющих соотношений
        r - количество слов в множестве определяющих соотношений
        p - параметр условия C(p)
        yield копредставление, удовлетворяющее условиям C(p)-T(3)
    """
    all_relations = GenerateRelators(n, l, l)
    for t in range(r, r + 1):
        for relations in itertools.combinations(all_relations, t):
            corepresentation = Corepresentation(relations)
            if corepresentation.C(p):
                yield corepresentation
