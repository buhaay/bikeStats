from django.db import models

# Create your models here.
class Statistics(models.Model):
	def __str__(self):
		return '{}, {} km, {}'.format(self.date, self.distance, self.ride_time)

	date = models.DateField('Numer tygodnia.')
	distance = models.DecimalField('Przebyty dystans.', max_digits=5, decimal_places=2)
	ride_time = models.DurationField('Czas jazdy.')
	max_speed = models.DecimalField('Maksymalna prędkość', max_digits=3, decimal_places=1)
	average_speed = models.DecimalField('Średnia prędkość.', max_digits=3, decimal_places=1)
	calories = models.DecimalField('Kalorie.', max_digits=5, decimal_places=1)
	f_calories = models.DecimalField('F_kalorie.', max_digits=5, decimal_places=1)

