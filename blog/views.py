from django.shortcuts import render_to_response
ARTICLES = {
    "kabali-tracker":{"title":"BookMyShow Movie Ticket Tracker", "pub_date":"18/06/2016"},
    "python-is-really-private":{"title":"Python - Private Methods Not Actually Private!", "pub_date":"15/02/2013"},
    "python-args-kwargs":{"title":"", "pub_date":""},
    "python-is-vs-equals":{"title":"", "pub_date":""},
    "python-remove-list-items":{"title":"", "pub_date":""},
    "python-tailf":{"title":"", "pub_date":""},
    "python-underscores":{"title":"", "pub_date":""},
    "python-virtualenv":{"title":"", "pub_date":""},
    "python-class-instance-attributes":{"title":"Python - Difference between class and instance attributes", "pub_date":"16/02/2013"},
    "python-build-interpreter":{"title":"Python - Build a Basic Python Iterator", "pub_date":"17/02/2013"},
    "python-cyclic-imports":{"title":"Python - Circular (or cyclic) imports in Python", "pub_date":"21/02/2013"},
    "train-track":{"title":"A small app to track your train", "pub_date":"23/07/2016"},
    "customize-pseudo-elements":{"title":"Customize pseudo elements like placeholders", "pub_date":"28/08/2014"},
    "python-remove-list-items":{"title":"Python - Removing Items from a List", "pub_date":"02/03/2013"},
    "python-tailf":{"title":"Python - Pythonic Equivalent of tail -f", "pub_date":"i02/06/2013"},
    "python-args-kwargs":{"title":"Python - args and kwargs", "pub_date":"02/05/2013"},
    "python-old-vs-new-style-classes":{"title":"Python - Old vs New Style Classes", "pub_date":"02/01/2013"},
    "python-is-operator":{"title":"Python - is Operator", "pub_date":"31/01/2013"},
    "python-call-by-reference":{"title":"Python - Call by Reference", "pub_date":"30/01/2013"},
    "python-list-slicing":{"title":"Python - List Slicing", "pub_date":"29/01/2013"},
    "python-itertools-1":{"title":"Python - Itertools Part 1", "pub_date":"27/01/2013"},
    "python-itertools-2":{"title":"Python - Itertools Part 2", "pub_date":"28/01/2013"},
    "":{"title":"", "pub_date":""},
    "":{"title":"", "pub_date":""},
    "":{"title":"", "pub_date":""},
}
def show_article(request, path):
    context = {"articles":ARTICLES}
    if path:
        path = path.split('/')[0]
        template = '%s.html'%path
        context["article"] = ARTICLES[path]
    else:
        template = "index.html"
    return render_to_response(template, context)
