# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils import timezone
import csv
from django.http import HttpResponse
import urllib
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
#Export in CSV
def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])
        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif exclude:
            excludeset = set(exclude)
            field_names = field_names - excludeset
        
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
        
        writer = csv.writer(response)
        if header:
            writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([unicode(getattr(obj, field)).encode('utf-8') for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv
#inventory 
def make_inv_action(description="Инвентаризировать"):
    def make_inv(self, request, queryset):  
     queryset.update(date_inv=timezone.now()) 
     rows_updated = queryset.update(inv=True)   
     message_bit = "%s " % rows_updated
     self.message_user(request, "Успешно проинвентаризировано! (Объектов:%s) " % message_bit)
    make_inv.short_description = description
    return make_inv      



# Register your models here.
from showbase.models import Podotchet, Vedomost, Check, Place, Persons, Otmetka
#admin.site.register(Podotchet)

class CommentInline(admin.StackedInline):
    model = Otmetka
    extra = 3

class PodotchetAdmin(admin.ModelAdmin):
   search_fields = ['name_el','inv_number','place']
   list_display = ('inv','name_el','inv_number','place','date_inv','comment','author','list_t','date_now')
   list_display_links = ('name_el',)
   ordering = ('-inv',)
   actions_on_bottom = True
   actions_on_top = False
   list_filter = ('list_t','place','date_inv')
   actions = [make_inv_action("Инвентаризировать"),export_as_csv_action("Экспортировать выделенное в CSV файл", fields=['name_el','inv_number','place','date_now']),]  
   list_per_page=50
   fieldsets = [
       (None,               {'fields': ['list_t']}),
       ('Основная информация', {'fields': ['inv_number','name_el', 'person', 'place']}),
       ('Статус инвентаризации', {'fields': ['inv','date_inv']}),
       ('Дополнительная информация', {'fields': ['comment','otmetka']}),
       ('Информация о списании', {'classes': ('collapse',),
           'fields': ['spisano','date_spis'],
                                  }),
    ]
   inlines = [CommentInline]


# make author   
   def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
# Filter by user
   def get_queryset(self, request): 
        qs = super(PodotchetAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
         return qs.filter()
        else:
         return qs.filter(author=request.user)

#   def has_change_permission(self, request, obj=None):
#        if not obj:
#            # the changelist itself
#            return True
#        return obj.user == request.user
 
   
#    Add custom fields
#   def hrcode(self,obj):
#    url = conditional_escape("http://chart.apis.google.com/chart?%s" % \
#            urllib.urlencode({'chs':'150x150', 'cht':'qr', 'chl':obj.inv_number, 'choe':'UTF-8'}))
#    return mark_safe(u"""<img class="qrcode" src="%s" width="150" height="150" />""" % (url))
#-----------------------------------------------------------------
#   def hrcode(self,obj):
#    url = conditional_escape("http://chart.apis.google.com/chart?%s" % \
#            urllib.urlencode({'chst':'d_bubble_text_small', 'chld':'bb|%s|FFFFFF|000000'% obj.inv_number}))
#    return mark_safe(u"""<img class="qrcode" src="%s" width="175" height="75" />""" % (url)) 
   

admin.site.register(Podotchet, PodotchetAdmin)
admin.site.register(Vedomost)
admin.site.register(Check)
admin.site.register(Persons)
admin.site.register(Place)