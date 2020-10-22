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
    ToDo: Getting array of "cleaned" phrases
    '''
    array_of_phrases = phrase_cleaner('prepod_mipt.txt')
    '''
    ToDo: Creating the list of phrases in new file
    '''
    text = phrase_creator(array_of_phrases)
    '''
    ToDo: Markovifying them
    '''
    text_model = markovify.NewlineText(text)
    '''
    ToDo: Printing them out
    '''
    for i in range(100):
        print(text_model.make_short_sentence(300))
