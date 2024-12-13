from django.contrib.auth.base_user import BaseUserManager
from accounts.models.role_master_models import RoleMaster
from utility.role import Role


class CustomManager(BaseUserManager):
    def _create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        **kwargs,
    ):
        if not email:
            return ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email: str, password: str, **kwargs):
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_admin", True)
        try:
            staff_role = RoleMaster.objects.get(name=Role.ADMIN)
        except RoleMaster.DoesNotExist:
            raise ValueError(f"Role {Role.ATTENDEE} does not exist in the database")

        kwargs.setdefault("role_id", staff_role.id)

        return self._create_user(
            email=email, password=password, **kwargs
        )

    def create_superuser(self, email: str, password: str, **kwargs):
        try:
            super_admin_role = RoleMaster.objects.get(name=Role.SUPER_ADMIN)
        except RoleMaster.DoesNotExist:
            raise ValueError(f"Role {Role.SUPER_ADMIN} does not exist in the database")
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("role_id", super_admin_role.id)

        return self._create_user(
            email=email, password=password,**kwargs
        )




class CustomManager(BaseUserManager):
    def _create_user(
        self,
        email: str,
        password: str,
        first_name: str = "",
        last_name: str = "",
        **kwargs,
    ):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **kwargs):
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_admin", True)
        try:
            staff_role = RoleMaster.objects.get(name=Role.ATTENDEE)
        except RoleMaster.DoesNotExist:
            raise ValueError(f"Role {Role.ATTENDEE} does not exist in the database")

        kwargs.setdefault("role_id", staff_role.id)

        return self._create_user(email=email, password=password, **kwargs)

    def create_superuser(self, email: str, password: str, **kwargs):
        try:
            super_admin_role = RoleMaster.objects.get(name=Role.SUPER_ADMIN)
        except RoleMaster.DoesNotExist:
            raise ValueError(f"Role {Role.SUPER_ADMIN} does not exist in the database")
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("role_id", super_admin_role.id)

        return self._create_user(email=email, password=password, **kwargs)
