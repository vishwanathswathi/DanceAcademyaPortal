from django.contrib import admin
from App.models import Contact
from App.models import music,bharatanatyam,kuchipudi,westerndance,guitar,keyboard,video


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','email','message']
admin.site.register(Contact,ContactAdmin)

class musicAdmin(admin.ModelAdmin):
    list_display =['image']
admin.site.register(music,musicAdmin)

class bharatanatyamAdmin(admin.ModelAdmin):
    list_display =['image']
admin.site.register(bharatanatyam,bharatanatyamAdmin)


class kuchipudiAdmin(admin.ModelAdmin):
    list_display =['image']
admin.site.register(kuchipudi,kuchipudiAdmin)

class westerndanceAdmin(admin.ModelAdmin):
    list_display =['image']
admin.site.register(westerndance,westerndanceAdmin)

class guitarAdmin(admin.ModelAdmin):
    list_display =['image']
admin.site.register(guitar,guitarAdmin)

class keyboardAdmin(admin.ModelAdmin):
    list_display =['image']
admin.site.register(keyboard,keyboardAdmin)

class videoAdmin(admin.ModelAdmin):
    list_display = ['video']
admin.site.register(video,videoAdmin)
