import os
import jieba
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import streamlit as st
folder_path = r"C:\Users\17475\Desktop\文本分析\file_learning\cache"


def segment_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        seg_list = jieba.cut(content)
        result = ' '.join(seg_list)
    return result


def process_files_in_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    segmented_content = ''
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        segmented_content = segmented_content + segment_file(file_path) + "\n"

    with open(r"C:\Users\17475\Desktop\文本分析\file_learning\cache\segement_result.txt", 'w', encoding='utf8') as file:
        file.write(segmented_content)


def start_train():
    try:
        st.write("分词中.....")
        process_files_in_folder(folder_path=folder_path)
        sentences = LineSentence(r"C:\\Users\\17475\Desktop\文本分析\\file_learning\cache\segement_result.txt")
        st.write("训练中....")
        model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        model.save(r'C:\Users\17475\Desktop\文本分析\file_learning\word2vec_model.model')
    except Exception as e:
        return 0
    return 1
