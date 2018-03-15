from django.contrib import admin

from .models import Article


#class BlockAdmin(admin.ModelAdmin)
#    list_display = ("name","desc","manager")


admin.site.register(Article)
