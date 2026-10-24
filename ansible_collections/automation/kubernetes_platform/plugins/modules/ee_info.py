#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2026, Wessel Hulleman
# MIT License (see LICENSE in the repository root)

from __future__ import annotations

DOCUMENTATION = r"""
---
module: ee_info
short_description: Report the Python runtime and package versions a task runs with
description:
  - Returns the Python version and executable, the ansible-core version and the installed versions of
    the given Python packages, as seen by the module itself.
  - Run it inside an execution environment to see exactly which runtime the automation uses.
options:
  packages:
    description: Python distribution names to report the installed version of.
    type: list
    elements: str
    default: [kubernetes]
author:
  - Wessel Hulleman (@wsslhllmn)
"""

EXAMPLES = r"""
- name: Show which runtime this playbook runs with
  automation.kubernetes_platform.ee_info:
    packages:
      - kubernetes
      - requests
  register: ee
"""

RETURN = r"""
python_version:
  description: Python version the module ran with.
  returned: always
  type: str
  sample: "3.11.9"
python_executable:
  description: Path of the Python interpreter the module ran with.
  returned: always
  type: str
  sample: /usr/bin/python3.11
ansible_core_version:
  description: Version of ansible-core.
  returned: always
  type: str
  sample: "2.16.14"
packages:
  description: Installed version per requested package, or null when it is not installed.
  returned: always
  type: dict
  sample: {"kubernetes": "31.0.0"}
"""

import platform
import sys
from importlib import metadata

from ansible.module_utils.ansible_release import __version__ as ansible_core_version
from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(packages=dict(type="list", elements="str", default=["kubernetes"])),
        supports_check_mode=True,
    )

    packages = {}
    for name in module.params["packages"]:
        try:
            packages[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            packages[name] = None

    module.exit_json(
        changed=False,
        python_version=platform.python_version(),
        python_executable=sys.executable,
        ansible_core_version=ansible_core_version,
        packages=packages,
    )


if __name__ == "__main__":
    main()
