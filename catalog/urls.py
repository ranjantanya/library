from django.conf.urls import url

from . import views


urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^books/$',views.BookListView.as_view(),name='books'),
url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
url(r'^authors/(?P<pk>\d+)$',views.AuthorDetailView.as_view(),name='author-detail'),
url(r'^borrowedbooks/$',views.BooksLoanedByCurrentUser.as_view(),name='borrowed'),
url(r'^allborrowed/$',views.AllBorrowedBooks.as_view(),name='all_borrowed'),
url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
url(r'^books/create/$',views.BookCreate.as_view(),name='book_create'),
url(r'^book/(?P<pk>\d+)/update/$',views.BookUpdate.as_view(),name='book_update'),
url(r'^book/(?P<pk>\d+)/delete/$',views.BookDelete.as_view(),name='book_delete'),



]