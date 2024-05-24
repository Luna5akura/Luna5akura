from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')

base_url = "https://wakatime.com/share/@974cd1bf-f67e-44b6-b583-0472a71ce20a/22838a5c-998d-4570-afa4-0858b9d26a45.svg"

markdown_content = f"""
# How does pi attract others? -- Picharm!

### Status: hapi hapi

![Light theme image]({base_url}?date={current_date})
![Dark theme image]({base_url}?date={current_date})
"""

# 将内容写入文件
with open('README.md', 'w') as file:
    file.write(markdown_content)

print("Markdown file has been updated with the current date.")
