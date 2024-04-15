from pathlib import Path
from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder):
    """
    将PDF文件的每一页转换为图片，并以PDF文件名作为图片文件名的一部分。
    
    :param pdf_path: PDF文件的路径。
    :param output_folder: 输出图片的文件夹路径。
    """
    # 使用Path对象从pdf_path中提取PDF文件的名称（不包括扩展名）
    pdf_name = Path(pdf_path).stem

    # 使用convert_from_path函数将PDF转换为图片列表
    images = convert_from_path(pdf_path)
    
    # 遍历图片列表，并将每一页保存为JPEG格式的文件
    for i, image in enumerate(images):
        # 构造输出图片的路径，包含PDF文件名和页码
        image_path = f'{output_folder}/{pdf_name}_page_{i+1}.jpg'
        image.save(image_path, 'JPEG')
        print(f'已保存：{image_path}')

# 示例使用
# pdf_path = r"D:\Coding\Advanced_math\input_PDFs\数学二解析1987.pdf"  # PDF文件路径
# output_folder = r"D:\Coding\Advanced_math\output_imgs_of_pages" # 输出图片的文件夹路径
# convert_pdf_to_images(pdf_path, output_folder)
print("*****************************************************************************")
print("完成pdf转图片！")  # 输出"完成pdf转图片！"
