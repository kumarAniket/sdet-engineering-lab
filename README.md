# 🏗️ Core Engineering Lab: L5 SWE-T Baseline

> **Objective:** Transitioning from traditional Quality Assurance to **Planetary-Scale Site Reliability Engineering (SRE)** and **Software Engineering in Test (SWE-T)**.

This repository serves as a centralized engineering workspace for executing a high-intensity, 26-module architectural roadmap. Every component is designed to meet the technical rigor of L4/L5 expectations at Google.

---

## 📂 Project Architecture

```text
.
├── 01-python-foundations/     # 🐍 Core Language & TDD
│   ├── class_design/          # OOP, Mixins, and Design Patterns
│   └── tdd_labs/              # Pytest, Mocking, and Property-based testing
│
├── 02-algorithms-dsa/         # ⚡ The Morning Blitz (LeetCode)
│   ├── dynamic_programming/   # Optimization and state management
│   └── distributed_dsa/       # Sorting/Searching at scale logic
│
├── 03-distributed-systems/    # 🌐 Core Infrastructure
│   ├── grpc_stubs/            # Protobuf definitions and service contracts
│   └── message_queues/        # Kafka/PubSub event-driven logic
│
├── 04-quality-observability/  # 📊 Reliability Engineering
│   ├── compliance_gates/      # Playwright (A11y/Visual) CI logic
│   └── slos_metrics/          # Prometheus/Grafana alerting definitions
│
├── 05-ai-ml-testing/          # 🤖 Non-Deterministic Validation
│   └── llm_evals/             # Model response consistency & safety checks
│
├── 06-architecture-sprints/   # 🏛️ Saturday System Design Labs
│   ├── sprint_01_gdrive/      # Metadata & Recursive systems
│   └── docs_design/           # ADRs (Architecture Decision Records)
│
├── 07-portfolio-projects/     # 🚀 L5 Tier Differentiators
│   └── slo_gated_pipeline/    # Automated Canary/Rollback infrastructure
│
└── docs/                      # 📖 Engineering Specs & Onboarding
