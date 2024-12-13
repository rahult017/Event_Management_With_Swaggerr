from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords  # type: ignore


class UserMaster(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("organizer", "Event Organizer"),
        ("attendee", "Attendee"),
    ]
    first_name = models.CharField(
        max_length=255, null=True, blank=True, help_text="First name of the user."
    )
    last_name = models.CharField(
        max_length=255, null=True, blank=True, help_text="Last name of the user."
    )
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="attendee")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
        help_text="Date and time when the role was created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Update Date",
        help_text="Date and time when the role was last updated.",
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Deleted At",
        help_text="Date and time when the role was deleted.",
    )
    history = HistoricalRecords()

    @property
    def get_first_name(self):
        """Get first name"""
        return f"{self.first_name} " if self.first_name else "first_name"

    @property
    def get_full_name(self):
        """Combine first name and last name."""
        return (
            f"{self.first_name} {self.last_name}"
            if self.first_name and self.last_name
            else ""
        )

    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?
        """
        return True

    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        """
        return True

    def __str__(self) -> str:
        out_put_string = (
            f"{self.first_name} {self.last_name}"
            if self.first_name and self.last_name
            else f"Email {self.email}"
        )
        return out_put_string

    # Manually defining the groups and user_permissions fields with custom related_name
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_master_groups",
        blank=True,
        help_text="Groups this user belongs to.",
        related_query_name="user_master_group",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_master_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user_master_permission",
    )

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-id"]
