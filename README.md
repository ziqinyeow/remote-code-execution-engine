# Remote Code Execution Engine

## Overview

- Full stack orchestrated microservice-based application
- Autoscaling feature with Kubernetes
- Messaging queue protocol
- Sleek user interface
- Multiple languages support:
  - Javascript
  - Python
  - Java
  - C++

## Branch

- [synchronous-docker-only](https://github.com/ziqinyeow/remote-code-execution-engine/tree/synchronous-docker-only) 📙
- [asynchronous-docker-kubernetes](https://github.com/ziqinyeow/remote-code-execution-engine/tree/asynchronous-docker-kubernetes) 📕

## Technical Specification

- Low latency
- Resilient to malicious software
- High availability
- Asynchronous

## Technology

Any framework regardless of completing architecture is totally allowed. This repo uses particularly the following technologies:

1. Frontend
   - Next.js
   - Typescript
   - TailwindCSS
   - RabbitMQ publisher
2. Backend
   - Python
   - Kubernetes SDK
   - RabbitMQ consumer
3. Tooling
   - Docker
   - RabbitMQ
   - Bash scripting
4. Orchestration
   - Kubernetes

## Prerequisite

Make sure yarn is installed.

```bash
npm i -g yarn
```

Make sure docker (prefably Docker Desktop) is installed or run the following.

```bash
brew install --cask docker
```

Make sure Kubernetes is enabled with Docker Desktop.

Make sure you can run `make` command with Makefile.
