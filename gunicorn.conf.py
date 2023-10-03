import logging
from splunk_otel.tracing import start_tracing

logging.basicConfig(level=logging.DEBUG)

def post_fork(server, worker):
    start_tracing()