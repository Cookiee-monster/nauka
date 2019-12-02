def find_anagrams(word, candidates):
    candidates = [x for x in candidates if len(x) == len(word)]
    anagrams = []
    for candidate in candidates:
        if candidate.lower() != word.lower():
            if sorted(candidate.lower()) == sorted(word.lower()):
                anagrams.append(candidate)
    return anagrams
