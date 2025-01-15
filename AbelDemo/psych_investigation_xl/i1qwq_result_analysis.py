import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from datetime import datetime
import numpy as np
import re
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc') 

# 设置中文字体
def setup_matplotlib_fonts():
    """设置 matplotlib 的字体，适配中文"""
    if os.sys.platform == 'darwin':  # macOS
        plt.rcParams['font.family'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang HK', 'Apple LiGothic']
    elif os.sys.platform == 'win32':  # Windows
        plt.rcParams['font.family'] = ['Microsoft YaHei', 'SimHei']
    else:  # Linux
        plt.rcParams['font.family'] = ['WenQuanYi Micro Hei', 'Droid Sans Fallback']
    
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 12






def extract_json_content(text: str) -> dict:
    """从文本中提取完整的JSON对象"""
    try:
        # 寻找最后一个完整的JSON结构
        pattern = r'\{[\s\S]*"emotions"[\s\S]*"themes"[\s\S]*"challenges"[\s\S]*"leader_performance"[\s\S]*\}'
        matches = list(re.finditer(pattern, text, re.DOTALL))
        
        if matches:
            # 获取最后一个匹配
            last_match = matches[-1].group()
            
            # 清理和格式化JSON字符串
            # 1. 替换换行符
            json_str = last_match.replace('\n', '')
            # 2. 替换多个空格
            json_str = re.sub(r'\s+', ' ', json_str)
            # 3. 确保数组和对象正确闭合
            json_str = json_str.replace('} }', '}}')
            json_str = json_str.replace('] ]', ']]')
            
            try:
                # 解析JSON
                result = json.loads(json_str)
                # 验证必要的字段
                if all(key in result for key in ['emotions', 'themes', 'challenges', 'leader_performance']):
                    return result
                else:
                    print("缺少必要的字段")
                    return None
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")
                print(f"错误位置附近的内容: {json_str[max(0, e.pos-50):min(len(json_str), e.pos+50)]}")
                return None
                
        return None
    except Exception as e:
        print(f"提取过程错误: {e}")
        return None

def load_summary_data(file_path):
    """加载并解析summary JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            
            print(f"\n找到 {len(raw_data.get('attend_results', []))} 条参与者反馈")
            print(f"找到 {len(raw_data.get('lead_results', []))} 条领导者反馈")
            
            attend_results = []
            lead_results = []
            
            # 处理参与者数据
            for idx, item in enumerate(raw_data.get('attend_results', []), 1):
                print(f"\n处理第 {idx} 条参与者数据...")
                json_data = extract_json_content(item)
                if json_data:
                    attend_results.append(json_data)
            
            # 处理领导者数据
            for idx, item in enumerate(raw_data.get('lead_results', []), 1):
                print(f"\n处理第 {idx} 条领导者数据...")
                json_data = extract_json_content(item)
                if json_data:
                    lead_results.append(json_data)
            
            print(f"\n成功解析 {len(attend_results)} 条参与者反馈")
            print(f"成功解析 {len(lead_results)} 条领导者反馈")
            
            # 打印第一条成功解析的数据（用于验证）
            if attend_results:
                print("\n参与者数据示例:")
                print(json.dumps(attend_results[0], indent=2, ensure_ascii=False))
            
            return {
                'attend_results': attend_results,
                'lead_results': lead_results
            }
            
    except Exception as e:
        print(f"加载数据时出错: {str(e)}")
        import traceback
        traceback.print_exc()
        return {'attend_results': [], 'lead_results': []}



def validate_summary_data(summary_data):
    """验证数据是否有效"""
    if not summary_data['attend_results'] and not summary_data['lead_results']:
        print("警告: 没有有效的反馈数据")
        return False
    
    # 打印第一条数据的示例（用于调试）
    if summary_data['attend_results']:
        print("\n参与者数据示例:")
        first_attend = summary_data['attend_results'][0]
        print("- 情感:", first_attend.get('emotions', {}))
        print("- 主题:", first_attend.get('themes', []))
        print("- 领导力表现:", first_attend.get('leader_performance', {}))
    
    return True


def generate_analysis_report(summary_data, vis_dir):
    """生成分析报告"""
    try:
        # 计算基本统计数据
        attend_count = len(summary_data['attend_results'])
        lead_count = len(summary_data['lead_results'])
        
        # 1. 情感分析
        attend_emotions = []
        lead_emotions = []
        
        for result in summary_data['attend_results']:
            for emotion in result['emotions']['positive']:
                attend_emotions.append(emotion['intensity'])
                
        for result in summary_data['lead_results']:
            for emotion in result['emotions']['positive']:
                lead_emotions.append(emotion['intensity'])
        
        avg_attend_emotion = np.mean(attend_emotions) if attend_emotions else 0
        avg_lead_emotion = np.mean(lead_emotions) if lead_emotions else 0
        
        # 2. 主题分析
        themes_data = {}
        for result in summary_data['attend_results']:
            for theme in result['themes']:
                if theme['name'] not in themes_data:
                    themes_data[theme['name']] = []
                themes_data[theme['name']].append(theme['percentage'])
        
        # 计算主题平均占比
        themes_avg = {name: np.mean(percentages) for name, percentages in themes_data.items()}
        
        # 3. 领导力评估
        attend_leadership = {'organization': [], 'empathy': [], 'leadership': []}
        lead_leadership = {'organization': [], 'empathy': [], 'leadership': []}
        
        for result in summary_data['attend_results']:
            perf = result['leader_performance']
            attend_leadership['organization'].append(perf['organization'])
            attend_leadership['empathy'].append(perf['empathy'])
            attend_leadership['leadership'].append(perf['leadership'])
            
        for result in summary_data['lead_results']:
            perf = result['leader_performance']
            lead_leadership['organization'].append(perf['organization'])
            lead_leadership['empathy'].append(perf['empathy'])
            lead_leadership['leadership'].append(perf['leadership'])
        
        # 生成报告文本
        report = f"""
团辅活动分析报告
=====================

基本信息：
----------
- 参与者反馈数量：{attend_count}
- 领导者反馈数量：{lead_count}
- 总反馈数量：{attend_count + lead_count}

情感分析：
----------
- 参与者平均情感强度：{avg_attend_emotion:.2f}
- 领导者平均情感强度：{avg_lead_emotion:.2f}

主题分析：
----------"""
        
        # 添加主题分析结果
        for theme, avg_percentage in themes_avg.items():
            report += f"\n- {theme}: {avg_percentage:.1f}%"
        
        report += """

领导力评估：
----------"""
        
        # 添加领导力评估结果
        metrics = {'organization': '组织能力', 'empathy': '同理心', 'leadership': '领导力'}
        for key, name in metrics.items():
            attend_avg = np.mean(attend_leadership[key]) if attend_leadership[key] else 0
            lead_avg = np.mean(lead_leadership[key]) if lead_leadership[key] else 0
            report += f"\n- {name}："
            report += f"\n  * 参与者评分：{attend_avg:.2f}"
            report += f"\n  * 领导者自评：{lead_avg:.2f}"
        
        report += f"""

可视化结果：
----------
可视化图表已保存在：{vis_dir}
- emotion_intensity_comparison.png: 情感强度对比图
- theme_distribution.png: 主题分布对比图
- leadership_radar.png: 领导力表现雷达图
"""
        
        # 保存报告到文件
        report_file = os.path.join("analysis_results", f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        return report
        
    except Exception as e:
        print(f"生成报告时出错: {e}")
        import traceback
        traceback.print_exc()
        return None

def process_leadership_data(summary_data):
    """处理领导力评估数据"""
    leadership_metrics = {
        '参与者': {'组织能力': [], '同理心': [], '领导力': []},
        '领导者': {'组织能力': [], '同理心': [], '领导力': []}
    }
    
    # 处理参与者评估数据
    for result in summary_data['attend_results']:
        perf = result.get('leader_performance', {})
        if perf:
            leadership_metrics['参与者']['组织能力'].append(float(perf.get('organization', 0)))
            leadership_metrics['参与者']['同理心'].append(float(perf.get('empathy', 0)))
            leadership_metrics['参与者']['领导力'].append(float(perf.get('leadership', 0)))
    
    # 处理领导者自评数据
    for result in summary_data['lead_results']:
        perf = result.get('leader_performance', {})
        if perf:
            leadership_metrics['领导者']['组织能力'].append(float(perf.get('organization', 0)))
            leadership_metrics['领导者']['同理心'].append(float(perf.get('empathy', 0)))
            leadership_metrics['领导者']['领导力'].append(float(perf.get('leadership', 0)))
    
    return leadership_metrics




def create_visualizations(summary_data):
    setup_matplotlib_fonts()
    """创建可视化图表"""
    vis_dir = "analysis_results/visualizations"
    if not os.path.exists(vis_dir):
        os.makedirs(vis_dir)
    
    # 设置绘图风格
    sns.set_style("whitegrid")
    
    try:
        # 1. 情感强度对比图
        emotions_data = []
        
        # 提取情感数据
        for result in summary_data['attend_results']:
            for emotion in result['emotions']['positive']:
                emotions_data.append({
                    '角色': '参与者',
                    '情感': emotion['name'],
                    '强度': emotion['intensity']
                })
                    
        for result in summary_data['lead_results']:
            for emotion in result['emotions']['positive']:
                emotions_data.append({
                    '角色': '领导者',
                    '情感': emotion['name'],
                    '强度': emotion['intensity']
                })
        
        if emotions_data:
            plt.figure(figsize=(10, 6))
            df_emotions = pd.DataFrame(emotions_data)
            
            # 计算每个角色的平均强度
            means = df_emotions.groupby('角色')['强度'].mean()
            
            # 创建条形图
            ax = means.plot(kind='bar', color=['lightblue', 'lightcoral'])
            
            # 设置y轴范围，使差异更明显
            plt.ylim(4.5, 5.2)  # 根据实际数据调整范围
            
            # 使用正确的格式化器
            from matplotlib.ticker import FormatStrFormatter
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            
            # 在条形上添加具体数值标签
            for i, v in enumerate(means):
                ax.text(i, v, f'{v:.2f}', 
                        horizontalalignment='center', 
                        verticalalignment='bottom')
            
            # 设置标题和标签
            plt.title('情感强度对比', fontproperties=font, fontsize=14)
            plt.xlabel('角色', fontproperties=font, fontsize=12)
            plt.ylabel('平均强度', fontproperties=font, fontsize=12)
            
            # 设置x轴刻度标签的字体
            ax.set_xticklabels(means.index, fontproperties=font)
            
            # 添加网格线
            plt.grid(True, axis='y', linestyle='--', alpha=0.7)
            
            plt.tight_layout()
            plt.savefig(os.path.join(vis_dir, 'emotion_intensity_comparison.png'), 
                        dpi=300, bbox_inches='tight')
            plt.close()


        # 2. 主题分布图
        themes_data = []
        
        # 提取主题数据
        for result in summary_data['attend_results']:
            for theme in result['themes']:
                themes_data.append({
                    '角色': '参与者',
                    '主题': theme['name'],
                    '占比': theme['percentage']
                })
        
        for result in summary_data['lead_results']:
            for theme in result['themes']:
                themes_data.append({
                    '角色': '领导者',
                    '主题': theme['name'],
                    '占比': theme['percentage']
                })
                
        if themes_data:
            plt.figure(figsize=(12, 6))
            df_themes = pd.DataFrame(themes_data)
            
            # 创建图形
            ax = sns.barplot(data=df_themes, x='占比', y='主题', hue='角色')
            
            # 设置标题和轴标签
            plt.title('主题分布对比', fontproperties=font, fontsize=14)
            plt.xlabel('占比 (%)', fontproperties=font, fontsize=12)
            plt.ylabel('主题', fontproperties=font, fontsize=12)
            
            # 设置y轴标签字体（主题名称）
            ax.set_yticklabels(ax.get_yticklabels(), fontproperties=font)
            
            # 设置图例字体
            legend = ax.legend(title='角色', prop=font)
            legend.get_title().set_fontproperties(font)
            
            # 调整布局
            plt.tight_layout()
            
            # 保存图片
            plt.savefig(os.path.join(vis_dir, 'theme_distribution.png'), 
                        dpi=300, bbox_inches='tight')
            plt.close()

        
        # 3. 领导力表现雷达图
        leadership_metrics = process_leadership_data(summary_data)
        
        # 打印调试信息
        print("\n领导力评估原始数据：")
        for role, metrics in leadership_metrics.items():
            print(f"\n{role}:")
            for metric, values in metrics.items():
                print(f"{metric}: {values}")

                
        # 提取领导力数据
        for result in summary_data['attend_results']:
            perf = result['leader_performance']
            leadership_metrics['参与者']['组织能力'].append(perf['organization'])
            leadership_metrics['参与者']['同理心'].append(perf['empathy'])
            leadership_metrics['参与者']['领导力'].append(perf['leadership'])
        
        for result in summary_data['lead_results']:
            perf = result['leader_performance']
            leadership_metrics['领导者']['组织能力'].append(perf['organization'])
            leadership_metrics['领导者']['同理心'].append(perf['empathy'])
            leadership_metrics['领导者']['领导力'].append(perf['leadership'])
        
        if any(leadership_metrics['参与者'].values()) or any(leadership_metrics['领导者'].values()):
            # 计算平均值
            categories = ['组织能力', '同理心', '领导力']
            attend_means = [np.mean(leadership_metrics['参与者'][cat]) for cat in categories]
            lead_means = [np.mean(leadership_metrics['领导者'][cat]) for cat in categories]
            
            # 创建雷达图
            angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
            angles = np.concatenate((angles, [angles[0]]))
            
            attend_values = np.concatenate((attend_means, [attend_means[0]]))
            lead_values = np.concatenate((lead_means, [lead_means[0]]))
            
            fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
            ax.plot(angles, attend_values, 'o-', linewidth=2, label='参与者评估')
            ax.fill(angles, attend_values, alpha=0.25)
            ax.plot(angles, lead_values, 'o-', linewidth=2, label='领导者自评')
            ax.fill(angles, lead_values, alpha=0.25)
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories,fontproperties=font)
            plt.title('领导力表现对比',fontproperties=font, fontsize=14)
            plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1),prop=font)
            plt.savefig(os.path.join(vis_dir, 'leadership_radar.png'), 
                       dpi=300, bbox_inches='tight')
            plt.close()
        
        return vis_dir
        
    except Exception as e:
        print(f"创建可视化时出错: {e}")
        import traceback
        traceback.print_exc()
        return vis_dir


def main():
    summary_file = "analysis_results/summary_20250115_124812.json"
    
    try:
        print("正在加载数据...")
        summary_data = load_summary_data(summary_file)
        
        # 验证数据
        if not validate_summary_data(summary_data):
            print("数据验证失败，程序终止")
            return
            
        print("\n正在创建可视化...")
        vis_dir = create_visualizations(summary_data)
        
        print("正在生成报告...")
        report = generate_analysis_report(summary_data, vis_dir)
        
        if report:
            print("\n=== 分析报告 ===")
            print(report)
            print("\n报告和可视化结果已保存到 analysis_results 目录")
        
    except Exception as e:
        print(f"分析过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
