import datetime

with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

status_message = "hapi hapi"

updated_content = readme_content.replace("{{status}}", status_message)

with open('README.md', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("README.md has been updated.")
