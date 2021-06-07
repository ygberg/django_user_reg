from django.contrib import admin
from user_app.models  import UserProfile

#admin.site.register(UserProfile)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',"portfoliosite",'profile_pic' )
    list_filter = ("profile_pic", )