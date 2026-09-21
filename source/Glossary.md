# ICA0024 Concept glossary

A study reference for Lectures 1-3. Terms explain the principles used in the questionnaires, without requiring product-specific syntax. Entries are grouped by lecture and ordered alphabetically within each group. Related concepts may be useful in more than one lecture.

## Lecture 1: Infrastructure as Code concepts

### Actual state

The observed condition of infrastructure at a particular time. It can differ from the desired state because of manual changes, failures, incomplete deployment, or changes outside the automation's control.

### Configuration drift

A difference between actual managed configuration and its intended baseline. A difference between environments is not automatically drift: explicitly approved differences, such as production capacity, can be intentional.

### Convergence

The process of bringing actual state into agreement with desired state. An operation that does nothing repeatedly may be idempotent but still fail to converge if the starting state is incorrect.

### Declarative configuration

A description of the state that should exist, leaving automation to determine the necessary operations. Declaring a result does not eliminate dependencies or guarantee that every operation can run in parallel.

### Dependency

A relationship in which one resource or operation needs another resource or its output. For example, configuring a new server may require its assigned address. Expressing this relationship is more reliable than relying on file order or copied values.

### Desired state

The intended condition of the resources being managed, expressed in maintained definitions and configuration values. It is the reference against which actual state is compared; it may describe only part of a system.

### Idempotence

The property that repeating an operation after it has reached its result produces no further state changes under unchanged relevant conditions. Checking state is compatible with idempotence. An unchanged result alone does not prove that the state is correct.

### Immutable infrastructure

An approach in which deployed instances are replaced with newly prepared instances when changes are needed. Persistent application data must survive replacement through separately managed storage or a tested migration or recovery process.

### Imperative configuration

Instructions describing operations to perform and their order. Their effects can depend on the starting state. An imperative procedure can be designed to be idempotent; declarative and idempotent describe different properties.

### Infrastructure as Code (IaC)

Managing infrastructure through maintained, machine-readable definitions that can be versioned, reviewed, validated, and applied repeatedly. Keeping a file in version control does not by itself guarantee correct automation or reproducible external inputs.

### Infrastructure as a Service (IaaS)

A service model that provides infrastructure resources such as virtual machines, storage, and networking. Customers typically manage guest operating systems and application software; the precise responsibility boundary depends on the service.

### Infrastructure pillars

Compute, storage, and network. Compute executes workloads, storage retains data, and networking connects resources. These are infrastructure capabilities rather than names of tools or deployment environments.

### Mutable infrastructure

An approach in which changes are applied to existing running instances. It can support targeted updates, but the process must manage drift and account for the state already present on each instance.

### Platform as a Service (PaaS)

A service model that provides a managed platform for deploying applications. Compared with IaaS, more operating-system and runtime maintenance typically moves to the provider, while the application team retains responsibility for its application and requirements.

### Source of truth

The authoritative maintained definition or record for a particular kind of information. Dependent configuration should obtain that information through a clear relationship rather than through independently edited copies. Authority does not remove the need to inspect actual state.

### Version control

Recording changes to definitions over time so they can be reviewed, compared, and traced. Restoring an earlier source revision can support recovery planning, but it does not automatically restore deleted data or reverse infrastructure changes safely.

## Lecture 2: Images and machine initialization

### Base image

An image used as the starting point for another image. A shared organizational base can contain a common baseline, while derived images add workload-specific software. Updating the base does not automatically update derived images or running instances.

### Boot-time initialization

Configuration performed when an instance starts, often to supply its identity or environment-specific values. Initialization and ongoing state reconciliation are different responsibilities; a first-start action is not automatically a continuous configuration check.

### Build-time configuration

Software installation and configuration performed while preparing an image. The result becomes part of a reusable artifact. Common, relatively stable requirements are often prepared here to reduce repeated work when instances start.

### Container

An isolated execution environment for application processes. Typical Linux containers share a host Linux kernel, unlike virtual machines with their own guest kernels. This affects compatibility and the isolation boundary; sharing a kernel does not mean having no isolation.

### Custom image

An image prepared with selected organizational or workload-specific software and configuration. It can provide a tested common starting state and reduce launch-time setup. Its usefulness depends on maintaining and validating its build process.

### Hypervisor

Software that provides and manages virtualized hardware on which virtual machines run. A hypervisor can run directly on physical hardware or within a host operating system, depending on its design.

### Image compatibility

Whether an image is suitable for a target platform, image format, and processor architecture. Equivalent intended software baselines may need different image artifacts for different targets; one image is not automatically portable everywhere.

### Image hierarchy

An organization of image definitions into shared bases and specialized descendants. It reduces duplicated baseline logic, but changes still require rebuilding and testing affected descendants and deliberately updating deployed instances.

### Machine image

A reusable artifact containing a starting operating-system and software state for a machine. Multiple instances can start from the same image and later diverge. Instance changes do not automatically modify the source image.

### Persistent data

Application information that must outlive a process or replaceable instance, such as user records. Image replacement must account for this data separately; recreating software is not the same as recovering application data.

### Rebuildability

The ability to recreate a system or artifact through a maintained, understood process rather than relying on undocumented manual changes. Rebuildability does not necessarily imply byte-for-byte identical output if the process uses changing external inputs.

### Reproducibility

The ability to obtain the same specified result from controlled inputs and a defined process. For matching software versions, the base image and dependencies must be controlled as well as the instructions. Exact binary reproducibility may require additional controls.

### Snapshot

A point-in-time capture of state, subject to the scope and consistency of the snapshot mechanism. It can support restoration or cloning, but does not explain how that state was constructed or replace maintained build definitions.

### Stock image

A supplied starting image, often provided by an operating-system or platform vendor. It can be used directly or customized. Its suitability and version still need to be selected and checked for the intended workload.

### Virtual machine (VM)

A machine-like environment with virtualized hardware and a guest operating system, including its own kernel. It consumes resources from an underlying host and can have a lifecycle independent of other virtual machines on that host.

## Lecture 3: Server state and configuration organization

### Change detection

Determining whether relevant observed or generated configuration differs from the intended result. Meaningful checks can trigger necessary updates or reloads. The presence of a directory alone does not establish that the intended software version is installed.

### Composition

Combining smaller configuration units into a complete deployment definition. The composition should make selected units, their inputs, and their relationships understandable; breaking a system into files does not automatically produce clear boundaries.

### Configuration baseline

An agreed starting set of settings and software requirements for a class of systems. A shared baseline can be combined with workload-specific requirements and approved environment differences. It must be maintained and checked against actual systems.

### Configuration override

A value that intentionally replaces a default or a value from another configuration layer. Clear, documented precedence rules are needed to explain which value takes effect and to prevent hidden conflicts.

### Configuration parameter

An explicit input that varies the behavior of a reusable definition, such as capacity or an environment-specific endpoint. Parameters allow shared logic to remain common while keeping intended differences visible and reviewable.

### Default value

A value used when no higher-priority value is supplied under the configuration scheme's rules. Useful defaults simplify reuse, but they should not conceal required choices or make the effective configuration hard to understand.

### Environment-specific configuration

Values and deliberate variations associated with an environment such as development or production. Keeping these separate from shared logic makes differences easier to review without independently maintaining complete copies of the same definitions.

### Functional verification

Checking that the system performs an intended behavior, such as serving a user request or accessing its database. Successful configuration operations do not by themselves establish that the full application works.

### Host group

A named selection of machines sharing a relevant purpose or property, such as web servers or all machines in one environment. Groups help apply common configuration broadly and specialized configuration only to the appropriate targets.

### Inventory

A maintained representation of managed hosts, groups, and relevant targeting information. It supports selecting and reaching configuration targets. It may be supplied statically or derived from current infrastructure information and is not a complete snapshot of server state.

### Partial state management

Managing only the resources or properties explicitly included in the automation's scope. Unmentioned resources may remain unmanaged; their omission is not automatically a request to remove them or proof that they meet a complete baseline.

### Reusable configuration unit

A coherent package of configuration responsibilities and supporting resources, sometimes called a role or module. Clear inputs and boundaries support reuse and focused maintenance. Units can still depend on one another and need integration checks.

### Separation of concerns

Organizing definitions around distinct responsibilities, for example resource creation, server configuration, and functional verification. This can improve ownership and review without requiring separate products or repositories for every concern.

### Service reload and restart

A reload asks a service to reread configuration where that behavior is supported; a restart stops and starts the service. The appropriate action depends on the service and change. Running either action unconditionally can introduce unnecessary work or disruption.
