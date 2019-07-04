from django.db import models

# Create your models here.

# store only base stats, calculate derived when character is accessed
class Char(models.Model):
	MAGE = 'M'
	TECHIE = 'T'
	FIGHTER = 'F'
	CLASS_CHOICES = [
		(MAGE, 'M'),
		(TECHIE, 'T'),
		(FIGHTER, 'F'),
	]
	name = models.CharField(max_length=30)
	age = models.IntegerField(default=0)
	char_class = models.CharField(
		max_length=1,
		choices=CLASS_CHOICES,
		default=MAGE,
	)
	vit = models.IntegerField(default=0)
	ten = models.IntegerField(default=0)
	stren = models.IntegerField(default=0)
	dex = models.IntegerField(default=0)
	awa = models.IntegerField(default=0)
	cha = models.IntegerField(default=0)
	ms = models.IntegerField(default=0)
	mag = models.IntegerField(default=0)
	intel = models.IntegerField(default=0)

	perks = models.TextField(max_length=10000) # prob excessive but it'll be O(10) Chars
	flaws = models.TextField(max_length=5000)
