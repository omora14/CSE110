import random

def get_determiner(quantity):
    if quantity == "single":
        determiners = ["A", "An", "The"]
    else:
        determiners = ["Some", "Many", "The"]
    return random.choice(determiners)

def get_noun(quantity):
    if quantity == "single":
        nouns = ["cat", "man", "woman"]
    else:
        nouns = ["dogs", "girls", "men"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    if tense == "past":
        if quantity == "single":
            verbs = ["laughed", "ate", "thought"]
        else:
            verbs = ["laughed", "ate", "thought"]
    elif tense == "present":
        if quantity == "single":
            verbs = ["laughs", "eats", "thinks"]
        else:
            verbs = ["laugh", "eat", "think"]
    else:
        if quantity == "single":
            verbs = ["will laugh", "will eat", "will think"]
        else:
            verbs = ["will laugh", "will eat", "will think"]
    return random.choice(verbs)

def get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_preposition()
    return preposition + " " + determiner + " " + noun

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase1 = get_prepositional_phrase(quantity)
    prep_phrase2 = get_prepositional_phrase(quantity)
    return determiner + " " + noun + " " + verb + " " + prep_phrase1 + " " + prep_phrase2 + "."

def main():
    sentences = []
    sentences.append(make_sentence("single", "past"))
    sentences.append(make_sentence("plural", "past"))
    sentences.append(make_sentence("single", "present"))
    sentences.append(make_sentence("plural", "present"))
    sentences.append(make_sentence("single", "future"))
    sentences.append(make_sentence("plural", "future"))

    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    main()
