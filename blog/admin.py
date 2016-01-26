from django.contrib import admin
from .models import Admin , Data , likes ,comment
	
# Register your models here.
admin.site.register(Admin)
admin.site.register(Data)
admin.site.register(likes)
admin.site.register(comment)