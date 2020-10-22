import os
import markovify
from vkparser import take_1000_posts, file_writer
from phrasefilter import phrase_cleaner
from phrasegen import phrase_creator


if __name__ == "__main__":
    '''
    ToDo: Taking 1000 posts from the vk group
    '''
    all_posts = take_1000_posts()
    '''
    ToDo: Writing them into the file
    '''
    file_writer(all_posts)
    '''
    ToDo: 
    '''
    array_of_phrases = phrase_cleaner('prepod_mipt.txt')

    text = phrase_creator(array_of_phrases)

    text_model = markovify.Text(text)

    for i in range(100):
        print(text_model.make_short_sentence(300))
