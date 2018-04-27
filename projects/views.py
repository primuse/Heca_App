from django.shortcuts import render, redirect
from .models import Project
from django.shortcuts import get_object_or_404
from .forms import ProjectForm

# Create your views here.
def project_list(request):
    posts = Project.objects.all()
    return render(request, 'projects/project_list.html', {'posts': posts})

def project_detail(request, post_id):
    post = get_object_or_404(Project, pk=post_id)
    return render(request, 'projects/project_detail.html', {'post':post})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post_id=post.id)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_new.html', {'form': form})

def project_delete(request, post_id):
    post = get_object_or_404(Project, pk=post_id)
    post.delete()
    return redirect('home')

def project_edit(request, post_id):
    post = get_object_or_404(Project, pk=post_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post_id=post.id)
    else:
        form = ProjectForm(instance=post)
    return render(request, 'projects/project_new.html', {'form': form})


def project_start(request, post_id):
    post = get_object_or_404(Project, pk=post_id)
    post.started()
    return redirect('detail', post_id=post.id)

def project_complete(request, post_id):
    post = get_object_or_404(Project, pk=post_id)
    post.completed()
    return redirect('home')