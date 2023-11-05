from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Poll, Choice
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# View for the list of polls
class PollListView(View):
    def get(self, request):
        polls = Poll.objects.all()
        return render(request, 'polls/poll_list.html', {'polls': polls})

# View for poll details and voting
class PollDetailView(View):
    def get(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        return render(request, 'polls/poll_detail.html', {'poll': poll})

    def post(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        try:
            selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/poll_detail.html', {
                'poll': poll,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('poll_detail', poll_id=poll_id)

# View for creating a new poll (requires login)
@method_decorator(login_required, name='dispatch')
class PollCreateView(View):
    def get(self, request):
        return render(request, 'polls/poll_create.html')

    def post(self, request):
        question = request.POST['question']
        choices = [choice.strip() for choice in request.POST['choices'].split(',')]

        if question and choices:
            poll = Poll.objects.create(question=question)
            for choice_text in choices:
                Choice.objects.create(poll=poll, choice_text=choice_text)
            return redirect('poll_list')
        else:
            return render(request, 'polls/poll_create.html', {'error_message': "Question and choices are required."})

# View for editing an existing poll (requires login)
@method_decorator(login_required, name='dispatch')
class PollEditView(View):
    def get(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        return render(request, 'polls/poll_edit.html', {'poll': poll})

    def post(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        new_question = request.POST['question']
        new_choices = [choice.strip() for choice in request.POST['choices'].split(',')]

        if new_question and new_choices:
            poll.question = new_question
            poll.choice_set.all().delete()
            for choice_text in new_choices:
                Choice.objects.create(poll=poll, choice_text=choice_text)
            poll.save()
            return redirect('poll_detail', poll_id=poll_id)
        else:
            return render(request, 'polls/poll_edit.html', {'poll': poll, 'error_message': "Question and choices are required."})
