from rest_framework import serializers
from bikeStatsApp.models import Statistics

class StatisticsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Statistics
		fields = ('date', 'distance', 'ride_time', 'max_speed', 'average_speed', 'calories', 'f_calories')

		# def create(self, validated_data):
		# 	return Statistics.objects.create(**validated_data)

		# def update(self, instance, validated_data):
		# 	instance.date = validated_data.get('date', instance.date)
		# 	instance.distance = validated_data.get('distance', instance.distance)
		# 	instance.ride_time = validated_data.get('ride_time', instance.ride_time)
		# 	instance.max_speed = validated_data.get('max_speed', instance.max_speed)
		# 	instance.average_speed = validated_data.get('average_speed', instance.average_speed)
		# 	instance.calories = validated_data.get('calories', instance.calories)
		# 	instance.f_calories = validated_data.get('f_calories', instance.f_calories)
		# 	instance.save()
		# 	return instance