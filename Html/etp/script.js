function validateName(){
    const name = document.getElementById("name").value;
    const nameInput = document.getElementById("name");
    const nameMessage = document.getElementById("nameMessage");
    if (name.length >=3){
        nameInput.style.borderColor = "green";
        nameMessage.textContent = "Name looks good";
        nameMessage.style.color = "green";
        return true;

    }
    else{
        nameInput.style.borderColor = "red";
        nameMessage.textContent = "Name should be greater than 3 character";
        nameMessage.style.color = "red";
        return false;
    }
}
function validateEmail(){
    const email = document.getElementById("email").value;
    const emailInput = document.getElementById("email");
    const emailMessage = document.getElementById("emailMessage");
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z{2,6}$]/;
    if (emailPattern.test(email)){
        emailInput.style.borderColor = "green";
        emailMessage.textContent = "Valid Email";
        emailMessage.style.color = "green";
        return true;

    }
    else{
        emailInput.style.borderColor = "red";
        emailMessage.textContent = "Enter a valid email";
        emailMessage.style.color = "red";
        return false;
    }
}
function validatePassword(){
    const password = document.getElementById("password").value;
    const passwordInput = document.getElementById("password");
    const passwordMessage = document.getElementById("passwordMessage");
    // const passwordPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z{2,6}$]/;
    if (password.length >=6){
        passwordInput.style.borderColor = "green";
        passwordMessage.textContent = "Valid password";
        passwordMessage.style.color = "green";
        return true;

    }
    else{
        passwordInput.style.borderColor = "red";
        passwordMessage.textContent = "Enter a valid password";
        passwordMessage.style.color = "red";
        return false;
    }
}

document.getElementById("myform").addEventListener("submit",function(event){
    const isvalidName=validateName();
    const isvalidEmail=validateEmail();
    const isvalidPassword=validatePassword();
    if (!isvalidName || !isvalidEmail || !isvalidPassword) {
        alert("Form is not submitted");
        event.preventDefault();
    }
    else{
        alert("Form is submitted successfully");
    }
});
