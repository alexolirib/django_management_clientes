from django.contrib import admin
from client.models import Person, Document

# personalizar admin
class PersonAdmin(admin.ModelAdmin):
    # fields e fieldsets = para formulario
    # fields = (('first_name','last_name' ),('age', 'salary'), 'bio', 'photo', 'doc')
    ordering = ('first_name',)
    fieldsets = (
        ('Dados pessoais', {'fields': (('first_name', 'last_name'),)}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': (('age', 'salary'), 'bio', 'photo', 'doc')
        })
    )
    search_fields = ('id', 'first_name')

    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'has_photo', 'doc')

    def has_photo(self, obj):
        if obj.photo:
            return "SIM"
        return "NÃo"

    has_photo.short_description = 'Possui foto'

    # fazer filtro
    list_filter = ('age', 'salary')

admin.site.register(Person, PersonAdmin)
admin.site.register(Document)
