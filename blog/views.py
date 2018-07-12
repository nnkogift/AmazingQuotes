from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


class PostViews:

    def post_view(request):
        posts = Post.objects.all().order_by("-timestamp")
        searchq = search(request)
        if searchq:
            posts = Post.objects.filter(Q(title__icontains=searchq) | Q(content__icontains=searchq) |
                                        Q(user_post__first_name__icontains=searchq) |
                                        Q(user_post__last_name__icontains=searchq)).distinct()

        paginator = Paginator(posts, 4) # 4 posts per page
        page = page_get(request)
        posts = paginator.get_page(page)

        return render(request, "blog.html", context={"posts": posts})

    def post_detail(request, id):
        post = get_object_or_404(Post, id=id)
        return render(request, "single-blog.html", context={"post": post})


def search(request):
    search = request.GET.get('search')
    return search


def page_get(request):
    return request.GET.get('page')