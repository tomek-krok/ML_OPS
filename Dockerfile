# Use a minimal Python image as the base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /uvx /bin/

# Install uv package manager
# RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy only dependency files first (to leverage caching)
COPY pyproject.toml uv.lock ./

# Install project dependencies using uv
# RUN uv pip install --system

# Install dependencies - followed by instuction https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    # uv sync --locked --no-install-project --no-editable
    uv sync --locked 

# Copy the rest of the application code
COPY . /app 

# Expose the application port
EXPOSE 8000

# Run the application with uv
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]