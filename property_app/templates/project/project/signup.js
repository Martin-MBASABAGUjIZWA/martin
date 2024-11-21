const username = document.querySelector('#username');
const password = document.querySelector('#password');
const password2 = document.querySelector('#password2');
const email = document.querySelector('#email');
const submit = document.querySelector('#submit');
submit.addEventListener('click', (Event) => {
    Event.preventDefault();
    if (username.value.trim() == "") {
        error(username, "username can not be empty");
    } else {
        success(username);

    }
    if (password.value.trim() == "") {
        error(password, "password is required");
    } else {
        if (password.value.length < 8) {
            error(password, "password must be at least 8 characters");
        } else if (password.value.length > 20) {
            error(password, "password must be at least 20 characters");
        } else {
            success(password);
        }

    }
    if (password2.value.trim() == "") {
        error(password2, "please confirm your password");
    } else {
        if (password2.value.trim() !== password.value.trim()) {
            error(password2, " your password is incorrect ");
        } else {
            success(password2);
        }
    }
    if (email.value.trim() == "") {
        error(email, "email can not be empty");
    } else {
        if (!isValidEmail(email.value.trim())) {
            error(email, "email is not valid");
        } else {
            success(email);
        }
    }
});

function error(element, msg) {
    element.style.border = '3px red solid ';
    const parent = element.parentElement;
    const p = parent.querySelector('p');
    p.textContent = msg;
    p.style.visibility = "visible";
}

function success(element) {
    element.style.border = '3px green solid ';
    const parent = element.parentElement;
    const p = parent.querySelector('p');
    p.style.visibility = "hidden";

}

function isValidEmail(email) {
    return /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}