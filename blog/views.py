from django.shortcuts import render


# Create your views here.
from .models import Post

def home(request):
    posts= Post.objects.all().order_by('-published_date')
    return render(request, 'blog/home.html',{'posts': posts})



from django.shortcuts import get_object_or_404

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


from django.shortcuts import render, redirect
from .models import Post

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title=title, content=content)
        post.save()
        return redirect('home')  # Redirect to home after saving
    return render(request, 'blog/create_post.html')


