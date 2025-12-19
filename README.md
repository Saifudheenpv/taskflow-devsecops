# 🚀 TaskFlow – Full DevSecOps GitOps Project

A production-grade **DevSecOps & GitOps platform** built on Kubernetes using real-world tools and best practices.

---

## 🧱 Architecture Overview

GitHub → Jenkins (CI) → SonarQube → Trivy  
GitHub → Argo CD (GitOps CD) → Kubernetes  
Prometheus + Grafana + Alertmanager → Observability

---

## 🔧 Tech Stack

- **CI/CD:** Jenkins
- **Code Quality:** SonarQube
- **Security:** Trivy
- **Containers:** Docker
- **Orchestration:** Kubernetes
- **GitOps:** Argo CD
- **Monitoring:** Prometheus & Grafana
- **Alerts:** Alertmanager
- **Ingress:** NGINX Ingress Controller

---

## 🔄 CI Pipeline Flow

1. Code pushed to GitHub
2. Jenkins triggers pipeline
3. SonarQube checks code quality
4. Docker images built
5. Trivy scans for vulnerabilities
6. Images pushed to Docker Hub

---

## 🚀 CD (GitOps) Flow

1. Kubernetes manifests stored in Git
2. Argo CD watches the repo
3. Any change in Git auto-syncs to cluster
4. Self-healing & drift correction enabled

---

## 📊 Observability

- Cluster & pod metrics via Prometheus
- Dashboards in Grafana
- Alerts via Alertmanager

---

## 🧪 Application

**TaskFlow** – Simple task management app  
- Backend: API service  
- Frontend: Web UI  
- Deployed on Kubernetes with Ingress

---

## 👨‍💻 Author

**Saifudheen PV**  
DevOps / Cloud Engineer  
GitHub: https://github.com/Saifudheenpv  
LinkedIn: https://linkedin.com/in/saifudheenpv07
