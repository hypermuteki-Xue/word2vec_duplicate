import os
from docx import Document

# 文件夹路径
folder_path = r'C:\Users\17475\Desktop\文本分析\期末\file'

# 获取文件夹中所有的docx文件
docx_files = [file for file in os.listdir(folder_path) if file.endswith('.docx')]

# 遍历每个docx文件
for docx_file in docx_files:
    try:
        docx_path = os.path.join(folder_path, docx_file)

        # 使用python-docx库读取docx文件
        doc = Document(docx_path)

        # 构造输出txt文件路径
        txt_file_path = os.path.splitext(docx_file)[0] + '.txt'
        txt_file_path = os.path.join(r"C:\Users\17475\Desktop\文本分析\file_learning\cache", txt_file_path)

        # 打开txt文件以写入模式
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            # 遍历每一段
            for i, paragraph in enumerate(doc.paragraphs, start=1):
                if len(paragraph.text) <= 2:
                    continue
                txt_file.write(f'第{i}段: {paragraph.text}\n')

        print(f'文本已提取并保存到 {txt_file_path}')
    except Exception as e:
        print(docx_file)
