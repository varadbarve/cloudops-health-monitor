# CloudOps Webiste Health Monitor

A lightweight Python application that checks website availability, measures response latency, and reports HTTP status codes. The application runs locally or inside a Docker container and uses GitHub Actions for automated testing and Docker image builds.

## Features

- Checks the availability of multiple websites.
- Records HTTP status codes and response latency.
- Handles common network errors and timeouts.
- Runs inside a Docker container.
- Includes automated unit tests using Python's built-in `unittest` framework.
- Uses GitHub Actions to run tests and build the Docker image automatically.

## Technology Stack

- **Language:** Python 3
- **Containerization:** Docker
- **Testing:** unittest
- **Version Control:** Git and GitHub
- **CI:** GitHub Actions
- **Development Environment:** Ubuntu on WSL 2 and Visual Studio Code

## Project Structure

```text
health-monitor/
├── .github/
│   └── workflows/
│       └── test.yml
├── tests/
│   └── test_app.py
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Prerequisites

To run the application locally, you need:

- Python 3
- Internet access to reach the configured websites

If running in a container then you also need Docker.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/varadbarve/cloudops-health-monitor.git
cd cloudops-health-monitor
```

Run the application:

```bash
python3 app.py
```

The application checks the configured websites and prints their status and response latency.

## Run with Docker

Build the Docker image:

```bash
docker build -t cloudops-health-monitor:1.0 .
```

Run the container:

```bash
docker run --rm cloudops-health-monitor:1.0
```

The container runs the same health checks as the local Python application.

## Run Tests

Execute the unit tests:

```bash
python3 -m unittest discover -s tests -v
```

The tests simulate successful and unsuccessful HTTP responses without making real network requests.

## Continuous Integration

The GitHub Actions workflow in `.github/workflows/test.yml` runs when code is pushed to the `main` branch or when a pull request targets `main`.

The workflow:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Runs the unit tests.
4. Builds the Docker image.