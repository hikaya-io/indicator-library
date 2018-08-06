from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
import uuid

# Create your models here.    created_by = models.ForeignKey('auth.User', related_name='indicators', null=True, blank=True, on_delete=models.SET_NULL)

class Source(models.Model):
    source_uuid = models.CharField(max_length=500,verbose_name='Source UUID', default=uuid.uuid4, unique=True, blank=True)
    name = models.CharField(max_length=500, blank=False)

class Frequency(models.Model):
    frequency_uuid = models.CharField(max_length=500, verbose_name='Frequency UUID', default=uuid.uuid4, unique=True, blank=True)
    frequency = models.CharField(max_length=500, blank=False)

class AdditionalFields(models.Model):
    additional_fields_uuid = models.CharField(max_length=500, verbose_name="Additional Field UUID", default=uuid.uuid4, unique=True, blank=True)
    additional_fields = JSONField()

class Indicator(models.Model):
    indicator_uuid = models.TextField(max_length=500,verbose_name='Indicator UUID', default=uuid.uuid4, unique=True, blank=True)
    level = models.TextField(blank=True)
    # class Meta:
    #     ordering = ('level',)
    objectives = models.CharField(max_length=500, blank=True,verbose_name="Objective")
    name = models.TextField(max_length = 1000, null=False)
    sector = models.CharField(max_length=500, null=True, blank=True)
    # class Meta:
    #     ordering = ('sector',)
    subsector = models.CharField(max_length=500, null=True, blank=True)
    comments = models.TextField(max_length=1500, null=True, blank=True)
    data_source = models.ForeignKey(Source, null=True, blank=True, verbose_name="Indicator Source", on_delete=models.CASCADE)
    additional_fields = models.ForeignKey(AdditionalFields, null=True, blank=True, on_delete=models.CASCADE)
    tags = models.CharField(max_length=500, null=True, blank=True)
    number = models.CharField(max_length=500, null=True, blank=True)
    definition = models.TextField(null=True, blank=True)
    justification = models.TextField(max_length=500, null=True, blank=True, verbose_name="Rationale or Justification for Indicator")
    unit_of_measure = models.TextField(max_length=500, null=True, blank=True, verbose_name="Unit of Measure")
    unit_description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Unit Description"),
    disaggregation = models.TextField(max_length=500, blank=True)
    direction_of_change = models.TextField(max_length=500, null=True, blank=True, verbose_name="Direction of Change"),
    baseline = models.TextField(max_length=500, null=True, blank=True)
    lop_target = models.IntegerField("LOP Target",default=0, blank=True)
    rationale_for_target = models.TextField(max_length=500, null=True, blank=True)
    means_of_verification = models.TextField(max_length=500, null=True, blank=True, verbose_name="Means of Verification")
    question_format = models.TextField(max_length=500, null=True, blank=True, verbose_name="Question Format"),
    data_collection_method = models.TextField(max_length=500, null=True, blank=True, verbose_name="Data Collection Method")
    data_collection_frequency = models.ForeignKey(Frequency, related_name="data_collection_frequency",null=True, blank=True, verbose_name="Frequency of Data Collection", on_delete=models.CASCADE)
    denominator = models.TextField(max_length=500, null=True, blank=True)
    numerator = models.TextField(max_length=500, null=True, blank=True)
    data_points = models.TextField(max_length=500, null=True, blank=True, verbose_name="Data Points")
    responsible_person = models.TextField(max_length=500, null=True, blank=True, verbose_name="Responsible Person(s) and Team")
    method_of_analysis = models.TextField(max_length=500, null=True, blank=True, verbose_name="Method of Analysis")
    information_use = models.TextField(max_length=500, null=True, blank=True, verbose_name="Information Use")
    reporting_frequency = models.ForeignKey(Frequency, null=True, blank=True, verbose_name="Frequency of Reporting", on_delete=models.CASCADE)
    quality_assurance = models.TextField(max_length=500, null=True, blank=True, verbose_name="Quality Assurance Measures")
    data_issues = models.TextField(max_length=500, null=True, blank=True, verbose_name="Data Issues")
    indicator_changes = models.TextField(max_length=500, null=True, blank=True, verbose_name="Changes to Indicator")
    comments = models.TextField(max_length=500, null=True, blank=True)
    key_performance_indicator = models.BooleanField("Key Performance Indicator?",default=False)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name
