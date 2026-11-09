from datetime import date

from django import forms

from .models import AdmissionApplication


class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = (
            "child_name",
            "date_of_birth",
            "gender",
            "class_sought",
            "parent_name",
            "phone_number",
            "email",
            "address",
        )
        widgets = {
            "child_name": forms.TextInput(attrs={"placeholder": "Student's full name"}),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "class_sought": forms.Select(
                choices=[
                    ("Nursery", "Nursery"),
                    ("KG", "Kindergarten"),
                    ("1", "Class 1"),
                    ("2", "Class 2"),
                    ("3", "Class 3"),
                    ("4", "Class 4"),
                    ("5", "Class 5"),
                    ("6", "Class 6"),
                    ("7", "Class 7"),
                    ("8", "Class 8"),
                    ("9", "Class 9"),
                ]
            ),
            "parent_name": forms.TextInput(attrs={"placeholder": "Parent or guardian name"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "+880 1XXX XXXXXX"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "address": forms.Textarea(attrs={"rows": 3, "placeholder": "Present residential address"}),
        }

    def clean_date_of_birth(self):
        birth_date = self.cleaned_data["date_of_birth"]
        if birth_date >= date.today():
            raise forms.ValidationError("Date of birth must be in the past.")
        return birth_date

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"].strip()
        digits = "".join(character for character in phone_number if character.isdigit())
        if len(digits) < 10:
            raise forms.ValidationError("Please enter a valid contact number.")
        return phone_number
