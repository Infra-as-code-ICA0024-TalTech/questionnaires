# ICA0024 Infrastructure as Code

## Answer key and marking guidance for Lectures 1 to 3

**Instructor copy.** The student questionnaire contains 30 single-answer multiple-choice questions worth **60 marks**, with **20 marks per lecture**. In each lecture, Q1-Q4 carry 1 mark each, Q5-Q8 carry 2, and Q9-Q10 carry 4. Scenarios also use multiple-choice answers.

Award the full question value for the correct choice and zero otherwise, with no negative marking. Explanations below provide feedback; students do not submit free-form answers. Questions assess principles, responsibilities, and design trade-offs without requiring product syntax. The [source map](Source_map.md) identifies the lecture concepts behind each question. Any pass threshold should follow the course assessment policy.

## Lecture 1 Infrastructure as Code concepts

### L1 Q1 Answer B — 1 mark

Compute executes workloads, storage retains data, and networking connects resources. The alternatives describe activities, environments, or application-level concerns rather than the three infrastructure pillars.

### L1 Q2 Answer C — 1 mark

A declarative definition expresses the intended state. Automation determines the operations needed from the declaration and actual state. Declarative syntax alone does not remove dependencies or guarantee parallel execution.

### L1 Q3 Answer A — 1 mark

Once the desired state is satisfied, repeating an idempotent operation under unchanged relevant conditions should cause no further managed-state changes. Checking the current state is compatible with idempotence; doing nothing without checking does not establish correctness.

### L1 Q4 Answer D — 1 mark

PaaS typically transfers more operating-system and runtime-platform maintenance to the provider. The exact boundary depends on the service. The application team still owns its business requirements and application code.

### L1 Q5 Answer C — 2 marks

Review before application can catch mistakes, and a traceable history helps explain and investigate changes. Version control alone neither applies changes nor restores deleted data; reviewed changes still need validation.

### L1 Q6 Answer A — 2 marks

Drift is a difference between actual managed state and intended state. Investigate it before reconciliation: an unauthorized change may need reversal, while a legitimate change should be reviewed and recorded in the definition. A shared origin does not guarantee continued consistency.

### L1 Q7 Answer D — 2 marks

Mutable updates change an existing instance. Immutable updates replace it with an instance prepared from the updated definition or image. Persistent application data needs separate storage or a verified transfer/recovery process; infrastructure definitions do not generally contain that data.

### L1 Q8 Answer B — 2 marks

Provisioning establishes resources and connectivity; server configuration establishes software, files, and service state. Clear boundaries with explicit information flow support focused review and reuse. Separate repositories are optional and do not by themselves keep dependencies synchronized.

### L1 Q9 Answer A — 4 marks

Explicit dependencies identify what must exist or be known before another step can proceed. Passing current resource outputs avoids stale, duplicated addresses after replacement. File names alone do not encode those resource relationships, and correct ordering alone does not keep copied values current.

### L1 Q10 Answer C — 4 marks

A shared definition captures the common structure, while explicit environment values retain intended capacity differences. Compare definitions and actual state with the agreed design, then review and validate changes. Identical values are not required, and undocumented manual exceptions undermine the shared source of truth.

## Lecture 2 Images and machine initialization

### L2 Q1 Answer B — 1 mark

An image provides the starting state for multiple instances. The instances can change independently after launch; those changes do not automatically rewrite the image.

### L2 Q2 Answer D — 1 mark

Image building prepares a reusable artifact. Deployment uses that artifact to create running instances. Producing a new image does not automatically update existing machines or eliminate instance-specific initialization.

### L2 Q3 Answer A — 1 mark

The problem is hidden manual changes and the lack of a maintained, repeatable creation process. A shared baseline or an automated, rebuildable image is not inherently an anti-pattern, even if the team calls it a golden image.

### L2 Q4 Answer C — 1 mark

Machine images must be compatible with the destination platform and processor architecture. A common intended baseline can require different artifacts or formats for different targets; the exact requirements depend on the target platforms.

### L2 Q5 Answer B — 2 marks

A stock image is a supplied starting point. A custom image adds selected software and configuration, providing a tested baseline and reducing repeated initialization. It still requires maintenance, instance-specific settings, and separate protection of persistent data.

### L2 Q6 Answer D — 2 marks

Build-time work becomes part of a reusable image; first-start initialization can supply values specific to an instance or environment. Other divisions may be valid, but this one directly separates the stable shared baseline from the varying inputs. First-start initialization alone is not ongoing reconciliation.

### L2 Q7 Answer A — 2 marks

Typical Linux containers share a host kernel while isolating aspects of their execution environment. A VM has a guest kernel over virtualized hardware. Kernel sharing affects compatibility and isolation; neither approach guarantees that arbitrary images work on every platform.

### L2 Q8 Answer C — 2 marks

A snapshot captures state at a point in time, within its scope and consistency limits. It can support restoration but does not explain the intended build process or make hidden manual changes reviewable. Rebuildable definitions and data backups serve different purposes.

### L2 Q9 Answer B — 4 marks

A shared baseline reduces inconsistent copies while workload-specific definitions preserve useful differences. Updating source does not update existing artifacts or instances: affected images must be rebuilt, tested, and deliberately rolled out. Validation should cover both the policy and the workloads.

### L2 Q10 Answer D — 4 marks

Version-controlled instructions do not freeze external inputs such as base images and packages. Reproduction requires controlled versions and available artifacts. An immutable update builds and validates a new image, replaces instances deliberately, and protects persistent data through suitable storage or a verified migration/recovery process.

## Lecture 3 Server state and configuration organization

### L3 Q1 Answer C — 1 mark

An inventory identifies target hosts and groups and can associate relevant information with them. It supports selecting the appropriate targets for configuration; it is not a complete backup of their state.

### L3 Q2 Answer A — 1 mark

The system in the question manages explicitly declared resources. A resource outside that scope is not automatically declared absent, so unmanaged state can remain even after successful configuration.

### L3 Q3 Answer D — 1 mark

Grouping related responsibilities creates units that can be understood, reused, and maintained. Such units can still have dependencies and need integration testing; splitting files does not guarantee independence or parallelism.

### L3 Q4 Answer B — 1 mark

Shared logic plus explicit environment values preserves reuse and makes intentional differences reviewable. A documented configuration scheme makes the effective values understandable; copying whole definitions or hiding overrides makes divergence harder to control.

### L3 Q5 Answer C — 2 marks

Grouping selects the appropriate targets; reusable units define the configuration to apply. Composing a common baseline with workload-specific units avoids both duplicated baseline logic and installation of every workload on every host. No particular inventory syntax or folder layout is required.

### L3 Q6 Answer A — 2 marks

A running-state declaration describes a condition that may already hold. A restart request describes an operation. Repeated execution can therefore leave a healthy service undisturbed with the first approach and disrupt it with the second. Relevant changes can still justify a restart.

### L3 Q7 Answer B — 2 marks

Apply and validate compatible changes before activation, then reload when relevant state changed. This avoids repeated reloads and allows the service to consume a coherent configuration. A running process does not necessarily reread changed files automatically.

### L3 Q8 Answer D — 2 marks

Configuration checks establish selected resource conditions, not necessarily end-to-end behavior. A representative request can expose failures in connectivity, dependencies, or application behavior that file, package, and process checks miss. Configuration success and functional failure can coexist.

### L3 Q9 Answer A — 4 marks

Coherent units support reuse and focused review, but extra interfaces and indirection can obscure dependencies and effective values. Documented inputs, visible composition, clear override rules, and integration checks address those costs. A small system may still be adequately served by a single file.

### L3 Q10 Answer C — 4 marks

Directory existence is not evidence of the desired software version or a complete installation. Repeated no-ops can preserve an incorrect state. Compare meaningful observed state with intended state, update when needed, and verify the result; changing a timestamp or log does not establish actual configuration.

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
