from django.db import models
from core.models import User
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Perspective(models.Model):
    perspective_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perspective_name = models.CharField(max_length=120, blank=False)
    perspective_weight = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='bsc_perspective')

    def __str__(self):
        return f"{self.perspective_name}"


class Objectives(models.Model):
    objective_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objective_name = models.CharField(max_length=120, blank=False)
    objective_weight = models.FloatField(blank=False)
    perspective = models.ForeignKey(Perspective, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='bsc_objective')

    def __str__(self):
        return f"{self.objective_name}"


class KPI(models.Model):
    kpi_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kpi_name = models.CharField(max_length=120, blank=False)
    kpi_target = models.FloatField(blank=True, default=0)
    kpi_q1 = models.IntegerField(blank = True, null = True)
    kpi_q2 = models.IntegerField(blank = True, null = True)
    kpi_q3 = models.IntegerField(blank = True, null = True)
    kpi_q4 = models.IntegerField(blank = True, null = True)
    kpi_weight = models.FloatField(blank=True, default=0)

    class Types(models.TextChoices):
        Percentage = "Percentage", "Percentage"
        ETB = "ETB", "ETB"
        USD = "USD", "USD"
        Numbers = "Numbers", "Numbers"
        Levels = "Levels", "Levels"

    default_kpi_unit_measurement = Types.Percentage

    kpi_unit_measurement = models.CharField(
        _("kpi_unit_measurement"), max_length=50, choices=Types.choices, default=default_kpi_unit_measurement
    )
    perspective = models.ForeignKey(Perspective, on_delete=models.CASCADE)
    objective = models.ForeignKey(Objectives, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bsc_user')
    January = models.FloatField(blank=True, default=0)
    February = models.FloatField(blank=True, default=0)
    March = models.FloatField(blank=True, default=0)
    April = models.FloatField(blank=True, default=0)
    May = models.FloatField(blank=True, default=0)
    June = models.FloatField(blank=True, default=0)
    July = models.FloatField(blank=True, default=0)
    August = models.FloatField(blank=True, default=0)
    September = models.FloatField(blank=True, default=0)
    October = models.FloatField(blank=True, default=0)
    November = models.FloatField(blank=True, default=0)
    December = models.FloatField(blank=True, default=0)
    Score_January = models.FloatField(blank=True, default=0)
    Score_February = models.FloatField(blank=True, default=0)
    Score_March = models.FloatField(blank=True, default=0)
    Score_April = models.FloatField(blank=True, default=0)
    Score_May = models.FloatField(blank=True, default=0)
    Score_June = models.FloatField(blank=True, default=0)
    Score_July = models.FloatField(blank=True, default=0)
    Score_August = models.FloatField(blank=True, default=0)
    Score_September = models.FloatField(blank=True, default=0)
    Score_October = models.FloatField(blank=True, default=0)
    Score_November = models.FloatField(blank=True, default=0)
    Score_December = models.FloatField(blank=True, default=0)
    aggregate = models.FloatField(blank=True, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.kpi_name}"
