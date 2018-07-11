# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class AdditionalFields(models.Model):
    additional_fields_uuid = models.CharField(unique=True, max_length=255)
    additional_fields = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'quickstart_additionalfields'


class Frequency(models.Model):
    frequency_uuid = models.CharField(unique=True, max_length=255)
    frequency = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'quickstart_frequency'


class Indicator(models.Model):
    indicator_uuid = models.CharField(unique=True, max_length=255)
    level = models.CharField(max_length=255)
    objectives = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sector = models.TextField()  # This field type is a guess.
    subsector = models.TextField()  # This field type is a guess.
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    number = models.CharField(max_length=255, blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    justification = models.TextField(blank=True, null=True)
    unit_of_measure = models.CharField(max_length=135, blank=True, null=True)
    disaggregation = models.CharField(max_length=255)
    baseline = models.CharField(max_length=255, blank=True, null=True)
    lop_target = models.IntegerField()
    rationale_for_target = models.TextField(blank=True, null=True)
    means_of_verification = models.CharField(max_length=255, blank=True, null=True)
    data_collection_method = models.CharField(max_length=255, blank=True, null=True)
    denominator = models.CharField(max_length=255, blank=True, null=True)
    numerator = models.CharField(max_length=255, blank=True, null=True)
    data_points = models.TextField(blank=True, null=True)
    responsible_person = models.CharField(max_length=255, blank=True, null=True)
    method_of_analysis = models.CharField(max_length=255, blank=True, null=True)
    information_use = models.CharField(max_length=255, blank=True, null=True)
    quality_assurance = models.TextField(blank=True, null=True)
    data_issues = models.TextField(blank=True, null=True)
    indicator_changes = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    key_performance_indicator = models.BooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    additional_fields = models.ForeignKey(AdditionalFields, models.DO_NOTHING, blank=True, null=True)
    data_collection_frequency = models.ForeignKey(Frequency, models.DO_NOTHING, blank=True, null=True)
    data_source = models.ForeignKey('Source', models.DO_NOTHING, blank=True, null=True)
    reporting_frequency = models.ForeignKey(Frequency, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quickstart_indicator'


class Source(models.Model):
    source_uuid = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'quickstart_source'
