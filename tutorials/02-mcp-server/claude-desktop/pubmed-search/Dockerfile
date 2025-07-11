FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create requirements file with FastMCP
RUN echo "fastmcp>=0.1.0" > requirements.txt && \
    echo "httpx>=0.27.0" >> requirements.txt && \
    echo "mcp>=1.0.0" >> requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the MCP server code
COPY pubmed_mcp.py .

ENTRYPOINT ["python", "pubmed_mcp.py"]
CMD ["stdio"]