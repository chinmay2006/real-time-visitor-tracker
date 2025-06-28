import json
from google.cloud import pubsub_v1

def log_visit(request):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('active-mountain-462107-r9', 'visitor-events')

    payload = {
        "message": "New visit to portfolio",
        "timestamp": request.headers.get('X-Cloud-Trace-Context', 'unknown'),
        "user_agent": request.headers.get('User-Agent', 'unknown')
    }

    data = json.dumps(payload).encode("utf-8")
    publisher.publish(topic_path, data)

    return "Visit logged", 200
