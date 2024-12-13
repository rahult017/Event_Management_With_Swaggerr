from django.contrib import admin
from accounts.models.users_models import UserMaster
from accounts.models.role_master_models import RoleMaster
# Register your models here.
admin.site.register(UserMaster)
admin.site.register(RoleMaster)