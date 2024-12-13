from django.db import models
from simple_history.models import HistoricalRecords

class RoleMaster(models.Model):
    """
    Model to store role details.
    """

    name = models.CharField(max_length=100, help_text="Enter the name of the role.")
    is_active = models.BooleanField(
        default=True, help_text="Whether the role is active."
    )
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

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "role_master"
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["-id"]
