# Generated by Django 2.2.1 on 2019-05-10 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moneris', '0002_auto_20190509_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('sale_order', models.AutoField(primary_key=True, serialize=False)),
                ('payment', models.CharField(choices=[('draft', 'Draft'), ('paid', 'Paid'), ('cancelled', 'Cancel')], max_length=111)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('payment_acquire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_by', to='moneris.Moneris')),
            ],
        ),
    ]
