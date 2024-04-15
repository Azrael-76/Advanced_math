from PIL import Image

def crop_image(input_image_path, output_image_path, coordinates):
    """
    根据给定的坐标信息从原始图片中切割出题目区域并保存到本地目录。

    参数:
    input_image_path: 输入的原始图片路径。
    output_image_path: 输出的切割后图片路径。
    coordinates: [[{'x': 44, 'y': 73}, {'x': 374, 'y': 73}, {'x': 374, 'y': 90}, {'x': 44, 'y': 90}], [{'x': 30, 'y': 232}, {'x': 433, 'y': 232}, {'x': 433, 'y': 297}, {'x': 30, 'y': 297}], [{'x': 31, 'y': 300}, {'x': 426, 'y': 300}, {'x': 426, 'y': 366}, {'x': 31, 'y': 366}], [{'x': 31, 'y': 367}, {'x': 388, 'y': 367}, {'x': 388, 'y': 433}, {'x': 31, 'y': 433}], [{'x': 31, 'y': 436}, {'x': 422, 'y': 436}, {'x': 422, 'y': 482}, {'x': 31, 'y': 482}]]
    是一个列表，其中每个元素是一个包含四个端点坐标的字典，代表一个题目的四个端点坐标。每4个坐标代表一个题目的四个端点坐标。所以要每次取4个坐标，然后切割出题目区域。
    并保存到本地目录。可以采取依次命名的方式，如cut1_1, cut1_2, cut1_3...
    """

    # 打开原始图片
    image = Image.open(input_image_path)
    # 依次切割出题目区域
    for i, coor in enumerate(coordinates):
        # 切割出题目区域
        cropped_image = image.crop((coor[0]['x'], coor[0]['y'], coor[2]['x'], coor[2]['y']))
        # 保存到本地目录
        cropped_image.save(f"{output_image_path[:-4]}_{i+1}.jpg") # output_image_path[:-4]是为了去掉.jpg后缀
        print(f"Saved {output_image_path[:-4]}_{i+1}.jpg")
    # 关闭原始图片
    image.close()
    print("*****************************************************************************")
    print("完成切割题目")  

# 示例用法
if __name__ == '__main__':
    input_image_path = r"D:\Coding\Advanced_math\output_imgs_of_pages\数学二解析1987_page_2.jpg"
    output_image_path = r"D:\Coding\Advanced_math\output_imgs_of_ques\数学二解析1987_page_2.jpg"
    coordinates = [[{'x': 44, 'y': 73}, {'x': 374, 'y': 73}, {'x': 374, 'y': 90}, {'x': 44, 'y': 90}], [{'x': 30, 'y': 232}, {'x': 433, 'y': 232}, {'x': 433, 'y': 297}, {'x': 30, 'y': 297}], [{'x': 31, 'y': 300}, {'x': 426, 'y': 300}, {'x': 426, 'y': 366}, {'x': 31, 'y': 366}], [{'x': 31, 'y': 367}, {'x': 388, 'y': 367}, {'x': 388, 'y': 433}, {'x': 31, 'y': 433}], [{'x': 31, 'y': 436}, {'x': 422, 'y': 436}, {'x': 422, 'y': 482}, {'x': 31, 'y': 482}]]
    crop_image(input_image_path, output_image_path, coordinates)
    print("Done!")



