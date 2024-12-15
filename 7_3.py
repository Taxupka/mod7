class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                string = file.read().lower()
                for char in string:
                    if char in  [',', '.', '=', '!', '?', ';', ':', '-']:
                        string = string.replace(char, '')
                    else:
                        continue


                    all_words[self.file_names] = string.split()
        return all_words


    def find(self, word):

        index = {}

        for name, words in self.get_all_words().items():
            if word.lower() in words:
                    ind = words.index(word.lower()) + 1
                    index[name] = ind
                    return index


    def count(self, word):
        counter = {}
        for name, words in self.get_all_words().items():
            ind = words.count(word.lower())
            counter[name] = ind
            return counter



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего