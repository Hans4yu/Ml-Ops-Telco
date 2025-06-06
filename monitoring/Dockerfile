FROM prom/prometheus:latest

COPY prometheus.yml /etc/prometheus/prometheus.yml

# Expose Prometheus web interface port
EXPOSE 9090

# No need for custom entrypoint since the base image already has one

# Commands to build and run (for reference only, not part of Dockerfile):
# docker build -t cc-monitoring .\monitoring\
# docker run -p 9090:9090 cc-monitoring