from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author

from .forms import RenewBookForm

def index(request):
    """
    View for home page of site.
    """
    num_books = Book.objects.all().count()
    num_specific_books = Book.objects.filter(title__icontains='great').count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_views = request.session.get('num_views',1)
    request.session['num_views'] = num_views+1
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors, 'num_specific':num_specific_books, 'num_views':num_views},
    )


class BookListView(generic.ListView):
    model=Book
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context['somedata'] = 'this is some data'
        return context


    # context_object_name = "my_book_list"
    # queryset = Book.objects.filter(title__icontains='great')
    # template_name = 'books/my_arbitrary_template_name_list.html'

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model= Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author


class BooksLoanedByCurrentUser(LoginRequiredMixin,generic.ListView):
    model=BookInstance
    template_name = 'catalog/bookinstance_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__iexact='o').order_by('due_back')



class AllBorrowedBooks(PermissionRequiredMixin,generic.ListView):
    model=BookInstance
    permission_required = 'catalog.can_view_borrowed'
    template_name = 'catalog/bookinstance_list_staff.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__iexact='o').order_by('due_back')



@permission_required('catalog.can_renew')
def renew_book_librarian(request, pk):
    """
    View function for book renewal
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all_borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})



class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'12/10/2016',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model=Book
    fields = '__all__'
    initial = {'genre':'Fantasy'}

class BookUpdate(UpdateView):
    model = Book
    fields= '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('books'))
        return super(BookDelete, self).post(request, *args, **kwargs)
def mylinkview(request):

    # ... your python code/script
    return HttpResponseRedirect(reverse('books'))


