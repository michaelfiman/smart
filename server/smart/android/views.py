from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from pyswitcherv2 import switcher




def check_up(request):
    return HttpResponse("UP")

def switcher_status(request):
    from pyswitcherv2 import switcher
    phone_id = "cb7f"
    dev_id = "d3ed1e"
    dev_pass = "37353234"
    switcher_local_ip = "192.168.1.6"
    credentials = switcher.Credentials(phone_id, dev_id, dev_pass, switcher_local_ip)
    credentials.validate()
    switcher = switcher.Switcher(credentials, False)
    return HttpResponse(switcher.get_state())

def switcher_on(request, time=60):
    from pyswitcherv2 import switcher
    phone_id = "cb7f"
    dev_id = "d3ed1e"
    dev_pass = "37353234"
    switcher_local_ip = "192.168.1.6"
    credentials = switcher.Credentials(phone_id, dev_id, dev_pass, switcher_local_ip)
    credentials.validate()
    switcher = switcher.Switcher(credentials, False)
    return HttpResponse(switcher.turn_on(time))

def switcher_off(request):
    from pyswitcherv2 import switcher
    phone_id = "cb7f"
    dev_id = "d3ed1e"
    dev_pass = "37353234"
    switcher_local_ip = "192.168.1.6"
    credentials = switcher.Credentials(phone_id, dev_id, dev_pass, switcher_local_ip)
    credentials.validate()
    switcher = switcher.Switcher(credentials, False)
    return HttpResponse(switcher.turn_off())
