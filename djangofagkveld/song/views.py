from django.shortcuts import render
from .models import Participants, Tasks
# Create your views here.
import random


def lag(request):
    number_of_teams = request.GET.get('number_of_teams')
    
    if number_of_teams == None:
        number_of_teams = 0
    letter_list = ["Lag A", "Lag B", "Lag C", "Lag D", "Lag E", "Lag F", "Lag G", "Lag H"]
    lag_list = []
    if number_of_teams != None and int(number_of_teams) > 0:
        participants = Participants.objects.all()
        part_list = [part.name for part in participants]
        random.shuffle(part_list)
        idx = 0
        for i in range(0, len(part_list), int(number_of_teams)):
            lag_list.append([part_list[i:i+int(number_of_teams)], letter_list[idx]])
            idx += 1

    context = {
        'lag_list': lag_list,
        'number_of_teams': number_of_teams,
        'letter_list': letter_list,
    }

    return render(request, 'results/lag.html', context)

def index(request):
    participants = Participants.objects.all()

    part_list = []
    max_points = 0
    for participant in participants:
        bordtennis = checkNoneValue(participant.bordtennis)
        fifa = checkNoneValue(participant.fifa)
        foccia = checkNoneValue(participant.foccia)
        gulbolle = checkNoneValue(participant.gulbolle)
        klinkbong = checkNoneValue(participant.klinkbong)
        bonuspoeng = checkNoneValue(participant.bonuspoeng)
        kaptein = checkNoneValue(participant.kaptein)
        extra = 0
        for i in participant.points:
            extra += int(i)

        points = bordtennis + fifa + foccia + gulbolle + klinkbong + bonuspoeng + kaptein + extra
        max_points = max(max_points, points)
        part_list.append([participant.name, points, 0])
    
    part_list.sort(key=lambda x: x[1])
    part_list.reverse()

    if (max_points > 0):
        for i in part_list:
            i[2] = round(i[1] / max_points * 100, 0)

    context = {
        'part_list': part_list,
        'max_value': max_points,
    }

    return render(request, 'results/index.html', context)

def checkNoneValue(value):
    if value == None:
        return 0
    return int(value)

def oppgave(request, oppgave_id):
    task = Tasks.objects.get(id = oppgave_id)

    context = {
        'task': task,
    }

    return render(request, 'results/oppgave.html', context)


def oppgaver(request):
    oppgaver = Tasks.objects.all()

    context = {
        'oppgaver': oppgaver,
    }

    return render(request, 'results/oppgaver.html', context)

