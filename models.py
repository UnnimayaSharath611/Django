from django.db import models

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    # Social Media Links
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    # Contact Details
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # About Information
    about_text = models.TextField(blank=True, null=True)

    # Resume & Projects
    resume_link = models.URLField(blank=True, null=True)
    projects_link = models.URLField(blank=True, null=True)
    portfolio_link = models.URLField(blank=True, null=True)

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.IntegerField(default=2020)

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience_entries')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skill_entries')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

class SocialMediaLinks(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=50)  # e.g., "LinkedIn", "Twitter"
    url = models.URLField()

    def __str__(self):
        return f"{self.platform}: {self.url}"

class FooterData(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    twitter = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return f"Footer Information"


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
