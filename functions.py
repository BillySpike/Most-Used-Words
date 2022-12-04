from collections import Counter
import re
import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def most_words(name, title):
    text = open_file(name)
    string_list = string_to_list(text)
    word_count = list_to_dictionary(string_list)
    word_count = remove_words(word_count)
    show_data(name, title, word_count)


def combine_files(file_list, file3):
    data = ""
    for i in file_list:
        with open(i + ".txt", 'r', encoding='utf-8') as f:
            data += "\n"
            data += f.read()
    with open(file3, 'w', encoding='utf-8') as f2:
        f2.write(data)
    f2.close()
    f.close()
    return


def open_file(name):
    file = open(name, 'r', encoding='utf-8')
    document = file.read()
    file.close()
    return document


def string_to_list(document):
    newline_break = document.replace("\n", " ")
    no_punctuation = re.sub(r'[^\w\s]', '', newline_break)
    long_string = re.sub(r'\w*\d\w*', '', no_punctuation).strip()
    document_list = list(long_string.lower().split(" "))
    return document_list


def list_to_dictionary(document_list):
    words = []
    for k in document_list:
        if k == "":
            continue
        words.append(lemmatizer.lemmatize(k))
    word_dict = Counter(words)
    return word_dict


def remove_words(word_dict):
    plurals = []

    common_words = ["and", "or", "the", "was", "it", "she", "he", "that", "is", "her", "a", "in", "as", "his", "of",
                    "we", "us", "an", "to", "at", "you", "but", "who", "than", "thats", "your", "for", "may", "more",
                    "with", "not", "about", "from", "also", "well", "this", "would", "yet", "ourselves", "hers",
                    "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having",
                    "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of",
                    "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the",
                    "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me",
                    "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above",
                    "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them",
                    "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because",
                    "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has",
                    "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t",
                    "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here",
                    "than", "from", "like", "get", "set", "make", "still", "going", "could", "lot", "even", "weve",
                    "first", "much", "way", "around", "wanted", "what", "one", "dont", "want", "q", "a", "since", "see",
                    "another", "hi", "_", "wa", "u", "ha"]

    for k in common_words:
        if k in word_dict:
            del word_dict[k]

    with open("MasterList.txt") as f:
            master_list = f.readlines()
    master_list = [x.strip() for x in master_list]

    for i in master_list:
        if i in word_dict:
            word_dict[i[:-1]] = word_dict[i[:-1]] + word_dict[i]
            plurals.append(i)

    if "losses" in word_dict:
        word_dict["loss"] = word_dict["loss"] + word_dict["losses"]
        plurals.append("losses")

    if "loss" in plurals:
        plurals.remove("loss")

    for j in plurals:
        del word_dict[j]



    return word_dict


def show_data(name, title, word_dict):
    # print("\n-------------------------------------------------------\n" + name +
    #      "\n-------------------------------------------------------")

    # for word, count in word_dict.most_common(10):
    #    print(word, ": ", count)

    for word, count in word_dict.most_common():
        line = ((word + "," + str(count)).encode("ascii", "ignore"))
        print(line.decode())

    df = pd.DataFrame(word_dict.most_common(10), columns=['Word', 'Count'])
    df.plot.bar(x='Word', y='Count')
    plt.xticks(rotation=25)
    plt.title(title)
    return

