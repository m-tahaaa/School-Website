from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="AdmissionApplication", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("child_name", models.CharField(max_length=150)),
            ("date_of_birth", models.DateField()),
            ("gender", models.CharField(choices=[("male", "Male"), ("female", "Female"), ("other", "Other")], max_length=10)),
            ("class_sought", models.CharField(max_length=50)),
            ("parent_name", models.CharField(max_length=150)),
            ("phone_number", models.CharField(max_length=20)),
            ("email", models.EmailField(blank=True, max_length=254)),
            ("address", models.TextField()),
            ("submission_date", models.DateTimeField(auto_now_add=True, db_index=True)),
            ("status", models.CharField(choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")], db_index=True, default="pending", max_length=10)),
        ], options={"ordering": ["-submission_date"], "verbose_name": "admission application", "verbose_name_plural": "admission applications"}),
        migrations.CreateModel(name="Event", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=180)), ("event_date", models.DateField(db_index=True)), ("description", models.TextField()), ("venue", models.CharField(max_length=150)),
        ]),
        migrations.CreateModel(name="GalleryPhoto", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=150)), ("image", models.FileField(upload_to="gallery/%Y/%m/")), ("category", models.CharField(choices=[("campus", "Campus"), ("academics", "Academics"), ("events", "Events"), ("sports", "Sports")], db_index=True, default="campus", max_length=20)), ("date_added", models.DateTimeField(auto_now_add=True, db_index=True)),
        ]),
        migrations.CreateModel(name="Notice", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=180)), ("category", models.CharField(choices=[("general", "General"), ("exam", "Exam"), ("sports", "Sports"), ("holiday", "Holiday")], db_index=True, default="general", max_length=20)), ("content", models.TextField()), ("date_posted", models.DateTimeField(auto_now_add=True, db_index=True)), ("is_pinned", models.BooleanField(db_index=True, default=False)),
        ], options={"ordering": ["-is_pinned", "-date_posted"], "verbose_name": "notice", "verbose_name_plural": "notices"}),
        migrations.AddIndex(model_name="admissionapplication", index=models.Index(fields=["status", "-submission_date"], name="school_admi_status_1c4a0f_idx")),
        migrations.AddIndex(model_name="admissionapplication", index=models.Index(fields=["class_sought", "-submission_date"], name="school_admi_class_s_6ad3fd_idx")),
        migrations.AddIndex(model_name="notice", index=models.Index(fields=["category", "-date_posted"], name="school_noti_categor_9e30bf_idx")),
        migrations.AddIndex(model_name="notice", index=models.Index(fields=["is_pinned", "-date_posted"], name="school_noti_is_pinn_3f17b0_idx")),
        migrations.AddIndex(model_name="event", index=models.Index(fields=["event_date", "venue"], name="school_even_event_d_6a8b8d_idx")),
    ]
