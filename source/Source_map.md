# ICA0024 Assessment source map

Review windows use **HH:MM:SS from the start of the original recording**. They identify the underlying concepts, not necessarily the exact wording of a question. The practical scenarios apply those principles to new situations. Codebase organization questions assess defensible design choices rather than a single directory layout taught as a rule.

The questions were revised to remove demo-code reading, command recall, and product-specific behavior. Tool demonstrations remain part of the lecture evidence, but students are assessed on the transferable principles illustrated by them. Automated transcripts can contain recognition errors; the supplied slides provide supporting context.

## Lecture 1

Source recording: `Lecture1.mp4`. Supporting slides cover infrastructure pillars, service models, desired state, drift, immutability, idempotence, declarative definitions, the source of truth, and resource dependencies.

| Question | Lecture concepts and review windows |
|---|---|
| L1 Q1 | Infrastructure pillars, 00:42:30–00:49:30 |
| L1 Q2 | Declarative state, 02:06:00–02:13:30 |
| L1 Q3 | Idempotence, 01:59:00–02:08:30 |
| L1 Q4 | Cloud abstraction and responsibility, 00:59:30–01:02:00 |
| L1 Q5 | Codified change and traceability, 00:56:00–00:59:30; 02:17:00–02:21:00 |
| L1 Q6 | Configuration drift, 01:38:00–01:40:00; 01:45:00–01:47:00 |
| L1 Q7 | Immutable replacement, 01:40:00–01:45:00; 01:47:00–01:50:30 |
| L1 Q8 | Infrastructure creation and configuration responsibilities, 02:39:00–02:42:30; 02:52:30–02:56:30 |
| L1 Q9 | Resource dependencies and derived connection information, 02:42:00–02:48:30; applied dependency scenario |
| L1 Q10 | Source of truth and traceable changes, 02:17:00–02:21:00; drift, 01:38:00–01:47:00; applied organization scenario |

L1 Q10 asks students to apply the principles of shared definitions and explicit intended differences. No particular repository structure is required.

## Lecture 2

Source recording: `Lecture2.mp4`. Supporting slides cover hypervisors, image formats, stock and custom images, base images and layers, image building, immutable servers, snapshots versus rebuildability, initialization, and containers versus machines.

| Question | Lecture concepts and review windows |
|---|---|
| L2 Q1 | Images as machine starting points, 00:25:00–00:27:00; 00:51:00–00:58:30 |
| L2 Q2 | Image artifacts and their use, 00:50:00–00:58:30; 01:20:00–01:26:00 |
| L2 Q3 | Manually maintained golden-image anti-pattern, 00:42:45–00:45:45 |
| L2 Q4 | Image variants and architecture, 00:30:30–00:34:00; supporting hypervisor and image-format slides |
| L2 Q5 | Stock and custom baselines, 00:33:00–00:42:00 |
| L2 Q6 | Image state and instance initialization, 01:03:30–01:07:30; 01:13:00–01:19:30 |
| L2 Q7 | Containers, VMs, and shared kernels, 01:51:00–02:07:00 |
| L2 Q8 | Snapshot versus rebuildable state, 01:07:00–01:12:30; supporting state-management slides |
| L2 Q9 | Image hierarchy and shared baselines, 00:45:45–00:50:00; immutable deployment and validation, 02:08:00–02:15:30; applied image-family scenario |
| L2 Q10 | Rebuildability and changing inputs, 00:39:00–00:42:00; 01:07:00–01:12:30; rollout and validation, 02:08:00–02:15:30 |

L2 Q10 applies rebuildability to changing external inputs. Students need not name an image registry, package manager, or a particular version-control mechanism.

## Lecture 3

Source recording: `Lecture3.mp4`. Supporting slides cover inventory, partial state, imperative versus declarative configuration, resource types, tasks, playbooks, reusable roles, and collections.

| Question | Lecture concepts and review windows |
|---|---|
| L3 Q1 | Inventory and grouping, 00:16:30–00:18:30; 01:37:30–01:40:30 |
| L3 Q2 | Partial state management, 00:23:30–00:30:30; 00:50:00–00:52:30; 01:25:30–01:29:30 |
| L3 Q3 | Organizing reusable configuration, 00:58:00–01:03:00; 01:15:00–01:17:30 |
| L3 Q4 | Configuration values and defaults, 02:05:00–02:14:00; applied environment-configuration choice |
| L3 Q5 | Applying common and specialized configuration to groups, 01:01:00–01:03:00; 01:59:00–02:04:00 |
| L3 Q6 | Desired service state and operational procedures, 00:27:30–00:29:30; 01:38:30–01:40:00; 02:39:00–02:40:00 |
| L3 Q7 | Responding to configuration changes, 00:46:00–00:46:45; 02:30:30–02:34:30 |
| L3 Q8 | Configuration and functional verification, 01:29:30–01:30:30; 02:36:30–02:41:30 |
| L3 Q9 | Reusable units and composition, 00:58:00–01:03:00; 01:15:00–01:17:30; 01:59:00–02:14:00; applied codebase-design comparison |
| L3 Q10 | Limits of existence-only state checks, 00:47:00–00:49:30; 01:25:30–01:29:30; applied desired-state scenario |

L3 Q9 deliberately asks students to weigh modularity against indirection and complexity. The rubric accepts multiple reasonable organizations. L3 Q10 distinguishes a shallow guard condition from evidence that the intended state has been achieved; no knowledge of a specific automation module is needed.

## Source provenance

Recordings, automated transcripts, original source hashes, and supporting screenshots remain with the instructor's original course materials and are not included in this repository. Earlier drafts included specific demo-code excerpts; the current assessment uses self-contained conceptual scenarios instead.
