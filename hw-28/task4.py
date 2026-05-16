import os
import json
from jinja2 import Template

# Определение текущей папки скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Читаем список пользователей из файла (превращаем строки в словари Python)
users = []
users_file_path = os.path.join(script_dir, "users.txt")

with open(users_file_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():  # Пропускаем пустые строки
            user_dict = json.loads(line.strip())  # Превращаем текст в словарь
            users.append(user_dict)

# 2. Читаем файл HTML-шаблона
template_path = os.path.join(script_dir, "template.html")
with open(template_path, "r", encoding="utf-8") as f:
    html_template = f.read()

# 3. Рендерим шаблон с помощью Jinja
template = Template(html_template)
rendered_html = template.render(users_list=users)

# 4. Выводим готовый HTML-код на экран
print(rendered_html)
