__author__ = 'oucb'
from nose.tools import *
from ex49.ex49 import *

def test_Sentence():
    sentence_room = Sentence(('noun', 'door'), ('verb', 'go'), ('direction', 'north'))
    assert_equal(sentence_room.subject, 'door')
    assert_equal(sentence_room.verb, 'go')
    assert_equal(sentence_room.object, 'north')

def test_peek():
    assert_equal(peek([('verb', 'go')]), 'verb')

def test_match():
    assert_equal(match([('verb', 'go')], 'verb'), ('verb', 'go'))

def test_skip():
    word_list = [('stop', 'of'), ('stop', 'the'), ('verb', 'go')]
    skip(word_list, 'stop')
    assert_equal(word_list, [('verb', 'go')])

def test_parse_verb():
    word_list = [('stop', 'of'), ('stop', 'the'), ('verb', 'kill')]
    assert_equal(parse_verb(word_list), ('verb', 'kill'))
    parse_list = [('noun', 'door'), ('stop', 'the'), ('verb', 'kill')]
    assert_raises(ParseError, parse_verb, word_list)

def test_parse_object():
    word_list = [('noun', 'door'), ('stop', 'the'), ('verb', 'kill')]
    assert_equal(parse_object(word_list), ('noun', 'door'))
    parse_list = [('direction', 'north'), ('stop', 'the'), ('verb', 'kill')]
    assert_equal(parse_object(parse_list), ('direction', 'north'))
    word_list = [('verb', 'go'), ('stop', 'the'), ('direction', 'north')]
    assert_raises(ParseError, parse_object, word_list)

def test_parse_subject():
    word_list = [('verb', 'go'), ('stop', 'the'), ('direction', 'north')]
    subject_obj = parse_subject(word_list, ('noun', 'door'))
    assert_equal(subject_obj.subject, 'door')
    assert_equal(subject_obj.verb, 'go')
    assert_equal(subject_obj.object, 'north')

def test_parse_sentence():
    word_list = [('noun', 'door'), ('verb', 'go'), ('stop', 'the'), ('direction', 'north')]
    sentence_obj = parse_sentence(word_list)
    assert_equal(sentence_obj.subject, 'door')
    assert_equal(sentence_obj.verb, 'go')
    assert_equal(sentence_obj.object, 'north')
    word_list = [('verb', 'go'), ('stop', 'the'), ('direction', 'north')]
    sentence_obj = parse_sentence(word_list)
    assert_equal(sentence_obj.subject, 'player')
    assert_equal(sentence_obj.verb, 'go')
    assert_equal(sentence_obj.object, 'north')
    word_list = [('stop', 'the'), ('direction', 'north')]
    assert_raises(ParseError, parse_sentence, word_list)





    