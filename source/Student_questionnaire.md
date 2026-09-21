# ICA0024 Infrastructure as Code

## Understanding check for Lectures 1 to 3

**Name:** ____________________  **Date:** ____________________

Answer all 30 questions. Each lecture is worth **20 marks**, for **60 marks** in total. Suggested time: **75–90 minutes**, or 25–30 minutes per lecture.

For multiple-choice questions, select one answer. For short answers, use two to four sentences unless asked otherwise. For practical scenarios, explain your design and reasoning in plain language; a simple diagram is welcome. No code, commands, product-specific knowledge, or access to the demo repositories is required. Write your answers on a separate sheet or in the quiz response fields.

## Lecture 1 Infrastructure as Code concepts

### L1 Q1 Infrastructure pillars — 1 mark

Which set contains the three infrastructure pillars introduced in the lecture?

- A. Deployment, testing, and monitoring
- B. Compute, storage, and network
- C. Development, testing, and production
- D. Applications, users, and source code

### L1 Q2 Declarative configuration — 1 mark

Which statement best describes a declarative infrastructure definition?

- A. It records every command an administrator previously executed.
- B. It specifies the exact sequence of operations for every starting state.
- C. It describes the desired state, while automation determines how to reach it.
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

### L1 Q5 Version-controlled infrastructure definitions — 2 marks

Give two benefits of version-controlling infrastructure definitions beyond simply having a backup copy. Explain how each benefit helps a team deliver changes reliably.

### L1 Q6 Configuration drift — 2 marks

Two servers were created from the same definition. An administrator later changes a managed setting manually on only one server. Explain what configuration drift means in this situation and describe one way to detect or reconcile it.

### L1 Q7 Mutable and immutable infrastructure — 2 marks

A server needs a new operating-system configuration. Contrast an in-place mutable update with an immutable replacement. Explain what must happen to persistent application data when using the replacement approach.

### L1 Q8 Separating infrastructure and server configuration — 2 marks

A deployment needs networks and virtual machines, as well as software and service configuration inside those machines. Explain the distinction between these two responsibilities and one benefit of keeping their definitions organized separately.

### L1 Q9 Dependencies and changing resource information — 4 marks

An application server needs a network before it can be created. A later configuration step needs the server's assigned address. A team records that address manually in several places. Replacing the server may change the address.

1. Explain the dependency order and which resource information should pass between stages. Why is arranging files in a particular order not enough to express these relationships reliably? **(2 marks)**
2. Propose a way to keep dependent configuration consistent when a server is replaced. Explain why it is preferable to maintaining several handwritten copies of the address. **(2 marks)**

### L1 Q10 Shared definitions and environment differences — 4 marks

Development and production started from copied infrastructure definitions. They are intended to share the same application structure, but production needs greater capacity. After several independent edits, nobody knows whether other differences are intentional.

1. Propose how to organize the shared definitions and environment-specific values. Explain which differences should remain explicit. **(2 marks)**
2. Explain how the team could discover accidental differences and keep future changes reviewable while still allowing the legitimate capacity difference. **(2 marks)**

## Lecture 2 Images and machine initialization

### L2 Q1 Image and running machine — 1 mark

What is the relationship between a machine image and a virtual machine?

- A. The image is the live machine's current CPU and memory usage.
- B. One image can initialize multiple VM instances, which can later develop different state.
- C. Every image can initialize only one VM.
- D. Launching a VM automatically updates the source image whenever the VM changes.

### L2 Q2 Image building and deployment — 1 mark

What distinguishes building a machine image from deploying machines based on that image?

- A. Building an image automatically replaces every running machine.
- B. Deployment modifies the shared source image whenever an instance changes.
- C. Building an image removes the need for any instance-specific configuration.
- D. Building creates a reusable starting artifact; deployment creates running instances from it.

### L2 Q3 Rebuildability — 1 mark

The lecture describes a problematic form of a "golden image." What makes that example an anti-pattern?

- A. The image was modified manually and cannot be reliably recreated from a maintained build definition.
- B. The organization uses a shared base image.
- C. The image has been tested before use.
- D. The image is generated by an automated build pipeline.

### L2 Q4 Image compatibility — 1 mark

A team wants to use the same machine baseline on two virtualization platforms and on different processor architectures. Which assumption is sound?

- A. Any machine image can boot unchanged on every platform and processor architecture.
- B. Matching the application's name guarantees that its machine image is compatible.
- C. The team must check platform and architecture compatibility and may need separate image variants.
- D. Only disk size determines whether the image can boot.

### L2 Q5 Stock and custom images — 2 marks

Explain the difference between a stock image and a custom image. Give one reason an organization would maintain a custom image instead of configuring every new machine entirely from a stock image at launch time.

### L2 Q6 Build time and boot time — 2 marks

Explain how configuration prepared during image building differs from configuration applied when an instance first starts. Give one suitable example for each stage.

### L2 Q7 Containers and virtual machines — 2 marks

Explain one important difference between a typical Linux container and a virtual machine in how they use the operating-system kernel. State one practical consequence for their isolation or compatibility.

### L2 Q8 Snapshot and rebuildable definition — 2 marks

A team keeps a snapshot of a working server but has no maintained instructions for recreating its configuration. Explain one thing the snapshot provides and one reason it does not replace a rebuildable definition.

### L2 Q9 Organizing an image family — 4 marks

A company needs web-server and database-server images. Both must share a security baseline, but each needs different software. Today, two separate build definitions contain copied baseline steps. A policy update was applied to only one copy.

1. Propose an organization for the image definitions that separates shared baseline work from workload-specific work. Explain how it reduces the risk illustrated here. **(2 marks)**
2. Explain what must happen to the derived images and running machines after the shared baseline changes. Include a check before the new baseline is used in production. **(2 marks)**

### L2 Q10 Reproducible builds and immutable updates — 4 marks

An image build always selects the latest available base image and software packages. A team claims: "Our build instructions are version-controlled, so running them next month must produce the same software versions."

1. Assess the claim. Identify two inputs that can change independently of the instructions and explain how to control them when reproducing an approved version. **(2 marks)**
2. The team deliberately prepares a patched image. Describe an immutable update to the running application, including validation and preservation of persistent data. **(2 marks)**

## Lecture 3 Server state and configuration organization

### L3 Q1 Inventory — 1 mark

What is the main purpose of an inventory in server configuration management?

- A. To store a complete binary snapshot of every server
- B. To replace all reusable configuration definitions
- C. To identify managed hosts and groups and associate relevant targeting information
- D. To record only the operations that previously failed

### L3 Q2 Partial state management — 1 mark

An automation system manages only the resources explicitly declared to it. Its declaration requires a web service but says nothing about an unrelated package installed manually. What should you expect after a successful run?

- A. The unrelated package can remain because it is outside the declared scope.
- B. Every package not named in the declaration is automatically removed.
- C. The machine is necessarily recreated from a stock image.
- D. Success proves that every aspect of the machine matches a complete baseline.

### L3 Q3 Reusable configuration units — 1 mark

What is the strongest reason to organize server configuration into reusable units for common setup, web services, and databases?

- A. It guarantees that all configuration actions can run simultaneously.
- B. It makes each unit independent of every other resource and input.
- C. It removes the need to test how the units work together.
- D. It groups related responsibilities so they can be understood, reused, and maintained separately.

### L3 Q4 Configuration values and shared logic — 1 mark

Development and production use the same service configuration logic but need different capacity values. Which organization best supports reuse and makes the intended differences clear?

- A. Copy the full logic for each environment and edit the copies independently.
- B. Keep shared logic reusable and supply explicit environment-specific values through a documented configuration scheme.
- C. Hide the production values inside unrelated shared configuration files.
- D. Require both environments to have identical capacity so no values differ.

### L3 Q5 Grouping by responsibility — 2 marks

A fleet contains web, database, and batch-processing servers. All need a common baseline, but their workload-specific configuration differs. Explain how host grouping and reusable configuration units can express both requirements without applying every workload to every server.

### L3 Q6 Desired state and operational actions — 2 marks

Explain the difference between declaring that a service should be running and requesting that it restart on every automation run. Why does the distinction matter for repeated execution?

### L3 Q7 Responding to configuration changes — 2 marks

A service must reload to use changed configuration. Explain why it can be useful to reload only after relevant changes, and why several compatible configuration changes might be applied before a single reload.

### L3 Q8 Configuration success and functional success — 2 marks

Every configuration step reports success, but users still cannot use the application. Explain why these outcomes are compatible and give one functional check that could reveal a problem missed by configuration-level checks.

### L3 Q9 Comparing codebase organizations — 4 marks

A team is choosing between one large configuration file for all server types and environments, and smaller reusable units with a separate place to select which units and values each environment uses.

1. Propose sensible boundaries for the smaller units and explain one advantage over the single large file as the system grows. **(2 marks)**
2. Explain one cost or risk introduced by splitting the configuration, and how you would keep the resulting codebase understandable and safe to change. **(2 marks)**

### L3 Q10 Checking the intended state — 4 marks

A deployment process skips software setup whenever it finds a directory named "application". The directory remains after the desired application version changes. The process reports success without checking the installed version or whether the application works.

1. Explain why this check is insufficient and why an unchanged result does not by itself prove that automation has reached the desired state. **(2 marks)**
2. Propose a better way to decide whether an update is needed, and one check after the update that would provide evidence that the intended result was achieved. **(2 marks)**
