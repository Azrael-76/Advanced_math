import os
import sys
from typing import List
from docx import Document  # 导入Document用于操作docx文档

from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> ocr_api20210707Client:
        config = open_api_models.Config(
            access_key_id="LTAI5tMXTEwFZPAFSPAg9d5e",
            access_key_secret="278wFSI2WHiFJMWvwuq1iPdFzV1u4N"
        )
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def main(image_path: str) -> None:  # 修改此处，直接接收图片路径参数
        client = Sample.create_client()
        # 使用传入的image_path，而不是硬编码的路径
        body_stream = StreamClient.read_from_file_path(image_path)
        recognize_edu_paper_structed_request = ocr_api_20210707_models.RecognizeEduPaperStructedRequest(
            url='',
            subject='default',
            need_rotate=False,
            body=body_stream
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 调用API并获取返回值
            response = client.recognize_edu_paper_structed_with_options(recognize_edu_paper_structed_request, runtime)
            # 打印API的返回值
            # print("API Response:", response)
            
            # 创建一个新的Word文档
            doc = Document()
            # 将API的返回值添加到文档中
            doc.add_paragraph(str(response))
            # 根据输入的图片名字来命名docx文档
            image_name = os.path.splitext(os.path.basename(image_path))[0]  # 从路径中提取文件名（不含扩展名）
            docx_path = f"D:\\Coding\\Advanced_math\\output_raw_docx\\{image_name}.docx"
            doc.save(docx_path)  # 保存文档
            # print(f"Document saved to {docx_path}")
            
        except Exception as error:
            # 错误处理
            print("Error occurred:", error)
            if hasattr(error, 'data') and error.data:
                print("Recommendation:", error.data.get("Recommend"))

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
    print("*****************************************************************************")
    print("完成调用API")  # 输出"完成调用API！"