from django.contrib import admin

# Register your models here.
from .models import Author,Book,Genre,BookInstance
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','date_of_birth')
    fields = ['first_name', 'last_name',('date_of_birth', 'date_of_death')]
    inlines=[BookInline]

admin.site.register(Author,AuthorAdmin)

# Register the Admin classes for Book using the decorator
class BookInstanceInline(admin.TabularInline):
    extra = 0
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BookInstanceInline]



# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('None',{'fields':('book','imprint','id')}),
        ('Availability',{'fields':('status','due_back','borrower')})
    )


