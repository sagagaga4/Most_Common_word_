
from urllib.request import urlopen
from html.parser import HTMLParser
import json
import collections


class WordsParser(HTMLParser):
    # tags storage for searching

    search_tags = ['p', 'div', 'span', 'a', 'h1', 'h2', 'h2', 'h3', 'h4']
    current_tag = ''
    # most commmon words list

    common_words = {}

    def handle_starttag(self, tag, attr):
        self.current_tag = tag

    def handle_data(self, data):
        #matching between tags to search
        if self.current_tag in self.search_tags:
            for word in data.strip().split():
                # letters only filter

                common_word = word.lower()
                common_word = common_word.replace('.', '')
                common_word = common_word.replace(':', '')
                common_word = common_word.replace(',', '')
                common_word = common_word.replace('"', '')

                # 2 words filtering

                if (
                    len(common_word) > 2 and
                    common_word not in ['the', 'and', 'all'] and
                    common_word[0].isalpha()
                ):

                

                    try:
                        # Common word counter

                        self.common_words[common_word] += 1

                    except:
                        # common word storage

                        self.common_words.update({common_word: 1})


url_enter = input(
    "Enter URL adress you would like to scrape most common word out of:")

if __name__ == '__main__':
    url = url_enter
    response = urlopen(url)
    html = response.read().decode('utf-8', errors='ignore')
    words_parser = WordsParser()
    words_parser.feed(html)
    words_count = collections.Counter(words_parser.common_words)
    most_common = words_count.most_common(25)

    for word, count in most_common:
        print(word, str(count) + ' times', sep=": ")
