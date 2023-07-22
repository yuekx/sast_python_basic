import argparse
import json
import random
import streamlit as st

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    2. -c 表示是否选择文章

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-c", "--choose", action="store_true", help="是否选择文章")
    
    args = parser.parse_args()
    return args



def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data



def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        user_input = st.text_input(f"请输入{hint}：")
        keys.append(user_input)

    return keys


def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for i in range(len(keys)):
        article = article.replace("{{"+str(i+1)+"}}", keys[i])

    return article

if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]

    st.title("欢迎来到填词游戏！")

    if args.choose:
        option=st.selectbox('请选择文章：',('贵系日常','你说得对','我推的孩子'))        
    
    else:
        if 'option' not in st.session_state:
            st.session_state['option']=random.choice(('贵系日常','你说得对','我推的孩子'))
        option = st.session_state.option
        st.subheader('随机选择的文章为：'+option)


    for a in articles:
        if a["title"] == option:
            t_article = a["article"]
            t_key = get_inputs(a["hints"])
            break
    
    t_article=replace(t_article,t_key)
    if st.button("生成我的奇妙文章！"):
        st.write(t_article)
        st.download_button(
            label="保存我的奇妙文章！",
            data=t_article,
            file_name=option+".txt")



