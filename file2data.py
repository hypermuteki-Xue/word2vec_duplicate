import os
import pymysql

connect = pymysql.connect(host='localhost', user='root', password='1234', port=3306, database='mydb1')
cursor = connect.cursor()

table_name = "ArticleTable"

cache_path = r"C:\Users\17475\Desktop\文本分析\file_learning\cache"

for file_name in os.listdir(cache_path):
    file_address = ""
    file_main_sentence = ""
    txt_path = os.path.join(cache_path, file_name)

    with open(txt_path, 'r', encoding='utf8') as file:
        file_data = file.read()

    file_content = file_data.split("。")

    flag = 0
    for i, paragraph in enumerate(file_content):
        if '人民政府' in paragraph and flag == 0:
            file_address = paragraph
            flag = 1
        if flag == 1:
            if i + 4 <= len(file_content):
                file_main_sentence = '。'.join(file_content[i + 1:i + 4])
            else:
                file_main_sentence = '。'.join(file_content[i + 1])
            break


    try:
        sql = f"INSERT INTO {table_name} (FileName, SendingUnit, SubjectSentence, ArticleContent) VALUES (%s, %s, %s, %s)"
        values = (file_name, file_address, file_main_sentence, file_data)
        cursor.execute(sql, values)
        connect.commit()
        print(f"Data inserted for {file_name}")
    except Exception as e:
        print(f"Error inserting data for {file_name}: {str(e)}")

# Close the cursor and connection
cursor.close()
connect.close()
