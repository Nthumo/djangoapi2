from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll

def poll_list(request):
    NUMBER = 10
    polls = Poll.objects.all()[:NUMBER]
    data = {'results': list(polls.values('question', 'slug'))}

    return JsonResponse(data)

def poll_detail(pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {'results': {
        'question': poll.question,
        'slug': poll.slug,
    }}

    return JsonResponse(data)



