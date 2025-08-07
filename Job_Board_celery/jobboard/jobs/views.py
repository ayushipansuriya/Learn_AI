from rest_framework import viewsets
from .models import Job, Subscriber
from .serializers import JobSerializer, SubscriberSerializer
from .tasks import send_job_alert_emails

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = serializer.save()
        send_job_alert_emails.delay(job.id)

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

