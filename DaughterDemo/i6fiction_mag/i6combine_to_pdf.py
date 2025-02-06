from PIL import Image
import img2pdf
from pathlib import Path
import re

def natural_sort_key(s):
    """自然排序的key函数"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def get_page_info(filename):
    """从文件名中提取页码和子页码"""
    match = re.search(r'page(\d+)_(\d+)', filename)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None

def create_pdf(input_dir, output_pdf, start_subpage=None, end_subpage=None):
    # 获取所有图片文件
    image_dir = Path(input_dir)
    page_images = {}  # 使用字典存储每页的图片
    
    # 支持的图片格式
    supported_formats = ('.jpg', '.jpeg', '.png', '.webp')
    
    # 收集所有图片
    for img_path in image_dir.glob("*.*"):
        if img_path.suffix.lower() in supported_formats:
            page_num, sub_page = get_page_info(img_path.name)
            if page_num is not None:  # 只处理符合命名规则的文件
                # 检查是否在指定的子页面范围内
                if (start_subpage is None or sub_page >= start_subpage) and \
                   (end_subpage is None or sub_page <= end_subpage):
                    if page_num not in page_images:
                        page_images[page_num] = {}
                    page_images[page_num][sub_page] = str(img_path)
    
    # 按页码和子页码排序
    sorted_images = []
    for page_num in sorted(page_images.keys()):
        sub_pages = page_images[page_num]
        for sub_page in sorted(sub_pages.keys()):
            sorted_images.append(page_images[page_num][sub_page])
    
    print(f"找到 {len(sorted_images)} 个图片文件")
    
    # 转换所有图片为RGB模式的JPG（避免格式兼容问题）
    converted_images = []
    for img_path in sorted_images:
        try:
            with Image.open(img_path) as img:
                if img.mode != 'RGB' or Path(img_path).suffix.lower() != '.jpg':
                    rgb_img = img.convert('RGB')
                    temp_path = str(image_dir / f"temp_{Path(img_path).stem}.jpg")
                    rgb_img.save(temp_path, 'JPEG')
                    converted_images.append(temp_path)
                else:
                    converted_images.append(img_path)
        except Exception as e:
            print(f"处理图片 {img_path} 时出错: {e}")
    
    # 创建PDF
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(converted_images))
        print(f"PDF创建成功: {output_pdf}")
    except Exception as e:
        print(f"创建PDF时出错: {e}")
    
    # 清理临时文件
    for path in converted_images:
        if "temp_" in path:
            try:
                Path(path).unlink()
            except Exception as e:
                print(f"删除临时文件 {path} 时出错: {e}")

if __name__ == "__main__":
    # 配置路径
    input_directory = "/Users/abel/Downloads/magazine_downloads"
    
    # 定义起始和结束页码
    start_page = 0
    end_page = 53
    
    # 生成包含页码信息的输出文件名
    output_filename = f"magazine_page{start_page}-{end_page}.pdf"
    output_pdf = str(output_filename)
    
    # 创建PDF
    create_pdf(
        input_directory, 
        output_pdf,
        start_subpage=start_page,
        end_subpage=end_page
    )

    # create_pdf(
    #     input_directory, 
    #     output_pdf
 
    # )    