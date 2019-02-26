# Return your favorite phrase by passing values
# class for a new favorite phrase
class FavWords():
    def __init__(self, first_word, second_word):
        self.first_word = first_word
        self.second_word = second_word
        self.fav_words = self.first_word + self.second_word
    
    def a_new_phrase(self):
        return self.fav_words


# begin program
def begin(word_1, word_2):
    new_word = FavWords(word_1, word_2)
    return new_word.a_new_phrase()