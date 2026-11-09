from django.core.validators import FileExtensionValidator
from django.db import models


class Notice(models.Model):
    class Category(models.TextChoices):
        GENERAL = "general", "General"
        EXAM = "exam", "Exam"
        SPORTS = "sports", "Sports"
        HOLIDAY = "holiday", "Holiday"

    title = models.CharField(max_length=180)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.GENERAL,
        db_index=True,
    )
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, db_index=True)
    is_pinned = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-is_pinned", "-date_posted"]
        indexes = [
            models.Index(fields=["category", "-date_posted"]),
            models.Index(fields=["is_pinned", "-date_posted"]),
        ]
        verbose_name = "notice"
        verbose_name_plural = "notices"

    def __str__(self):
        return self.title


class AdmissionApplication(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    child_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=Gender.choices)
    class_sought = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        db_index=True,
    )

    class Meta:
        ordering = ["-submission_date"]
        indexes = [
            models.Index(fields=["status", "-submission_date"]),
            models.Index(fields=["class_sought", "-submission_date"]),
        ]
        verbose_name = "admission application"
        verbose_name_plural = "admission applications"

    def __str__(self):
        return f"{self.child_name} - {self.class_sought}"


class GalleryPhoto(models.Model):
    class Category(models.TextChoices):
        CAMPUS = "campus", "Campus"
        ACADEMICS = "academics", "Academics"
        EVENTS = "events", "Events"
        SPORTS = "sports", "Sports"

    title = models.CharField(max_length=150)
    image = models.FileField(
        upload_to="gallery/%Y/%m/",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"])],
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.CAMPUS,
        db_index=True,
    )
    date_added = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-date_added"]
        verbose_name = "gallery photo"
        verbose_name_plural = "gallery photos"

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=180)
    event_date = models.DateField(db_index=True)
    description = models.TextField()
    venue = models.CharField(max_length=150)

    class Meta:
        ordering = ["event_date", "title"]
        indexes = [models.Index(fields=["event_date", "venue"])]

    def __str__(self):
        return f"{self.title} ({self.event_date:%d %b %Y})"
