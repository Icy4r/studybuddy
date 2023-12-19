from django.shortcuts import render
from django.http import HttpResponseRedirect

from posts.models import Post
from posts.forms import PostForm

# Create your views here.
def view_polls(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, 'posts.html', context=context)

def add_post(request):

    if request.method == "POST":
        # create form instance
        form = PostForm(request.POST)

        if form.is_valid():
            # process the data
            if request.user.is_authenticated:
                curr_user = request.user
                new_post = Post(user=curr_user, name=form.cleaned_data['name'], title=form.cleaned_data['title'], location=form.cleaned_data['location'],
                            message=form.cleaned_data['message'], date=form.cleaned_data['date'])
                new_post.save()

            return HttpResponseRedirect("/posts/")

    else:
        form = PostForm()
    
    context = {'form': form}

    return render(request, 'add_post.html', context=context)

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, "post_details.html", context=context)

