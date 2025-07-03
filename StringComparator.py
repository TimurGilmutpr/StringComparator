from nltk.util import ngrams
from collections import Counter

class StringComparator:
    """
    Класс для сравнения строк и исправления опечаток
    """
    def __init__(self):
        pass
    
    @staticmethod
    def ngram_similarity(s1, s2, n=2):
        """
        Вычисляет сходство n-грамм между двумя строками.
        Использует коэффициент Сёренсена-Дайса: 2 * |A ∩ B| / (|A| + |B|)
        """
        s1, s2 = s1.lower(), s2.lower()
        ngrams1 = Counter(ngrams(s1, n))
        ngrams2 = Counter(ngrams(s2, n))
        
        common = ngrams1 & ngrams2
        intersection = sum(common.values())
        
        total1 = sum(ngrams1.values())
        total2 = sum(ngrams2.values())
        total = total1 + total2
        
        if total == 0:
            return 0.0
        
        return (2 * intersection) / total

    @staticmethod
    def find_similar_ngram(word, word_list, threshold = .3, n = 2):
        #result = []
        result = {}
        for w in word_list:
            score = Comparison_of_embendines.ngram_similarity(word, w, n)
            if score > threshold:
                #result.append((w, score))
                result[w] = score
        return result
    
    @staticmethod    
    def damerau_levenshtein(s1, s2):
        """
        Вычисляет расстояние Дамерау-Левенштейна с оптимизированной обработкой транспозиции.
        """
        d = {}
        len1, len2 = len(s1), len(s2)
        for i in range(-1, len1 + 1):
            d[(i, -1)] = i + 1
        for j in range(-1, len2 + 1):
            d[(-1, j)] = j + 1
        
        for i in range(len1):
            for j in range(len2):
                cost = 0 if s1[i] == s2[j] else 1
                d[(i, j)] = min(
                    d[(i-1, j)] + 1,
                    d[(i, j-1)] + 1,
                    d[(i-1, j-1)] + cost
                )
                if i > 0 and j > 0 and s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                    d[(i, j)] = min(d[(i, j)], d[(i-2, j-2)] + cost)
        return d[(len1-1, len2-1)]

    @staticmethod
    def suggest_correction(word, dictionary, max_distance=2):
        """
        Ищет варианты исправления опечаток в словаре.
        Этапы:
        1. Предварительная фильтрация по длине и n-граммам
        2. Точный расчет расстояния Дамерау-Левенштейна
        """
        suggestions = []
        candidates = [w for w in dictionary if abs(len(w) - len(word)) <= max_distance]
        ngram_candidates = Comparison_of_embendines.find_similar_ngram(word, candidates, threshold=0.4)
        for candidate in ngram_candidates:
            dist = Comparison_of_embendines.damerau_levenshtein(word, candidate)
            if dist <= max_distance:
                suggestions.append((candidate, dist))
        
        return sorted(suggestions, key=lambda x: x[1])
