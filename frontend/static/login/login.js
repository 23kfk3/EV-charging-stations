const formOpenBtn = document.querySelector("#form-open"),
  home = document.querySelector(".home"),
  formContainer = document.querySelector(".form_container"),
  formCloseBtn = document.querySelector(".form_close"),
  signupBtn = document.querySelector("#signup"),
  loginBtn = document.querySelector("#login"),
  pwShowHide = document.querySelectorAll(".pw_hide");

formOpenBtn.addEventListener("click", () => home.classList.add("show"));
formCloseBtn.addEventListener("click", () => home.classList.remove("show"));

pwShowHide.forEach((icon) => {
  icon.addEventListener("click", () => {
    let getPwInput = icon.parentElement.querySelector("input");
    if (getPwInput.type === "password") {
      getPwInput.type = "text";
      icon.classList.replace("uil-eye-slash", "uil-eye");
    } else {
      getPwInput.type = "password";
      icon.classList.replace("uil-eye", "uil-eye-slash");
    }
  });
});

signupBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.add("active");
});
loginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.remove("active");
});

function login() {
  var emailVal = document.getElementById("email").value;
  var passwordVal = document.getElementById("password").value;
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: emailVal,
      password: passwordVal,
    }),
  }
  fetch('/api/login', requestOptions)
    .then(response => {
      if (response.status == 202) {
        alert('Logged in successfully')
        window.location.replace('/')
      } else {
        alert('Incorrect email or password')
      }
    })
}

function signup() {
  var emailVal = document.getElementById("email2").value;
  var passwordVal = document.getElementById("password2").value;
  var name = document.getElementById("name").value;
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: emailVal,
      password: passwordVal,
    }),
  }
  fetch('/api/sign-up', requestOptions)
    .then(response => {
      if(response.status == 201){
        alert("User created successfully")
        window.location.replace('/')
      } else {
        alert("The email already exists")
      }
    })
}