# Overwatch Observability Review Lab 🧪

A self-contained, 15-minute hands-on reviewer lab for **Overwatch Observability**.

Overwatch is a lightweight browser extension + local Rust helper that overlays your existing monitoring tools (**Datadog, Grafana, New Relic, PagerDuty**). When an incident triggers, Overwatch:
1. Diagnoses the alert in-place.
2. Proposes the exact remediation command (e.g. `kubectl patch`, `systemctl restart`, `bash`).
3. **Waits for human approval** — no autonomous AI breaking production.
4. Executes the fix locally on your machine with full audit logging.

This lab lets you test the full loop against synthetic alerts without connecting any production systems.

---

## Quickstart (15 Minutes)

### 1. Start the Lab
```bash
git clone https://github.com/overwatchobs/review-lab.git
cd review-lab
docker compose up -d
```
Verify services are running:
- Mock Incident Dashboard: [http://localhost:3000](http://localhost:3000)
- Demo API Service: [http://localhost:8080/health](http://localhost:8080/health)

### 2. Install the Overwatch Extension & Helper
- Install the [Overwatch Browser Extension](https://chrome.google.com/webstore) (or load in developer mode).
- Start the local helper daemon:
  ```bash
  curl -sSL https://overwatch-observability.com/install.sh | bash
  ```
- In the extension settings, enter your **VIP Reviewer Code** to activate Business Tier features (unlimited investigations, audit logs, local CLI execution).

### 3. Trigger Failure Scenarios

#### Scenario 1: Out Of Memory (OOMKill / CrashLoop)
Simulates memory leak leading to container termination:
```bash
./scenarios/01-oom-kill.sh
```

#### Scenario 2: Broken Ingress / 502 Bad Gateway
Simulates a routing/upstream DNS misconfiguration:
```bash
./scenarios/02-broken-ingress.sh
```

#### Scenario 3: Database Connection Pool Exhaustion (504 Timeout)
Simulates client pool starvation:
```bash
./scenarios/03-db-connection-pool.sh
```

### 4. Review & Remediate
1. Open the [Mock Incident Dashboard](http://localhost:3000).
2. Overwatch will automatically parse the alert context from the page.
3. Click **"Diagnose with Overwatch"**.
4. Inspect the suggested remediation command.
5. Click **"Approve & Run Locally"** to have the local helper execute the fix.
6. Refresh the dashboard to verify recovery!
