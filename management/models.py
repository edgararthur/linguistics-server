from django.db import models


class News(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/')
    type = models.CharField(max_length=10, default="News")  # TODO: Add choices for different types of news?

    def __str__(self):
        return f"{self.title}"


class Publications(models.Model):
    title = models.CharField(max_length=225)
    authors = models.TextField()
    abstract = models.TextField()
    file = models.FileField(upload_to='publications_file/')

    def __str__(self):
        return f"{self.title} {self.authors} {self.abstract}"


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
    description = models.TextField()
    position = models.CharField(max_length=200)
    year = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{self.name} {self.image}  {self.position} {self.year}"


class Consultants(models.Model):
    name = models.CharField(max_length=225)
    area_of_expertise = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.name} {self.area_of_expertise}"


class Collaborations(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    link = models.CharField(max_length=225)
    team = models.TextField()

    def __str__(self):
        return f"{self.title} {self.team}"


class Events(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    date = models.DateField(auto_now_add=False)
    location = models.CharField(max_length=225)
    image = models.ImageField(upload_to="events_images/")

    def __str__(self):
        return f"{self.title} {self.date} {self.location}"
    

class Projects(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    link = models.CharField(max_length=225)
    team = models.TextField()

    def __str__(self):
        return f"{self.title} {self.team}"

class Achievements(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=False)
    image = models.ImageField(upload_to="achievements_images/")

    def __str__(self):
        return f"{self.title} {self.description} {self.date} {self.image}"


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email} {self.message}"
    
