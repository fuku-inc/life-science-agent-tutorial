FROM python:3.11-slim

WORKDIR /docs

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy documentation files
COPY docs/ docs/
COPY mkdocs.yml .

# Expose port
EXPOSE 8000

# Start mkdocs server
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]