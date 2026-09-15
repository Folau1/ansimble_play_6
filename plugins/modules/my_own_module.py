#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os

from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file with specified content

version_added: "1.0.0"

description:
    - Creates a text file at the specified path.
    - Writes specified content into the file.
    - Changes the file only if it does not exist or its content differs.

options:
    path:
        description:
            - Path to the text file.
        required: true
        type: str
    content:
        description:
            - Content that should be written to the file.
        required: true
        type: str

author:
    - Alexander
'''

EXAMPLES = r'''
- name: Create test file
  my_own_module:
    path: /tmp/test_file.txt
    content: "Hello from my own Ansible module"
'''

RETURN = r'''
path:
    description: Path to the file.
    returned: always
    type: str

message:
    description: Result of module execution.
    returned: always
    type: str
'''


def run_module():

    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    changed = False

    try:
        current_content = None

        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                current_content = file.read()

        if current_content != content:
            changed = True

            if not module.check_mode:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)

        if changed:
            message = 'File created or content changed'
        else:
            message = 'File already has required content'

        module.exit_json(
            changed=changed,
            path=path,
            message=message
        )

    except Exception as error:
        module.fail_json(
            msg='Failed to create file: {0}'.format(error)
        )


def main():
    run_module()


if __name__ == '__main__':
    main()
