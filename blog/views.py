from django.shortcuts import render


def about_us(request):
    """ A view to return the index page """

    return render(request, 'blog/about-us.html')


def history(request):
    """ A view to return the index page """

    return render(request, 'blog/history.html')


def rug_weaving(request):
    """ A view to return the index page """

    return render(request, 'blog/rug_weaving.html')


def rug_repair(request):
    """ A view to return the index page """

    return render(request, 'blog/rug_repair.html')

