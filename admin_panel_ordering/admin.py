
from django.contrib import admin

# Register your models here.
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminMixin

from .models import Author,Book,Membership

class MembershipInline(SortableInlineAdminMixin,admin.TabularInline): #SortableInlineAdminMixin
	model = Membership
	fields = ['author','book','my_order']
	

class BookAdmin(SortableAdminMixin,admin.ModelAdmin):
	list_displayst_editable = ('authors', 'title','my_order',)
	list_display = ('title',)
	inlines = (MembershipInline,)
	

		
class AuthorAdmin(SortableAdminMixin,admin.ModelAdmin):
	list_displayst_editable = ('name','my_order',)
	list_display = ('name',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
