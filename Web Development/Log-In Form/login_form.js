var form = document.getElementById("login");

form.addEventListener("submit", function (event) {

    event.preventDefault()

    let name = document.getElementById("name").value.trim()
    let email = document.getElementById("email").value.trim()
    let password = document.getElementById("password").value.trim()

    let errormsg = "";

    if (name === "") {
        errormsg = "Name cannot be empty.";
    }

    else if (!email.includes("@")) {
        errormsg = "Please enter a valid email.";
    }

    else if (password.length < 6) {
        errormsg = "Password must contain at least of 6 characters.";
    }

    if (errormsg) {
        document.getElementById("error").textContent = errormsg;
    }

    else {
        document.getElementById("error").textContent = "";
        alert("You have logged in!");
    }
})
