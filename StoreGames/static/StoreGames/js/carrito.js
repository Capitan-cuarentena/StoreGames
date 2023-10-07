document.addEventListener("DOMContentLoaded", function() {
    // Seleccionar todos los elementos de botón de incrementar y disminuir
    const incrementButtons = document.querySelectorAll(".btn-outline-secondary:last-child");
    const decrementButtons = document.querySelectorAll(".btn-outline-secondary:first-child");


    // Buscar el formulario por su ID
    const csrfForm = document.getElementById("csrf-form");

    // Obtener el valor del token CSRF
    const csrftoken = csrfForm.querySelector('[name=csrfmiddlewaretoken]').value;

    // Agregar event listeners para los botones de incrementar
    incrementButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            const input = button.parentElement.querySelector(".form-control");
            const currentValue = parseInt(input.value);
            input.value = currentValue + 1;
        });
    });

    // Agregar event listeners para los botones de disminuir
    decrementButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            const input = button.parentElement.querySelector(".form-control");
            const currentValue = parseInt(input.value);
            if (currentValue > 1) {
                input.value = currentValue - 1;
            }
        });
    });

})
