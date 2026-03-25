FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /workspaces

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the workspace
COPY .. /workspaces

CMD ["sleep", "infinity"]




