# sast2023 word game

## 环境配置

streamlit==1.24.1

## 使用设置

约定以下参数：\
--file -f&emsp;接文章的路径\
--choose -c&emsp;是否选择文章（不加-c则从题库中随机抽取文章）

文章使用 JSON 存储，格式如下：\
{\
&emsp;&emsp;"language":"文章语言",\
&emsp;&emsp;"articles": [\
&emsp;&emsp;{\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"title":"文章标题",\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"article":"文章内容",\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"hints":["填词提示",...]\
&emsp;&emsp;}\
&emsp;&emsp;...\
&emsp;&emsp;]\
}

## 游戏功能

使用命令streamlit run main.py -- -f example.json可进入游戏并随机抽取文章\
使用命令streamlit run main.py -- -c -f example.json可进入游戏并自己选择文章

根据提示填词后，点击“生成我的奇妙文章！”按钮即可生成文章\
点击“保存我的奇妙文章！”按钮可以以.txt格式下载生成的文章
