# ICA0024 Infrastructure as Code

## Understanding check for Lectures 1 to 3

**Name:** ____________________  **Date:** ____________________

Answer all 30 questions. Each lecture is worth **20 marks**, for **60 marks** in total. Suggested time: **75–90 minutes**, or 25–30 minutes per lecture.

For multiple-choice questions, select one answer. For short answers, use two to four sentences unless asked otherwise. For practical scenarios, explain your reasoning; code or pseudocode is welcome where requested. Write your answers on a separate sheet or in a digital document. The code excerpts contain everything needed to answer the scenarios. You do not need to deploy any cloud resources.

## Lecture 1 Infrastructure as Code concepts

### L1 Q1 Infrastructure pillars — 1 mark

Which set contains the three infrastructure pillars introduced in the lecture?

- A. Git, Terraform, and Ansible
- B. Compute, storage, and network
- C. Development, testing, and production
- D. Applications, users, and source code

### L1 Q2 Declarative configuration — 1 mark

Which statement best describes a declarative infrastructure definition?

- A. It records every command an administrator previously executed.
- B. It specifies the exact order of all API calls that a tool must make.
- C. It describes the desired state, while a tool works out how to reach it.
- D. It guarantees that every operation can run in parallel.

### L1 Q3 Idempotence — 1 mark

An automation run has successfully reached the desired state. Its inputs and the relevant external state then remain unchanged. What should a second idempotent run do?

- A. Leave the managed state unchanged because it already satisfies the declaration.
- B. Recreate all resources to prove they can be recreated.
- C. Skip checking the current state and report success.
- D. Add another copy of each declared resource.

### L1 Q4 Cloud service models — 1 mark

A team moves from managing virtual machines under IaaS to a managed application platform under PaaS. Which responsibility would typically move towards the provider?

- A. Deciding the application's business requirements
- B. Maintaining the team's application source code
- C. Choosing which application features to release
- D. Maintaining more of the underlying operating system and runtime platform

### L1 Q5 Why keep infrastructure definitions in Git — 2 marks

Give two benefits of version-controlling infrastructure definitions beyond simply having a backup copy. Explain how each benefit helps a team deliver changes reliably.

### L1 Q6 Configuration drift — 2 marks

Two servers were created from the same definition. An administrator later changes a setting manually on only one server. Explain what configuration drift means in this situation and describe one way to detect or reconcile it.

### L1 Q7 Mutable and immutable infrastructure — 2 marks

A server needs a new operating-system configuration. Contrast an in-place mutable update with an immutable replacement. Explain what must happen to persistent application data when using the replacement approach.

### L1 Q8 Tool responsibilities in demo 01 — 2 marks

In `demo-01`, `main.tf` creates an EC2 instance and writes an Ansible inventory; `playbook.yml` installs and configures Nginx. Explain the distinct responsibilities of Terraform and Ansible in this workflow.

### L1 Q9 Dependencies and generated inventory — 4 marks

Consider these excerpts from `demo-01/main.tf`:

```hcl
# Within aws_instance.server
key_name               = aws_key_pair.main_key.key_name
vpc_security_group_ids = [aws_security_group.main_security_group.id]
```

```yaml
# Within the Terraform-generated inventory template
ansible_host: ${aws_instance.server.public_ip}
```

1. Identify the two resources that the instance references and explain what those references tell Terraform about dependency ordering. **(2 marks)**
2. Explain why generating `ansible_host` from the instance output is more reliable than copying an IP address into a separate inventory by hand. Include what must happen to the inventory when a replacement instance receives a new public IP. **(2 marks)**

### L1 Q10 Predicting a repeated run — 4 marks

The following is a shortened version of tasks in `demo-01/playbook.yml`:

```yaml
- name: Install nginx
  apt:
    name: nginx
    state: present

- name: Create custom index.html
  copy:
    content: "Course homepage\n"
    dest: /var/www/html/index.html

- name: Start and enable nginx
  systemd:
    name: nginx
    state: started
    enabled: yes
```

Assume the first run succeeds and all relevant inputs remain unchanged.

1. Predict the effect of a second run on the package, file, and service. Explain why this illustrates idempotence. **(2 marks)**
2. Someone then manually changes the contents of `index.html`. What should the next run do, and why? **(2 marks)**

## Lecture 2 Images and machine initialization

### L2 Q1 Image and running machine — 1 mark

What is the relationship between a machine image and a virtual machine?

- A. The image is the live machine's current CPU and memory usage.
- B. One image can be used to initialize multiple VM instances, which can later develop different state.
- C. Every image can initialize only one VM.
- D. Launching a VM automatically updates the source image whenever the VM changes.

### L2 Q2 Packer output — 1 mark

What is the principal artifact produced by the AWS Packer build in `demo-02`?

- A. A continuously reconciled Kubernetes deployment
- B. A Terraform state file describing the production fleet
- C. An Ansible inventory containing all running servers
- D. A custom AMI built using a temporary instance

### L2 Q3 Rebuildability — 1 mark

The lecture describes a problematic form of a “golden image.” What makes that example an anti-pattern?

- A. The image was modified manually and cannot be reliably recreated from a maintained build definition.
- B. The organization uses a shared base image.
- C. The image has been tested before use.
- D. The image is generated by an automated build pipeline.

### L2 Q4 Regions and architectures — 1 mark

A team needs equivalent Ubuntu-based machines in two AWS regions and on both x86-64 and ARM64 processors. Which assumption is sound?

- A. One AMI ID is valid in every region and on both architectures.
- B. The VM instance type converts any image to the required architecture automatically.
- C. The team must select suitable images for each region and architecture combination.
- D. Only the size of the VM's disk determines whether the image can boot.

### L2 Q5 Stock and custom images — 2 marks

Explain the difference between a stock image and a custom image. Give one reason an organization would maintain a custom image instead of configuring every new machine entirely from a stock image at launch time.

### L2 Q6 Build time and boot time — 2 marks

Explain the difference between Packer provisioning during an image build and cloud-init configuration when a machine boots. Give one suitable example for each stage.

### L2 Q7 Containers and virtual machines — 2 marks

Explain one important difference between a typical Linux container and a virtual machine in how they use the operating-system kernel. State one practical consequence for their isolation or compatibility.

### L2 Q8 Image layers — 2 marks

A company needs web-server and database-server images with the same security baseline. Propose a simple image hierarchy and explain one maintenance benefit compared with independently repeating the baseline setup in every image build.

### L2 Q9 Reading the image build — 4 marks

`demo-02/devops-ubuntu-26.04-aws.pkr.hcl` defines two build sources:

```hcl
source "amazon-ebs" "ubuntu-north" {
  region = "eu-north-1"
  # Other settings omitted
}

source "amazon-ebs" "ubuntu-west" {
  region = "eu-west-1"
  # Other settings omitted
}

# The build uses both sources. Its provisioning scripts include,
# in this order:
# cloud-init.sh, base.sh, git.sh, aws-cli.sh, motd.sh,
# disable-auto-updates.sh, cleanup.sh, zerodisk.sh
```

The first script waits for the initial cloud-init process to finish. The final scripts clean temporary files and prepare the disk before the image is captured.

1. Describe the build lifecycle from source image to resulting AMI, including the role of the temporary VM and what happens to it after a successful build. **(2 marks)**
2. Why does the build wait for cloud-init before changing the operating system, and why does cleanup belong after software installation? **(2 marks)**

### L2 Q10 Repeating a build and rolling out an update — 4 marks

The Packer template selects its source image using `most_recent = true`. Its `base.sh` script runs `apt-get update` and `apt-get dist-upgrade`. A student claims: “The code is in Git, so rebuilding next month is guaranteed to produce exactly the same software versions.”

1. Assess that claim. Identify two inputs that can change without a change to the Git commit, and explain how to control them when reproducible versions are required. **(2 marks)**
2. The team deliberately builds a patched image. Describe an immutable rollout to the running application, including validation and preservation of persistent data. **(2 marks)**

## Lecture 3 Server state and Ansible

### L3 Q1 Inventory — 1 mark

What is the main purpose of an Ansible inventory?

- A. To store a binary snapshot of every server
- B. To replace all role defaults and templates
- C. To identify managed hosts and groups, with variables such as connection details
- D. To record only the commands that previously failed

### L3 Q2 Partial state — 1 mark

A playbook ensures that Nginx is installed but says nothing about an unrelated package installed manually. What should you generally expect?

- A. The unrelated package remains unless a task explicitly manages or removes it.
- B. Ansible removes every package absent from the playbook.
- C. Ansible recreates the server from a stock image.
- D. The playbook must fail because the server has additional state.

### L3 Q3 Roles — 1 mark

Why does `demo-03a` separate `common`, `web`, `database`, and `batch` into roles?

- A. Roles guarantee that all tasks run simultaneously.
- B. Each role creates its own independent Ansible installation.
- C. Roles prevent the use of variables shared across hosts.
- D. Roles package related tasks and supporting files so they can be organized and reused.

### L3 Q4 Variable precedence — 1 mark

Consider a simplified version of the demo's port configuration using a scalar variable named `app_port`. Role defaults set it to `8080`, the target host's group variables set it to `3000`, and the playbook command includes `-e app_port=9000`. What value should `{{ app_port }}` produce?

- A. `8080`, because the role owns its configuration
- B. `9000`, because the extra variable overrides the other supplied values
- C. `3000`, because group variables always override command-line values
- D. An error, because the same variable cannot appear in multiple places

### L3 Q5 Selecting hosts and roles — 2 marks

In `demo-03a/provisioning/provision.yml`, the `common` role targets `fleet`, while the `web`, `database`, and `batch` roles target their respective host groups. Explain which roles a host belonging to `web_servers` should receive and why the grouping is useful.

### L3 Q6 Service state — 2 marks

Explain the difference between `state: started` and `enabled: yes` in a service task. Why is `state: restarted` different from `state: started` when a playbook is run repeatedly?

### L3 Q7 Registering results — 2 marks

The infrastructure playbook in `demo-03a` uses:

```yaml
- name: Create web security group
  amazon.aws.ec2_security_group:
    # Other settings omitted
    state: present
  register: web_sg

# A later EC2 task uses:
# security_group: "{{ web_sg.group_id }}"
```

Explain what `register` does here and why the later task uses the returned group ID instead of a manually copied value. These are excerpts; no execution is required.

### L3 Q8 Provisioning and testing — 2 marks

The demo separates `00_create.sh`, `50_provision.sh`, and `60_test.sh`. Explain the difference between creating infrastructure and provisioning its operating-system/application state. Why is a separate functional test useful even when provisioning exits successfully?

### L3 Q9 Templates and handlers — 4 marks

Consider this shortened excerpt from the web role in `demo-03a`:

```yaml
# tasks/main.yml
- name: Configure Nginx for web application
  template:
    src: nginx-site.conf.j2
    dest: /etc/nginx/sites-available/{{ project_name }}
  notify:
    - reload nginx

# handlers/main.yml
- name: reload nginx
  systemd:
    name: nginx
    state: reloaded
```

Assume a successful play, no forced handler flushes, and no other task notifying this handler.

1. When should the handler run if rendering the template changes the destination file? What happens on the next run if the rendered file is identical? **(2 marks)**
2. Suppose three changed tasks notify the same handler before the normal end-of-tasks handler phase. How many times should it run in that phase, and why is this useful? **(2 marks)**

### L3 Q10 A misleading idempotence guard — 4 marks

The web role contains this dependency-installation task:

```yaml
- name: Install Node.js dependencies
  shell: |
    cd "{{ app_directory }}"
    npm install
  become_user: "{{ app_user }}"
  args:
    creates: "{{ app_directory }}/node_modules"
```

The `node_modules` directory already exists from an earlier deployment. A new application release changes the required dependencies in `package.json`.

1. Predict whether this task runs and explain the resulting risk. **(2 marks)**
2. Propose a change-aware way to install updated dependencies and one check that would show the application has the intended dependency state. Simply forcing every task to report `ok` is not a solution. **(2 marks)**
