from celery import shared_task
from django.core.mail import send_mail
from .models import Job, Subscriber
from django.conf import settings

@shared_task
def send_job_alert_emails(job_id):
    job = Job.objects.get(id=job_id)
    subscribers = Subscriber.objects.filter(
        skill__iexact=job.skill,
        location__iexact=job.location
    )
    for sub in subscribers:
        send_mail(
            subject=f"New Job Alert: {job.title}",
            message=f"{job.description}\n\nLocation: {job.location}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.email],
        )
