from django.http import HttpResponse

from main.tasks import high_latency_task


def home(request):
    high_latency_task.delay()
    return HttpResponse('this is home')
