# K8S 云原生 Web 服务部署平台

## 项目简介

本项目是一个基于 Docker 与 Kubernetes 的云原生 Web 服务部署实践项目，包含 FastAPI 后端服务与 Nginx 前端静态页面。

项目从 Dockerfile 镜像构建、Docker Compose 本地编排开始，逐步迁移到 Kubernetes 三节点集群环境，覆盖 Deployment、Service、ConfigMap、Secret、健康检查、资源限制、HPA、CronJob、滚动更新与版本回滚等核心能力。

## 技术栈

- 前端：HTML + Nginx
- 后端：FastAPI + Uvicorn
- 容器化：Dockerfile
- 本地编排：Docker Compose
- 集群部署：Kubernetes
- 容器运行时：containerd
- K8S 资源：Deployment、Service、ConfigMap、Secret、HPA、CronJob

## 项目结构

```text
k8s-cloud-native-demo/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── frontend/
│   ├── index.html
│   ├── nginx.conf
│   ├── Dockerfile
│   └── .dockerignore
├── k8s/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── backend-hpa.yaml
│   └── backend-health-cronjob.yaml
├── docker-compose.yml
└── README.md
