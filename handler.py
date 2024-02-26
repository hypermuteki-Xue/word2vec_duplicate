from gensim.models import Word2Vec
import jieba
import pymysql
import traceback
from tqdm import tqdm
import streamlit as st

def get_similarity_whole_text(input_text):
    similarity = {}
    connect = pymysql.connect(host='localhost', user='root', password='1234', database='mydb1', port=3306)
    cursor = connect.cursor()
    sql = 'select filename,articlecontent from articletable'
    cursor.execute(sql)
    results = cursor.fetchall()
    for text_tuple in tqdm(results):
        file_name = text_tuple[0]
        whole_text=text_tuple[1]
        try:
            sim_radio = get_similarity_between_two_sentences(input_text, whole_text)
            if sim_radio >= 0.5:
                similarity[file_name] = [sim_radio,whole_text]
        except Exception as e:
            traceback.print_exc()
    cursor.close()
    connect.close()
    sorted_similarity = sorted(similarity.items(), key=lambda x: x[1][0], reverse=True)
    top_10_similarity = sorted_similarity[:1]
    return dict(top_10_similarity)


def get_similarity_main_sentence(input_sentence):
    similarity = {}
    connect = pymysql.connect(host='localhost', user='root', password='1234', database='mydb1', port=3306)
    cursor = connect.cursor()
    sql = 'select filename,subjectsentence from articletable'
    cursor.execute(sql)
    results = cursor.fetchall()
    for sentence_tuple in tqdm(results):
        file_name = sentence_tuple[0]
        main_sentence = sentence_tuple[1]
        try:
            sim_radio = get_similarity_between_two_sentences(input_sentence, main_sentence)
            if sim_radio >= 0.3:
                similarity[file_name] = [sim_radio,main_sentence]
        except Exception as e:
            traceback.print_exc()
    cursor.close()
    connect.close()
    sorted_similarity = sorted(similarity.items(), key=lambda x: x[1][0], reverse=True)

    # 取前十个数据
    top_10_similarity = sorted_similarity[:10]
    return dict(top_10_similarity)
def get_similarity_address(input_address):
    similarity = {}
    connect = pymysql.connect(host='localhost', user='root', password='1234', database='mydb1', port=3306)
    cursor = connect.cursor()
    sql = 'select filename,sendingunit from articletable'
    cursor.execute(sql)
    results = cursor.fetchall()
    i=0
    for address_tuple in tqdm(results):
        i=i+1
        file_name = address_tuple[0]
        address_name = address_tuple[1]
        try:
            sim_radio = get_similarity_between_two_sentences(input_address, address_name)
            if sim_radio >= 0.7:
                similarity[file_name] = [sim_radio,address_name]
        except Exception as e:
            st.write("出错了，请联系维修人员")
    cursor.close()
    connect.close()
    sorted_similarity = sorted(similarity.items(), key=lambda x: x[1][0], reverse=True)

    # 取前十个数据
    top_10_similarity = sorted_similarity[:10]
    return dict(top_10_similarity)


def get_similarity_between_two_sentences(sentence_one, sentence_two):
    model = Word2Vec.load(r'C:\Users\17475\Desktop\文本分析\file_learning\word2vec_model.model')
    input_seg_list1 = list(jieba.cut(sentence_one))
    input_seg_list2 = list(jieba.cut(sentence_two))

    vector1 = sum(model.wv[word] for word in input_seg_list1 if word in model.wv) / len(input_seg_list1)
    vector2 = sum(model.wv[word] for word in input_seg_list2 if word in model.wv) / len(input_seg_list2)

    similarity = model.wv.cosine_similarities(vector1, [vector2])[0]

    return abs(similarity)
