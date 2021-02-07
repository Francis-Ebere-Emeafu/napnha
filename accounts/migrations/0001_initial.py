# Generated by Django 2.2.14 on 2021-02-07 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('community_of_origin', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.PositiveIntegerField(blank=True, choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('bio', models.TextField(blank=True, null=True)),
                ('year_of_award', models.DateField(blank=True, null=True)),
                ('nysc_service_year', models.DateField(blank=True, null=True)),
                ('place_of_primary_assignment', models.CharField(blank=True, max_length=300, null=True)),
                ('state_code', models.CharField(blank=True, max_length=30, null=True)),
                ('call_up_num', models.CharField(blank=True, max_length=30, null=True)),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='certificates')),
                ('napnha_number', models.PositiveIntegerField(blank=True, null=True)),
                ('profession', models.CharField(blank=True, max_length=200, null=True)),
                ('office_or_ministry', models.CharField(blank=True, max_length=200, null=True)),
                ('current_level', models.CharField(blank=True, max_length=200)),
                ('office_address', models.TextField(blank=True, null=True)),
                ('residential_address', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('confirm_email', models.BooleanField(default=False)),
                ('next_payment_due', models.DateField(blank=True, null=True)),
                ('registered_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('lga_of_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.LGA')),
                ('state_of_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state_of_origin', to='location.State')),
                ('state_of_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='state_of_service', to='location.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Renewal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
    ]
