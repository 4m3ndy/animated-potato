# animated-potato
This repository defines a flask app that exposes metrics from a certain file defined at `data/metrics_from_special_app.txt` path by default.

## Requirements (Locally)
- Docker - In case running the app in a container.
- Python3
- pip3

## How to run
### Locally
The application runs by default runs on `HOST=0.0.0.0` and `PORT=12345` and it reads the metrics from file path `METRICS_FILE_PATH="data/metrics_from_special_app.txt"`, in case you want to override these values you need to change it in `scripts/startup.sh`, for example:
```bash
HOST=0.0.0.0
PORT=8080
METRICS_FILE_PATH="/tmp/metrics_from_special_app.txt"
```

then install the required dependencies using `pip3 install -r requirments.txt`, then run the service using `python3 wsgi.py`

### Using Docker
```bash
docker build -f Dockerfile -t syndica:v1.0.0 .
docker run -it -p 12345:12345 syndica:v1.0.0
```

#### Use the following Helper scripts to deploy the application on linux server:

Before using the helper tickets, please make sure that you clone the repository at the following path `/op/animated-potato`

| Command | Description |
| --- | --- |
| `scripts/deploy.sh` | Installs the required dependencies and configure systemd service to run the application |
| `scripts/startup.sh` | To start the application using gunicorn. |

## Improvements (In case of more time)
* Deploy this application as Kubernetes Workload
* Define Ansible Playbook for a better deployment process to ensure idempotency
* Use Redis insted of `SimpleCache` for a better caching mechanism by running async Job to detect any changes would happen to `data/metrics_from_special_app.txt` file and re-update it's value in Redis DB.