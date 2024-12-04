import os
import time
import requests
from pathlib import Path
from tqdm import tqdm
import random

# 配置
base_url = "http://202.96.31.36:8888/fliphtml5/password/main/qikan/etwx/2021/12/974/web/html5/tablet/normal/"
download_path = Path("/Users/abel/AbelProject/PythonRepository/DaughterDemo/i5magzine_download/images")
max_pages = 52  # 最大可能的页数

def check_page_exists(page_num):
    """检查页面是否存在"""
    url = f"{base_url}etwx974SL_{page_num}_l.jpg"
    response = requests.head(url)
    return response.status_code == 200

def find_last_page():
    """使用二分查找找到最后一页"""
    left, right = 1, max_pages
    last_valid = 1
    
    while left <= right:
        mid = (left + right) // 2
        if check_page_exists(mid):
            last_valid = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return last_valid

def download_image(url, filename):
    file_path = download_path / filename
    
    # 检查文件是否已存在
    if file_path.exists():
        print(f"Skip existing file: {filename}")
        return False  # 返回False表示没有进行实际下载
        
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            total_size = int(response.headers.get('content-length', 0))
            
            with open(file_path, 'wb') as f, tqdm(
                desc=filename,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as pbar:
                for data in response.iter_content(chunk_size=1024):
                    size = f.write(data)
                    pbar.update(size)
            print(f"Downloaded: {filename}")
            return True  # 返回True表示进行了实际下载
        else:
            print(f"Failed to download {filename}, status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

def random_sleep():
    """随机等待1-3秒"""
    time.sleep(random.uniform(1, 3))

def main():
    download_path.mkdir(parents=True, exist_ok=True)
    
    print("正在检测杂志页数...")
    last_page = find_last_page()
    print(f"检测到杂志共 {last_page} 页")
    
    # 首页
    print("下载首页...")
    if download_image(f"{base_url}etwx974SL_1.jpg", f"page_1.jpg"):
        random_sleep()
    if download_image(f"{base_url}etwx974SL_1_l.jpg", f"page_1_left.jpg"):
        random_sleep()
    if download_image(f"{base_url}etwx974SL_1_r.jpg", f"page_1_right.jpg"):
        random_sleep()
    
    # 中间页
    print("下载中间页...")
    for i in range(2, last_page):
        downloaded = False  # 标记该页是否有实际下载
        
        # 下载左页
        if download_image(f"{base_url}etwx974SL_{i}_l.jpg", f"page_{i}_left.jpg"):
            downloaded = True
            random_sleep()
            
        # 下载右页
        if download_image(f"{base_url}etwx974SL_{i}_r.jpg", f"page_{i}_right.jpg"):
            downloaded = True
            random_sleep()
            
        if downloaded:
            print(f"完成第 {i}/{last_page} 页的下载")
        else:
            print(f"跳过第 {i}/{last_page} 页 (文件已存在)")
    
    # 末页
    print("下载末页...")
    if download_image(f"{base_url}etwx974SL_{last_page}.jpg", f"page_{last_page}.jpg"):
        random_sleep()
    if download_image(f"{base_url}etwx974SL_{last_page}_l.jpg", f"page_{last_page}_left.jpg"):
        random_sleep()
    if download_image(f"{base_url}etwx974SL_{last_page}_r.jpg", f"page_{last_page}_right.jpg"):
        random_sleep()

if __name__ == "__main__":
    main()
