# ICA0024 Infrastructure as Code

## Understanding check for Lectures 1 to 9

**Name:** ____________________  **Date:** ____________________

Each lecture has its own set of 10 questions worth **20 marks**. Answer the questions for the lecture you are assigned. Suggested time: **15–20 minutes** per lecture.

Every question is multiple choice with **one correct answer**. Select the best answer from A-D, including for practical scenarios. No written explanation, code, commands, product-specific knowledge, or access to the demo repositories is required.

## Lecture 1 Infrastructure as Code concepts

### L1 Q1 Infrastructure pillars — 1 mark

Which set contains the three infrastructure pillars introduced in the lecture?

- A. Deployment, tests, and monitoring
- B. Compute, storage, and networking
- C. Development, test, and production
- D. Applications, users, and code

### L1 Q2 Declarative configuration — 1 mark

Which statement best describes a declarative infrastructure definition?

- A. It is a script listing commands to run, in the order an administrator would type them.
- B. It specifies the exact sequence of operations needed for each possible starting state.
- C. It describes the desired state, and the tool works out the steps needed to reach it.
- D. It lets the tool run independent changes in parallel, which is what makes it declarative.

### L1 Q3 Idempotence — 1 mark

An automation run has successfully reached the desired state. Its inputs and the relevant external state then remain unchanged. What should a second idempotent run do?

- A. Check the current state, find nothing to change, and make no changes.
- B. Recreate the resources so the team can show they are still reproducible from the code.
- C. Skip checking the current state, since the previous run already succeeded, and report success.
- D. Add another copy of each declared resource.

### L1 Q4 Cloud service models — 1 mark

A team moves from managing virtual machines under IaaS to a managed application platform under PaaS. Which responsibility would typically move towards the provider?

- A. Deciding which business requirements the application should meet
- B. Maintaining and reviewing the team's own application source code
- C. Choosing which application features to release and when
- D. Patching and upgrading the operating system and the runtime

### L1 Q5 Version-controlled infrastructure definitions — 2 marks

Which pair of benefits best explains how version-controlling infrastructure definitions helps a team deliver changes reliably?

- A. It preserves change history, so reverting a definition also restores any deleted application data.
- B. It gives one shared definition, and storing it in Git keeps the running infrastructure in sync with it.
- C. Changes can be reviewed and checked before they apply, and the history shows who changed what and why.
- D. It makes environment differences visible, so validation is no longer needed once a change is approved.

### L1 Q6 Configuration drift — 2 marks

Two servers were created from the same definition. An administrator changes a managed setting manually on one server. Which description and response best address the situation?

- A. The server has drifted; compare it with the definition, then restore the setting or review and update the definition.
- B. The definition is now obsolete; copy the new setting into it and apply it to the other server straight away, without a review.
- C. The servers are still consistent because they came from the same definition, so a note about the manual change in the operations log is enough.
- D. The difference is a fault in the server; rebuild both servers immediately.

### L1 Q7 Mutable and immutable infrastructure — 2 marks

A server needs an operating-system configuration change and stores application data that must survive the update. Which plan correctly distinguishes mutable and immutable approaches?

- A. A mutable update replaces the server; an immutable update modifies the existing server and keeps its identity and data in place.
- B. Both approaches modify the existing server; the immutable one also records the change in version control.
- C. A mutable update changes the existing server; an immutable update replaces it and rebuilds the application data from the infrastructure definition.
- D. A mutable update changes the existing server; an immutable update replaces it and keeps the data in separate storage or migrates it.

### L1 Q8 Separating infrastructure and server configuration — 2 marks

A deployment needs networks and virtual machines, plus software and service configuration inside those machines. Which organization best separates responsibilities while keeping the deployment coordinated?

- A. Keep a complete, independent copy of the whole setup for each environment, so that a change made for one environment stays out of the others.
- B. Separate provisioning from server configuration, pass the needed resource details between them, and review each part on its own.
- C. Put provisioning and configuration in separate repositories and rely on operators to keep the connection details in sync.
- D. Keep resource provisioning in code, and document the manual software setup as the interface between the two.

### L1 Q9 Dependencies and changing resource information — 4 marks

An application server requires a network. A later configuration step needs the server's assigned address, which may change when the server is replaced. The team currently copies that address into several files. Which design best preserves both dependency order and current connection information?

- A. Declare the network-to-server and server-to-configuration dependencies, and derive the address from the current server output.
- B. Number the definition files in deployment order, and keep the original address as a default value in each configuration file so it stays available.
- C. Start the stages together, and keep retrying the configuration against the previously recorded address until the server becomes reachable.
- D. Create the network and the server in order, and let each configuration stage keep its own reviewed copy of the address.

### L1 Q10 Shared definitions and environment differences — 4 marks

Development and production use copied infrastructure definitions. They should share an application structure, but production needs greater capacity. Independent edits have introduced differences whose purpose is unclear. Which approach best preserves legitimate differences and prevents accidental divergence?

- A. Keep the definitions separate and periodically copy production over development, using production capacity as the shared baseline.
- B. Require identical definitions and values in both environments, and record production capacity changes in an operations checklist.
- C. Share the common structure, keep environment-specific values explicit, and review today's differences against the intended design.
- D. Create one shared definition, allow manual environment-specific changes after deployment, and review changes to the shared definition.

## Lecture 2 Images and machine initialization

### L2 Q1 Image and running machine — 1 mark

What is the relationship between a machine image and a virtual machine?

- A. The image is a live record of the machine's current CPU and memory usage.
- B. Each image can start a single VM, so a second VM needs its own copy of the image.
- C. When a running VM changes, those changes are usually written back to its source image.
- D. One image can start many VMs, and each VM can then change independently.

### L2 Q2 Image building and deployment — 1 mark

What distinguishes building a machine image from deploying machines based on that image?

- A. Building creates a reusable artifact; deploying starts running machines from it.
- B. Building a new image also updates the machines that were started from the old one.
- C. Deploying a machine updates the shared source image whenever that machine changes.
- D. Building an image removes the need for any instance-specific configuration at launch.

### L2 Q3 Rebuildability — 1 mark

The lecture describes a problematic form of a "golden image." What makes that example an anti-pattern?

- A. The organization shares one base image across many teams and services.
- B. The image is tested before use, which slows down releases.
- C. It was changed by hand and cannot be rebuilt from a maintained definition.
- D. The image is produced by an automated pipeline instead of by an administrator.

### L2 Q4 Image compatibility — 1 mark

A team wants to use the same machine baseline on two virtualization platforms and on different processor architectures. Which assumption is sound?

- A. A machine image can usually boot unchanged on any platform and processor architecture.
- B. Check each platform and architecture; you may need separate image variants.
- C. If the application name and version match, the machine images will be compatible.
- D. The disk size is what decides whether an image can boot on a platform.

### L2 Q5 Stock and custom images — 2 marks

An organization starts every server from a supplied stock image and repeats the same security and software setup at launch. What is the strongest reason to maintain a custom image?

- A. It provides a tested company baseline, which reduces repeated setup but still needs maintenance.
- B. It captures live application data, so separate data backups are no longer needed.
- C. It picks up future security fixes as they are released, so its build definition can stay unchanged.
- D. It removes environment differences, so settings and machine identities should be built into it as well.

### L2 Q6 Build time and boot time — 2 marks

A fleet needs the same monitoring software on every machine, but each instance needs a distinct identity and environment-specific connection settings. Which division of work best fits image building and boot-time initialization?

- A. Put the monitoring software and one shared machine identity in the image; change environment settings by hand after launch.
- B. Install everything at boot time, because a reusable image cannot contain configured software.
- C. Put the monitoring software in the image; supply identity and environment settings during boot-time initialization.
- D. Put the production connection settings in each image, and keep boot-time initialization for a check that the machine boots.

### L2 Q7 Containers and virtual machines — 2 marks

Which statement correctly compares a typical Linux container with a virtual machine and identifies a consequence?

- A. Containers and VMs both boot their own kernel, so they provide the same kernel isolation boundary.
- B. Containers share the host kernel, so a process in one container can see and change files in another.
- C. VMs run their own guest kernel, which means any VM image can run unchanged on every processor architecture and hypervisor.
- D. Containers share the host kernel and VMs run their own, so a workload needing another kernel may need a VM.

### L2 Q8 Snapshot and rebuildable definition — 2 marks

A team has a snapshot of a working server but no maintained definition of how it was configured. Which assessment is most accurate?

- A. It records how the server was configured, so future changes can be reviewed from its creation history.
- B. It can restore the captured state, yet a maintained definition is needed to review and rebuild the setup.
- C. It is of no use for recovery, because restoring a machine requires a rebuildable definition.
- D. It shows that future builds will match the server, as long as the same stock image name is selected.

### L2 Q9 Organizing an image family — 4 marks

Web-server and database-server images share a security baseline but need different software. Their separate build definitions contain copied baseline steps, and a policy update reached only one copy. Which plan best addresses both organization and rollout?

- A. Build one image with both workloads installed, and apply baseline changes to whichever running servers currently need them.
- B. Share a common baseline with separate workload definitions; committing a new baseline version also updates existing images and running machines.
- C. Share a common baseline with separate workload definitions; rebuild affected images, test policy and workloads, then replace machines deliberately.
- D. Keep the copied baseline steps and review each copy, then validate the baseline definition before replacing machines from existing images.

### L2 Q10 Reproducible builds and immutable updates — 4 marks

A version-controlled image build always selects the latest base image and packages. The team wants to reproduce an approved version and later roll out a deliberately patched version. Which plan meets both goals?

- A. Pin and keep the approved base image and packages; build and test a patched image, then replace instances while protecting persistent data.
- B. Re-run the same source revision with the latest inputs, update existing servers in place, and call the unchanged source an immutable release.
- C. Record the approved base image but keep selecting the latest packages, then replace the machines and rebuild their data from the build definition.
- D. Control both base and package versions, patch running machines by hand, and rely on their original image for any future replacement.

## Lecture 3 Server state and configuration organization

### L3 Q1 Inventory — 1 mark

What is the main purpose of an inventory in server configuration management?

- A. To store a complete binary snapshot of each managed server
- B. To list managed hosts and groups and attach targeting information to them
- C. To replace reusable configuration definitions with a separate list of settings for each host
- D. To record which operations failed during the previous run

### L3 Q2 Partial state management — 1 mark

An automation system manages only the resources explicitly declared to it. Its declaration requires a web service but says nothing about an unrelated package installed manually. What should you expect after a successful run?

- A. Every package not named in the declaration is removed automatically during the run.
- B. The machine is recreated from a stock image so that it matches the declaration.
- C. The successful run shows the whole machine now matches a complete baseline.
- D. The package can stay, as the automation never touches what it was not told to manage.

### L3 Q3 Reusable configuration units — 1 mark

What is the strongest reason to organize server configuration into reusable units for common setup, web services, and databases?

- A. It groups related work so each part can be understood, reused and maintained.
- B. It guarantees that the configuration actions can run at the same time.
- C. It makes each unit independent of the other resources and inputs it might use.
- D. It removes the need to test how the units behave when combined on one server.

### L3 Q4 Agent-based and agentless tools — 1 mark

A team manages a fleet of servers with a configuration tool. What is the main practical difference between an agentless tool and an agent-based one?

- A. Agentless tools connect over an existing protocol such as SSH; agent-based tools need software on every node.
- B. Agentless tools cannot be idempotent, because checking a node's state before changing it needs an agent running there.
- C. Agentless tools need no network access to the managed nodes, while agent-based tools do.
- D. Agent-based tools are limited to Windows machines, while agentless tools are limited to Linux.

### L3 Q5 Grouping by responsibility — 2 marks

Web, database, and batch-processing servers all need a common baseline but different workload configuration. Which organization expresses both requirements with the least duplicated baseline logic?

- A. Keep a complete copy of the baseline in each workload group, so each team can change its own copy freely.
- B. Apply every configuration unit to every server, and let operators disable the unwanted services afterwards.
- C. Use workload groups for connection settings, and put the whole server configuration into one sequence that runs on every host.
- D. Apply one reusable baseline to the whole fleet, and select workload-specific units through the matching host groups.

### L3 Q6 Desired state and operational actions — 2 marks

A service is already running and its relevant configuration has not changed. How does declaring that it should be running differ from requesting a restart on every automation run?

- A. Both requests stop and start the service again, because automation cannot confirm a running state without restarting it.
- B. The declaration takes effect on the first deployment, after which a restart request is needed to recover from a later failure.
- C. The declaration can leave the healthy service alone, while an unconditional restart disrupts it on every run.
- D. The restart request becomes a no-op after its first success, even though the automation repeats it on later runs.

### L3 Q7 Responding to configuration changes — 2 marks

Several compatible configuration changes must be applied before a service reloads them. Which approach best avoids unnecessary work while activating a coherent configuration?

- A. Reload after each file is copied, even when its contents did not change, so each step is visible on its own.
- B. Apply and validate all the changes, then reload once if relevant configuration actually changed.
- C. Reload before changing the files, then skip the final reload if the configuration steps report success.
- D. Apply the changes and skip the reload while the service keeps running, since a running process reads new settings by itself.

### L3 Q8 Configuration success and functional success — 2 marks

All configuration steps report success, but users cannot use the application. Which interpretation and follow-up check are most useful?

- A. Successful configuration means the application works; compare the automation exit codes from two consecutive runs.
- B. The deployment must have drifted; check whether the expected configuration files still exist.
- C. Configuration can succeed while the application fails; send a representative request through it and its dependencies.
- D. A running service shows the application is reachable; compare installed package names with the deployment log.

### L3 Q9 Comparing codebase organizations — 4 marks

A growing team is considering replacing one large configuration file with reusable units and explicit environment composition. Which proposal best balances reuse with the cost of added structure?

- A. Split each operation into its own unit and select units implicitly; the large number of files makes ownership and the effective configuration self-explanatory.
- B. Copy each environment into its own repository; independent changes remove the need to coordinate common behavior across environments.
- C. Keep one universal unit and add environment conditions throughout it; using a single file removes the need to document how environment values interact.
- D. Use coherent baseline and workload units with documented inputs and override rules, and test how they combine, since added interfaces can hide conflicts.

### L3 Q10 Checking the intended state — 4 marks

A deployment skips software setup whenever an 'application' directory exists. The directory remains after the desired version changes, so the process reports success without inspecting the version or behavior. Which correction best establishes the intended state?

- A. Keep the directory check but run the process twice; two unchanged runs show that the desired version is installed.
- B. Compare the installed version with the desired one, fix any mismatch, then check the version and the application's behavior.
- C. Recreate the directory on each run, and treat its new timestamp as proof that the application has been updated.
- D. Write the desired version to the deployment log whenever the directory exists, and use that log as the check on future runs.

## Lecture 4 Resilience and verifying configuration code

### L4 Q1 Chaos engineering — 1 mark

What is the main purpose of chaos engineering practices, such as randomly terminating servers in a running system?

- A. To cut cloud costs by finding servers that have no remaining users and can be deleted
- B. To identify who owns each server, by waiting to see which team complains after it stops
- C. To show, again and again, that the system recovers from failures without users noticing
- D. To reduce the need for monitoring, since failures introduced on purpose need no alerts

### L4 Q2 Regions and availability zones — 1 mark

A service must stay available if one data center in a cloud region fails. Which placement fits the lecture's description of regions and availability zones?

- A. Spread instances across availability zones, which are separate data centers in one region
- B. Put the instances in one availability zone, since each zone already spans several regions
- C. Use a different region for each instance, because zones in a region usually share a building
- D. Add instances inside one zone, since extra capacity there gives the same failure protection

### L4 Q3 Scream test — 1 mark

An engineer finds a server that seems unused, has no known owner, and receives almost no traffic. What does a "scream test" involve?

- A. Deleting the server and its backups at once, since unused infrastructure only adds cost
- B. Sending a burst of traffic to it to check whether it survives a sudden spike in load
- C. Rebuilding it from code under a new name, so that its owner can be identified later
- D. Stopping the server for a while and waiting to see whether anyone reports a problem

### L4 Q4 Organizing a growing playbook — 1 mark

A single playbook has grown to several hundred lines. It configures web servers, databases, and batch jobs, and a service's restart handler is defined far from the tasks that notify it. Which reorganization fits the lecture's advice?

- A. Keep one file so every dependency stays visible, and add comments that link tasks to handlers
- B. Split it into roles or included files that each fit in your head, grouping what changes together
- C. Split it into one file per task so each file stays short, even if handlers end up far from tasks
- D. Copy it into one repository per server type, so each copy can shrink as the copies diverge

### L4 Q5 Testing from a clean state — 2 marks

A developer tests a provisioning definition by applying each new change to the same long-lived test machine. Every run passes, but the first run on a new machine fails. Which explanation and practice are most useful?

- A. The new machine has drifted; recreate it from a snapshot of the test machine and run again
- B. Earlier runs left state that the code needs but never creates; also test it from a clean state
- C. The code is not idempotent; run it twice on the test machine to show it will work anywhere
- D. New machines may be slower to start; add retries and waits, as the code works on the test machine

### L4 Q6 Restart tests — 2 marks

Provisioning completes and the application responds. Why is it also worth testing that the machine and its services still work after a restart?

- A. A restart is the most reliable way to apply configuration, so each run should end with one
- B. A restart resets the machine to its image, which shows whether provisioning is still needed
- C. A clean boot can stand in for functional checks, as a machine that starts usually serves users
- D. Services can work after provisioning yet fail after a reboot; a tested restart can be automated

### L4 Q7 Changes reported on every run — 2 marks

On every run against an already provisioned server, two tasks report a change to the same directory: one sets its owner to one user, the other to a different user. What is the best diagnosis and fix?

- A. Two tasks manage one resource in conflicting ways; give the directory one intended state
- B. The changes may be harmless if the run succeeds, so they can be ignored once the server works
- C. The server drifts after each run; rebuild it from a fresh image before the next run starts
- D. Add a service restart at the end of the run so the service picks up the owner set last

### L4 Q8 Guardrails for generated code — 2 marks

A team uses an AI coding assistant to generate infrastructure code. Which approach gives the most dependable evidence that the generated code meets the team's goals?

- A. Ask the same assistant to confirm its output, since it can explain the reasoning behind it
- B. Run the code once in one environment; if it works there, it can usually be trusted elsewhere
- C. Define acceptance tests and policies, and iterate on the code until all of them pass
- D. Use the most capable model available, since its output rarely needs tests or review

### L4 Q9 Changing production without disruption — 4 marks

A web shop announces multi-hour maintenance windows for each release and avoids changes on Fridays, because losing a production server would be a disaster. The team wants to make routine changes during working hours without users noticing. Which plan best fits the principles from the lecture?

- A. Make servers rebuildable from code, spread them across zones, rehearse failures, and deploy without downtime
- B. Keep the maintenance windows but shorten them, and require two engineers to approve any change that is made on a Friday
- C. Take more frequent snapshots of the production servers, and restore them by hand whenever a release causes an outage
- D. Start terminating random production servers straight away, and add monitoring later if users begin to report failures

### L4 Q10 Acting on an AI code review — 4 marks

An AI assistant reviewed a playbook it helped write. It reported a private key committed to the repository, a bug that leaves the application stopped after a restart, and a shell command used where a state-aware module now exists. Unasked, it also split the small playbook into many files. Which response is best?

- A. Accept all of the changes as generated, including the new file layout, because the review found the problems by itself
- B. Make the repository private so the key can stay, fix the bug by hand, and keep the shell command because it already works
- C. Set the findings aside, because the playbook completed without errors and a successful run usually means the code is correct
- D. Remove the key from version control, fix the bug with a test that reproduces it, use the module, and undo the needless split

## Lecture 5 Declarative cloud provisioning and state

### L5 Q1 Looking up existing resources — 1 mark

A provisioning definition needs the ID of a shared network and the most recent approved base image. Another team maintains both. What does a read-only data lookup of these objects do?

- A. It imports both objects, so later runs of this definition will manage and update them.
- B. It reads current details of objects managed elsewhere, without creating, changing or deleting them.
- C. It creates private copies of the network and image, so the two teams no longer depend on each other.
- D. It records the values on the first run, so later runs usually keep using that original image.

### L5 Q2 Removing a resource from the definition — 1 mark

A team uses a provisioning tool that records the resources it created in a state file. They delete one server's definition from the code and apply again, changing nothing else. What should they expect?

- A. The server stays running, because removing its definition just means the tool stops managing it.
- B. The tool deletes every server in the account that does not appear in the current definitions.
- C. The apply fails until someone deletes the server by hand and then removes its state entry.
- D. The tool finds the server in its state but not in the code, and plans to destroy it.

### L5 Q3 Provider plugins — 1 mark

One project manages virtual machines in a public cloud, records at a separate DNS provider, and alert rules in a monitoring service. What makes this possible with a single declarative tool?

- A. Provider plugins expose each service's API as resource types, so one project can combine them.
- B. The tool manages other services once the cloud vendor has added them to its own API.
- C. Each service needs a separate project, because a single run cannot combine several providers.
- D. The tool signs in to each web console and repeats the clicks an administrator would make.

### L5 Q4 Diagram boxes and planned resources — 1 mark

An architecture diagram shows a load balancer, a group of database nodes, and a front end. The provisioning plan lists sixteen resources to add. What best explains the difference?

- A. The tool usually adds a hidden backup copy of each resource, so that rollback is possible.
- B. The plan lists each attribute of a resource, such as its size or tags, as a separate resource.
- C. The tool mirrors the provider's model, where one box can need several API objects.
- D. The plan counts each resource twice, so just eight of them will actually be created.

### L5 Q5 Sharing state in a team — 2 marks

A provisioning project's state lives on one engineer's laptop and covers the whole platform. Eight people now change the networks, databases and application servers at different rates. Which approach best fits the lecture's guidance?

- A. Give each engineer a personal copy of the state, and merge the copies at the end of each week.
- B. Keep one state for everything in the code repository, so that reviews also show its changes.
- C. Delete the state before each run, so the tool rebuilds its knowledge from the account every time.
- D. Use shared protected state, one run per state at a time, and split states by layer and change rate.

### L5 Q6 Competing rule definitions — 2 marks

A firewall group is defined with its rules written inline. A colleague adds more rules for the same group as separate rule resources. Each apply now reports changes, although nobody edited the code. What is the most likely cause and fix?

- A. Two definitions compete for the same rules; choose one modeling style for that group.
- B. The provider is reporting a temporary fault, and retrying the apply a few times usually settles it.
- C. The account has drifted on its own, and refreshing the state once will stop the repeated changes.
- D. Separate rule resources take priority over inline rules, so the colleague's rules win.

### L5 Q7 Create-time provisioning scripts — 2 marks

A server definition includes a script that installs and configures software when the server is first created. Later, the team edits the script to change a setting. What should they expect, and what fits larger setups?

- A. Existing servers are updated in place on the next apply, and inline scripts scale well to large setups.
- B. The tool reruns every script on each apply, so the scripts need to be safe to repeat on every server.
- C. Existing servers keep the old setup, as the script ran only at creation; big setups can use a configuration tool.
- D. The next apply fails, because a script attached to a resource is locked once that resource has been created.

### L5 Q8 Reviewing destructive plan entries — 2 marks

After a small change, the preview reports six resources to add and three to destroy. Which response is most appropriate before approving the apply?

- A. Approve it, because a plan that also adds new resources will recreate anything that it destroys.
- B. Check what would be destroyed and why; replacing a helper that holds no data can be harmless.
- C. Cancel it, since any plan that destroys resources means that the code was changed incorrectly.
- D. Skip the preview next time and apply directly, because a preview may list changes that will not happen.

### L5 Q9 Clients and a changing group of nodes — 4 marks

A search cluster runs on several nodes. Its web front end is configured with the address of each node. Adding a node means reconfiguring the front end, and when a node fails, some requests still reach it. Which design best addresses both problems?

- A. Keep the node list in the front end, generate it from provisioning outputs, and redeploy the front end after each change.
- B. Give each node a public address and publish the list, so that users can pick a responsive node themselves.
- C. Put a load balancer with health checks in front of the nodes, and point the front end at its stable address.
- D. Run larger nodes, which can make failures less likely, and keep the front end configured with the node addresses.

### L5 Q10 Rerunning derived configuration — 4 marks

Each node in a cluster needs a file listing all cluster members. A separate step generates and copies that file, and it reruns only when the node it targets changes. After the cluster grows from three to four nodes, the plan copies the file only to the new node. What is the best correction?

- A. Make the step rerun whenever the set of members changes, so every node receives the updated list.
- B. Keep the step as it is, because existing nodes can usually discover a new member without help.
- C. Recreate the four nodes on every apply, so that each one starts with a fresh file.
- D. Copy the updated file to the existing nodes by hand after each scale-up, and note it in the runbook.

## Lecture 6 Choosing cloud deployment options

### L6 Q1 Paying for functions — 1 mark

A team deploys a scheduled job on a function-as-a-service platform. For most of the month nothing invokes it. How is its compute typically charged under the model described in the lecture?

- A. By the execution time and memory used, so idle periods add no compute charge.
- B. By the hour from deployment, as with a virtual machine, whether or not it runs.
- C. By a flat monthly fee for each function that is deployed on the platform.
- D. By the size of the deployed code package, regardless of how often it is called.

### L6 Q2 Packaging as container images — 1 mark

The instructor prefers packaging applications as container images, even where a function platform can also run a plain code archive. What is the main reason given?

- A. Container images remove the need to grant runtime permissions to the application.
- B. A container image is usually cheaper to store in a registry than a code archive.
- C. One image can run as a function, on a container service, or on a VM with little change.
- D. Container images make the application immune to differences between cloud providers.

### L6 Q3 DNS under infrastructure as code — 1 mark

An organization wants its public DNS setup managed as infrastructure as code. Which division of responsibility matches the lecture?

- A. Keep DNS records manual, because DNS providers rarely offer an API for automation.
- B. Buy the domain outside the code; manage its records as code through the provider's API.
- C. Manage records as code only when DNS is hosted by the same cloud as the application.
- D. Include the domain purchase in the code, so that a destroy run also gives up the domain.

### L6 Q4 Small code change, large cost change — 1 mark

A teammate approves enabling a load balancer because the change adds only a few lines of infrastructure code. What else should the review consider?

- A. Nothing more, since a short change to a definition has a similarly small effect.
- B. Mainly the formatting, since cost questions can usually be left to the billing team.
- C. Whether traffic is high today, since a load balancer with no traffic is free of charge.
- D. The running cost, since a load balancer can be billed monthly even with no traffic.

### L6 Q5 Where scheduling lives — 2 marks

A batch job runs for a few minutes each hour. Design 1 keeps a container running all the time and lets the application decide when to start the job. Design 2 uses an external scheduler that starts the job on demand. Which comparison is most accurate?

- A. Design 1 is cheaper, since starting work on demand costs more than keeping one container running.
- B. Both use the same compute, since the platform bills for the schedule rather than running time.
- C. Design 2 uses compute only while the job runs; design 1 uses it for the whole time it stays up.
- D. Design 2 needs no permissions setup, since the platform scheduler can start any job by itself.

### L6 Q6 Console defaults and explicit definitions — 2 marks

A function created by hand in the web console wrote logs without any extra setup. The same function, recreated from infrastructure code, runs but writes no logs. What is the most likely explanation?

- A. Functions created from code cannot write logs, so a logging agent has to be installed.
- B. The console added default permissions and resources that the code must declare explicitly.
- C. Logs from code-created functions may be delayed by a day, so waiting is usually enough.
- D. The code-created function runs on a VM, so its logs stay on that machine's local disk.

### L6 Q7 Secrets in automated deployments — 2 marks

An application needs a database password at runtime. The infrastructure tool keeps a state record of the resources it manages. Which approach best follows the lecture's guidance?

- A. Set the password as an environment value in the definition, as the state sits in a private bucket.
- B. Build the password into the container image, so the definition and state can leave it out.
- C. Keep the password in state on purpose, so the tool can notice when someone changes it.
- D. Keep the value out of state, pass the app the secret's name, and let it read only that secret.

### L6 Q8 What a lower-level service asks of you — 2 marks

A team moves the same web application from a function service with a built-in URL to a container service. Which extra infrastructure will they most likely have to define?

- A. Network placement and firewall rules, because the containers get addresses in a network.
- B. Nothing extra, because both services hide networking and expose a public URL by default.
- C. A Kubernetes cluster, because a container service can only run containers inside one.
- D. Host operating-system patching, because the container service may expose its VMs to the team.

### L6 Q9 Choosing a compute platform — 4 marks

A small company runs a web app that gets a handful of requests per hour, with occasional short spikes, plus a background job that runs for a few minutes every hour. Both parts are small and already packaged as container images. The company has a tight budget and no existing Kubernetes platform. Which deployment best fits the trade-offs discussed in the lecture?

- A. A managed Kubernetes cluster behind a load balancer, since a cluster is the usual way to run two containers.
- B. Functions for both parts, a scheduled event for the job, and the function URL instead of a load balancer.
- C. An always-on container service for both parts behind a load balancer, keeping spare capacity for spikes.
- D. One large VM sized for the biggest spike, since a VM is usually cheaper than functions for low traffic.

### L6 Q10 Organizing alternative deployments — 4 marks

A team keeps three versions of one deployment (functions, a container service, and a VM) as separate infrastructure projects that all use the same image registry. Only some setups need a load balancer, and each apply currently builds and pushes the images. Which organization is most suitable?

- A. Give each project its own registry copy, enable the load balancer in every setup, and keep the image builds in the apply.
- B. Merge all three versions into one project to share the registry, and comment out the load balancer where it is not needed.
- C. Keep the registry in a shared project, add an off-by-default load balancer toggle, and build images in a separate script.
- D. Let each project create the registry when it is missing, and switch the load balancer on whenever traffic might need it.

## Lecture 7 Modules, testing, and automated quality checks

### L7 Q1 Integration tests for infrastructure code — 1 mark

Why does the lecture value integration tests on real targets more than unit tests for infrastructure code?

- A. Unit tests usually run too slowly to fit into a delivery pipeline for infrastructure code.
- B. Integration tests also check style and conventions, so a separate linter is no longer needed.
- C. Unit tests cannot be written for infrastructure code in any of the common tools.
- D. Most failures appear only when code meets a real system and its packages and services.

### L7 Q2 Module interface — 1 mark

In the lecture's view, what forms the interface of a reusable infrastructure module?

- A. The full set of resources it creates, which callers edit directly when they need changes
- B. The input parameters it publishes, with defaults, that callers set to adjust its behavior
- C. The folder layout of its source files, which callers copy into their own projects
- D. The commit history of its repository, which callers usually read to learn how to use it

### L7 Q3 Linters — 1 mark

An automation tool already refuses to run a definition with invalid syntax. What does adding a linter contribute?

- A. It replaces integration tests, since a definition that passes linting will behave correctly on real targets.
- B. It runs the definition against a temporary machine and reports which resources failed to start.
- C. It flags valid code that is risky or breaks agreed rules, such as a value parsed as an unexpected type.
- D. It can repeat the tool's syntax check earlier, but it usually reports nothing the tool would accept.

### L7 Q4 Modules as maintained products — 1 mark

A team plans to extract repeated infrastructure code into a module that other teams will use. Which view matches the lecture?

- A. A shared module is a product needing tests, docs and releases; it pays off as complexity and teams grow.
- B. A module is mainly a way to shorten files, so it needs no separate testing once the original code worked.
- C. Every project should start with modules, because modules have no maintenance cost compared with plain code.
- D. Modules mostly pay off for code published to public registries, much less for structure inside one company.

### L7 Q5 Order of pipeline checks — 2 marks

A delivery pipeline for infrastructure code runs linting, policy checks, smoke tests, a staging deployment with integration tests, and then production. Why are the static checks placed first?

- A. They catch many problems in seconds, before slower stages spend time or create real resources.
- B. They can find every problem a staging deployment would find, so later stages rarely fail.
- C. Production approval usually depends on how many lint warnings were fixed, more than on test results.
- D. Passing them first lets the later stages skip their own checks and finish the release faster.

### L7 Q6 Assessing a third-party module — 2 marks

A team finds a public module that does what it needs. Which assessment best fits the lecture's advice before depending on it?

- A. Prefer the module with the most parameters, since a larger interface usually signals higher quality.
- B. Use it if its download count is high, because popularity shows it was tested on your platforms.
- C. Check recent releases, issue fixes, and docs; if it looks inactive, consider insourcing a copy.
- D. Avoid public modules entirely, because code written by outsiders cannot be reviewed or adapted.

### L7 Q7 Providers and modules — 2 marks

A team wants to manage a new cloud service with code and also standardize how other teams use it. Which split of responsibilities matches the lecture's layering?

- A. Write a module that calls the service's API directly, and use a provider only to store shared default values.
- B. Use a provider for the service's API, and build a module that combines its resources into a reusable unit.
- C. Ask the cloud vendor for a module, since providers are usually written by each team for its own project.
- D. Treat provider and module as two names for the same layer, so either one can hold the team's conventions.

### L7 Q8 Policy as code — 2 marks

A security team wants every infrastructure project to tag resources with their environment and to stay below an agreed instance size. The code is syntactically valid and passes linting. Which approach fits best?

- A. Rely on reviewers to remember the rules, since automated checks can only find syntax errors.
- B. Add the rules as comments in each module, so users can read them before applying changes.
- C. Wait for monitoring to report oversized or untagged resources after they reach production.
- D. Define the rules once as policies and check them in every project's pipeline before release.

### L7 Q9 Adopting a breaking module release — 4 marks

Staging and production both use version 1.8.2 of a shared network module. Version 2.0.0 adds a feature the team needs and renames some inputs. How should the consuming team adopt it?

- A. Point both environments at the latest release, apply to production first since it needs the feature most, then fix staging.
- B. Edit the 1.8.2 code in place to add the feature, keeping the version number so no one has to update references.
- C. Switch to 2.0.0 everywhere at once; semantic versioning guarantees a major release will apply cleanly.
- D. Pin 2.0.0, update the renamed inputs, run lint and policy checks, apply to staging, test and monitor, then production.

### L7 Q10 Testing a module across platforms — 4 marks

An internal configuration module must support the company's Ubuntu and Rocky Linux servers, which start from company-prepared base images. Its only tests are unit tests that run on a laptop. Which testing plan best fits the lecture?

- A. Add more unit tests until coverage is complete, since they are fast and need no real machines.
- B. In the pipeline, run it on disposable containers or VMs from images like the company's, for each OS.
- C. Test on as many operating systems and clouds as possible first, since the module may be used elsewhere.
- D. Run it once by hand on a production server for each OS, and keep that server as the reference test target.

## Lecture 8 Module versioning and interface design

### L8 Q1 Semantic versioning — 1 mark

A module follows semantic versioning (major.minor.patch). Its authors release version 1.5.0 after 1.4.2. What should consumers expect?

- A. The release may remove or rename inputs, so existing callers must be updated first.
- B. It adds backward-compatible functionality, so current usage should keep working.
- C. It contains a bug fix alone, and no new functionality is available in this release.
- D. It is a test build that usually should not be used outside the authors' own team.

### L8 Q2 Explicit module versions — 1 mark

Why should an environment definition refer to an explicit module version rather than to "latest"?

- A. So a new module release cannot change the environment until its team chooses to upgrade.
- B. Because explicit versions download faster, which mainly shortens each deployment run.
- C. So the module authors can patch that same version in place whenever they find a bug.
- D. Because pinning makes the tool pick the newest compatible release on each run automatically.

### L8 Q3 Published module versions — 1 mark

A team published version 1.1 of a module through its release pipeline. A day later they find a bug in it. What is the appropriate response?

- A. Fix the code and overwrite the published 1.1, so consumers get the fix without a version change.
- B. Delete version 1.1 from the repository, so consumers can no longer deploy anything from it.
- C. Ask each consuming team to apply the fix to its own local copy of the module code.
- D. Fix it in the source, test it, and publish a new version such as 1.1.1, leaving 1.1 as it is.

### L8 Q4 Value of a module — 1 mark

Which module design is least likely to justify the extra layer it adds?

- A. A module that creates a network with its subnets, routes, and gateways from a few inputs
- B. A module that applies the company's disk, tagging, and network conventions to each new VM
- C. A module that wraps one resource and exposes nearly every setting of it as a parameter
- D. A module that combines web servers, a database, and placement rules into one application setup

### L8 Q5 Choosing module parameters — 2 marks

A team is writing an internal module that creates database servers for several application teams. Which approach to the module's parameters is most sound?

- A. Expose every setting of the underlying resources, because more parameters make a module easier to use.
- B. Hardcode the settings, so consumers request a module change for each difference they need.
- C. Add a parameter for anything a consumer might want one day, since unused parameters usually cost nothing.
- D. Expose what consumers truly vary, such as size and versions, and fix the rest; each parameter is a promise.

### L8 Q6 Open for extension — 2 marks

A web-server module must support a growing number of sites, each with its own host name and port. Which design applies the open-closed principle?

- A. Add a new conditional block to the module code each time a team requests another site.
- B. Accept a list of site definitions, so consumers add sites without changing the module.
- C. Copy the module for each new site and adjust the copy, so the sites can stay independent.
- D. Support one site in the module, and let teams edit server files by hand for extra sites.

### L8 Q7 Module contracts — 2 marks

A module installs and configures a MySQL database. A team asks for it to install PostgreSQL as well, selected by a parameter. What is the strongest design response?

- A. Build a separate module; the engines differ, and one interface would fill with engine-specific inputs.
- B. Add the parameter, because a module with more options can usually serve more consumers at little extra cost.
- C. Add the parameter, since an engine choice is a simple pass-through value, much like an instance size.
- D. Refuse the request, because a module must never gain new options once its first version is published.

### L8 Q8 Patching through parameters — 2 marks

A vulnerability is announced in the database package version used in every environment. The module that installs the package takes its version as a parameter. What is the most suitable response?

- A. Wait for a new module release, because a package version change requires new module code.
- B. Edit the module code in each environment's copy, so production can be patched before the others.
- C. Change the version value in the environment configurations and roll it out; no module release is needed.
- D. Hardcode the fixed version inside the module, so environments can no longer choose different versions.

### L8 Q9 Shared module across teams — 4 marks

A platform team owns a network module used by teams B, C, and D. Team B urgently needs a new optional feature, team C is still on an older version, and the platform team worries about breaking anyone. Which arrangement best balances speed and safety?

- A. Let team B contribute it under agreed tests and policy checks, release a new minor version, announce it, and let teams upgrade when ready.
- B. Let team B edit the module and republish the current version number, so consumers get the feature at once without editing their own definitions.
- C. Have team B fork the module into its own repository and maintain it there, since separate copies usually avoid coordination between the teams.
- D. Freeze the module until the teams agree on one roadmap, then require every consumer to upgrade to each new release on the day it is published.

### L8 Q10 Reusing and writing modules — 4 marks

An organization runs VMs on an on-premises virtualization platform and networks and databases in a public cloud. It is starting to codify this infrastructure and has several company conventions for VMs. Which plan uses modules best?

- A. Write internal modules for every component, including the cloud networks, so the company controls the code and depends on no external releases.
- B. Use public registry modules throughout, and apply company conventions such as tagging and disk sizing by hand, since they usually change too often.
- C. Use well-maintained public modules at pinned versions for generic parts, and write internal modules for company concepts such as a standard VM.
- D. Keep everything in one project without modules until the cloud and on-premises parts use identical tools, and then start splitting it up.

## Lecture 9 GitOps, pipelines, and team workflows

### L9 Q1 GitOps and continuous delivery — 1 mark

How does the lecture characterize GitOps?

- A. As a Kubernetes-only practice in which an agent in the cluster applies manifests from Git
- B. As continuous delivery applied to infrastructure and operations code kept in Git
- C. As a hosted service that stores repositories and runs their pipelines in one place
- D. As a branching model in which each environment gets its own long-lived Git branch

### L9 Q2 Pull-based delivery — 1 mark

In a pull-based GitOps setup, how do changes reach the infrastructure?

- A. A pipeline in the hosted Git service connects to each target and pushes the change
- B. An engineer pulls the repository to a laptop and applies the change from there
- C. An agent in or near the infrastructure regularly fetches the repository and applies it
- D. Each target server waits until an operator copies the new files onto it by hand

### L9 Q3 Repository ownership — 1 mark

In the cross-team workflow from the lecture, who merges another team's change into the main branch of the network team's repository?

- A. The team that wrote the change, as soon as its pull request passes the pipeline checks
- B. The pipeline itself, which merges each pull request automatically once its checks are green
- C. A central change board, which approves merges for every repository in the organization
- D. The network team that owns the repository, after it reviews the checked pull request

### L9 Q4 Continuous reconciliation — 1 mark

Besides declarative, versioned code and automated delivery, some definitions of GitOps add a controller that keeps reconciling the infrastructure with Git. How did the lecture treat this fourth principle?

- A. As essential, because GitOps without a controller inside a Kubernetes cluster is not GitOps
- B. As optional, because scheduled pipeline runs can do much of the same checking against Git
- C. As harmful, because a controller that keeps changing the infrastructure itself causes drift
- D. As a replacement for version control, because the controller stores the desired state itself

### L9 Q5 Push-based delivery — 2 marks

A team's pipelines run in a public hosted CI/CD service. They run the provisioning and configuration tools that push changes into the company's private infrastructure. What does this push model require the team to consider?

- A. The CI/CD service needs network access and credentials for the targets, which must be secured.
- B. Nothing beyond a pull model, because both models need the same access to the infrastructure.
- C. Pull requests stop working, because a push model delivers direct commits to the main branch instead.
- D. Changes can no longer be traced, because a pushed change leaves no record in the repository.

### L9 Q6 Pipelines as guardrails — 2 marks

Why does the lecture call a repository's CI/CD pipeline guardrails for the team that owns the repository?

- A. It deploys each pull request to production at once, so users find mistakes quickly.
- B. It replaces human review, so owners no longer look at changes that other teams propose.
- C. Its checks block changes that break the owners' rules, codifying what the owners know.
- D. It is maintained by a central platform team, so the owners cannot weaken its checks.

### L9 Q7 Releasing and deploying applications — 2 marks

An application pipeline tests each build and publishes it to an artifact repository. In the GitOps setup described in the lecture, what decides which application version runs in each environment?

- A. The application pipeline, which deploys each published build to every environment at once
- B. Engineers, who copy artifacts to servers by hand and note the versions in a shared document
- C. Each environment, which picks up the newest published artifact on its own schedule
- D. The infrastructure repository, where version bumps can be committed by people or automation

### L9 Q8 A complete record of change — 2 marks

After an outage, a team must find out which change reached production, who approved it, and whether its checks passed. Some recent changes were applied from engineers' laptops. Which practice gives the team a complete record in future?

- A. Deliver every change through reviewed commits and the pipeline, whose logs record each run.
- B. Ask engineers to post a summary in the team chat whenever they apply a change from a laptop.
- C. Take a snapshot of production every night, and compare snapshots when an incident happens.
- D. Keep the pipeline for routine work, but let senior engineers apply urgent changes directly.

### L9 Q9 Replacing tickets with pull requests — 4 marks

A database team often needs small network changes, such as an opened port or a new route, in the network team's infrastructure repository. Each request goes through tickets and takes days of back-and-forth for a change of a few lines. Both teams are technical. Which workflow best fits the lecture?

- A. Give the database team administrator access to the network devices, so it can make small changes itself and inform the network team afterwards.
- B. Let the database team push to the main branch of the network repository, so its changes deploy at once and the network team reviews them later.
- C. Let the database team open pull requests whose pipeline checks run without deploying; the network team reviews green ones and merging deploys them.
- D. Keep the tickets, but have the network team collect them for a weekly maintenance window, so that the requested changes are reviewed together.

### L9 Q10 Layer repositories and simple interfaces — 4 marks

An organization keeps its infrastructure in one repository per layer (network, machine images, server configuration, and application deployment), each owned by one team. Other teams often need to add simple entries, such as DNS records or batch jobs, to layers they do not own, while the owners keep refactoring the internals. Which organization best supports both kinds of change?

- A. Merge the layers into one repository that every team can change directly, so no team waits for an owner to act.
- B. Keep the internals with the owners, and expose simple data files that others change through checked pull requests.
- C. Let each team copy the layers it needs into its own repository and apply its copy independently of the owners.
- D. Freeze the internals and route outside requests through tickets, so that the owners make every change themselves.
