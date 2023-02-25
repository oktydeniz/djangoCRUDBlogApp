from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog, Category

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Python Programing Language",
            "img": "https://via.placeholder.com/150/B4E4FF",
            "active": True,
            "is_home": True,
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque eaque, laborum "
                           "molestias nostrum reprehenderit voluptatibus."
        },
        {
            "id": 2,
            "title": "Swift Programing Language",
            "img": "https://via.placeholder.com/150/95BDFF",
            "active": True,
            "is_home": True,
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque eaque, laborum "
                           "molestias nostrum reprehenderit voluptatibus."
        }
        , {
            "id": 3,
            "title": "Kotlin Programing Language",
            "img": "https://via.placeholder.com/150/F7C8E0",
            "active": True,
            "is_home": False,
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque eaque, laborum "
                           "molestias nostrum reprehenderit voluptatibus."
        },
        {
            "id": 4,
            "title": "Java Programing Language",
            "img": "https://via.placeholder.com/150/DFFFD8",
            "active": False,
            "is_home": True,
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque eaque, laborum "
                           "molestias nostrum reprehenderit voluptatibus."
        },
        {
            "id": 5,
            "title": "Obj-C Programing Language",
            "img": "https://via.placeholder.com/150/61876E",
            "active": False,
            "is_home": False,
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque eaque, laborum "
                           "molestias nostrum reprehenderit voluptatibus."
        }
        ,
        {
            "id": 5,
            "title": "C# Programing Language",
            "img": "https://via.placeholder.com/150/F6F6C9",
            "active": True,
            "is_home": False,
            "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque eaque, laborum "
                           "molestias nostrum reprehenderit voluptatibus."
        }

    ]
}


def home(request):
    context = {
        "blogs": Blog.objects.filter(isHome=True, isActive=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(isActive=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)


def blogs_detail(request, slug):
    # selected = [blog for blog in blogs if blog["id"] == id][0]

    selected = Blog.objects.get(slug=slug)
    return render(request, "blog/blogs-details.html", {
        "blog": selected,
    })


def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(isActive=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)
