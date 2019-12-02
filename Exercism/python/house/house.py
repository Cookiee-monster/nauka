def recite(start_verse, end_verse):

    verses = [("is", "the horse and the hound and the horn"),
                 ("belonged to", "the farmer sowing his corn"),
                 ("kept", "the rooster that crowed in the morn"),
                 ("woke", "the priest all shaven and shorn"),
                 ("married", "the man all tattered and torn"),
                 ("kissed", "the maiden all forlorn"),
                 ("milked", "the cow with the crumpled horn"),
                 ("tossed", "the dog"),
                 ("worried", "the cat"),
                 ("killed", "the rat"),
                 ("ate", "the malt"),
                 ("lay in", "the house that Jack built.")]

    result = []
    for iteration in range(-start_verse, -end_verse - 1, -1):
        rhyme = "This is {}".format(verses[iteration][1])
        while iteration != -1:
            iteration += 1
            rhyme += " that {} {}".format(verses[iteration][0], verses[iteration][1])
        result.append(rhyme)
    return result
