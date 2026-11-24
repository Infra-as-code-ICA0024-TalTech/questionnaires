# ICA0024 Infrastructure as Code

## Answer key and marking guidance for Lectures 1 to 9

**Instructor copy.** The student questionnaire contains 89 single-answer multiple-choice questions, 10 per lecture worth **20 marks** each, except Lecture 9 with 9 questions worth **18 marks**. In each lecture, Q1-Q4 carry 1 mark each, Q5-Q8 carry 2, and Q9-Q10 carry 4; in Lecture 9, Q5-Q7 carry 2 and Q8-Q9 carry 4. Scenarios also use multiple-choice answers.

Award the full question value for the correct choice and zero otherwise, with no negative marking. Explanations below provide feedback; students do not submit free-form answers. Questions assess principles, responsibilities, and design trade-offs without requiring product syntax. The [source map](Source_map.md) identifies the lecture concepts behind each question. Any pass threshold should follow the course assessment policy.

## Lecture 1 Infrastructure as Code concepts

### L1 Q1 Answer B — 1 mark

Compute executes workloads, storage retains data, and networking connects resources. The alternatives describe activities, environments, or application-level concerns rather than the three infrastructure pillars.

### L1 Q2 Answer C — 1 mark

A declarative definition expresses the intended state. Automation determines the operations needed from the declaration and actual state. Parallel execution may be possible, but it is not what makes a definition declarative, and declarations still have dependencies.

### L1 Q3 Answer A — 1 mark

Once the desired state is satisfied, repeating an idempotent operation under unchanged relevant conditions should cause no further managed-state changes. Checking the current state is compatible with idempotence; doing nothing without checking does not establish correctness.

### L1 Q4 Answer D — 1 mark

PaaS typically transfers more operating-system and runtime-platform maintenance to the provider. The exact boundary depends on the service. The application team still owns its business requirements and application code.

### L1 Q5 Answer C — 2 marks

Review and automated checks before application can catch mistakes, for example firewall rules codified in Git and checked by pipeline policies before they reached the devices. The commit history records who changed what, when, and why, and makes rollback possible. Version control alone neither applies changes nor restores deleted data: code lives in Git, and only automation delivers the change. Reviewed changes still need validation.

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

### L2 Q1 Answer D — 1 mark

An image provides the starting state for multiple instances. The instances can change independently after launch; those changes do not automatically rewrite the image.

### L2 Q2 Answer A — 1 mark

Image building prepares a reusable artifact. Deployment uses that artifact to create running instances. Producing a new image does not automatically update existing machines or eliminate instance-specific initialization.

### L2 Q3 Answer C — 1 mark

The problem is hidden manual changes and the lack of a maintained, repeatable creation process. A shared baseline or an automated, rebuildable image is not inherently an anti-pattern, even if the team calls it a golden image.

### L2 Q4 Answer B — 1 mark

Machine images must be compatible with the destination platform and processor architecture. A common intended baseline can require different artifacts or formats for different targets; the exact requirements depend on the target platforms.

### L2 Q5 Answer A — 2 marks

A stock image is a supplied starting point. A custom image adds selected software and configuration, providing a tested baseline and reducing repeated initialization. It still requires maintenance, instance-specific settings, and separate protection of persistent data.

### L2 Q6 Answer C — 2 marks

Build-time work becomes part of a reusable image; boot-time initialization can supply values specific to an instance or environment. Other divisions may be valid, but this one directly separates the stable shared baseline from the varying inputs. Boot-time initialization alone is not ongoing reconciliation.

### L2 Q7 Answer D — 2 marks

Typical Linux containers share a host kernel while isolating aspects of their execution environment. A VM has a guest kernel over virtualized hardware. Kernel sharing affects compatibility and isolation; neither approach guarantees that arbitrary images work on every platform.

### L2 Q8 Answer B — 2 marks

A snapshot captures state at a point in time, within its scope and consistency limits. It can support restoration but does not explain the intended build process or make hidden manual changes reviewable. Rebuildable definitions and data backups serve different purposes.

### L2 Q9 Answer C — 4 marks

A shared baseline reduces inconsistent copies while workload-specific definitions preserve useful differences. Updating source does not update existing artifacts or instances: affected images must be rebuilt, tested, and deliberately rolled out. Validation should cover both the policy and the workloads.

### L2 Q10 Answer A — 4 marks

Version-controlled instructions do not freeze external inputs such as base images and packages, so reproduction requires controlled versions and available artifacts. A built image is a versioned artifact: keeping the previous version allows a rollback, and each new image is tested before release. An immutable update builds and validates a new image, replaces instances deliberately, and protects persistent data through separate storage or a verified copy. Done this way, machines can be replaced in minutes while their data is preserved.

## Lecture 3 Server state and configuration organization

### L3 Q1 Answer B — 1 mark

An inventory identifies target hosts and groups and can associate relevant information with them. It supports selecting the appropriate targets for configuration; it is not a complete backup of their state.

### L3 Q2 Answer D — 1 mark

The system in the question manages explicitly declared resources. A resource outside that scope is not automatically declared absent, so unmanaged state can remain even after successful configuration.

### L3 Q3 Answer A — 1 mark

Grouping related responsibilities creates units that can be understood, reused, and maintained. Such units can still have dependencies and need integration testing; splitting files does not guarantee independence or parallelism.

### L3 Q4 Answer A — 1 mark

Agentless tools reach nodes through protocols that are already available, typically SSH or WinRM, so nothing extra has to be installed. Agent-based tools need an agent on each node, which can then apply configuration on its own schedule. Both kinds can be idempotent, both rely on network connectivity, and neither is limited to one operating system.

### L3 Q5 Answer D — 2 marks

Grouping selects the appropriate targets; reusable units define the configuration to apply. Composing a common baseline with workload-specific units avoids both duplicated baseline logic and installation of every workload on every host. No particular inventory syntax or folder layout is required.

### L3 Q6 Answer C — 2 marks

A running-state declaration describes a condition that may already hold. A restart request describes an operation. Repeated execution can therefore leave a healthy service undisturbed with the first approach and disrupt it with the second. Relevant changes can still justify a restart.

### L3 Q7 Answer B — 2 marks

Apply and validate compatible changes before activation, then reload when relevant state changed. This avoids repeated reloads and allows the service to consume a coherent configuration. A running process does not necessarily reread changed files automatically.

### L3 Q8 Answer C — 2 marks

Configuration checks establish selected resource conditions, not necessarily end-to-end behavior. A representative request can expose failures in connectivity, dependencies, or application behavior that file, package, and process checks miss. Configuration success and functional failure can coexist.

### L3 Q9 Answer D — 4 marks

Coherent units support reuse and focused review, but extra interfaces and indirection can obscure dependencies and effective values. Documented inputs, visible composition, clear override rules, and integration checks address those costs. A small system may still be adequately served by a single file.

### L3 Q10 Answer B — 4 marks

Directory existence is not evidence of the desired software version or a complete installation. Repeated no-ops can preserve an incorrect state. Compare meaningful observed state with intended state, update when needed, and verify the result; changing a timestamp or log does not establish actual configuration.

## Lecture 4 Resilience and verifying configuration code

### L4 Q1 Answer C — 1 mark

Chaos engineering deliberately introduces failures, such as terminating servers or whole zones, to prove continuously that automated recovery works and that users do not notice. Stopping a server to find its owner is the scream test, not chaos engineering. Deliberate failures depend on monitoring and alerting rather than replacing them.

### L4 Q2 Answer A — 1 mark

A region is a geographic location; its availability zones are physically separate data centers located close to each other. Placing instances in different zones lets the service survive the loss of one data center. Extra instances in a single zone share that zone's failure, and moving every instance to a different region is not needed for this goal.

### L4 Q3 Answer D — 1 mark

A scream test stops, rather than deletes, seemingly unused infrastructure and waits to see whether anyone complains. Silence suggests the resource is unused; a complaint identifies a dependency or owner. Because the resource is only stopped, it can be brought back. The same approach can also check whether monitoring and alerting notice the outage.

### L4 Q4 Answer B — 1 mark

A good rule of thumb is to work on code that fits in your head. When a playbook grows to several hundred lines, split it into included task files or roles, separate concerns such as web servers, databases, and batch jobs, and keep things that change for the same reason, such as a service's tasks and its handler, close together. Comments do not reduce the size, one file per task scatters related parts, and per-type copies duplicate code that then diverges.

### L4 Q5 Answer B — 2 marks

Repeatedly applying changes to one machine accumulates state, so a step that only worked because of earlier leftovers can go unnoticed. Testing regularly from an empty state, as well as on an already provisioned machine, shows the code works on any compatible new machine. Running twice on the same machine or adding retries does not reveal the missing step.

### L4 Q6 Answer D — 2 marks

A service can be configured and running yet fail to come back after a reboot or service restart. Testing restarts shows the provisioned setup is valid beyond the first run. Once restarts are known to work, monitoring can restart unresponsive servers automatically. A restart does not replace functional checks, and it does not reset a machine to its image.

### L4 Q7 Answer A — 2 marks

When two tasks set the same resource to different states, each run undoes the other and reports a change, so the definition never converges. Giving the directory one intended state, managed in one place, restores a clean re-run with no changes. Ignoring constant changes hides real problems, and rebuilding or restarting does not remove the conflict in the code.

### L4 Q8 Answer C — 2 marks

Acceptance criteria expressed as tests and policies act as guardrails: generated code is revised until it passes them, an approach known as loop engineering. Self-confirmation by the same assistant, a single successful run in one environment, or trust in a stronger model do not show that the code meets the requirements. The team still needs to understand the tests and the code.

### L4 Q9 Answer A — 4 marks

When servers can be rebuilt from code, are spread across availability zones, and are monitored, losing one is not a disaster. Rehearsing failures, as in chaos engineering, proves that recovery works, and zero-downtime methods such as blue-green deployment keep changes invisible to users. Maintenance windows and Friday rules work around missing automation, manual snapshot restores keep the outage, and chaos without monitoring is reckless.

### L4 Q10 Answer D — 4 marks

Secrets such as private keys do not belong in version control, even in a private repository. A bug found in review should be fixed together with a test that would have caught it, so it cannot silently return. A module with built-in state management is more reliable than a shell command with a guard. AI suggestions still need review: an unrequested split of a small playbook adds structure without benefit.

## Lecture 5 Declarative cloud provisioning and state

### L5 Q1 Answer B — 1 mark

A data lookup queries information about an object that already exists and is managed somewhere else, such as a shared network or the latest matching image. The definition can then use that information, but the tool does not take ownership of the object or create, change or delete it. The lookup runs again on later runs, so a "latest" query can return a newer image.

### L5 Q2 Answer D — 1 mark

A tool that keeps state compares the code, the recorded state and the real infrastructure. A resource that is recorded in state but missing from the code is treated as no longer wanted, so the plan proposes destroying it. Resources the tool never created are not in its state and are left alone. Leaving the server running is the behavior of a tool that manages only what is currently declared.

### L5 Q3 Answer A — 1 mark

Provider plugins translate declared resources into calls to a particular service's API. Because providers are independent, one project and one run can combine resources from a cloud, a DNS provider, a CDN or a monitoring service. The large community library of providers is a main reason such tools are widely used. They work through APIs, not by automating web consoles.

### L5 Q4 Answer C — 1 mark

A declarative provisioning tool reflects the resource model of the provider it talks to. One diagram box, such as a load balancer, can need several API objects: the balancer, a listener, a target group and one attachment per node, plus firewall rules and keys. The complexity comes from the provider's model, so you need to understand that model to write the definition.

### L5 Q5 Answer D — 2 marks

When several people share a project, state should live in shared storage rather than on one laptop, and only one run should change a given state at a time. Splitting state by layer and frequency of change reduces waiting and limits how much each run can affect. State can contain sensitive values, such as a generated private key, so it needs protection. Personal copies or a deleted state lose track of what the tool created.

### L5 Q6 Answer A — 2 marks

Some providers let you model the same thing as nested blocks inside a resource or as separate resources linked to it. Using both for one group means two definitions claim the same rules, so each apply undoes the other's result and a change loop follows. Pick one style for that group; the separate-resource style is now usually preferred for this case.

### L5 Q7 Answer C — 2 marks

A create-time provisioning script runs when the resource is created and is not rerun on later applies while the resource exists, so editing it does not change existing servers. Such scripts mix imperative steps into a declarative definition. They can work for small setups, but larger ones can keep the provisioning tool for machines and use a configuration tool, or a prebuilt image, for the software inside them.

### L5 Q8 Answer B — 2 marks

A plan is a preview, so use it to check what each destroy or replace entry refers to and why it happens. Often the destroyed items are helper resources that only run commands and can only be replaced, so recreating them loses nothing. Destroying a resource that holds data or serves traffic needs much more care. Destroy entries are not automatically wrong, and adding resources does not undo a deletion.

### L5 Q9 Answer C — 4 marks

A load balancer gives clients one stable endpoint, so nodes can be added or replaced without reconfiguring the front end. Its health checks take failing nodes out of rotation, so requests stop reaching them. It can also absorb traffic spikes. Generating the node list automatically still needs a redeploy on each change and does nothing about failures. Larger nodes do not remove failures, and publishing node addresses pushes the problem onto users.

### L5 Q10 Answer A — 4 marks

The file depends on the whole membership, so the step should rerun when the membership changes, for example by including the node identifiers in what triggers it. Every node then gets the updated list, not only the new one. Reading the plan reveals this mistake before it is applied. Recreating all nodes on every run is disruptive, manual copying breaks reproducibility, and assuming automatic discovery ignores how the cluster is configured.

## Lecture 6 Choosing cloud deployment options

### L6 Q1 Answer A — 1 mark

Function-as-a-service platforms charge for the compute actually used while code runs, measured by execution time and allocated memory. A deployed function that is not invoked adds no compute charge. This makes functions very cheap for low or sporadic load, although high sustained traffic can make them expensive.

### L6 Q2 Answer C — 1 mark

A container image is a portable package: the same image can run as a function, on a container service, or on a VM, so changing the platform does not mean repackaging the application. The image may need small adjustments for a particular platform. It does not remove permission needs or provider differences, and storage cost is not the reason given.

### L6 Q3 Answer B — 1 mark

Purchasing a domain is usually a one-time business action outside infrastructure code. The DNS records, whether hosted by the cloud provider or an external DNS service, are managed through an API and can be defined and reviewed as code. Hosting DNS with another provider does not prevent this.

### L6 Q4 Answer D — 1 mark

A design change that looks small in code can change the running cost a lot. A load balancer is billed for as long as it exists, even with no traffic, while a function URL or direct public address may cost little or nothing. Reviewers should weigh the cost and the traffic actually expected, not just the size of the diff.

### L6 Q5 Answer C — 2 marks

A container that runs all the time and handles its own schedule uses compute for its whole lifetime, even between jobs. Moving the scheduling to an external service or timer means the job runs, and is paid for, only when needed. The scheduler still needs explicit permission to start the job.

### L6 Q6 Answer B — 2 marks

Web consoles often create supporting resources and permissions, such as permission to write logs, automatically. Infrastructure code creates only what it declares, so the role, its permissions, and the log group must be defined explicitly. This makes the setup visible and reviewable but means console defaults cannot be assumed.

### L6 Q7 Answer D — 2 marks

Secret values should not be written into the tool's state or into plain configuration, where anyone with access to them could read the secret. Store the value in a secrets service, give the application only a reference such as the secret's name, and grant its identity read access to that specific secret. Baking secrets into images or relying on a private state bucket still spreads the value.

### L6 Q8 Answer A — 2 marks

A function service with a built-in URL handles networking for you. A container service is a lower-level service: containers get addresses inside a network, so the team must choose the network and subnets and define firewall rules, or the containers cannot be reached. The provider still manages the hosts, and no Kubernetes cluster is needed.

### L6 Q9 Answer B — 4 marks

With low, bursty traffic and a short periodic job, pay-per-execution functions scale with demand and cost almost nothing while idle. A scheduled event starts the job only when needed, and the built-in function URL avoids the fixed cost of a load balancer. A shared cluster could grow with the company later, but like always-on containers or a VM sized for peak load it pays for idle capacity every hour, which is hard to justify on a tight budget without an existing platform.

### L6 Q10 Answer C — 4 marks

A resource used by several projects, such as a shared registry, is best managed once in its own project, with each deployment referring to it. A toggle that is off by default makes the costly load balancer an explicit, reviewable choice instead of manual commenting or a vague rule. Building and pushing images is an imperative build step, so a separate script or pipeline keeps the infrastructure definition focused on the desired state.

## Lecture 7 Modules, testing, and automated quality checks

### L7 Q1 Answer D — 1 mark

Infrastructure code mostly orchestrates real systems, so its typical failures appear only when it runs against a target: different distributions ship different packages, paths, and service behavior. Unit tests can be written, but they exercise little of that. Integration tests do not replace linters, which catch a different class of problems before anything runs.

### L7 Q2 Answer B — 1 mark

A module's published parameters and their defaults are how users interact with it: defaults give a working result, and overridable inputs act as extension points. The internal resources and file layout are implementation details that callers should not need to edit or copy. Commit history explains changes but is not the interface.

### L7 Q3 Answer C — 1 mark

The tool's own parser already rejects invalid syntax. A linter applies further rules to code that is syntactically valid, catching risky constructs, convention violations, deprecated usage, or ambiguous values such as a number that some parsers read as a string. It is a static check and does not replace running the code on real targets.

### L7 Q4 Answer A — 1 mark

A shared module is a software product: good modules need tests, documentation, examples, a release process, and ongoing effort. That cost is justified as infrastructure complexity and the number of teams grow, because modules also make delegation and knowledge transfer easier. Small setups may not need modules, and modules are also useful inside one organization.

### L7 Q5 Answer A — 2 marks

Linting and policy checks are fast and need no infrastructure, so placing them first gives quick feedback and stops obvious problems before costly stages create resources. They cannot replace deployment and integration tests, which find problems that only appear on real targets. Each stage still runs its own checks.

### L7 Q6 Answer C — 2 marks

Signs of a healthy module include recent releases, active issue and security fixing, an evolving interface, and good documentation and examples. If a module looks inactive, its code can still be insourced, adapted, and maintained by the team. Download counts mostly reflect how widely the underlying software is used, not that the module was tested on your platforms; the number of parameters is not a quality measure either.

### L7 Q7 Answer B — 2 marks

A provider, or a library of tasks, is the integration layer that turns definitions into API calls for a platform. A module sits one level higher: it combines those resources with the organization's choices into a reusable unit with an interface. Conventions belong in the module, not in the provider.

### L7 Q8 Answer D — 2 marks

Rules such as required tags, size limits, or approved providers are valid code from the tool's and linter's point of view, so they need a policy engine. Defining them once as policy as code lets the same organization-wide rules run automatically in every project's pipeline and block a release that violates them. Comments and reviewer memory are not enforced, and monitoring catches the problem only after it has reached production.

### L7 Q9 Answer D — 4 marks

A major version signals breaking changes, so the team should pin the new exact version and adapt its inputs. The change should then move through a staged pipeline: automated lint and policy checks, a lower environment such as staging, tests and monitoring, and only then production. Applying to production first, assuming a major release is safe, or changing released code without a new version all remove the predictability that versioning provides.

### L7 Q10 Answer B — 4 marks

Unit tests add little for infrastructure code because the behavior that breaks depends on the real target: package names, defaults, and libraries differ between distributions. Integration tests should run automatically in the pipeline on disposable containers or VMs built from images that match the organization's real baselines, one per supported platform. Testing every possible platform is costly and unnecessary for an internal module, and production servers should not serve as test targets.

## Lecture 8 Module versioning and interface design

### L8 Q1 Answer B — 1 mark

In semantic versioning, a minor increment signals new functionality that is backward compatible, so existing usage should keep working. Breaking changes call for a major increment, and a patch increment signals a fix that does not change the interface. The scheme sets shared expectations between module authors and consumers.

### L8 Q2 Answer A — 1 mark

Depending on an explicit version means the environment changes only when its owners deliberately upgrade and test the new version. Referring to "latest" puts the environment at the mercy of the module authors: any new release can change or break it. Published versions are not patched in place, and pinning does not pick newer releases.

### L8 Q3 Answer D — 1 mark

A published version is a frozen, tested point in time that consumers rely on. Fixes go into the source, pass the release pipeline again, and appear as a new version, here a patch release. Overwriting a published version silently changes what pinned consumers deploy, and removing it or asking consumers to patch copies breaks the shared release process.

### L8 Q4 Answer C — 1 mark

A module that manages a single resource and passes nearly every setting through adds indirection without capturing any knowledge; using the resource directly is usually simpler. Modules earn their place when they combine many related resources, encode the organization's conventions, or package a repeated composition. Such a single-resource module is over-designed.

### L8 Q5 Answer D — 2 marks

Parameters should cover what consumers legitimately need to vary, such as size, security-relevant versions, and naming, while the rest stays fixed inside the module. Each parameter is a promise the authors must keep supporting, so unneeded parameters add logic and maintenance burden. Hardcoding everything forces a module change for every ordinary difference. Internal modules can usually expose fewer parameters than public ones because their consumers are known.

### L8 Q6 Answer B — 2 marks

The open-closed principle keeps a module open for extension and closed for modification. A list of site definitions is an extension point: consumers add sites by changing their inputs, and the module code stays the same. Adding conditionals or copying the module changes or duplicates its code for each request, and manual edits bypass the module.

### L8 Q7 Answer A — 2 marks

MySQL and PostgreSQL need different configuration, so supporting both behind one parameter roughly doubles the module's logic and fills its interface with inputs that apply to only one engine. That is a different contract and is better served by a separate module. An instance size is a simple pass-through value; an engine choice is not. Modules can gain options in new versions, so refusing all change is not the principle.

### L8 Q8 Answer C — 2 marks

When a patchable package version is a module parameter, patching becomes a configuration change in each environment, rolled out through the usual process; the module code and its release stay unchanged. The environments share the module's structure while their parameter values differ. A new module release is needed only when the fix changes the module's structure or logic, such as a major package upgrade.

### L8 Q9 Answer A — 4 marks

With shared ownership and agreed guardrails (tests, static and policy checks, and test infrastructure), any team can contribute a change safely. Releasing it as a new backward-compatible version and announcing it lets team B adopt it at once while teams C and D upgrade on their own schedule. Republishing an existing version breaks the isolation that pinned versions provide, forks let the copies diverge, and forced upgrades remove the consumers' control.

### L8 Q10 Answer C — 4 marks

Start by checking the available providers and existing modules: a well-maintained public module for a generic component, such as a cloud network, saves effort and testing and can be used at a pinned version. Internal modules are worth writing for concepts specific to the organization that recur, such as a standard VM with its disk, tagging, and network conventions. Rewriting generic components in-house duplicates work, manual conventions drift, and waiting for identical tools is not required to modularize.

## Lecture 9 GitOps, pipelines, and team workflows

### L9 Q1 Answer B — 1 mark

GitOps is continuous delivery applied to a different type of code: infrastructure, configuration, and operations code kept in Git and delivered through automation. It is not limited to Kubernetes; servers, cloud resources, and other infrastructure can be managed the same way. Git hosting services provide the pipelines, but GitOps is the practice rather than the service, and it is not a branching model.

### L9 Q2 Answer C — 1 mark

In the pull model, a component running inside or near the infrastructure, such as a Puppet agent, ansible-pull, or Argo CD, periodically pulls the repository and applies the changes. Because it lives close to the infrastructure, it holds the permissions there. A pipeline that connects to the targets is the push model, and changes applied by hand or from a laptop bypass automated delivery.

### L9 Q3 Answer D — 1 mark

The team that owns a repository defines its structure, pipelines, and rules, and only it can push or merge to the main branch. Other teams submit pull requests; the pipeline checks them without deploying, and the owners review the green request and merge it, which triggers delivery. The pipeline informs the decision but does not replace the owners, and the aim is to avoid slow, central approval paths.

### L9 Q4 Answer B — 1 mark

The setup has the three core principles: declarative code, versioned and immutable code in Git, and automatic delivery. A fourth principle, a desired state controller that keeps checking the target against Git, is optional: GitOps works without it, and scheduled pipeline runs give much of the same verification, though only at each run rather than continuously. GitOps is not limited to Kubernetes, scheduled runs correct drift rather than cause it, and the desired state stays in Git.

### L9 Q5 Answer A — 2 marks

In the push model, the CI/CD service runs tools such as Terraform, Ansible, or Helm and connects directly to the infrastructure, so it needs network access and credentials for the targets. When the CI/CD service is public rather than internal, that access must be secured carefully. Pull requests and commit history work the same way in both models, and either model can work, depending on the tools and security requirements.

### L9 Q6 Answer C — 2 marks

The pipeline's checks, such as syntax, policy, security, and vulnerability checks, block any change that breaks the owning team's rules. The pipeline definition is code stored in the same repository and maintained by that team, so it codifies the team's knowledge. Pull request pipelines verify without deploying, and the owners still review complex or risky changes, but much of the routine review is delegated to automation.

### L9 Q7 Answer A — 2 marks

The commit history shows who changed what and why, the pull request shows the review, and the pipeline logs show when each change ran and with what result; observability then shows the state of the infrastructure. The record is complete only when automation is the single path for changes. Changes applied from laptops or directly by senior engineers bypass it, and chat messages or snapshots do not show who approved a change or whether its checks passed. Emergency access, if a team needs it, should still leave a commit afterwards, so that the code and the record catch up with the change.

### L9 Q8 Answer C — 4 marks

In GitOps, self-service means pull requests to the owning team's repository instead of the back-and-forth of tickets between teams. The owners' pipeline checks each request automatically and gives feedback without deploying; the owners review a green request when they can and merge it, and the merge delivers the change. The owners keep control of the main branch while delegating implementation to the requesting team and much of the review to automation. Direct device access or direct pushes remove that control, and batching tickets keeps the delays.

### L9 Q9 Answer B — 4 marks

The owning team stays responsible for the complex internals of its layer, but changes that other teams need often should be easy to make: simple interface files such as YAML or JSON in the repository, sometimes a separate repository or a self-service portal, changed through pull requests that the owners' pipeline checks. In one real case, batch jobs moved into a repository that the data warehouse team could change under policy and security checks, which ended the waiting. A shared repository without owners, private copies, and tickets for every change each lose either control or flow.

## Interpreting the results

| Questions | Understanding to revisit |
|---|---|
| L1 Q2 Q3 Q6; L3 Q2 Q6 Q10 | Desired state, idempotence, managed scope, and convergence |
| L1 Q5 Q8 Q9 Q10 | Reviewable definitions, separation of concerns, dependencies, and environment differences |
| L2 Q1 Q2 Q5 Q6 Q8 | Images, initialization, snapshots, and rebuildability |
| L2 Q3 Q9 Q10 | Maintained image definitions, shared baselines, reproducible inputs, and deliberate rollout |
| L2 Q4 Q7 | Compatibility and isolation boundaries |
| L3 Q1 Q4 | Inventory and how tools reach managed nodes |
| L3 Q3 Q5 Q9 | Reusable units and codebase organization trade-offs |
| L3 Q7 Q8 Q10 | Change-aware operations and verification of intended outcomes |
| L4 | Resilience, testing from clean and provisioned states, code organization, and safe changes |
| L5 | Provisioning state, plans, providers, and lookups of existing resources |
| L6 | Choosing and organizing cloud deployment options, cost, and secrets |
| L7 | Modules as products, providers versus modules, testing, linting, and policy checks |
| L8 | Module versioning, releases, and interface design |
| L9 | GitOps principles, pull and push delivery, cross-team pull requests, pipelines as guardrails, and repository ownership |

For an oral follow-up, change one assumption in a scenario and ask the student to explain how the design or outcome changes. Assess transferable reasoning rather than recall of a command or a demo file.
