# ICA0024 Infrastructure as Code

## Understanding check for Lectures 1 to 3

**Name:** ____________________  **Date:** ____________________

Answer all 30 questions. Each lecture is worth **20 marks**, for **60 marks** in total. Suggested time: **45–60 minutes**, or 15–20 minutes per lecture.

Every question is multiple choice with **one correct answer**. Select the best answer from A-D, including for practical scenarios. No written explanation, code, commands, product-specific knowledge, or access to the demo repositories is required.

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

Which pair of benefits best explains how version-controlling infrastructure definitions helps a team deliver changes reliably?

- A. It preserves change history and makes reverting a definition sufficient to restore deleted application data.
- B. It provides a shared definition and keeps running infrastructure synchronized whenever a change is committed.
- C. It makes proposed changes reviewable and records who changed the intended configuration and why.
- D. It makes environment differences visible and makes validation unnecessary after a change is approved.

### L1 Q6 Configuration drift — 2 marks

Two servers were created from the same definition. An administrator changes a managed setting manually on one server. Which description and response best address the situation?

- A. The server has drifted from the declared state; compare the difference and either restore the approved setting or review and update the definition.
- B. The definition has become obsolete; copy the changed setting into it and apply it to the other server without further review.
- C. The servers are still consistent because they share an original definition; record the manual change only in an operational log.
- D. The difference is necessarily a fault; rebuild both servers immediately without checking why the setting was changed.

### L1 Q7 Mutable and immutable infrastructure — 2 marks

A server needs an operating-system configuration change and stores application data that must survive the update. Which plan correctly distinguishes mutable and immutable approaches?

- A. A mutable update replaces the server; an immutable update modifies the existing server while preserving its identity.
- B. Both approaches modify the existing server; the immutable approach additionally records the change in version control.
- C. A mutable update changes the existing server; an immutable update replaces it and recreates persistent data from the infrastructure definition.
- D. A mutable update changes the existing server; an immutable update replaces it and preserves persistent data separately or through a verified migration.

### L1 Q8 Separating infrastructure and server configuration — 2 marks

A deployment needs networks and virtual machines, plus software and service configuration inside those machines. Which organization best separates responsibilities while keeping the deployment coordinated?

- A. Maintain each environment as a complete independent copy so changes to shared configuration never affect another environment.
- B. Separate resource provisioning from server configuration, pass required resource information between them, and review each concern independently.
- C. Put provisioning and configuration in separate repositories and rely on operators to keep their connection details synchronized.
- D. Keep only resource provisioning in code and document the manual software setup as the interface between the two responsibilities.

### L1 Q9 Dependencies and changing resource information — 4 marks

An application server requires a network. A later configuration step needs the server's assigned address, which may change when the server is replaced. The team currently copies that address into several files. Which design best preserves both dependency order and current connection information?

- A. Represent network-to-server and server-to-configuration dependencies explicitly, and derive the connection address from the current server output.
- B. Number the definition files in deployment order, and retain the original address as a default in each configuration file.
- C. Start all stages together, and retry configuration against the previously recorded address until the server becomes reachable.
- D. Create the network and server in order, and let each configuration stage maintain its own reviewed copy of the assigned address.

### L1 Q10 Shared definitions and environment differences — 4 marks

Development and production use copied infrastructure definitions. They should share an application structure, but production needs greater capacity. Independent edits have introduced differences whose purpose is unclear. Which approach best preserves legitimate differences and prevents accidental divergence?

- A. Keep independent definitions and periodically copy production over development, treating production capacity as the shared baseline.
- B. Require identical definitions and values everywhere, recording production capacity changes only in an operational checklist.
- C. Share the common structure, keep environment values explicit, and review existing differences against intended state before validating future changes.
- D. Create a shared definition, permit manual environment-specific changes after deployment, and review only changes to the shared definition.

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

An organization starts every server from a supplied stock image and repeats the same security and software setup at launch. What is the strongest reason to maintain a custom image?

- A. A custom image captures live application data, so it replaces the need for separate data backups.
- B. A custom image contains a tested organizational baseline, reducing repeated setup while still requiring maintenance.
- C. A custom image incorporates future security fixes automatically, so its original build definition can remain unchanged.
- D. A custom image removes environment differences, so all settings and machine identities should be embedded in it.

### L2 Q6 Build time and boot time — 2 marks

A fleet needs the same monitoring software on every machine, but each instance needs a distinct identity and environment-specific connection settings. Which division of work best fits image building and first-start initialization?

- A. Embed the monitoring software and one shared machine identity in the image; change environment settings manually after launch.
- B. Install everything at first start because reusable images cannot contain configured software.
- C. Embed all production connection settings in every image; use first-start initialization only to check whether the machine boots.
- D. Prepare the shared monitoring software in the image; supply instance identity and environment settings during first-start initialization.

### L2 Q7 Containers and virtual machines — 2 marks

Which statement correctly compares a typical Linux container with a virtual machine and identifies a consequence?

- A. Containers normally share the host kernel, while VMs run guest kernels; a workload requiring a different kernel may need a VM.
- B. Containers and VMs each boot their own kernel, so they provide the same kernel isolation boundary.
- C. Containers share the host kernel, so they cannot isolate processes or files from other containers.
- D. VMs run guest kernels, so any VM image can run unchanged on every processor architecture and hypervisor.

### L2 Q8 Snapshot and rebuildable definition — 2 marks

A team has a snapshot of a working server but no maintained definition of how it was configured. Which assessment is most accurate?

- A. The snapshot records the intended configuration process, so future changes can be reviewed directly from its creation history.
- B. The snapshot is unsuitable for recovery because only a rebuildable definition can restore a machine's state.
- C. The snapshot may restore captured state, but a maintained definition is still needed to review and deliberately reproduce the configuration process.
- D. The snapshot proves future builds will match the server, provided the same stock image name is selected each time.

### L2 Q9 Organizing an image family — 4 marks

Web-server and database-server images share a security baseline but need different software. Their separate build definitions contain copied baseline steps, and a policy update reached only one copy. Which plan best addresses both organization and rollout?

- A. Build one image with both workloads installed; apply a baseline change to whichever running servers currently need it.
- B. Reuse a common baseline with separate workload definitions; rebuild affected images, validate policy and workload behavior, then deliberately replace affected machines.
- C. Reuse a common baseline with separate workload definitions; committing its new version also updates existing images and running machines.
- D. Keep the copied baseline steps and review each copy; validate only the baseline definition before replacing machines with existing images.

### L2 Q10 Reproducible builds and immutable updates — 4 marks

A version-controlled image build always selects the latest base image and packages. The team wants to reproduce an approved version and later roll out a deliberately patched version. Which plan meets both goals?

- A. Re-run the same source revision with latest inputs; update existing servers in place and call the unchanged source an immutable release.
- B. Record the approved base image but continue selecting latest packages; replace all machines and recreate their application data from the build definition.
- C. Control both base and package versions; patch running machines manually and rely on their original image for future replacements.
- D. Record and retain approved base and package artifacts; build and validate a patched image, check replacement instances, and preserve persistent data during rollout.

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

Web, database, and batch-processing servers all need a common baseline but different workload configuration. Which organization expresses both requirements with the least duplicated baseline logic?

- A. Maintain a complete baseline copy for every workload group so each team can change it independently.
- B. Apply every configuration unit to every server and let operators disable the unwanted services afterward.
- C. Apply one reusable baseline to the fleet and select workload-specific units through the corresponding host groups.
- D. Use workload groups only for connection settings and put all server configuration into one sequence applied to every host.

### L3 Q6 Desired state and operational actions — 2 marks

A service is already running and its relevant configuration has not changed. How does declaring that it should be running differ from requesting a restart on every automation run?

- A. The desired-state declaration can leave it running undisturbed; an unconditional restart requests another operation and can cause unnecessary disruption.
- B. Both requests must stop and start it again, because automation cannot confirm a running state without restarting.
- C. The desired-state declaration starts it only on the first deployment; the restart request is the only way to recover it after a later failure.
- D. The restart request becomes a no-op after its first success, even if the automation explicitly requests it on every run.

### L3 Q7 Responding to configuration changes — 2 marks

Several compatible configuration changes must be applied before a service reloads them. Which approach best avoids unnecessary work while activating a coherent configuration?

- A. Reload after every file is copied, even when its contents are unchanged, to make each step independently visible.
- B. Apply and validate the compatible changes, then reload once if relevant configuration actually changed.
- C. Reload before changing the files, then skip the final reload if the configuration steps report success.
- D. Apply all changes and avoid reloading while the service remains running, because a running process always reads updated settings.

### L3 Q8 Configuration success and functional success — 2 marks

All configuration steps report success, but users cannot use the application. Which interpretation and follow-up check are most useful?

- A. Successful configuration proves the application works; compare automation exit codes from two consecutive runs.
- B. The deployment must have drifted; check only whether all expected configuration files still exist.
- C. A running service proves the application is reachable; compare installed package names with the deployment log.
- D. Managed resources may be configured correctly while the user workflow still fails; exercise a representative request through the application and its dependencies.

### L3 Q9 Comparing codebase organizations — 4 marks

A growing team is considering replacing one large configuration file with reusable units and explicit environment composition. Which proposal best balances reuse with the cost of added structure?

- A. Use coherent baseline and workload units with documented inputs and override rules; test their composition because extra interfaces can hide dependencies or conflicts.
- B. Split every operation into its own unit and select them implicitly; the resulting file count makes ownership and effective configuration self-explanatory.
- C. Copy each environment into its own repository; independent changes remove the need to coordinate common behavior across environments.
- D. Keep one universal unit and add environment conditions throughout it; using one file removes the need to document how environment values interact.

### L3 Q10 Checking the intended state — 4 marks

A deployment skips software setup whenever an 'application' directory exists. The directory remains after the desired version changes, so the process reports success without inspecting the version or behavior. Which correction best establishes the intended state?

- A. Keep the directory check and run the process twice; two unchanged runs establish that the desired version is installed.
- B. Recreate the directory on every run and treat its new timestamp as proof that the application has been updated.
- C. Compare the installed version or artifact with the desired one, repair missing or mismatched state, then verify the version and representative application behavior.
- D. Update the deployment log with the desired version whenever the directory exists, then use that log as the check on future runs.
