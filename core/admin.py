from django.contrib import admin
from core.models import Attendance, Signup

admin.site.site_title = "Linguisitics Association of Ghana"
admin.site.site_header = "Linguistics Association of Ghana"
admin.site.index_title = "Site administration"

admin.site.register(Attendance)
admin.site.register(Signup)
