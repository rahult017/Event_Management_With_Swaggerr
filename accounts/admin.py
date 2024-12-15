from django.contrib import admin
from accounts.models.users_models import UserMaster
from accounts.models.role_master_models import RoleMaster
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(UserMaster,SimpleHistoryAdmin)
admin.site.register(RoleMaster,SimpleHistoryAdmin)