from django.shortcuts import render

def blog(request):
    context = {
        'nama' : 'Blog Saya'
    }
    return render(request, 'blog/blog.html', context)
