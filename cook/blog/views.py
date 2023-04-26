from django.shortcuts import render
from django.views.generic import ListView


from .models import Post


class PostListView(ListView):
    model = Post
    
    def get_queryset(self) -> QuerySet[Any]:
        pass
    
post_list = PostListView.as_view()
    

def home(request):
    return render(request, 'base.html')
