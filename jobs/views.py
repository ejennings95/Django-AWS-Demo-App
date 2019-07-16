from django.shortcuts import render
from .models import Job
import boto3

def home(request):
    jobs = Job.objects
    # sns = boto3.client('sns', region_name='us-west-2')
    # email() = sns.publish(
    #             TopicArn=os.environ['arn:aws:sns:us-west-2:384672189964:ElasticBeanstalkNotifications-Environment-myportfolio'],
    #             Message='Hello World!',
    #         )
    return render(request, 'jobs/home.html', {'jobs':jobs})
