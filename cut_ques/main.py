# from docx import Document
# from output_ques_json_word2word import extract_questions_word
# from get_coordinates import get_coordinates
# from get_coordinates_new import get_coordinates_part,get_coordinates_sub
# from cut_img import crop_image
# from pdf2img import convert_pdf_to_images
# from api_Alicloud import Sample


# import os
# from pathlib import Path


# # 输入的PDF原文档
# input_pdf_path = r"D:\Coding\Advanced_math\input_PDFs\数学二解析1987.pdf"

# # 提取PDF文件名（不包括扩展名）
# pdf_filename = Path(input_pdf_path).stem

# # 构造其他文件的路径
# base_dir = Path(r"D:\Coding\Advanced_math")
# input_img_path = base_dir / f"output_imgs_of_pages\{pdf_filename}_page_3.jpg"
# input_docx_path = base_dir / f"output_raw_docx\{pdf_filename}_page_3.docx"
# # "D:\\Coding\\Advanced_math\\output_raw_docx\\{image_name}.docx"
# output_docx_path = base_dir / f"output_cut_docx\{pdf_filename}_page_3.docx"
# output_img_path = base_dir / f"output_imgs_of_ques\{pdf_filename}_page_3.jpg"
# output_folder = base_dir / "output_imgs_of_pages"

# # 下面是您的代码逻辑
# # 切割pdf
# convert_pdf_to_images(input_pdf_path, str(base_dir / "output_imgs_of_pages"))

# # 识别图片
# Sample.main(str(input_img_path))

# # 提取题目
# extract_questions_word(str(input_docx_path), str(output_docx_path))

# # 读取题目的坐标信息
# coordinates = get_coordinates_sub(str(input_docx_path))

# # 切割图片
# # print(input_img_path, output_img_path)
# crop_image(str(input_img_path), str(output_folder), coordinates)

# print("Done!")

from pathlib import Path
import os
from docx import Document
from output_ques_json_word2word import extract_questions_word
from get_coordinates import get_coordinates
from get_coordinates_new import get_coordinates_part, get_coordinates_sub
from cut_img import crop_image
from pdf2img import convert_pdf_to_images
from api_Alicloud import Sample

# 基础目录路径
base_dir = Path(r"D:\Coding\Advanced_math")

# 循环处理1988年到2022年的考研数学真题
for year in range(1988, 2024):  # 包括1988年到2023年
    # 构造PDF文件路径
    input_pdf_path = base_dir / f"input_PDFs\{year}年考研数学（三）真题.pdf"
    output_folder = base_dir / "output_imgs_of_pages"
    
    # 创建以年份命名的文件夹
    year_folder = base_dir / f"output_imgs_of_ques\数三\{year}"
    if not year_folder.exists():
        year_folder.mkdir(parents=True, exist_ok=True)
    
    # 提取PDF文件名（不包括扩展名）
    pdf_filename = input_pdf_path.stem
    
    # 切割pdf
    convert_pdf_to_images(str(input_pdf_path), str(output_folder))
    
    for i in range(1, 10):
        input_img_path = base_dir / f"output_imgs_of_pages\{pdf_filename}_page_{i+1}.jpg"
        if not input_img_path.exists():
            break  # 如果图片不存在，跳出循环
        
        input_docx_path = base_dir / f"output_raw_docx\{pdf_filename}_page_{i+1}.docx"
        output_docx_path = base_dir / f"output_cut_docx\{pdf_filename}_page_{i+1}.docx"
        
        # 修改output_img_path，使图片保存到对应年份的文件夹中
        output_img_path = year_folder / f"{pdf_filename}_page_{i+1}.jpg"
    
        # 识别图片
        Sample.main(str(input_img_path))
        
        # 提取题目
        extract_questions_word(str(input_docx_path), str(output_docx_path))
        
        # 读取题目的坐标信息
        coordinates = get_coordinates_sub(str(input_docx_path))
        
        # 切割图片
        crop_image(str(input_img_path), str(output_img_path), coordinates)
        
        print(f"{year}年考研数学真题第{i+1}页处理完成！")

print("所有年份处理完成！")