import requests
import json
import chardet
import time
from datetime import datetime
import os
from typing import Dict, List

# API 配置
API_URL = "https://a1729llm.skill-net.xyz/qwq_stream_chat"
HEADERS = {
    "CF-Access-Client-Id": "136a687f2d63aca6b2ba84fa936cd326.access",
    "CF-Access-Client-Secret": "386b73fcf559d2a9a63998cf9d58ed19fd8f808ea1d9c5b500d124c49daaa003",
    "Content-Type": "application/json"
}

# JSON 分析模板
ANALYSIS_PROMPT = '''请以JSON格式分析以下团辅活动反馈，格式如下：
{
    "emotions":{"positive":[{"name":"情绪","intensity":5}],"neutral":[],"negative":[]},
    "themes":[{"name":"主题","percentage":30,"keywords":[]}],
    "challenges":[{"issue":"问题","severity":3,"description":""}],
    "key_events":["事件1"],
    "leader_performance":{"organization":4,"empathy":4,"leadership":4}
}

反馈文本：'''

def detect_file_encoding(file_path: str) -> str:
    """检测文件编码"""
    # 首先检查文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
        
    # 读取文件内容
    with open(file_path, 'rb') as file:
        # 读取足够的字节来检测编码
        raw_data = file.read()
        if not raw_data:
            raise ValueError(f"文件为空: {file_path}")
            
        # 使用chardet检测编码
        result = chardet.detect(raw_data)
        if result['encoding'] is None:
            raise ValueError(f"无法检测文件编码: {file_path}")
            
        print(f"文件 {os.path.basename(file_path)} 的编码检测结果: {result}")
        return result['encoding']

class FeedbackAnalyzer:
    def __init__(self):
        self.results_dir = "analysis_results"
        self.create_results_directory()
        
    def create_results_directory(self):
        """创建结果存储目录"""
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
            os.makedirs(os.path.join(self.results_dir, "raw"))
            os.makedirs(os.path.join(self.results_dir, "processed"))

    def analyze_feedback(self, feedback_text: str, index: int, feedback_type: str) -> Dict:
        """发送单个反馈到API进行分析，支持流式返回"""
        try:
            payload = {
                "text": ANALYSIS_PROMPT + feedback_text
            }
            
            print(f"\n正在处理第 {index} 条{feedback_type}反馈...")
            print(f"发送时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("反馈内容前100字: ", feedback_text[:100], "...")
            
            # 使用stream=True获取流式响应
            response = requests.post(API_URL, headers=HEADERS, json=payload, stream=True)
            response.raise_for_status()
            
            # 保存原始反馈
            raw_feedback_path = os.path.join(
                self.results_dir, 
                "raw", 
                f"{feedback_type}_{index}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )
            with open(raw_feedback_path, 'w', encoding='utf-8') as f:
                f.write(feedback_text)
            
            # 收集完整响应
            full_response = ""
            print("\nQwQ 的分析结果:")
            print("-" * 50)
            
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    # 处理二进制数据
                    chunk_text = chunk.decode('utf-8')
                    # 实时显示响应
                    print(chunk_text, end='', flush=True)
                    full_response += chunk_text
            
            print("\n" + "-" * 50)
            
            # 保存 QwQ 的分析结果
            result_path = os.path.join(
                self.results_dir, 
                "processed", 
                f"{feedback_type}_{index}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
            
            try:
                # 尝试解析为JSON并保存
                result_json = json.loads(full_response)
                with open(result_path, 'w', encoding='utf-8') as f:
                    json.dump(result_json, f, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                # 如果不是有效的JSON，保存原始响应
                with open(result_path.replace('.json', '.txt'), 'w', encoding='utf-8') as f:
                    f.write(full_response)
            
            time.sleep(1)  # 添加短暂延迟
            return full_response
            
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None

    def process_feedbacks(self, feedbacks: List[str], feedback_type: str) -> List[str]:
        """处理一组反馈"""
        results = []
        for i, feedback in enumerate(feedbacks, 1):
            if feedback:
                print(f"\n处理{feedback_type}反馈 {i}/{len(feedbacks)}")
                print("=" * 30)
                result = self.analyze_feedback(feedback, i, feedback_type)
                if result:
                    results.append(result)
                    print(f"{feedback_type} {i} 分析完成")
                else:
                    print(f"{feedback_type} {i} 分析失败")
        return results

def read_feedback_files(attend_path: str, lead_path: str) -> tuple:
    """读取反馈文件，返回所有反馈列表"""
    try:
        # 检测文件编码
        attend_encoding = detect_file_encoding(attend_path)
        lead_encoding = detect_file_encoding(lead_path)
        
        print(f"检测到参与者文件编码: {attend_encoding}")
        print(f"检测到带领者文件编码: {lead_encoding}")
        
        # 读取参与者文件
        with open(attend_path, 'r', encoding=attend_encoding) as f:
            attend_feedbacks = [fb.strip() for fb in f.read().split('\n\n') if fb.strip()]
        
        # 读取带领者文件
        with open(lead_path, 'r', encoding=lead_encoding) as f:
            lead_feedbacks = [fb.strip() for fb in f.read().split('\n\n') if fb.strip()]
        
        return attend_feedbacks, lead_feedbacks
    
    except Exception as e:
        print(f"读取文件时出错: {e}")
        # 尝试其他常见编码
        encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030', 'big5', 'ascii']
        for encoding in encodings:
            try:
                print(f"尝试使用 {encoding} 编码读取...")
                with open(attend_path, 'r', encoding=encoding) as f:
                    attend_feedbacks = [fb.strip() for fb in f.read().split('\n\n') if fb.strip()]
                with open(lead_path, 'r', encoding=encoding) as f:
                    lead_feedbacks = [fb.strip() for fb in f.read().split('\n\n') if fb.strip()]
                print(f"成功使用 {encoding} 编码读取文件")
                return attend_feedbacks, lead_feedbacks
            except UnicodeDecodeError:
                continue
        raise Exception("无法找到正确的文件编码")

def main():
    # 文件路径
    attend_path = "/Users/abel/AbelProject/PythonRepository/AbelDemo/psych_investigation_xl/data/sample_2025.1.10attend.txt"
    lead_path = "/Users/abel/AbelProject/PythonRepository/AbelDemo/psych_investigation_xl/data/sample_2025.1.10lead.txt"
    
    try:
        analyzer = FeedbackAnalyzer()
        
        # 读取文件
        attend_feedbacks, lead_feedbacks = read_feedback_files(attend_path, lead_path)
        
        print(f"\n=== 开始分析 ===")
        print(f"总共需要处理:")
        print(f"- {len(attend_feedbacks)} 条参与者反馈")
        print(f"- {len(lead_feedbacks)} 条带领者反馈")
        
        # 处理反馈
        attend_results = analyzer.process_feedbacks(attend_feedbacks, "参与者")
        lead_results = analyzer.process_feedbacks(lead_feedbacks, "带领者")
        
        # 保存汇总结果
        print("\n=== 保存分析结果 ===")
        summary_path = os.path.join(analyzer.results_dir, f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump({
                "attend_results": attend_results,
                "lead_results": lead_results,
                "statistics": {
                    "attend_count": len(attend_results),
                    "lead_count": len(lead_results),
                    "total_count": len(attend_results) + len(lead_results),
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
            }, f, ensure_ascii=False, indent=2)
        
        print(f"汇总结果已保存到 {summary_path}")
        
        # 输出统计信息
        print("\n=== 分析完成统计 ===")
        print(f"成功分析参与者反馈: {len(attend_results)}/{len(attend_feedbacks)}")
        print(f"成功分析带领者反馈: {len(lead_results)}/{len(lead_feedbacks)}")
        print(f"总耗时: {time.time() - start_time:.2f} 秒")
        
    except Exception as e:
        print(f"程序执行出错: {e}")

if __name__ == "__main__":
    start_time = time.time()
    main()
