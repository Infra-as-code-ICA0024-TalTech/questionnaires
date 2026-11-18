# ICA0024 Assessment source map

Review windows use **HH:MM:SS from the start of the original recording**. They identify the underlying concepts, not necessarily the exact wording of a question. The practical scenarios apply those principles to new situations. Codebase organization questions assess defensible design choices rather than a single directory layout taught as a rule.

The questions were revised to remove demo-code reading, command recall, and product-specific behavior. All questions use single-answer multiple choice; the former explanations and scenarios retain their concept coverage through choices and answer feedback. Tool demonstrations remain part of the lecture evidence, but students are assessed on the transferable principles illustrated by them. Automated transcripts can contain recognition errors. In November 2026 every question was rechecked against per-lecture analyses (sections, concepts as defined in the lecture, and student questions) built from the transcripts, and the review windows below were corrected against the transcripts. Concept slides from the course Miro board now exist for every lecture; the slide titles named below are those of the board export (untitled board pages are described by their content). Lecture 9 was added from its recording of 17 November 2026; lab administration is not assessed.

## Lecture 1

Source recording: `Lecture1.mp4`, automated transcript `Lecture1.txt`. Concept slides: "Configuration Drift", "Agile Infrastructure", "The promise", four untitled idempotence pages (definition, a non-idempotent script, a guarded script, and a declarative user and package), "Imperative vs Declarative", and "Maturity Matrix".

| Question | Lecture concepts and review windows |
|---|---|
| L1 Q1 | Infrastructure pillars and virtualization, 00:42:45–00:49:30 |
| L1 Q2 | Declarative versus imperative code, 02:06:00–02:14:00; slide "Imperative vs Declarative" |
| L1 Q3 | Idempotence, 01:59:15–02:08:40; untitled idempotence slides |
| L1 Q4 | Delegating layers to the provider, PaaS, 00:59:30–01:01:10 |
| L1 Q5 | Firewall rules codified in Git with pipeline policy checks and rollback, 00:55:20–00:58:35; history and rollback, 01:27:30–01:28:15; code in Git, delivery only through automation, who, when, and why, 02:18:30–02:20:30; slide "The promise" |
| L1 Q6 | Source of truth and drift, 01:38:15–01:40:00; drift between desired and actual state, 01:45:15–01:47:30; slide "Configuration Drift" |
| L1 Q7 | Immutable infrastructure, cattle versus pets, backups and replacement procedures, 01:40:00–01:45:15; state kept through backups, snapshots, and code, 01:47:00–01:50:30 |
| L1 Q8 | Combining tools for different layers, 02:20:30–02:24:05; slide "Maturity Matrix"; provisioning generates the configuration tool's inventory, 02:41:45–02:42:25; configuration of the new server, 02:54:48–02:57:00 |
| L1 Q9 | Generated inventory, 02:41:45–02:42:25; dependency order between resources, 02:45:15–02:46:05; a dependent file updated when the server's address changes, 02:47:55–02:49:50; applied dependency scenario |
| L1 Q10 | Differing development, QA, and production environments, 01:28:40–01:29:40; source of truth and drift, 01:38:15–01:40:00; fewer distinct configurations, 01:52:15–01:53:00; traceable changes, 02:18:30–02:20:30; applied organization scenario |

L1 Q10 asks students to recognize an application of shared definitions and explicit intended differences. No particular repository structure is required.

## Lecture 2

Source recording: `Lecture2.mp4`, automated transcript `Lecture2.txt`. Concept slides: "Golden Image", "cloud-init", "Local Hypervisors", "Datacenter Hypervisors", "Clouds", "Immutable Servers", "Stock Images", "Custom Images", "Image Formats", "AMI" (and an untitled image-catalogue page), "Snapshot vs Rebuildable", "Container Images", "Docker", "Immutable Infrastructure", "Containers vs Machines", "Base Image", "Image Layers", "Functions", "Function Layers", "Application vs Platform", and three pages on working with LLMs.

| Question | Lecture concepts and review windows |
|---|---|
| L2 Q1 | A machine image as a disk snapshot with metadata, 00:25:50–00:26:50; many machines from one image, replacement and scaling, 01:45:14–01:47:00 |
| L2 Q2 | Building an image from a temporary machine, 00:50:00–00:58:30; build demo, 01:20:30–01:27:10; an image as an artifact used by others, 02:08:20–02:09:00 |
| L2 Q3 | Manually maintained golden-image anti-pattern, 00:42:45–00:45:45; slide "Golden Image" |
| L2 Q4 | Incompatible image formats and rebuilding per target, 00:25:50–00:27:30; images per region, architecture, and version, 00:30:30–00:33:00; slides "Image Formats", "Datacenter Hypervisors", "Clouds" |
| L2 Q5 | Building on stock images, 00:32:55–00:33:30; when a custom image library pays off, 00:40:50–00:42:00; moving stable state into the image, 00:59:50–01:03:15; slides "Stock Images", "Custom Images" |
| L2 Q6 | Layering state between the image and creation-time initialization, 01:03:15–01:06:00; first-boot initialization from user data, 01:13:30–01:16:30; slide "cloud-init" |
| L2 Q7 | Containers, VMs, and shared kernels, 01:51:00–02:07:00; slide "Containers vs Machines" |
| L2 Q8 | Hand-made golden snapshots, 00:42:45–00:45:30; copying a machine versus reproducible builds at scale, 01:08:30–01:12:15; slide "Snapshot vs Rebuildable" |
| L2 Q9 | Image hierarchy and shared baselines, 00:45:45–00:50:00; slides "Base Image", "Image Layers"; testing an image before release, 02:08:20–02:15:25; applied image-family scenario |
| L2 Q10 | Replacing machines from fresh images while preserving data, 00:39:00–00:42:00; regular rebuilds from source, 01:49:00–01:50:35; image versions, rollback, and testing before release, 02:08:20–02:11:40; applied rebuild scenario |

L2 Q10 applies rebuildability to changing external inputs. Students need not name an image registry, package manager, or a particular version-control mechanism.

## Lecture 3

Source recording: `Lecture3.mp4`, automated transcript `Lecture3.txt`. Concept slides: "Inventory", "Imperative vs Declarative", "Partial State Management", "Existing vs Immutable", "Resource Types", "Services", "Modules / Tasks", untitled playbook and role folder layouts, "Collections", "Galaxy", "Playbooks", "Roles", six task-example pages, and "Notes".

| Question | Lecture concepts and review windows |
|---|---|
| L3 Q1 | Inventory and host groups, 00:16:30–00:18:30; dynamic inventory and separating listing, data, and code, 01:09:00–01:16:15; slide "Inventory" |
| L3 Q2 | Partial state management of existing servers, 00:23:30–00:30:30; slide "Partial State Management"; modules check and change one kind of object, 00:50:00–00:52:30; partial versus full control of a resource, 01:25:30–01:28:10 |
| L3 Q3 | Roles as reusable units versus runnable playbooks, 00:58:00–01:03:00; extracting and reusing roles, 01:16:10–01:17:00; slides "Roles", "Playbooks" |
| L3 Q4 | Agentless and agent-based configuration tools, 00:17:00–00:22:50 |
| L3 Q5 | Host groups, 00:17:15–00:18:30; plays mapping host groups to roles, 01:59:00–02:04:30 |
| L3 Q6 | Day-one declarative state versus day-two procedures, 00:27:30–00:29:30; re-run with no changes, 01:38:30–01:40:00; a separate restart procedure, 02:38:40–02:40:00 |
| L3 Q7 | Handlers that run once when notified, 00:46:00–00:46:45; 02:30:30–02:34:30 |
| L3 Q8 | Waiting for a condition versus managing a resource, 01:29:20–01:30:30; acceptance criteria checked from the users' perspective, 02:40:00–02:41:35 |
| L3 Q9 | Roles and composition, 00:58:00–01:03:00; three layers of listing, data, and code, 01:14:55–01:17:00; where variables come from, precedence, and starting in a single file, 02:04:40–02:16:00; applied codebase-design comparison |
| L3 Q10 | Presence-only versus full control of a resource, and tasks that converge whatever the starting state, 01:25:30–01:29:20; acceptance checks such as the right application version, 02:40:00–02:41:35; applied desired-state scenario |

L3 Q9 asks students to recognize a design that balances modularity against indirection and complexity, without requiring one specific repository layout. L3 Q10 distinguishes a shallow guard condition from evidence that the intended state has been achieved; no knowledge of a specific automation module is needed.

## Lecture 4

Source recording: `Lecture4.mp4`, automated transcript `Lecture4.txt`. Concept slides: "Chaos Engineering", "Cloud Topology", and "Scream Test".

| Question | Lecture concepts and review windows |
|---|---|
| L4 Q1 | Chaos engineering and continuous proof of recovery, 00:12:30–00:14:30; 00:17:15–00:21:10; slide "Chaos Engineering" |
| L4 Q2 | Regions, availability zones, and redundancy, 00:15:00–00:17:20; slide "Cloud Topology" |
| L4 Q3 | Scream test for unused infrastructure and alerting, 00:21:10–00:22:40; slide "Scream Test" |
| L4 Q4 | Keeping playbooks small enough to fit in your head, splitting them into included files or roles, and keeping what changes for the same reason together, 01:30:34–01:35:15 |
| L4 Q5 | Testing on empty and provisioned state, 00:27:00–00:30:35 |
| L4 Q6 | Restart tests and automated restarts, 00:11:15–00:12:30; 00:30:35–00:31:25 |
| L4 Q7 | Conflicting tasks and repeated changes on re-run, 01:40:50–01:43:30 |
| L4 Q8 | Tests as guardrails for generated code, 00:35:10–00:38:05; 00:39:00–00:39:30 |
| L4 Q9 | Reproducibility and deleting servers, 00:10:15–00:12:30; chaos engineering and zones, 00:12:30–00:21:10; zero-downtime changes, 00:22:40–00:24:45; applied operations scenario |
| L4 Q10 | Secrets outside version control, 01:27:36–01:27:50; 01:48:20–01:48:50; 01:50:05–01:51:00; fixing a found bug with a test, 01:51:15–01:52:05; state-aware modules versus shell commands, 01:52:40–01:56:00; constraining AI output, 01:56:40–01:59:15; applied review scenario |

## Lecture 5

Source recording: `Lecture5.mp4`, automated transcript `Lecture5.txt`. Concept slides: "Terraform is an infrastructure as code tool that", "Modules", "Registry", "HCL = HashiCorp", untitled pages showing infrastructure written in a general-purpose language, the search cluster behind a load balancer, the load balancer's listener and target group, and a two-zone cloud network, "API-first", "CRUD", "Clustered Software", and "Coordinated Scaling".

| Question | Lecture concepts and review windows |
|---|---|
| L5 Q1 | Data sources for existing resources, 01:10:15–01:15:05; querying the latest image for instances, 01:21:40–01:22:50 |
| L5 Q2 | State as a third source of information and cleanup of removed resources, 00:42:45–00:47:30 |
| L5 Q3 | Provider plugins and multi-provider projects, 00:56:00–01:03:05; 01:03:15–01:06:30 |
| L5 Q4 | Tool reflects the provider's model, 01:28:15–01:29:10; load balancer object model, 01:38:20–01:45:50; untitled listener and target-group slide; plan resource count, 01:56:15–01:56:45 |
| L5 Q5 | Remote state, one run at a time, splitting state, 00:47:30–00:49:40; private key stored in state, 02:16:50–02:17:15 |
| L5 Q6 | Inline versus separate rule models and change loops, 01:17:05–01:21:10; 01:53:11–01:54:00 |
| L5 Q7 | Create-time provisioners and mixing paradigms, 01:29:45–01:32:30; splitting provisioning and configuration, baking into images, 02:10:00–02:11:20 |
| L5 Q8 | Plan as dry run and apply confirmation, 01:55:40–01:57:00; reviewing destroy entries, 02:07:50–02:08:20 |
| L5 Q9 | Purpose of a load balancer and health checks, 01:49:00–01:55:35; front end isolated behind one endpoint, 02:11:40–02:12:05; node failure excluded, 02:18:15–02:20:40; slide "Clustered Software" and the untitled search-cluster diagram |
| L5 Q10 | Cluster configuration derived from all nodes, triggers and dependencies, 01:32:30–01:38:20; missing trigger found in plan and fixed, 02:05:10–02:08:20; slide "Coordinated Scaling" |

## Lecture 6

Source recording: `Lecture6.mp4`, automated transcript `Lecture6.txt`. Concept slides: "scheduler (Laravel app background jobs)", "Container Image", and "AWS Cloud".

| Question | Lecture concepts and review windows |
|---|---|
| L6 Q1 | Pay-per-execution pricing of functions, 00:17:27–00:19:20; 00:46:00–00:47:40; 00:59:00–01:00:20 |
| L6 Q2 | Container images as a portable package across compute platforms, 00:19:55–00:20:36; 00:47:10–00:47:40; slide "Container Image" |
| L6 Q3 | DNS records as code, domain purchase outside it, 00:24:00–00:25:35 |
| L6 Q4 | Cost impact of small design changes, fixed load-balancer cost, 00:26:20–00:27:30; 00:30:45–00:31:20; 01:49:10–01:49:55 |
| L6 Q5 | External scheduling versus in-application scheduling, 00:22:25–00:23:20; 00:28:20–00:28:45; 00:35:20–00:35:56; slide "scheduler (Laravel app background jobs)" |
| L6 Q6 | Console defaults versus explicitly declared permissions and log groups, 01:16:14–01:16:44; 01:18:40–01:19:10 |
| L6 Q7 | Secret storage, references, and least-privilege access, 00:37:17–00:39:25; 01:10:43–01:11:33; 01:20:47–01:21:06; 01:27:40–01:28:26; 01:48:30–01:48:48 |
| L6 Q8 | Networking responsibilities on lower-level services, 01:38:19–01:38:55; 01:45:25–01:46:32 |
| L6 Q9 | Choosing a compute platform by traffic, budget, and existing platform, 00:09:26–00:10:09; 00:17:27–00:19:20; 00:26:20–00:27:30; 00:35:59–00:36:20; cost estimate and choice by traffic and architecture, 00:59:50–01:02:00; slide "AWS Cloud"; applied platform-selection scenario |
| L6 Q10 | Shared resources in their own project, conditional resources, image builds outside the definition, 01:15:00–01:16:08; 01:31:00–01:32:14; 01:33:13–01:33:40; 01:36:49–01:37:33; 01:49:10–01:49:59; applied organization scenario |

## Lecture 7

Source recording: `Lecture7.mp4`, automated transcript `Lecture7.txt`. Concept slides: "Linters", "Policy Engines", "Testing", "Structuring", "Continuous Integration", "Module Interface", "Versioning", "Testing Boundaries", "Module Quality", "Integration Tests", "Refactoring", and "Monitoring vs Testing".

| Question | Lecture concepts and review windows |
|---|---|
| L7 Q1 | Unit versus integration tests for modules, 00:39:00–00:43:30; slides "Testing", "Integration Tests" |
| L7 Q2 | Module interface: defaults and overridable parameters as extension points, 00:29:05–00:33:05; slide "Module Interface" |
| L7 Q3 | Linters as static checks beyond syntax, 00:58:20–01:06:00; slide "Linters" |
| L7 Q4 | Modules as software products and when modularity pays off, 00:17:20–00:20:00; 00:23:30–00:24:40; slides "Structuring", "Refactoring" |
| L7 Q5 | Delivery pipeline order: lint, policy, smoke tests, staging, production, 01:06:00–01:11:40; slide "Continuous Integration" |
| L7 Q6 | Assessing and insourcing third-party modules, 00:12:30–00:15:30; 00:16:40–00:17:20; 00:21:37–00:24:00; slide "Module Quality" |
| L7 Q7 | Providers and tasks as the integration layer, modules as the next abstraction, 00:05:15–00:12:30 |
| L7 Q8 | Policy as code for organization-wide rules, 01:06:00–01:10:40; slide "Policy Engines" |
| L7 Q9 | Versioned upgrades through a staged pipeline, 00:25:00–00:29:05; 00:56:40–00:58:20; 01:10:40–01:11:40; slides "Versioning", "Monitoring vs Testing"; applied upgrade scenario |
| L7 Q10 | Integration testing on relevant real targets, 00:39:00–00:43:00; 00:43:00–00:50:20; 00:54:30–00:55:30; 00:56:40–00:57:20; slide "Testing Boundaries"; applied testing scenario |

## Lecture 8

Source recording: `Lecture8.mp4`, automated transcript `Lecture8.txt`. Concept slides: "Module Interface" and "Versioning", revisited from Lecture 7; most of the lecture used a live whiteboard.

| Question | Lecture concepts and review windows |
|---|---|
| L8 Q1 | Semantic versioning and expectations between module authors and consumers, 00:13:39–00:15:10; slide "Versioning" |
| L8 Q2 | Depending on explicit module versions instead of "latest", 00:27:37–00:28:30; 01:19:22–01:19:45 |
| L8 Q3 | Release pipeline, artifact repository, and frozen published versions, 00:16:25–00:21:10 |
| L8 Q4 | Single-resource module judged over-designed versus modules that package many resources or conventions, 00:56:20–00:58:45; 01:14:18–01:14:50; 00:58:45–01:00:50 |
| L8 Q5 | Choosing what to parameterize and parameters as promises, 00:37:25–00:38:20; 00:44:00–00:45:20; 00:50:40–00:51:45; slide "Module Interface" |
| L8 Q6 | Open-closed principle and list-based extension points, 00:38:40–00:42:24; 00:47:36–00:50:40 |
| L8 Q7 | A second database engine as a different contract and interface growth, 00:42:24–00:45:00 |
| L8 Q8 | Patching through module parameters versus module releases, 00:34:23–00:37:20; 00:45:29–00:46:10 |
| L8 Q9 | Independent consumers, release notification, and shared ownership with guardrails, 00:21:10–00:27:27; 00:16:25–00:21:10; applied team scenario |
| L8 Q10 | Reusing public modules and writing internal modules for company concepts, 00:58:45–01:04:30; 01:14:00–01:21:20; 01:24:30–01:28:40; 01:30:40–01:31:20; applied hybrid-organization scenario |

## Lecture 9

Source recording: `Lecture9.mp4` (17 November 2026), automated transcript `Lecture9.txt`. Concept slides: "Change" (Change Management), "Collaboration", "GitOps", and "Apps", used as section titles over a live whiteboard. Lab 4 instructions, defenses, and account limitations discussed in the second half are not assessed.

| Question | Lecture concepts and review windows |
|---|---|
| L9 Q1 | GitOps as continuous delivery applied to infrastructure and operations code, 00:09:44–00:14:40; not only for Kubernetes, 00:21:20–00:22:00; slide "GitOps" |
| L9 Q2 | Pull-based delivery by an agent in or near the infrastructure, 00:41:52–00:43:37 |
| L9 Q3 | Repository ownership: only the owners push or merge to the main branch, 00:23:20–00:24:30; owners review a green pull request and merge it, 00:27:40–00:29:30 |
| L9 Q4 | Four GitOps principles, the desired state controller as optional, scheduled pipelines, 00:16:57–00:22:41 |
| L9 Q5 | Push-based delivery from CI/CD and its security implications, 00:43:37–00:44:55; both models workable depending on tools and security, 00:48:20–00:48:40 |
| L9 Q6 | The pipeline as guardrails defined by the owning team in its repository, 00:19:40–00:20:50; codified knowledge that blocks non-compliant pull requests, 00:26:25–00:27:35; delegating review to automation, 00:31:50–00:32:30; slide "Collaboration" |
| L9 Q7 | Application release pipelines, artifact repositories, and version bumps committed to the infrastructure repository, 00:48:46–00:52:55; slide "Apps" |
| L9 Q8 | Git history, pipeline logs, and observability as the record of change, 00:16:05–00:16:55; automated delivery as the only path, 00:18:25–00:18:45; 00:22:44–00:23:08 |
| L9 Q9 | Slow cross-team change requests, 00:02:57–00:05:55; slide "Change"; pull requests checked by the owners' pipeline instead of tickets, "cosmic ping pong", 00:25:00–00:32:30; applied cross-team scenario |
| L9 Q10 | Teams allowing pull requests to each other's repositories, 00:32:35–00:33:25; batch jobs moved into a repository another team could change under checks, 00:33:25–00:36:50; simple interface files or a portal for frequent outside changes, 00:36:50–00:39:20; applied repository-organization scenario |

L9 Q9 and Q10 avoid the version-control basics already assessed in L1 Q5 and the shared definitions of L1 Q10; they assess how ownership, pull requests, and pipelines let teams change each other's infrastructure.

## Source provenance

Recordings, automated transcripts, original source hashes, and supporting screenshots remain with the instructor's original course materials and are not included in this repository. Earlier drafts included specific demo-code excerpts; the current assessment uses self-contained conceptual scenarios instead.
