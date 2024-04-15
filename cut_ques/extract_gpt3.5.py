# coding=utf-8
import json

def extract_question_info(json_data):
    try:
        data = json.loads(json_data)
        if "body" in data and "Data" in data["body"]:
            body_data = json.loads(data["body"]["Data"])
            if "doc_layout" in body_data:
                for item in body_data["doc_layout"]:
                    if "layout_type" in item and item["layout_type"] == "text":
                        if "pos" in item:
                            for pos_item in item["pos"]:
                                if pos_item["x"] == 691 and pos_item["y"] == 1002:  # Assuming this is the question position
                                    print("题目内容:", item)
                                    # Extract other relevant information here
                                    break
        else:
            print("JSON 数据中缺少题目信息")
    except json.JSONDecodeError as e:
        print("JSON 解析出错:", e)

# 这里是你提供的 JSON 数据
json_data = '''
{
    "headers": {
        "date": "Sat, 13 Apr 2024 09:35:38 GMT",
        "content-type": "application/json;charset=utf-8",
        "content-length": "23412",
        "connection": "keep-alive",
        "keep-alive": "timeout=25",
        "vary": "Accept-Encoding",
        "access-control-allow-origin": "*",
        "access-control-expose-headers": "*",
        "x-acs-request-id": "31367459-C195-5F51-BD98-167785546837",
        "x-acs-trace-id": "e970153b9a3ccc9fbf128567e036290b",
        "etag": "2hydMMiotGuSKjaZ7zvmi1Q3"
    },
    "statusCode": 200,
    "body": {
        "Data": "{\"algo_version\":\"\",\"doc_layout\":[{\"layout_type\":\"text\",\"pos\":[{\"x\":107,\"y\":960},{\"x\":107,\"y\":1042},{\"x\":1278,\"y\":1042},{\"x\":1278,\"y\":960}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":106,\"y\":655},{\"x\":106,\"y\":733},{\"x\":1270,\"y\":733},{\"x\":1270,\"y\":655}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":108,\"y\":758},{\"x\":108,\"y\":795},{\"x\":736,\"y\":795},{\"x\":736,\"y\":758}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":105,\"y\":585},{\"x\":105,\"y\":620},{\"x\":746,\"y\":620},{\"x\":746,\"y\":585}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":556,\"y\":346},{\"x\":556,\"y\":392},{\"x\":817,\"y\":392},{\"x\":817,\"y\":346}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":573,\"y\":448},{\"x\":573,\"y\":485},{\"x\":805,\"y\":485},{\"x\":805,\"y\":448}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":108,\"y\":846},{\"x\":108,\"y\":908},{\"x\":1277,\"y\":908},{\"x\":1277,\"y\":845}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":107,\"y\":802},{\"x\":107,\"y\":839},{\"x\":1270,\"y\":839},{\"x\":1270,\"y\":802}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":275,\"y\":229},{\"x\":275,\"y\":288},{\"x\":1108,\"y\":288},{\"x\":1108,\"y\":229}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":152,\"y\":1562},{\"x\":152,\"y\":1678},{\"x\":1241,\"y\":1678},{\"x\":1241,\"y\":1562}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":148,\"y\":1096},{\"x\":148,\"y\":1167},{\"x\":903,\"y\":1167},{\"x\":903,\"y\":1096}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":147,\"y\":1374},{\"x\":147,\"y\":1412},{\"x\":1240,\"y\":1412},{\"x\":1240,\"y\":1374}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":108,\"y\":1315},{\"x\":108,\"y\":1345},{\"x\":354,\"y\":1345},{\"x\":354,\"y\":1315}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":147,\"y\":1215},{\"x\":147,\"y\":1257},{\"x\":678,\"y\":1257},{\"x\":678,\"y\":1215}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":258,\"y\":176},{\"x\":258,\"y\":229},{\"x\":1108,\"y\":229},{\"x\":1108,\"y\":176}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":152,\"y\":1704},{\"x\":152,\"y\":1810},{\"x\":1240,\"y\":1810},{\"x\":1240,\"y\":1704}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":107,\"y\":1105},{\"x\":107,\"y\":1146},{\"x\":1270,\"y\":1146},{\"x\":1270,\"y\":1105}]},{\"layout_type\":\"text\",\"pos\":[{\"x\":107,\"y\":941},{\"x\":107,\"y\":986},{\"x\":1270,\"y\":986},{\"x\":1270,\"y\":941}]}]}",
        "ContentType": "application/json"
    }
}
'''

# 提取题目信息
extract_question_info(json_data)
