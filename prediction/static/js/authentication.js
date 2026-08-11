
function showLogin() {

    document.getElementById("loginForm").style.display = "block";
    document.getElementById("registerForm").style.display = "none";

    document.getElementById("loginTab").classList.add("active");
    document.getElementById("registerTab").classList.remove("active");
}


function showRegister() {

    document.getElementById("loginForm").style.display = "none";
    document.getElementById("registerForm").style.display = "block";

    document.getElementById("registerTab").classList.add("active");
    document.getElementById("loginTab").classList.remove("active");
}


async function login() {

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const message = document.getElementById("message");

    if (username === "" || password === "") {
        message.style.color = "red";
        message.innerHTML = "Please fill all fields.";
        return;
    }

    try {

     const response = await fetch("/prediction/login/",  {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })

        });

        const data = await response.json();

        if (response.ok) {

            localStorage.setItem("access", data.access);
            localStorage.setItem("refresh", data.refresh);

            message.style.color = "green";
            message.innerHTML = "Login Successful";

            setTimeout(() => {
                window.location.href = "/prediction/dashboard-page/";
            }, 1000);

        } else {

            message.style.color = "red";
            message.innerHTML = data.detail || "Invalid Username or Password";

        }

    } catch (error) {

        console.log(error);

        message.style.color = "red";
        message.innerHTML = "Server Error";

    }

}


async function register() {

    const username = document.getElementById("register-username").value.trim();
    const email = document.getElementById("register-email").value.trim();
    const password = document.getElementById("register-password").value.trim();

    const message = document.getElementById("register-message");

    if (username === "" || email === "" || password === "") {

        message.style.color = "red";
        message.innerHTML = "Please fill all fields.";
        return;

    }

    try {

        const response = await fetch("/prediction/register/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                email: email,
                password: password
            })

        });

        const data = await response.json();

        if (response.ok) {

            message.style.color = "green";
            message.innerHTML = "Registration Successful";

            document.getElementById("register-username").value = "";
            document.getElementById("register-email").value = "";
            document.getElementById("register-password").value = "";

            setTimeout(() => {

                showLogin();

            }, 1000);

        } else {

            message.style.color = "red";

            if (data.username) {
                message.innerHTML = data.username[0];
            }
            else if (data.email) {
                message.innerHTML = data.email[0];
            }
            else if (data.password) {
                message.innerHTML = data.password[0];
            }
            else if (data.detail) {
                message.innerHTML = data.detail;
            }
            else {
                message.innerHTML = "Registration Failed";
            }

        }

    } catch (error) {

        console.log(error);

        message.style.color = "red";
        message.innerHTML = "Server Error";

    }

}