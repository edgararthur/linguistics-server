from django.db import models


class News(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return f"{self.title}"


class Members(models.Model):
    REGULAR_MEMBER = 'regular member'
    HONARY_MEMBER = 'honary member'

    MEMBERSHIPS = [
        (REGULAR_MEMBER, 'regular member'),
        (HONARY_MEMBER, 'honary member'),
    ]

    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to="members_images/")
    type_of_membership = models.CharField(max_length=20, choices=MEMBERSHIPS)

    def __str__(self):
        return f"{self.name}"


class Leadership(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to="leadership/")
    position = models.CharField(max_length=200)
    year = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{self.name}  {self.image}  {self.postion}  {self.year}"


class Consultants(models.Model):
    name = models.CharField(max_length=225)
    type_of_consult = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.name} {self.type_of_consult}"


class Collaborations(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    link = models.CharField(max_length=225)
    team = models.TextField()

    def __str__(self):
        return f"{self.title} {self.team}"
