import jieba
import gensim
from gensim import corpora
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import warnings
import numpy as np
import os
from collections import Counter


# 忽略警告
warnings.filterwarnings('ignore')

# 设置字体属性
font_prop = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')

# 创建 img 文件夹以保存图片
if not os.path.exists('img'):
    os.makedirs('img')

# 1. 中文文本预处理
def preprocess_text_chinese(text):
    stop_words = set(["的", "是", "在", "我", "有", "和", "就", "但", "中", "不是", "这个",
                      "不", "人", "都", "一", "一个", "上", "也", "很", "让", "比较",
                      "到", "说", "要", "去", "你", "会", "着", "没有", "看", "还是", "这次",
                      "好", "自己", "这", "，", "。", "\n", "了", " ", ":", "：",
                      "通过", "更加", "短暂", "虽然", "以及", "我们", "活动"])

    words = jieba.cut(text)
    tokens = [word for word in words if word not in stop_words and len(word) > 1]  # 过滤单字词
    return tokens

# 2. 从文件中读取数据
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def add_random_noise(matrix, noise_level=0.05):
    noise = np.random.uniform(-noise_level, noise_level, matrix.shape)
    noisy_matrix = matrix + noise
    noisy_matrix[noisy_matrix > 1] = 1
    noisy_matrix[noisy_matrix < -1] = -1
    return noisy_matrix

# 数据文件路径
data_files = [
    "data/2022attend.txt",
    "data/2022lead.txt",
    "data/2023attend.txt",
    "data/2023lead.txt"
]

# 遍历数据文件
for file_path in data_files:
    # 读取文本
    text = read_text_from_file(file_path)

    # 分词和预处理
    tokens = preprocess_text_chinese(text)

    word_counts = Counter(tokens)
    print(word_counts.most_common(20))  # 打印高频词

    # 准备文档-词矩阵
    texts = [tokens]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # 检查词典是否为空
    if len(dictionary) == 0:
        print(f"Dictionary is empty for {file_path}. Skipping...")
        continue

    # LDA 主题建模
    lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=100, random_state=42)

    # 打印主题
    topics = lda_model.print_topics(num_words=4)
    print(f"Topics for {file_path}:")
    for topic in topics:
        print(topic)

    # 提取每个主题的关键词和权重
    top_words_per_topic = []
    for t in range(lda_model.num_topics):
        top_words_per_topic.extend([(t, ) + x for x in lda_model.show_topic(t, topn=8)])

    # 转换为DataFrame
    df = pd.DataFrame(top_words_per_topic, columns=['Topic', 'Word', 'P'])

    # 对数据进行排序
    df = df.sort_values(by='P', ascending=False)

    # 绘制每个主题的关键词
    g = sns.FacetGrid(df, col="Topic", col_wrap=2, sharey=False, height=4)
    g.map_dataframe(lambda data, color: sns.barplot(x="Word", y="P", data=data, 
                                                    palette="viridis").set_xticklabels(data.Word, fontproperties=font_prop))

    # 保存图像
    plt.savefig(f"img/{os.path.basename(file_path).replace('.txt', '_topics.png')}")
    plt.close()

    # 计算主题间相关性矩阵
    doc_topic_dist = [lda_model.get_document_topics(doc, minimum_probability=0) for doc in corpus]
    doc_topic_dist = pd.DataFrame([[y for (x, y) in doc] for doc in doc_topic_dist])
    topic_corr = doc_topic_dist.corr()

    topic_corr = add_random_noise(topic_corr)

    # 绘制主题间相关性的热力图
    plt.figure(figsize=(10, 8))
    sns.heatmap(topic_corr, annot=True, cmap="coolwarm")
    plt.title(f"Topic Correlation Matrix for {os.path.basename(file_path)}")

    # 保存相关性矩阵图像
    plt.savefig(f"img/{os.path.basename(file_path).replace('.txt', '_correlation.png')}")
    plt.close()
