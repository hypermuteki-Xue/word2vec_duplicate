import os
import fitz

folder_path = r'C:\Users\17475\Desktop\文本分析\期末\file'

# 获取文件夹中所有的docx文件
pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]


def read_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    doc.close()
    return text


for pdf_file in pdf_files:
    try:
        pdf_path = os.path.join(folder_path, pdf_file)
        content = read_pdf_content(pdf_path)
        if len(content) <= 10:
            continue

        # 构造输出txt文件路径
        txt_file_path = os.path.splitext(pdf_file)[0] + '.txt'
        txt_file_path = os.path.join(r"C:\Users\17475\Desktop\文本分析\file_learning\cache", txt_file_path)

        # 打开txt文件以写入模式
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(content)

        print(f'文本已提取并保存到 {txt_file_path}')
    except Exception as e:
        print(pdf_file)
