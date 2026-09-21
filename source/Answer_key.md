# ICA0024 Infrastructure as Code

## Answer key and marking guidance for Lectures 1 to 3

**Instructor copy.** The student questionnaire contains 30 questions worth **60 marks**, with **20 marks per lecture**. Each lecture has four multiple-choice questions worth 1 mark each, four short explanations worth 2 marks each, and two practical scenarios worth 4 marks each.

Award credit for equivalent explanations and defensible design choices. Grade the reasoning, responsibilities, and trade-offs rather than exact vocabulary, directory names, or any product's syntax. No code or command is required. The [source map](Source_map.md) identifies the lecture concepts behind the questions and distinguishes applied design scenarios from direct recall. No negative marking is suggested; any pass threshold should follow the course assessment policy.

## Lecture 1 Infrastructure as Code concepts

### L1 Q1 Answer B — 1 mark

Compute executes workloads, storage retains data, and networking connects resources. The alternatives describe activities, environments, or application-level concerns rather than the three infrastructure pillars.

### L1 Q2 Answer C — 1 mark

A declarative definition expresses the intended state. Automation determines the operations needed from the declaration and actual state. Declarative syntax alone does not remove dependencies or guarantee parallel execution.

### L1 Q3 Answer A — 1 mark

Once the desired state is satisfied, repeating an idempotent operation under unchanged relevant conditions should cause no further managed-state changes. Checking the current state is compatible with idempotence; doing nothing without checking does not establish correctness.

### L1 Q4 Answer D — 1 mark

PaaS typically transfers more operating-system and runtime-platform maintenance to the provider. The exact boundary depends on the service. The application team still owns its business requirements and application code.

### L1 Q5 Version control — 2 marks

Award **1 mark each** for two distinct benefits explained in relation to reliable delivery, such as a reviewable change history, peer review before application, automated validation of proposed changes, or a shared record of intended configuration that reduces undocumented edits.

Do not award a separate benefit for merely keeping another copy. A prior definition can support investigation or recovery planning, but reverting a source revision does not automatically restore deleted data or guarantee safe infrastructure rollback.

### L1 Q6 Configuration drift — 2 marks

- **1 mark:** Actual managed configuration has diverged from the declared or intended state; the manual edit creates a difference from the baseline.
- **1 mark:** A sound detection or reconciliation method: compare actual state with the declaration, investigate the difference, and either restore the approved state or review and record a legitimate change before applying it consistently.

### L1 Q7 Mutable and immutable changes — 2 marks

- **1 mark:** A mutable update modifies the existing server; an immutable update replaces it with one prepared from the updated definition or image.
- **1 mark:** Preserve persistent data separately or use a tested migration/backup/restore process before retiring the old server. Replacement must not discard the only copy of application data.

### L1 Q8 Separating responsibilities — 2 marks

- **1 mark:** Infrastructure definitions establish resources and connectivity; server configuration establishes software, files, and service state within those resources.
- **1 mark:** A justified benefit of separating these concerns, such as clearer ownership, reuse of configuration across different resource layouts, focused review, or separate validation of different change types.

Do not require separate repositories or separate products. Separation can exist within a single codebase with a clear interface between responsibilities.

### L1 Q9 Dependencies and resource information — 4 marks

- **1 mark:** The network must exist before the dependent server can be created, and the server's assigned address must be known before the dependent configuration step can use it.
- **1 mark:** Dependencies and required outputs should be explicitly represented; file ordering alone does not describe or maintain the resource relationships reliably.
- **1 mark:** Have the authoritative resource information supply the dependent configuration, and refresh that information when the server is replaced.
- **1 mark:** This avoids independently maintained copies becoming stale or inconsistent and reduces the chance of configuring the wrong machine.

Accept generated configuration, a maintained inventory fed by resource outputs, or another clearly explained way of resolving current information. Do not require a particular dependency syntax or product.

### L1 Q10 Shared definitions and environment differences — 4 marks

- **1 mark:** Keep the common application structure in a shared, reusable definition rather than independently editing full copies.
- **1 mark:** Keep legitimate environment values, including capacity, explicit and associated with the intended environment. Shared structure need not imply identical values everywhere.
- **1 mark:** Compare existing definitions and actual state against the intended baseline and documented exceptions to identify accidental differences.
- **1 mark:** Review and version shared changes and environment values, validating their effects in the relevant environments before applying them.

Accept different folder or repository layouts if they preserve a clear shared definition and explicit differences. Do not require a particular layout or insist that all differences are drift.

## Lecture 2 Images and machine initialization

### L2 Q1 Answer B — 1 mark

An image provides the starting state for multiple instances. The instances can change independently after launch; those changes do not automatically rewrite the image.

### L2 Q2 Answer D — 1 mark

Image building prepares a reusable artifact. Deployment uses that artifact to create running instances. Producing a new image does not automatically update existing machines or eliminate instance-specific initialization.

### L2 Q3 Answer A — 1 mark

The problem is hidden manual changes and the lack of a maintained, repeatable creation process. A shared baseline or an automated, rebuildable image is not inherently an anti-pattern, even if the team calls it a golden image.

### L2 Q4 Answer C — 1 mark

Machine images must be compatible with the destination platform and processor architecture. A common intended baseline can require different artifacts or formats for different targets; the exact requirements depend on the target platforms.

### L2 Q5 Stock and custom images — 2 marks

- **1 mark:** A stock image is a supplied starting image; a custom image adds selected organizational software or configuration to a starting image.
- **1 mark:** A sound reason, such as a consistent security baseline, less repeated installation, faster initialization, or a tested common starting state.

### L2 Q6 Build time and boot time — 2 marks

- **1 mark:** Build-time configuration becomes part of a reusable image, for example common software or a shared security baseline.
- **1 mark:** Boot-time initialization configures a particular instance when it starts, for example its environment-specific settings or instance identity.

Accept different placements if the distinction and trade-off are sound. First-start initialization is not automatically ongoing state reconciliation.

### L2 Q7 Containers and virtual machines — 2 marks

- **1 mark:** Typical Linux containers share a host kernel; virtual machines run a guest operating system with its own kernel over virtualized hardware.
- **1 mark:** A valid consequence for isolation or compatibility, such as sharing a kernel-level boundary, needing a compatible host kernel, or being able to run a different guest kernel in a VM.

Do not accept claims that containers have no isolation or that any image runs unchanged on any operating system and processor architecture.

### L2 Q8 Snapshot and rebuildable definition — 2 marks

- **1 mark:** A snapshot captures a point-in-time state that may help restore or clone a machine, subject to its scope and consistency.
- **1 mark:** It does not explain or maintain the intended construction process; hidden configuration and manual changes remain difficult to review, modify, and recreate deliberately. A maintained build definition makes those inputs and steps explicit.

Do not imply snapshots are useless or that definitions replace backups of persistent data.

### L2 Q9 Organizing an image family — 4 marks

- **1 mark:** Define a common baseline once and build separate workload-specific images from it, or reuse an equivalent common build unit in both image definitions.
- **1 mark:** Central ownership of shared baseline logic reduces duplicated edits and inconsistent policy implementation while keeping workload differences separate.
- **1 mark:** Rebuild the affected derived images and explicitly roll out or replace the running machines; changes to a shared definition do not propagate automatically into existing artifacts or instances.
- **1 mark:** Validate the new baseline and derived workload behavior before production use, such as checking the policy setting and exercising the application on a candidate image.

Accept a dependency diagram or prose. Reuse alone does not prove that a built artifact or running fleet is current.

### L2 Q10 Reproducibility and immutable updates — 4 marks

- **1 mark:** The selected base image can change independently of the build instructions; record and select the approved version when reproducing it.
- **1 mark:** Software package versions or their source contents can change; control the approved versions and ensure the required artifacts remain available. Versioned instructions alone do not freeze external inputs.
- **1 mark:** Build and validate the patched image, create replacement instances, check application health, and move the workload to the replacements with a considered recovery path.
- **1 mark:** Preserve persistent data on suitably managed storage or use a tested migration/restore process before retiring old instances.

Do not require a specific package manager, image identifier, or artifact-storage product.

## Lecture 3 Server state and configuration organization

### L3 Q1 Answer C — 1 mark

An inventory identifies target hosts and groups and can associate relevant information with them. It supports selecting the appropriate targets for configuration; it is not a complete backup of their state.

### L3 Q2 Answer A — 1 mark

The system in the question manages explicitly declared resources. A resource outside that scope is not automatically declared absent, so unmanaged state can remain even after successful configuration.

### L3 Q3 Answer D — 1 mark

Grouping related responsibilities creates units that can be understood, reused, and maintained. Such units can still have dependencies and need integration testing; splitting files does not guarantee independence or parallelism.

### L3 Q4 Answer B — 1 mark

Shared logic plus explicit environment values preserves reuse and makes intentional differences reviewable. A documented configuration scheme makes the effective values understandable; copying whole definitions or hiding overrides makes divergence harder to control.

### L3 Q5 Grouping by responsibility — 2 marks

- **1 mark:** Apply a common baseline to the fleet or a shared parent grouping.
- **1 mark:** Apply workload-specific units only to the corresponding web, database, or batch groups. Explain that separating selection from reusable definitions avoids copying the baseline or installing every workload everywhere.

Do not require a particular inventory syntax, directory structure, or naming convention.

### L3 Q6 Desired state and operational actions — 2 marks

- **1 mark:** Declaring a running service describes a condition; requesting a restart describes an operation even when that condition is already satisfied.
- **1 mark:** Reapplying the desired state can leave an already running service undisturbed, while unconditional restarts can cause unnecessary disruption. A restart may still be appropriate when a relevant change requires it.

### L3 Q7 Responding to changes — 2 marks

- **1 mark:** Change-aware reloads apply necessary configuration changes while avoiding unnecessary disruption when relevant configuration is unchanged.
- **1 mark:** Combining compatible changes before one reload avoids redundant work and lets the service consume a coherent configuration. The changes should be validated and ordered appropriately before activation.

Assess the principle, not a product's notification rules or handler timing.

### L3 Q8 Functional verification — 2 marks

- **1 mark:** Configuration success establishes that selected operations or resource checks succeeded, not that the complete application works for its users.
- **1 mark:** A relevant functional check, such as making a representative application request, confirming database access from the application, or verifying communication between components.

Award credit for explaining the check's purpose; a successful configuration exit status alone is not a functional check.

### L3 Q9 Comparing codebase organizations — 4 marks

- **1 mark:** Propose coherent units, for example a common baseline plus separate web, database, and batch responsibilities, with a clear place for environment selection and values.
- **1 mark:** Explain a benefit such as focused review, reuse, clearer ownership, or reducing duplicated logic as the system grows.
- **1 mark:** Identify a real cost or risk: more interfaces and indirection, unclear dependencies, conflicting defaults, or excessive fragmentation that makes the effective configuration hard to follow.
- **1 mark:** Address that risk with clear interfaces, documented inputs and override rules, visible composition, sensible unit size, or appropriate integration validation.

A single file can be adequate for a small system. Do not award full credit for claiming that more files are always better, or require one prescribed repository layout.

### L3 Q10 Checking the intended state — 4 marks

- **1 mark:** Directory existence does not establish that the intended software version or configuration is present.
- **1 mark:** Repeatedly doing nothing can leave an incorrect state unchanged. Idempotence and convergence to the desired state are related but distinct properties; a no-op alone is not evidence of successful configuration.
- **1 mark:** Compare a meaningful observed state, such as the installed version or artifact identity, with the desired version/configuration and update when they differ. Include handling missing or incomplete installations in a sound explanation.
- **1 mark:** Verify the intended version/configuration or exercise the relevant application behavior after the update. Rechecking directory existence alone is insufficient.

Accept in-place reconciliation or replacement from a verified artifact if the student explains how the intended state is established and checked.

## Interpreting the results

| Questions | Understanding to revisit |
|---|---|
| L1 Q2 Q3 Q6; L3 Q2 Q6 Q10 | Desired state, idempotence, managed scope, and convergence |
| L1 Q5 Q8 Q9 Q10 | Reviewable definitions, separation of concerns, dependencies, and environment differences |
| L2 Q1 Q2 Q5 Q6 Q8 | Images, initialization, snapshots, and rebuildability |
| L2 Q3 Q9 Q10 | Maintained image definitions, shared baselines, reproducible inputs, and deliberate rollout |
| L2 Q4 Q7 | Compatibility and isolation boundaries |
| L3 Q1 Q3 Q4 Q5 Q9 | Inventory, reusable units, configuration values, and codebase organization trade-offs |
| L3 Q7 Q8 Q10 | Change-aware operations and verification of intended outcomes |

For an oral follow-up, change one assumption in a scenario and ask the student to explain how the design or outcome changes. Assess transferable reasoning rather than recall of a command or a demo file.
