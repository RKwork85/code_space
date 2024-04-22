
import json

# 读取JSON文件
with open('self_cognition_gmAI.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 写入JSONL文件
with open('output.jsonl', 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')