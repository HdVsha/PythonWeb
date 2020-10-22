from vkparser import take_1000_posts, file_writer
from phrasefilter import phrase_cleaner


if __name__ == "__main__":
    all_posts = take_1000_posts()
    file_writer(all_posts)
    array_of_phrases = phrase_cleaner('prepod_mipt.txt')
