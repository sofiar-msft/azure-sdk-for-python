"""
Examples to show usage of the azure-core-tracing-opentelemetry
with the servicebus SDK and exporting to Azure monitor backend.

This example traces calls for receiving messages from the servicebus queue.

An alternative path to export using the OpenTelemetry exporter for Azure Monitor
is also mentioned in the sample. Please take a look at the commented code.
"""

import os

# Declare OpenTelemetry as enabled tracing plugin for Azure SDKs
from azure.core.settings import settings

settings.tracing_implementation = "opentelemetry"

# In the below example, we use a simple console exporter, uncomment these lines to use
# the OpenTelemetry exporter for Azure Monitor.
# Example of a trace exporter for Azure Monitor, but you can use anything OpenTelemetry supports.

# from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
# exporter = AzureMonitorTraceExporter(
#     connection_string="the connection string used for your Application Insights resource"
# )


# Regular open telemetry usage from here, see https://github.com/open-telemetry/opentelemetry-python
# for details
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# azure monitor trace exporter to send telemetry to appinsights
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

# Simple console exporter
exporter = ConsoleSpanExporter()
span_processor = SimpleSpanProcessor(exporter)
# see issue https://github.com/open-telemetry/opentelemetry-python/issues/3713
trace.get_tracer_provider().add_span_processor(span_processor)  # type: ignore

# Example with Servicebus SDKs
from azure.servicebus import ServiceBusClient, ServiceBusMessage

connstr = os.environ["SERVICE_BUS_CONN_STR"]
queue_name = os.environ["SERVICE_BUS_QUEUE_NAME"]

with tracer.start_as_current_span(name="MyApplication2"):
    with ServiceBusClient.from_connection_string(connstr) as client:
        with client.get_queue_sender(queue_name) as sender:
            # Sending a single message
            single_message = ServiceBusMessage("Single message")
            sender.send_messages(single_message)
        # continually receives new messages until it doesn't receive any new messages for 5 (max_wait_time) seconds.
        with client.get_queue_receiver(queue_name=queue_name, max_wait_time=5) as receiver:
            # Receive all messages
            for msg in receiver:
                print("Received: " + str(msg))
                receiver.complete_message(msg)
