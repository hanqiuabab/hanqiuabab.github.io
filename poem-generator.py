import requests
from datetime import datetime
import os

# 获取诗词
response = requests.get("https://v1.jinrishici.com/all.json")
data = response.json()

title = data.get("origin", "无题")
author = data.get("author", "佚名")
content = data.get("content", "").replace("，", "，\n").replace("。", "。\n")  # 自动换行

# 日期和文件路径
date_str = datetime.now().strftime('%Y-%m-%d')
filename = f"content/posts/{date_str}.md"

# Front Matter for Hugo PaperMod
front_matter = f"""---
title: "《{title}》 - {author}"
date: {date_str}
tags: ["每日一诗", "自动发布"]
categories: ["诗词"]
draft: false
---

{content}
"""

# 确保路径存在
os.makedirs("content/posts", exist_ok=True)

# 写入文件
with open(filename, "w", encoding="utf-8") as f:
    f.write(front_matter)