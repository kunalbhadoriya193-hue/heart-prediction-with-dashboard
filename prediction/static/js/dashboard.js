async function loadDashboard() {

    const token = localStorage.getItem("access");

    if (!token) {
        window.location.href = "/prediction/auth/";
        return;
    }

    try {

        const response = await fetch("http://127.0.0.1:8000/prediction/dashboard/", {

            method: "GET",

            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }

        });

        if (!response.ok) {

            localStorage.clear();
            window.location.href = "/prediction/auth/";
            return;

        }

        const data = await response.json();

        document.getElementById("total").innerText = data.total_predictions;
        document.getElementById("heart").innerText = data.heart_disease;
        document.getElementById("healthy").innerText = data.no_heart_disease;

    } catch (error) {

        console.log(error);
        alert("Unable to load dashboard.");

    }

}

loadDashboard();


function logout() {

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    window.location.href = "/prediction/auth/";
}