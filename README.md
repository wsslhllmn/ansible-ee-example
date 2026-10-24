# ansible-ee-example

A working example for the blog post
[Packaging Ansible Collections as Ansible Execution Environments](https://hulleman.io/blog/ansible-execution-environments/):
one Ansible Collection, packaged as its own execution environment.

## Try it

You need [ansible-builder](https://docs.ansible.com/projects/builder/en/latest/),
[ansible-navigator](https://docs.ansible.com/projects/navigator/) and Podman (or Docker).

```bash
git clone https://github.com/wsslhllmn/ansible-ee-example.git
cd ansible-ee-example
ansible-builder build -f execution-environment.yml -t kubernetes-ee:dev
ansible-navigator run playbooks/ee_info.yml \
  --eei kubernetes-ee:dev --mode stdout
```

`ee_info` prints which Python, `ansible-core` and `kubernetes` client the playbook ran with, inside the image.

`playbooks/deploy_cluster.yml` runs the (empty) roles of the collection inside the image. The roles are
placeholders on purpose: this repo is about the execution environment, not about the automation inside it.

## What is where

```
ansible-ee-example/
├── ansible_collections/automation/kubernetes_platform/   # the collection, in the default path for ansible-galaxy
│   ├── galaxy.yml                                       # version, and the dependency on kubernetes.core
│   ├── plugins/modules/ee_info.py
│   ├── roles/{cluster,namespace,hardening}/            # empty placeholders
│   ├── requirements.txt                                 # own Python dependencies (none)
│   └── bindep.txt                                       # own system dependencies (none)
├── playbooks/                                           # copied to /playbooks in the image
├── execution-environment.yml                            # how the image is built
└── .gitlab-ci.yml                                       # the pipeline from the blog post
```

Differences from the blog post:

- **Base image:** the post uses an EE base image from a private registry; this repo uses the public, RHEL-based
  `registry.access.redhat.com/ubi9/ubi`, so anyone can build it. Replace it with your own base image.
- **Roles and dependencies:** the roles are empty placeholders and the collection only depends on
  `kubernetes.core`; the post shows a fuller `galaxy.yml`.

## Versioning

The version in `galaxy.yml` is the only version number. Tag a release with that same version (for example
`1.4.0`); the GitLab pipeline then builds the image and publishes the collection with that number.

## License

MIT
