import re
from docx import Document

def get_coordinates(input_docx_path):
    # 从word文档读取成一个字符串，从一整个字符串中提取题目的x和y坐标信息
    doc = Document(input_docx_path)
    extracted_data = []
    current_question = []
    coordinates = []
    # 读取成字符串
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text
    # print(text)
    #"text": "求微分方程;$$y ^ { m } + 6 y ' ' + \\left( 9 + a ^ { 2 } \\right) y ' = 1$$1的通解,其中常数a>0.",            "pos_list": [              [                {                  "x": 44,                  "y": 73                },                {                  "x": 374,                  "y": 73                },                {                  "x": 374,                  "y": 90                },                {                  "x": 44,                  "y": 90                }              ]            ],            "type": 15,            "num_choices": 0,            "table_list": []          }            "text": "(1)设常数k>0,则级数$$\\sum _ { n = 1 } ^ { \\infty } { \\left( - 1 \\right) ^ { n } } \\frac { k + n } { n ^ { 2 } }$$( ).(A)发散 (B)绝对收敛(C)条件收敛 (D)收敛或发散与k的取值有关",            "pos_list": [              [                {                  "x": 30,                  "y": 232                },                {                  "x": 433,                  "y": 232                },                {                  "x": 433,                  "y": 297                },                {                  "x": 30,                  "y": 297                }              ]            ],            "type": 0,            "num_choices": 0,            "table_list": []          }            "text": "(2)设$$I = t \\int _ { 0 } ^ { \\frac { 1 } { \\frac { 1 } { 2 } } } { f \\left( f x \\right) d x } ,$$,其中f(x)为连续数,$$s _ { 2 } > 0 , t > 0 ,$$,则I的值( ).(A)依赖于s,t (B)依赖于,t,x(C)依赖于t,x,不依赖于s (D)依赖于s,不依赖于:",            "pos_list": [              [                {                  "x": 31,                  "y": 300                },                {                  "x": 426,                  "y": 300                },                {                  "x": 426,                  "y": 366                },                {                  "x": 31,                  "y": 366                }              ]            ],            "type": 0,            "num_choices": 0,            "table_list": []          }            "text": "(3)设$$\\lim _ { x \\to { a } } \\frac { f \\left( x \\right) - f \\left( a \\right) } { \\left( x - a \\right) ^ { 2 } } = - 1 ,$$则在点x=a处( ).(A)f(x)可导且f'(a)≠0 (B)f(x)取得极大值(C)f(x)取得极小值 (D)f(x)的导数不存在",            "pos_list": [              [                {                  "x": 31,                  "y": 367                },                {                  "x": 388,                  "y": 367                },                {                  "x": 388,                  "y": 433                },                {                  "x": 31,                  "y": 433                }              ]            ],            "type": 0,            "num_choices": 0,            "table_list": []          }            "text": "(4)设A为阶矩阵,且|A|=a≠0,A\"是A的伴随矩阵,则|A⋅|=( ).(A)a $$\\left( B \\right) \\frac { 1 } { a }$$ $$\\left( C \\right) a ^ { n - 1 }$$ $$\\left( D \\right) a ^ { n }$$",            "pos_list": [              [                {                  "x": 31,                  "y": 436                },                {                  "x": 422,                  "y": 436                },                {                  "x": 422,                  "y": 482                },                {                  "x": 31,                  "y": 482                }              ]            ],            "type": 0,            "num_choices": 0,            "table_list": []          }
    # 查找x和y坐标信息
    pattern = re.compile(r'"pos_list": \[\s*\[\s*{.*?"x": (\d+),\s*"y": (\d+).*?},\s*{.*?"x": (\d+),\s*"y": (\d+).*?},\s*{.*?"x": (\d+),\s*"y": (\d+).*?},\s*{.*?"x": (\d+),\s*"y": (\d+).*?}\s*\]')
    matches = pattern.findall(text)
    # 提取坐标信息
    for match in matches:
        coordinates.append([{"x": int(match[0]), "y": int(match[1])}, {"x": int(match[2]), "y": int(match[3])}, {"x": int(match[4]), "y": int(match[5])}, {"x": int(match[6]), "y": int(match[7])}])


    print("*****************************************************************************")
    print(coordinates)
    print("完成提取坐标")  
    return coordinates
    


