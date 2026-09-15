# my_own_role

Role использует собственный Ansible-модуль `my_own_module` из Collection `my_own_namespace.yandex_cloud_elk`.

Модуль создаёт текстовый файл с заданным содержимым.

## Role Variables

Значения по умолчанию находятся в `defaults/main.yml`:

```yaml
my_own_module_path: /tmp/role_module_test.txt
my_own_module_content: "File created from Ansible role"
```

`my_own_module_path` определяет путь к создаваемому файлу.

`my_own_module_content` определяет содержимое файла.

Обе переменные при необходимости можно переопределить в playbook.

## Example Playbook

```yaml
---
- name: Test my own role
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_own_role
```
