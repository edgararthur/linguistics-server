from django.contrib import admin
from .models import News, Collaborations, Consultants, Members, Leadership

admin.site.site_title = "Linguisitics Association of Ghana"
admin.site.site_header = "Linguistics Association of Ghana"
admin.site.index_title = "Site administration"

admin.site.register(News)
admin.site.register(Collaborations)
admin.site.register(Consultants)
admin.site.register(Members)
admin.site.register(Leadership)
