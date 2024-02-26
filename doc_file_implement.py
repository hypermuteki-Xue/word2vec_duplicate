import win32com.client
import re
import glob
import os
from tqdm import tqdm
def read_entire_doc(doc_path):
    # 创建Word应用程序实例，并设置Visible参数为False
    word_app = win32com.client.Dispatch('Word.Application')
    word_app.Visible = False

    try:
        # 打开DOC文件
        doc = word_app.Documents.Open(doc_path)

        # 读取整个文档内容
        entire_content = ""
        for i, para in enumerate(doc.Paragraphs):
            # 检查段落长度
            if len(para.Range.Text.strip()) >= 2:
                if '附件'in para.Range.Text.strip():
                    break
                entire_content += f"第{i+1}段:{para.Range.Text.strip()}。"

        return entire_content

    except Exception as e:
        print(f"Error: {e}")

def clean_text(text):
    # 使用正则表达式剔除特殊字符，只保留中文、数字和换行符
    cleaned_text = re.sub(r'[^\u4e00-\u9fa5\d\n,，.。?!]+', '', text)
    return cleaned_text


def read_all_doc_files(folder_path):
    # 获取指定目录下所有的.doc文件
    doc_files = glob.glob(os.path.join(folder_path, '*.doc'))
    for each_doc_file in tqdm(doc_files):
        file_name = each_doc_file.split("\\")[-1].replace(".doc", '.txt')
        file_name = os.path.join(r"C:\Users\17475\Desktop\文本分析\file_learning\cache", file_name)
        if os.path.exists(file_name):
            continue
        text=read_entire_doc(each_doc_file)
        try:
            text=clean_text(text)
        except Exception as e:
            print(file_name)
        with open(file_name,'w',encoding='utf8') as file:
            file.write(str(text))


# 指定文件夹路径
folder_path = r'C:\Users\17475\Desktop\文本分析\期末\file'


# 读取并输出文档段落
print(read_all_doc_files(folder_path))
