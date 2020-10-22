import os


def phrase_creator(array_of_phrases):
    with open("corpus.txt", 'w') as file:
        for phrase in array_of_phrases:
            file.write(phrase)
    INFILE = "corpus.txt"
    OUTFILE = "output.txt"
    ENC = "utf-8"
    with open(INFILE, "r") as infile, open(OUTFILE, "w") as outfile:
        for line in infile:
            outfile.write(line)

    os.remove(INFILE)
    os.rename(OUTFILE, INFILE)

    with open("corpus.txt", 'r') as f:
        text = f.read()
    return text
