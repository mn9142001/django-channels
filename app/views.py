from django.http import JsonResponse
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()
# Create your views here.
def normal_view(request):
    return render(request, 'home.html')

def text_view(request):
    print(request.POST)
    async_to_sync(channel_layer.group_send)(
				"user_{0}".format(request.user.id),
				{'type': 'chat_message', 'message': request.POST.get('text')})
    return JsonResponse({'done': True})