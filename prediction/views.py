from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import (
    PredictionSerializer,
    PredictionHistroySerializer,
    UserRegisterSerializer,
)

from .models import PredictionSave
from .ml import model, scaler


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def home(request):

    if request.method == "GET":
        return Response({
            "message": "Heart Disease Prediction API"
        })

    serializer = PredictionSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data

    age = data["Age"]
    resting_bp = data["RestingBP"]
    cholesterol = data["Cholesterol"]
    fasting_bs = data["FastingBS"]
    max_hr = data["MaxHR"]
    oldpeak = data["Oldpeak"]

    sex = data["Sex"]
    chest_pain = data["ChestPainType"]
    resting_ecg = data["RestingECG"]
    exercise_angina = data["ExerciseAngina"]
    st_slope = data["ST_Slope"]

    sex_m = 1 if sex == "M" else 0

    chestpain_ata = 1 if chest_pain == "ATA" else 0
    chestpain_nap = 1 if chest_pain == "NAP" else 0
    chestpain_ta = 1 if chest_pain == "TA" else 0

    restingecg_normal = 1 if resting_ecg == "Normal" else 0
    restingecg_st = 1 if resting_ecg == "ST" else 0

    exerciseangina_y = 1 if exercise_angina == "Y" else 0

    stslope_flat = 1 if st_slope == "Flat" else 0
    stslope_up = 1 if st_slope == "Up" else 0

    input_features = [[
        age,
        resting_bp,
        cholesterol,
        fasting_bs,
        max_hr,
        oldpeak,
        sex_m,
        chestpain_ata,
        chestpain_nap,
        chestpain_ta,
        restingecg_normal,
        restingecg_st,
        exerciseangina_y,
        stslope_flat,
        stslope_up
    ]]

    input_scaled = scaler.transform(input_features)

    prediction = int(model.predict(input_scaled)[0])

    chance = None

    if hasattr(model, "predict_proba"):
        chance = float(model.predict_proba(input_scaled)[0][prediction])

    PredictionSave.objects.create(
        user = request.user,
        age=age,
        sex=sex,
        chest_pain=chest_pain,
        resting_bp=resting_bp,
        cholesterol=cholesterol,
        fasting_bs=fasting_bs,
        resting_ecg=resting_ecg,
        max_hr=max_hr,
        oldpeak=oldpeak,
        exercise_angina=exercise_angina,
        st_slope=st_slope,
        prediction=prediction,
        chance=chance
    )

    return Response(
        {
            "prediction": prediction,
            "result": "Heart Disease" if prediction == 1 else "No Heart Disease",
            "chance": chance
        },
        status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def history(request):

    predictions = PredictionSave.objects.filter(user=request.user)

    serializer = PredictionHistroySerializer(
        predictions,
        many=True
    )

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_history(request, id):

    try:
        prediction = PredictionSave.objects.get(
            id=id,
            user = request.user 
            )

        prediction.delete()

        return Response(
            {
                "message": "Deleted Successfully"
            },
            status=status.HTTP_200_OK
        )

    except PredictionSave.DoesNotExist:

        return Response(
            {
                "error": "Prediction not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

def home_page(request):
    return render(request, "home.html")

@api_view(["POST"])
def register(request):

    serializer = UserRegisterSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(
            {
                "message": "User Registered Successfully"
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):

    predictions = PredictionSave.objects.filter(user=request.user)

    total_predictions = predictions.count()

    heart_disease = predictions.filter(prediction=1).count()

    no_heart_disease = predictions.filter(prediction=0).count()

    return Response({
        "total_predictions": total_predictions,
        "heart_disease": heart_disease,
        "no_heart_disease": no_heart_disease,
    })

def auth_page(request):
    return render(request, "auth.html")

def dashboard_page(request):
    return render(request, "dashboard.html")


def prediction_page(request):
    return render(request, "predict.html ")

def history_page(request):
    return render(request, "history.html")