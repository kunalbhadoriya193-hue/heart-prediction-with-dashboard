from rest_framework import serializers
from django.contrib.auth.models import User
from.models import PredictionSave

class PredictionSerializer(serializers.Serializer):
    Age = serializers.IntegerField(min_value=1)
    Sex = serializers.ChoiceField(choices=["M", "F"])

    ChestPainType = serializers.ChoiceField(
        choices=["ATA", "NAP", "ASY", "TA"]
    )

    RestingBP = serializers.IntegerField(min_value=0)
    Cholesterol = serializers.IntegerField(min_value=0)
    FastingBS = serializers.ChoiceField(choices=[0, 1])

    RestingECG = serializers.ChoiceField(
        choices=["Normal", "ST", "LVH"]
    )

    MaxHR = serializers.IntegerField(min_value=1)

    ExerciseAngina = serializers.ChoiceField(
        choices=["Y", "N"]
    )

    Oldpeak = serializers.FloatField()

    ST_Slope = serializers.ChoiceField(
        choices=["Up", "Flat", "Down"]
    )
class PredictionHistroySerializer(serializers.ModelSerializer):
 class Meta:
    model = PredictionSave
    fields = "__all__"

class UserRegisterSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ["username","email","password"]
   
   def create(self, validated_data):
      user = User(
         username = validated_data["username"],
         email = validated_data["email"]
      )

      user.set_password(validated_data["password"])
      user.save()
      return user