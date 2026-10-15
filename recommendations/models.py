from django.db import models

class TravelPackage(models.Model):

    TRAVEL_TYPES = [
        ("Solo", "Solo"),
        ("Friends", "Friends"),
        ("Family", "Family"),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    travel_type = models.CharField(
        max_length=20,
        choices=TRAVEL_TYPES
    )

    price = models.IntegerField()

    food_score = models.IntegerField(default=3)
    nature_score = models.IntegerField(default=3)
    adventure_score = models.IntegerField(default=3)
    heritage_score = models.IntegerField(default=3)
    budget_score = models.IntegerField(default=3)
    comfort_score = models.IntegerField(default=3)

    def __str__(self):
        return self.name
