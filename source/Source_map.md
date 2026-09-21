# ICA0024 Assessment source map

The review windows below use **HH:MM:SS from the start of the original recording**. They locate the concepts used in each question. Practical questions apply those concepts to the supplied demo code; not every diagnostic conclusion is stated verbatim in the lecture. The answer key links official documentation where precise task behavior matters.

The full transcripts are automated and retain spoken wording, including repetitions and recognition errors. Question wording and technical names were checked against the supplied slide screenshots and demo source files. Administrative discussion and tool-history trivia are excluded from the assessment.

## Lecture 1

Source recording: `Lecture1.mp4`. Timestamped transcript retained with the original course materials. Supporting images: `sources/Lecture1_slides_1.png` and `sources/Lecture1_slides_2.png`.

| Question | Concept and review window | Demo source where relevant |
|---|---|---|
| L1 Q1 | Infrastructure pillars, 00:42:30–00:49:30 | — |
| L1 Q2 | Declarative state, 02:06:00–02:13:30 | — |
| L1 Q3 | Idempotence, 01:59:00–02:08:30 | — |
| L1 Q4 | Cloud abstraction and responsibility, 00:59:30–01:02:00 | — |
| L1 Q5 | Codified change and traceability, 00:56:00–00:59:30; 02:17:00–02:21:00 | — |
| L1 Q6 | Configuration drift, 01:38:00–01:40:00; 01:45:00–01:47:00 | — |
| L1 Q7 | Immutable replacement, 01:40:00–01:45:00; 01:47:00–01:50:30 | — |
| L1 Q8 | Terraform and Ansible handoff, 02:39:00–02:42:30; 02:52:30–02:56:30 | [main.tf](https://github.com/Infra-as-code-ICA0024-TalTech/demo-01/blob/main/main.tf), [playbook.yml](https://github.com/Infra-as-code-ICA0024-TalTech/demo-01/blob/main/playbook.yml) |
| L1 Q9 | Resource dependencies and inventory changes, 02:42:00–02:48:30 | [main.tf](https://github.com/Infra-as-code-ICA0024-TalTech/demo-01/blob/main/main.tf): `aws_instance.server`, `local_file.ansible_inventory` |
| L1 Q10 | Repeated Ansible runs and changing managed content, 02:53:00–02:58:30 | [playbook.yml](https://github.com/Infra-as-code-ICA0024-TalTech/demo-01/blob/main/playbook.yml): package, copy, and systemd tasks |

## Lecture 2

Source recording: `Lecture2.mp4`. Timestamped transcript retained with the original course materials. Supporting images: `sources/Lecture2_slides_1.png` and `sources/Lecture2_slides_2.png`.

| Question | Concept and review window | Demo source where relevant |
|---|---|---|
| L2 Q1 | Images as machine starting points, 00:25:00–00:27:00; 00:51:00–00:58:30 | — |
| L2 Q2 | Packer and custom image artifacts, 00:50:00–00:58:30; 01:20:00–01:26:00 | [Packer template](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/devops-ubuntu-26.04-aws.pkr.hcl) |
| L2 Q3 | The manually maintained golden-image anti-pattern, 00:42:45–00:45:45 | — |
| L2 Q4 | Region, architecture, and image variants, 00:30:30–00:34:00 | — |
| L2 Q5 | Stock and custom baselines, 00:33:00–00:42:00 | — |
| L2 Q6 | Initial image state, later configuration, and cloud-init, 01:03:30–01:07:30; 01:13:00–01:19:30 | [Test VM user_data](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/tests/test.tf) |
| L2 Q7 | Containers, VMs, and shared kernels, 01:51:00–02:07:00 | — |
| L2 Q8 | Image hierarchy and shared baseline, 00:45:45–00:50:00 | — |
| L2 Q9 | Build sources and provisioning, 01:20:00–01:36:30 | [Packer template](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/devops-ubuntu-26.04-aws.pkr.hcl), [cloud-init.sh](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/scripts/ubuntu/cloud-init.sh), [cleanup.sh](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/scripts/ubuntu/cleanup.sh) |
| L2 Q10 | Rebuildability, replacing machines, and artifact validation, 00:39:00–00:42:00; 01:07:00–01:12:30; 02:08:00–02:15:30 | [Packer source_ami_filter](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/devops-ubuntu-26.04-aws.pkr.hcl), [base.sh](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/scripts/ubuntu/base.sh), [test cycle](https://github.com/Infra-as-code-ICA0024-TalTech/demo-02/blob/main/tests/run-test-cycle.sh) |

For L2 Q10, controlling image and package versions is a reasoned application of rebuildability to the supplied code. Do not require the optional term “repository snapshot” if the student explains an equivalent way to control changing inputs.

## Lecture 3

Source recording: `Lecture3.mp4`. Timestamped transcript retained with the original course materials. Supporting image: `sources/Lecture3_slides.png`.

| Question | Concept and review window | Demo source where relevant |
|---|---|---|
| L3 Q1 | Inventory and grouping, 00:16:30–00:18:30; 01:37:30–01:40:30 | [Generated fleet inventory](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/infra/fleet.yml) |
| L3 Q2 | Partial state management, 00:23:30–00:30:30; 00:50:00–00:52:30; 01:25:30–01:29:30 | — |
| L3 Q3 | Tasks, playbooks, and reusable roles, 00:58:00–01:03:00; 01:15:00–01:17:30 | [Role organization](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/provision.yml) |
| L3 Q4 | Defaults, group variables, play variables, and extra variables, 02:05:00–02:14:00 | Simplified scalar version of the recorded `app.port` example; precedence reference in the key |
| L3 Q5 | Applying roles to groups, 01:01:00–01:03:00; 01:59:00–02:04:00 | [provision.yml](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/provision.yml), [inventory generation](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/infra/fleet.yml) |
| L3 Q6 | Desired service state and operational procedures, 00:27:30–00:29:30; 01:38:30–01:40:00; 02:39:00–02:40:00 | [Web service tasks](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/roles/web/tasks/main.yml), [restart.yml](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/restart.yml) |
| L3 Q7 | Registered results and derived values, 01:47:30–01:50:00 | [fleet.yml](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/infra/fleet.yml): `register: web_sg` and instance task |
| L3 Q8 | Provisioning and verifying useful behavior, 01:29:30–01:30:30; 01:45:30–01:59:30; 02:36:30–02:41:30 | [Workflow README](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/README.md), [test.yml](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/test.yml) |
| L3 Q9 | Handlers and managed template contents, 00:46:00–00:46:45; 02:30:30–02:34:30 | [Web template tasks](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/roles/web/tasks/main.yml), [handlers](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/roles/web/handlers/main.yml); exact notification timing is linked in the key |
| L3 Q10 | The limits of existence-only state checks, 00:47:00–00:49:30; 01:25:30–01:29:30 | [Web dependency task](https://github.com/Infra-as-code-ICA0024-TalTech/demo-03a/blob/main/provisioning/roles/web/tasks/main.yml): `Install Node.js dependencies`; students diagnose the printed code |

L3 Q10 deliberately distinguishes a guard condition from the application's actual state. Grade the reasoning applied to the code, not familiarity with a particular replacement npm command.

## Source provenance

The demo source files were inspected on **20 September 2026**. Demo links point to the private teaching repositories and require appropriate access; the `main` branch may change. The printed excerpts in the student questionnaire define the code being assessed.

Recordings, automated transcripts, original source hashes, and supporting screenshots remain in the instructor's original course materials and are not included in this repository.
