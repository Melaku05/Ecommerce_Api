from django.core.mail import  BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers

def say_hello(request):
    notify_customers.delay("Hello, world!")
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name': 'John'},
    #     )
    #     message.send(['jhon@melaku.com'])
    # except BadHeaderError:
    #     pass
    return render(request, 'hello.html', {'name': 'Mosh'})

