import matplotlib.pyplot as plt
# 绘图1
# # 股票数据
# companies = ['Unity Software Inc', 'Roblox Corporation', 'Anycolor Inc', 'MonoAl technology', 'Digital Domain Holdings 1', 'Qualcomm Incorporated', 'Hexagon AB', 
# 	'Sony Group Corporation', 'BILIBILI', 'Meta Platforms, Inc.', 'Nvidia Corp', 'Flowing Cloud Technology', 'XD Inc.', 'Fciyu Technology International', 'Global Digital MoJo', 'Alphabet (Google)', 'Oculus VisionTech, Inc', 'Autodesk, Inc.']
# categories = ['vr', 'vr', 'vr', 'AR VR game', 'local core', 'satellite', 'vr', 'AR VR', 'CN-VR', 'metaverse', 'metaverse', 'suppley', 'hk', 'hk', 'hk', 'Vr', 'vr', 'vr']

# # 创建图表
# plt.bar(companies, categories)

# plt.bar(companies, categories, color = 'gray', width = 0.4)
# plt.xlabel('Companies')
# plt.ylabel('Categories')
# plt.title('Portfolio Stocks')

# plt.xticks(rotation=90)
# plt.tight_layout()

# plt.show()

'''

This portfolio focuses on companies that are leaders or emerging players in the virtual reality industry 
and are involved in various aspects of virtual reality, such as gaming, education, entertainment, and technology. 
The portfolio also includes companies from different regions, such as the United States, Japan, China, Hong Kong, and Sweden, 
to provide diversity and mitigate risks.

'''

# 绘图2
import matplotlib.pyplot as plt
import random

# Company names and categories
companies = ['Unity Software Inc', 'Roblox Corporation', 'Anycolor Inc', 'MonoAl technology', 'Digital Domain Holdings 1', 
             'Qualcomm Incorporated', 'Hexagon AB', 'Sony Group Corporation', 'BILIBILI', 'Meta Platforms, Inc.',
             'Nvidia Corp', 'Flowing Cloud Technolog', 'XD Inc.', 'Fciyu Technology Internati', 'Global Digital MoJo',
             'Alphabet (Google)', 'Oculus VisionTech, Inc', 'Autodesk, Inc.']
categories = ['Virtual Reality Core', 'Virtual Reality Core', 'Virtual Reality Core', 'AR VR Gaming Core', 'Local Public Core',
              'Large Public Satellite', 'Virtual Reality', 'AR VR Technology', 'Virtual Reality', 'Cosmic Concept', 
              'Cosmic Leader', 'Provides in China', 'Listed in Hong Kong', 'Listed in Hong Kong', 'Established in Hong Kong',
              'VR Headset Equipment', 'Virtual Reality Tech Company', 'Extracted Table']

# Portfolio stocks with first 10 items being 70% and last 8 items being 30%
portfolio_stocks = [70 + i if i < 10 else 30 + i * 2 for i in range(len(companies))]

# Plotting the bar graph
plt.barh(companies, portfolio_stocks, color='blue')
plt.xlabel('Percentage of Portfolio')
plt.title('Portfolio Stocks')

for i, v in enumerate(portfolio_stocks):
    # plt.text(v + 3, i, str(v) + '', color='gray', fontweight='bold')
    plt.text(v + 3, i, '', color='gray', fontweight='bold')

plt.show()
