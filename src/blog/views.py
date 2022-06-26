from django.shortcuts import render, HttpResponse
from .models import Blog, HtmlTemplate

# Create your views here.

def home(request):
    blog = Blog.objects.first()
    html = HtmlTemplate.objects.filter(is_active=True).first().html_code
    # html = html.replace('{{blog.title}}', blog.title).replace('{{blog.description}}', blog.description)
    # return HttpResponse(html)
    context = {
        "blog":blog
    }
    f = open('templates/index.html', 'w')
    f.write(html)
    f.close()
    return render(request, "index.html", context)