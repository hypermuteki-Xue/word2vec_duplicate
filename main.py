import streamlit as st
import data2model
import handler


def main():
    # 添加背景样式
    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
            }
            .stApp {
                max-width: 800px;
                margin: 0 auto;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("文件语义搜索系统")

    # 创建一个下拉框，用于选择搜索类型
    search_type = st.selectbox("选择搜索类型", ["查找地址", "查找中心句", "查找全文"])

    # 创建一个文本框，接收用户输入的搜索查询
    search_query = st.text_input("输入内容")

    # 根据用户选择的搜索类型，调用相应的搜索函数
    if st.button("搜索"):
        with st.spinner("正在搜索，请稍候..."):
            if search_type == "查找地址":
                    result = handler.get_similarity_address(search_query)
            elif search_type == "查找中心句":
                    result = handler.get_similarity_main_sentence(search_query)
            elif search_type == "查找全文":
                    result = handler.get_similarity_whole_text(search_query)

            st.write("搜索结果:")
            for filename, content in result.items():
                    st.write(f"这个文件相似度较高: {filename}")
                    st.write(f"相似度为: {content[0]},其中内容是{content[1]}")
                    st.write("---")

            st.success("搜索结果展示完成")
    st.markdown("---")

    # 添加模型训练按钮
    if st.button("模型训练"):
        model_path=r"C:\Users\17475\Desktop\文本分析\file_learning\word2vec_model.model"
        bool=data2model.start_train()
        if bool ==1:
            st.write(f"训练成功，位于{model_path}")
        else:
            st.write("训练失败，请联系管理员")




if __name__ == "__main__":
    main()
