class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        st = ''
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for text in file:
                text = text.lower()
                for i in text:
                   if i in punctuation:
                        text = text.replace(i,'')
                st = st + text
            all_words.update({self.file_names:st.split()})
        return all_words
    def find(self,world):
        dist = {}
        world_ = self.get_all_words()[self.file_names]
        for i in range(len(world_)):
            if world.lower() == world_[i]:
                dist.update({self.file_names: i+1})
                return dist
    def count(self,world):
        dist = {}
        n = 1
        world_ = self.get_all_words()[self.file_names]
        dist.update({self.file_names: world_.count(world.lower())})
        return dist

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего










