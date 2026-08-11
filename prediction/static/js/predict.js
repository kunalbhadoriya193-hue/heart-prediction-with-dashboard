async function predict() {

    const token = localStorage.getItem("access");

    if (!token) {
        window.location.href = "/prediction/auth/";
        return;
    }

    const response = await fetch("/prediction/", {

        method: "POST",

        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            Age: Number(document.getElementById("age").value),

            Sex: document.getElementById("sex").value,

            ChestPainType: document.getElementById("chestPain").value,

            RestingBP: Number(document.getElementById("restingBP").value),

            Cholesterol: Number(document.getElementById("cholesterol").value),

            FastingBS: Number(document.getElementById("fastingBS").value),

            RestingECG: document.getElementById("restingECG").value,

            MaxHR: Number(document.getElementById("maxHR").value),

            Oldpeak: Number(document.getElementById("oldPeak").value),

            ExerciseAngina: document.getElementById("exerciseAngina").value,

            ST_Slope: document.getElementById("stSlope").value

        })

    });

    const data = await response.json();

    console.log(data);

    if (response.ok) {

        document.getElementById("result").innerHTML = data.result;

        document.getElementById("chance").innerHTML =
            "Chance : " + (data.chance * 100).toFixed(2) + "%";

    }
    else {

        alert(JSON.stringify(data));

    }

}