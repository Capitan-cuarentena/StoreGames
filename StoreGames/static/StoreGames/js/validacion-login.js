//exito de login
const FormLogin = document.querySelector("#FormLogin")
btnLogin.addEventListener('click',event => {
    event.preventDefault()
    
    if (emaillog.value !== "" && passlog.value !== "") {
        alert("Inicio de sesión exitoso");
    } else {
        alert("Completa todos los datos");
    }
});


