# [Helm](https://helm.sh/)

The package manager for Kubernetes.

Helm is the best way to find, share, and use software built for Kubernetes.

Helm helps you manage Kubernetes applications - Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.

Charts are easy to create, version, share, and publish - so starting using Helm and stop the copy-and-paste.

Helm is a graduated project in the CNCF and is maintained by the Helm community.

## Helm Architecture

### The Purpose of Helm

Helm is a tool for managing Kubernetes packages called charts, Helm can do the following:

* Create new charts from scratch
* Package charts into chart archive (tgz) files
* Interact with chart repositories where charts are stored
* Install and uninstall charts into an existing Kubernetes cluster
* Manage the release cycle of charts that have been installed with Helm

For Helm, there are three important concepts:

1. The chart is bundle of information necessary to create an instance of a Kubernetes application.
2. The config contains configuration information that can be merged into a packaged chart to create a releasble object.
3. A release is a running instance of a chart, combinded with a specific config.

### Components

Helm is an executable which is implemented into two distinct parts:

The Helm Client is a command-line client for end users. The client is responsible for the following:

* Local chart development
* Managing repositories
* Managing releases
* Interfacing with the Helm library
  * Sending charts to be installed
  * Requesting upgrading or uninstalling of existing releases

The Helm Library provides the logic for executing all Helm operations. It interfaces with the Kubernetes API server and provides the following capability:

* Combining a chart and configuration to build a release
* Installing charts into Kubernetes, and providing the subsequent release object
* Upgrading and uninstalling charts by interacting with Kubernetes

The standalone Helm library encapsulates the Helm logic so that it can be leveraged by different clients.

### Implementation

The Helm client an library is written in the Go programming language.

The library uses the Kubernetes client library to communicate with Kubernetes. Currently, that library uses REST+JSON. It stores information in Secrets located inside of Kubernetes. It does not need its own database.

Configuration files are, when possible, written in YAML.

---

### Reference
- Helm, https://helm.sh/, 2023-09-08-Fri.
- Helm Architecture, https://helm.sh/docs/topics/architecture/, 2023-09-08-Fri.
