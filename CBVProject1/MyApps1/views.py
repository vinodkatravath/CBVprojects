from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class HelloWorldView(View):
 def get(self,request):
    ss='''<h1>Hello from Class-Bassed-View</h1>
     <hr />
     <h2>Response given for get-method from client</h2>
     <h3>Have a nice day..!!</h3>
    <hr />
     <h4>***ALL THE BEST***</h4>
     '''
    return HttpResponse(ss)

from django.views.generic import TemplateView #--parent class
class TemplateCBV(TemplateView):
    template_name = "MyApps1/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Sai'
        context['age'] = 23
        context['height'] = 6.2
        return context;

from MyApps1.models import Book
from django.views.generic import ListView
class BookListView(ListView):
    model = Book; #book_list=Book.objects.all();

from MyApps1.models import Company
from django.views.generic import DetailView,ListView
class CompanyListView(ListView):
    model = Company      #companlist=Company.Objects.all();
    #default template_name is company_list var
    #defult context_object_name is company_list var
    #{{name}} {{loc}} {{ceo}}
class CompanyDetailView(DetailView):
    model = Company
    # default template_name is company_detail.html
    # defult context_object_name is "company" or given-object for company_list, which is in usagefor company_list.html
