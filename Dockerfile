FROM python:3.11-slim

LABEL maintainer="UCP Collective <contact@ucp-protocol.org>"
LABEL description="Ultra-Compressed Communication Protocol - AI Reasoning Enhancement"
LABEL version="1.0.0"

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy UCP source code
COPY *.py ./
COPY README.md ./
COPY LICENSE ./

# Create data directory for pattern storage
RUN mkdir -p /app/data
VOLUME ["/app/data"]

# Set environment variables
ENV PYTHONPATH=/app
ENV UCP_DATA_DIR=/app/data
ENV UCP_LOG_LEVEL=INFO

# Expose port for potential web interface
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python3 -c "from ucp_system import UCPSystem; UCPSystem().get_system_status()" || exit 1

# Default command - run UCP demonstration
CMD ["python3", "ucp_system.py"]

# Alternative commands:
# docker run ucp-protocol python3 ucp_core.py        # Core demo only
# docker run ucp-protocol python3 verify_ucp.py     # Verification tests
# docker run -it ucp-protocol /bin/bash              # Interactive shell