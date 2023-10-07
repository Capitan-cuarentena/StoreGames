const formulario = document.getElementById("formulario3");
const correoInput = document.getElementById("correo");
const mensajeEnviado = document.createElement("p");
mensajeEnviado.innerText = "Se ha enviado un correo electrónico.";
mensajeEnviado.style.color = "green";
mensajeEnviado.classList.add("mensaje-enviado");
mensajeEnviado.style.display = "none";
correoInput.parentNode.appendChild(mensajeEnviado);

formulario.addEventListener("submit", function (event) {
    event.preventDefault();

    setTimeout(function () {
        mensajeEnviado.style.display = "block";
    }, 0);
});


const formularioIngresoContenido = document.getElementById("formularioingresocontenido");
const nombreJuegoInput = document.getElementById("nombrejuego");
const mensajeIngresado = document.createElement("p");
mensajeIngresado.innerText = "Contenido ingresado correctamente.";
mensajeIngresado.style.color = "green";
mensajeIngresado.classList.add("mensaje-ingresado");
mensajeIngresado.style.display = "none";
nombreJuegoInput.parentNode.appendChild(mensajeIngresado);

formularioIngresoContenido.addEventListener("submit", function (event) {
    event.preventDefault();

    setTimeout(function () {
        mensajeIngresado.style.display = "block";
    }, 0);
});