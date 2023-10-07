const formulario = document.getElementById("formulario1");
const inputs = document.querySelectorAll('.form-control')

formulario.addEventListener('submit', e => {
    e.preventDefault();  
    
    if (campos.nombre && campos.apellido && campos.correo && campos.user && campos.pass && campos.pass2) {
        

        document.getElementById('formulario__mensaje-exito').classList.remove('d-none')
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.add('d-none')
        }, 5000)

        document.querySelectorAll(`.grupo__all`).forEach((item) => {
            item.classList.remove('formulario__grupo-correcto')
        })
        formulario.submit()
    }

    console.log('hola')
});

// mensaje error al click enviar y no esta formulario completo
document.getElementById('btnEnviar').addEventListener('click', () => {

    if (!campos.nombre || !campos.apellido || !campos.correo || !campos.user || !campos.pass || !campos.pass2) {
        document.getElementById('formulario__mensaje-error').classList.remove('d-none')
        console.log(campos)

        setTimeout(() => {
            document.getElementById('formulario__mensaje-error').classList.add('d-none')
        }, 5000)
    }
})

// boton limpiar
document.getElementById('resetForm').addEventListener('click', () => {
    formulario.reset()
    document.querySelectorAll(`.grupo__all`).forEach((item) => {
        item.classList.remove('formulario__grupo-correcto')
        item.classList.remove('formulario__grupo-incorrecto')
    })
})

// expresiones regulares
const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    user: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    pass: /^(?=.*[A-Z])(?=.*\d).{4,12}$/, // Al menos una letra mayuscula y al menos un numero

}


// boolean status de cada campo
let campos = {
    nombre: false,
    apellido: false,
    correo: false,
    user: false,
    pass: false, 
    pass2: false,

}

const validarForm = (e) => {
    switch(e.target.id){
        case 'nombre':
            validarCampo(expresiones.nombre, e.target, 'nombre');
        break

        case 'apellido':
            validarCampo(expresiones.apellido, e.target, 'apellido');
        break

        case 'correo':
            validarCampo(expresiones.correo, e.target, 'correo');
        break

        case 'user':
            validarCampo(expresiones.user, e.target, 'user');        
        break
        
        case 'pass':
            validarCampo(expresiones.pass, e.target, 'pass');  
            validarPassword2() 
        break

        case 'verificacionPass':
            validarPassword2()
        break


    }
}

// validacion segunda password
const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('pass')
    const inputPassword2 = document.getElementById('verificacionPass')

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById('grupo__verificacionPass').classList.add('formulario__grupo-incorrecto');
		document.getElementById('grupo__verificacionPass').classList.remove('formulario__grupo-correcto');
        document.querySelector('#grupo__verificacionPass .form-control__error-txt').classList.remove('d-none')
        campos.pass2 = false;
    }else{
        document.getElementById('grupo__verificacionPass').classList.remove('formulario__grupo-incorrecto');
		document.getElementById('grupo__verificacionPass').classList.add('formulario__grupo-correcto');
        document.querySelector('#grupo__verificacionPass .form-control__error-txt').classList.add('d-none')
        campos.pass2 = true;
    }
}

// funcion con acciones de validacion
const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} .form-control__error-txt`).classList.add('d-none')
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} .form-control__error-txt`).classList.remove('d-none')
		campos[campo] = false;
	}
}



// se aplican validaciones al levantar tecla y focus del input
inputs.forEach((input) => {
    input.addEventListener('keyup', validarForm)
    input.addEventListener('blur', validarForm)

})
