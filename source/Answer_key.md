# ICA0024 Infrastructure as Code

## Answer key and marking guidance for Lectures 1 to 3

**Instructor copy.** The student questionnaire contains 30 questions worth **60 marks**, with **20 marks per lecture**. Each lecture has four multiple-choice questions worth 1 mark each, four short answers worth 2 marks each, and two scenarios worth 4 marks each.

Award credit for equivalent explanations and technically sound alternatives. The bullets below identify credit-bearing ideas; students do not need to reproduce this wording. No negative marking is suggested. Track each lecture's score separately to identify topics needing review. Any pass threshold should follow the course's assessment policy.

Questions assess concepts in the recordings and supplied slides, with practical excerpts from the supplied `demo-01`, `demo-02`, and `demo-03a` code. Shortened excerpts are identified in the student copy. The [source map](Source_map.md) identifies lecture passages and code files. Local demo files may have evolved since the recordings; grade the code printed in the question.

## Lecture 1 Infrastructure as Code concepts

### L1 Q1 Answer B — 1 mark

Compute executes workloads, storage retains data, and networking connects components. The other choices name tools, environments, or application-level concerns.

### L1 Q2 Answer C — 1 mark

A declarative definition expresses the intended state. The tool determines the required operations from that definition and the current state. Declarative syntax does not mean every operation is independent or can run concurrently.

### L1 Q3 Answer A — 1 mark

Once the declaration is satisfied, repeating the operation under unchanged conditions should not further alter the managed state. Checking state is compatible with idempotence; duplicating or needlessly rebuilding resources is not required.

### L1 Q4 Answer D — 1 mark

PaaS typically transfers more operating-system and runtime-platform maintenance to the provider. The exact responsibility boundary depends on the service. The team still owns its application requirements and code.

### L1 Q5 Version control — 2 marks

Award **1 mark each** for two benefits connected to reliable delivery, for example:

- A reviewable change history helps identify what changed, who changed it, and why.
- Pull requests and review help catch mistakes before applying changes.
- Automated validation can run against proposed configuration changes.
- A shared definition reduces undocumented manual differences between environments.
- A known earlier definition helps investigate or plan recovery from a bad change.

Do not award a separate benefit for “having another copy.” Reverting a Git commit does not by itself restore deleted data or guarantee a safe infrastructure rollback.

### L1 Q6 Configuration drift — 2 marks

- **1 mark:** Actual managed configuration has diverged from its declared or intended state; the manually changed server now differs from that baseline.
- **1 mark:** Compare actual state with the definition, for example through a plan, configuration inspection, or a configuration-management run. Investigate whether the manual change is legitimate, then either update the reviewed declaration or reapply the intended configuration.

### L1 Q7 Mutable and immutable changes — 2 marks

- **1 mark:** Mutable updates modify the existing server; immutable updates create a replacement from a newly prepared definition or image and switch the workload to it.
- **1 mark:** Preserve persistent data separately or use a tested backup/migration/restore procedure before retiring the old server. Replacement must not discard the only copy of application data.

### L1 Q8 Tool responsibilities — 2 marks

- **1 mark:** In this demo, Terraform defines and provisions AWS resources and produces connection information, including the inventory.
- **1 mark:** Ansible connects to the target and manages software, files, and service configuration inside the operating system.

These are the roles of the tools in this particular workflow, not an assertion that Ansible cannot manage cloud resources. `demo-03a` demonstrates that it can.

### L1 Q9 Dependencies and inventory — 4 marks

- **1 mark:** `aws_key_pair.main_key` is referenced for the instance's SSH key-pair name.
- **1 mark:** `aws_security_group.main_security_group` is referenced for the attached security-group ID. Both resource references contribute implicit dependencies, so Terraform must obtain the required resource values before completing the dependent operation. Moving blocks up or down the file is not the dependency mechanism.
- **1 mark:** Using `aws_instance.server.public_ip` connects the inventory to the provisioned instance's actual output and avoids a separately maintained, potentially stale IP address.
- **1 mark:** Apply/regenerate the inventory after replacement and use that updated inventory for Ansible. A previously copied inventory does not update itself simply because a new instance exists.

Technical reference: [Terraform references and dependencies](https://developer.hashicorp.com/terraform/language/expressions/references).

### L1 Q10 Repeated runs and drift — 4 marks

- **1 mark:** The installed package remains present; the matching file does not need rewriting; a running and enabled service remains in that state.
- **1 mark:** This is idempotence: once the requested state is reached, repetition with unchanged relevant inputs does not produce additional managed-state changes. The shown `state: present` does not mean “upgrade to whatever version is newest.”
- **1 mark:** A manual edit makes the managed file differ from the declared content, so the next successful `copy` task restores the declared contents.
- **1 mark:** The restoration reconciles drift against the declaration. It does not require replacing the whole server or reinstalling Nginx.

## Lecture 2 Images and machine initialization

### L2 Q1 Answer B — 1 mark

An image supplies the starting state for instances. The instances can subsequently change independently; their changes do not automatically rewrite the source image.

### L2 Q2 Answer D — 1 mark

The Packer build prepares a temporary instance and captures a reusable AMI. It does not, by itself, operate the long-lived production fleet.

### L2 Q3 Answer A — 1 mark

The problem is the unrepeatable manual creation process and accumulated hidden changes. The lecturer explicitly distinguishes this from an automated, rebuildable image that an organization may also call a “golden image.” The name alone is not the anti-pattern.

### L2 Q4 Answer C — 1 mark

Image selection must match the target region and CPU architecture. Equivalent image contents in different regions do not imply the same AMI ID.

### L2 Q5 Stock and custom images — 2 marks

- **1 mark:** A stock image is a supplied starting image, such as a distribution vendor's Ubuntu image; a custom image adds an organization's chosen software or configuration.
- **1 mark:** A relevant reason, such as consistently applying a security baseline, reducing repeated installation work, shortening launch time, or maintaining a tested organization-specific starting state.

### L2 Q6 Build time and boot time — 2 marks

- **1 mark:** Packer provisioning prepares the image before it is reused, for example installing shared tooling or applying a common baseline.
- **1 mark:** Cloud-init can initialize an instance at boot using supplied metadata/user data, for example setting instance-specific configuration or running initial setup. It is not a general continuously running reconciliation loop; whether an individual action repeats depends on cloud-init configuration and module frequency.

Accept reasonable alternative placements if the student explains the trade-off between a larger prepared baseline and more work at launch.

### L2 Q7 Containers and VMs — 2 marks

- **1 mark:** Typical Linux containers share the host's Linux kernel, while VMs run a guest operating system with its own kernel over virtualized hardware.
- **1 mark:** A valid consequence: containers generally have a smaller startup/runtime overhead, share a kernel-level boundary, or require compatibility with the host kernel. VMs can provide different guest kernels. On a non-Linux desktop, Linux containers normally use a Linux VM underneath.

Do not accept “containers have no isolation” or “any container can run unchanged on any operating system and architecture.”

### L2 Q8 Image hierarchy — 2 marks

- **1 mark:** A suitable hierarchy is vendor Ubuntu → shared organization baseline → separate web and database images.
- **1 mark:** Shared baseline changes can be maintained centrally and reused, reducing duplicated provisioning logic and inconsistent baseline setup. Descendant images still need rebuilding and testing when the baseline changes; existing instances do not inherit the changes automatically.

### L2 Q9 Image build lifecycle — 4 marks

- **1 mark:** For each configured source, Packer starts a temporary VM from the selected stock image and runs the provisioners against it.
- **1 mark:** It captures the prepared machine state as a custom AMI and, on normal successful completion, removes the temporary build instance. The two configured targets produce regional AMIs; the image artifacts remain available.
- **1 mark:** Waiting for cloud-init avoids racing initial configuration, package-manager activity, or related boot-time setup.
- **1 mark:** Final cleanup removes build-time leftovers after installation has finished, so temporary files and caches are not needlessly captured in the reusable image. Cleanup is not proof that every secret or machine-specific identity has been sanitized.

### L2 Q10 Reproducibility and rollout — 4 marks

- **1 mark:** `most_recent = true` can resolve to a different source AMI later. Record or pin the approved source AMI for the relevant region/architecture when rebuilding the same version is required.
- **1 mark:** Package repositories and the versions selected by `dist-upgrade` can change. Control approved package versions and their availability, for example with a versioned repository snapshot or equivalent reproducible dependency source. Versioned build instructions alone do not freeze external inputs.
- **1 mark:** Build and validate the patched image, then create replacement instances and verify application health before directing traffic to them. Retain an appropriate recovery path until the replacement is proven.
- **1 mark:** Keep persistent application data on suitable separately managed storage or migrate/restore it through a tested procedure before retiring old instances. Running machines are not patched merely by publishing a new AMI.

## Lecture 3 Server state and Ansible

### L3 Q1 Answer C — 1 mark

Inventory identifies target hosts and groups and can associate variables such as SSH connection details with them.

### L3 Q2 Answer A — 1 mark

Ansible ordinarily manages the state expressed by the tasks. An omitted resource is not automatically declared absent; additional unmanaged state can remain.

### L3 Q3 Answer D — 1 mark

Roles organize related tasks, defaults, templates, handlers, and other supporting resources into reusable units. They do not guarantee task parallelism or prohibit shared variables.

### L3 Q4 Answer B — 1 mark

The command-line extra variable sets `app_port` to `9000`. Extra variables have higher variable precedence than the group variables and role defaults in this example. Multiple definitions are permitted; precedence determines the effective value. The scalar form in the question avoids unrelated dictionary-merging details.

Technical reference: [Ansible variable precedence](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html#understanding-variable-precedence).

### L3 Q5 Host selection — 2 marks

- **1 mark:** A web host belongs to `web_servers`, which is a child group of `fleet`, so it receives the `common` role in the first play and the `web` role in the web play during a normal full run.
- **1 mark:** This applies a shared baseline to the fleet while limiting specialized configuration to the appropriate hosts. It avoids installing the entire database or batch stack everywhere.

### L3 Q6 Service state — 2 marks

- **1 mark:** `state: started` requests that the service be running now, while `enabled: yes` requests that it start automatically at boot. These are distinct aspects of service state.
- **1 mark:** `state: restarted` requests a restart whenever the task executes, whereas `state: started` normally leaves an already running service running. Repeated restart operations can cause unnecessary disruption even if the final service state is “running.”

### L3 Q7 Registered results — 2 marks

- **1 mark:** `register: web_sg` stores the task's returned result in a variable named `web_sg`, including its `group_id`.
- **1 mark:** Referencing that returned ID passes the actual created or located resource into the later task and avoids manually duplicating a changing cloud identifier. The producing task must execute before its result is consumed in this sequence.

### L3 Q8 Provisioning and tests — 2 marks

- **1 mark:** Creation establishes infrastructure such as instances, security groups, and connection information; provisioning installs/configures the operating-system and application resources on those instances.
- **1 mark:** Successful tasks do not prove that the application works end to end. Functional tests can check health endpoints, database access, or communication between components that might still be misconfigured.

### L3 Q9 Handlers — 4 marks

- **1 mark:** A changed template task notifies `reload nginx`; in the stated scenario it runs at the normal handler phase after the play's regular tasks.
- **1 mark:** If the rendered file is unchanged on the next run, that task does not notify the handler, so it does not cause a reload.
- **1 mark:** The same handler runs once in that handler phase despite three notifications.
- **1 mark:** Combining notifications avoids redundant reloads and lets the service consume the completed configuration changes together.

Technical reference: [Ansible handlers and notification timing](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_handlers.html). A later explicit flush or later handler phase changes the scope of the “once” statement; the question intentionally excludes that complication.

### L3 Q10 Dependency guard — 4 marks

- **1 mark:** The existing `node_modules` path causes `creates` to skip the shell command.
- **1 mark:** Directory existence does not prove that installed dependencies match the new manifest; the application can retain stale or missing dependencies.
- **1 mark:** Propose a manifest/lockfile-aware installation step, for example register changes to deployed dependency definitions and run a suitable installation task when those change or dependencies are missing. A committed lockfile with `npm ci` is one valid approach, if the required files and installation conditions are handled correctly. A checksummed build artifact is another defensible approach.
- **1 mark:** Verify installed dependency versions against the intended manifest/lockfile or run a targeted application/smoke test that exercises the changed dependency. A combination is strongest. Merely testing whether the directory exists does not establish dependency correctness.

Technical references: [Ansible shell creates guard](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/shell_module.html) and [npm ci requirements](https://docs.npmjs.com/cli/v11/commands/npm-ci/).

## Interpreting the results

Use the question groups to choose a follow-up discussion:

| Questions | Understanding to revisit |
|---|---|
| L1 Q2 Q3 Q6 Q10 | Desired state, idempotence, and drift reconciliation |
| L1 Q5 Q8 Q9 | Reviewable change, tool boundaries, and resource dependencies |
| L2 Q3 Q8 Q10 | Rebuildable images, shared baselines, and controlled build inputs |
| L2 Q1 Q2 Q6 Q9 | Image lifecycle, build-time provisioning, and boot-time initialization |
| L3 Q1 Q3 Q4 Q5 Q7 | Inventory, roles, variable precedence, and passing discovered resource information |
| L3 Q2 Q6 Q9 Q10 | Partial state, change detection, and safe repeated execution |
| L3 Q8 | Functional verification beyond successful provisioning |

For a brief oral follow-up, ask the student to change one assumption in a scenario and predict the result. This helps distinguish memorized terminology from an explanation they can apply to the code.
