# automation.kubernetes_platform

Example collection for the blog post
[Packaging Ansible Collections as Ansible Execution Environments](https://hulleman.io/blog/ansible-execution-environments/).

The point of this collection is how it is packaged, not what it automates. The roles `cluster`, `namespace`
and `hardening` are empty placeholders; in a real collection they hold the tasks for those objects.

| Content | What it does |
|---|---|
| `roles/cluster`, `roles/namespace`, `roles/hardening` | Nothing yet: placeholders that show the structure |
| `plugins/modules/ee_info` | Reports the Python, `ansible-core` and package versions a task actually runs with |

Python dependencies: none of its own. The `kubernetes` client comes from `kubernetes.core`, which declares it
itself; ansible-builder picks it up from there.
