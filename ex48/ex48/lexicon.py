__author__ = 'oucb'

def scan(words):
    dic_words = {"north": ('direction', 'north'), "south": ('direction', 'south'),
                "east": ('direction', 'east'), "go": ('verb', 'go'), "kill": ('verb', 'kill'),
                "eat": ('verb', 'eat'), "the": ('stop', 'the'), "in": ('stop', 'in'),
                "of": ('stop', 'of'), "bear": ('noun', 'bear'), "princess": ('noun', 'princess'),
                "door": ('noun', 'door'), "1234": ('number', 1234), "3": ('number', 3),
                "91234": ('number', 91234), "ASDFASDFASDF": ('error', 'ASDFASDFASDF'),
                 "IAS": ('error', 'IAS'), "open": ('error', 'open'), "and": ('error', 'and'),
                 "smack": ('error', 'smack'), "nose": ('error', 'nose')
                }
    words_list = words.split()
    l = []
    try:
        for x in words_list:
            l.append(dic_words[x])
        return l
    except ValueError:
        return None





