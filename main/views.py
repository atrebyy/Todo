from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class AddTask(forms.Form):
    task = forms.CharField(label="Task to add")


class RemoveTask(forms.Form):
    tasks = forms.MultipleChoiceField(label="Task to remove")

    def __init__(self, *args, **kwargs):
        tasks = kwargs.pop("tasks", [])
        super(RemoveTask, self).__init__(*args, **kwargs)
        self.fields["tasks"].choices = [(task, task) for task in tasks]


def index(request):
    if "tasks" not in request.session or request.method == "POST":
        request.session["tasks"] = []
    return render(request, "main/index.html", {"tasks": request.session["tasks"]})


def add(request):
    if request.method == "POST":
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("main:index"))
        else:
            return render(request, "main/add.html", {"form": form})
    return render(request, "main/add.html", {"form": AddTask()})


def remove(request):
    if request.method == "POST":
        form = RemoveTask(request.POST, tasks=request.session.get("tasks", []))
        if form.is_valid():
            selected_tasks = form.cleaned_data["tasks"]
            tasks = request.session["tasks"]
            for task in selected_tasks:
                if task in tasks:
                    tasks.remove(task)
            request.session["tasks"] = tasks
            return HttpResponseRedirect(reverse("main:index"))
        else:
            return render(request, "main/remove.html", {"form": form})
    return render(
        request,
        "main/remove.html",
        {"form": RemoveTask(tasks=request.session.get("tasks", []))},
    )
