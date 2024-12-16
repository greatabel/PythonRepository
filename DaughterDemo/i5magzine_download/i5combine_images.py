from PIL import Image
import img2pdf
from pathlib import Path
import re

def natural_sort_key(s):
    """自然排序的key函数"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def get_page_number(filename):
    """从文件名中提取页码"""
    match = re.search(r'page_(\d+)', filename)
    return int(match.group(1)) if match else 0

def create_pdf(input_dir, output_pdf, start_page=None, end_page=None):
    # 获取所有jpg文件
    image_dir = Path(input_dir)
    page_images = {}  # 使用字典存储每页的图片
    
    # 收集所有图片并按页码和类型组织
    for img_path in image_dir.glob("*.jpg"):
        page_num = get_page_number(img_path.name)
        if page_num:  # 只处理有页码的文件
            # 检查是否在指定范围内
            if (start_page is None or page_num >= start_page) and \
               (end_page is None or page_num <= end_page):
                if page_num not in page_images:
                    page_images[page_num] = {'single': None, 'left': None, 'right': None}
                
                if '_left' in img_path.name:
                    page_images[page_num]['left'] = str(img_path)
                elif '_right' in img_path.name:
                    page_images[page_num]['right'] = str(img_path)
                else:  # 处理单页情况（如封面）
                    page_images[page_num]['single'] = str(img_path)
    
    # 按页码排序并确保正确顺序（single/left/right）
    sorted_images = []
    for page_num in sorted(page_images.keys()):
        if page_images[page_num]['single']:
            sorted_images.append(page_images[page_num]['single'])
        else:
            if page_images[page_num]['left']:
                sorted_images.append(page_images[page_num]['left'])
            if page_images[page_num]['right']:
                sorted_images.append(page_images[page_num]['right'])
    
    print(f"找到 {len(sorted_images)} 个图片文件")
    
    # 转换所有图片为RGB模式（避免RGBA问题）
    converted_images = []
    for img_path in sorted_images:
        try:
            with Image.open(img_path) as img:
                if img.mode != 'RGB':
                    rgb_img = img.convert('RGB')
                    temp_path = str(image_dir / f"temp_{Path(img_path).name}")
                    rgb_img.save(temp_path)
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
        if path.startswith(str(image_dir / "temp_")):
            Path(path).unlink()

if __name__ == "__main__":
    # 配置路径
    input_directory = "/Users/abel/AbelProject/PythonRepository/DaughterDemo/i5magzine_download/images"
    parent_directory = str(Path(input_directory).parent)  # 获取上级目录
    
    # 示例：创建不同范围的PDF
    # 完整版本
    # create_pdf(
    #     input_directory, 
    #     f"{parent_directory}/magazine_full.pdf"
    # )
    
    # 只处理1-10页
    create_pdf(
        input_directory, 
        f"{parent_directory}/magazine_16_to_25.pdf",
        start_page=16,
        end_page=25
    )
    
    # # 只处理20-25页
    # create_pdf(
    #     input_directory, 
    #     f"{parent_directory}/magazine_20_to_25.pdf",
    #     start_page=20,
    #     end_page=25
    # )
