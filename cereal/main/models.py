from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Cereal(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey('main.Manufacturer', null=True)

    def __unicode__(self):
        return "%s" % self.name



class NutritionalFacts(models.Model):
    cereal = models.OneToOneField("main.Cereal")
    type = models.CharField(max_length=3,null=True)
    calories = models.IntegerField(null=True)
    protein_g = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    sodium = models.IntegerField(null=True)
    dietary_fiber = models.IntegerField(null=True)
    carbs = models.IntegerField(null=True)
    sugars = models.IntegerField(null=True)
    display_shelf = models.IntegerField(null=True)
    potassium = models.IntegerField(null=True)
    vitamins = models.IntegerField(null=True)
    minerals = models.IntegerField(null=True)
    serving_size_weight = models.IntegerField(null=True)
    cups_per_serving = models.FloatField(null=True)
    manufacturer = models.ForeignKey('main.Manufacturer', null=True)

    def __unicode__(self):
        return self.cereal.name



    def nutrition_list(self):
        value_list = []
        value_list.append("Protein: %s" % self.protein_g)
        value_list.append("Calories: %s" % self.calories)
        value_list.append("Fat: %s" % self.fat)
        value_list.append("Sodium: %s" % self.sodium)
        value_list.append("Fiber: %s" % self.dietary_fiber)
        value_list.append("Carbs: %s" % self.carbs)
        value_list.append("Sugars: %s" % self.sugars)
        value_list.append("Potassium: %s" % self.potassium)
        value_list.append("Vitamins and Minerals: %s" % self.vitamins)

        return value_list

