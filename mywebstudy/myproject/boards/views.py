from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Board
from django.http import Http404
import datetime
# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
   #boards = Board.objects.all()
    #boards_names = list()

    #for board in boards:
     #   boards_names.append(board.name)

    #response_html = '<br>'.join(boards_names)

    #return HttpResponse(response_html)
def hours_head(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
def display_meta(request):
    values=request.META.items()
    values=list(values)
    # print(values)
    values.sort()
    html=[]
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))   
def search_form(request):
    print("this is search_form s")
    return render(request,"search_form.html")
def search1(request):
    if 'q' in request.GET:
        message='your search for %r' % request.GET['q']
    else:
        message="your submitted is empty"
    return HttpResponse(message)
def current_url(request):
    return HttpResponse("welcome to the page at %s" % request.path)
def current_ip(request):
    return HttpResponse("the host ip is %s" % request.get_host())
def search1(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        
        Boards=Board.objects.filter(name__icontains=q)
        print(q)
        return render(request,'search_results.html',{'query':q})
    else:

        return render('search_form.html',{'error':True})
def search(request):
    error=False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error=True
        else:
            q=request.GET['q']
            Boards=Board.objects.filter(name__icontains=q)
            return render(request,'search_results.html',{'query':q})
    return render('search_form.html',{'error':error})