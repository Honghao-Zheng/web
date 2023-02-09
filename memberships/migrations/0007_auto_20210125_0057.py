# Generated by Django 3.1.5 on 2021-01-25 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("memberships", "0006_failedpayment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="member",
            options={
                "permissions": (("has_sand_membership", "Member has paid sand"),),
                "verbose_name": "member",
                "verbose_name_plural": "members",
            },
        ),
        migrations.RenameField(
            model_name="failedpayment",
            old_name="stripe_user_id",
            new_name="stripe_customer_id",
        ),
        migrations.AddField(
            model_name="membership",
            name="last_payment_time",
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_subscription_id", models.CharField(max_length=255)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="memberships.member",
                    ),
                ),
            ],
        ),
    ]
