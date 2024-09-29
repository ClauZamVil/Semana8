document.addEventListener('DOMContentLoaded', function() {

    // Función de validación para el formulario de registro
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Evita el envío del formulario

            const fullName = document.getElementById('fullName').value;
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const dob = document.getElementById('dob').value;

            // Validaciones básicas
            if (password !== confirmPassword) {
                alert('Las contraseñas no coinciden.');
                return;
            }

            // Validar edad mínima (13 años)
            const birthDate = new Date(dob);
            const today = new Date();
            let age = today.getFullYear() - birthDate.getFullYear();
            const m = today.getMonth() - birthDate.getMonth();
            if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
                age--;
            }
            if (age < 13) {
                alert('Debes tener al menos 13 años para registrarte.');
                return;
            }

            // Validación de formato de correo electrónico
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Ingresa un correo electrónico válido.');
                return;
            }

            // Validación de fuerza de la contraseña
            if (!/(?=.*[0-9])(?=.*[A-Z]).{6,18}/.test(password)) {
                alert('La contraseña debe tener entre 6 y 18 caracteres, incluir al menos un número y una letra mayúscula.');
                return;
            }

            // Si todas las validaciones pasan
            alert('Registro completado con éxito!');
            registerForm.reset(); // Limpia el formulario
        });
    }

    // Función de validación para el formulario de inicio de sesión
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Evita el envío del formulario

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Validaciones básicas (puedes agregar más si es necesario)
            if (username === '' || password === '') {
                alert('Por favor, ingresa tu nombre de usuario y contraseña.');
                return;
            }

            // Si la validación pasa
            alert('Inicio de sesión exitoso!');
            loginForm.reset(); // Limpia el formulario
        });
    }

    // Función de validación para el formulario de recuperación de contraseña
    const recuperarForm = document.getElementById('recuperarForm');
    if (recuperarForm) {
        recuperarForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Evita el envío del formulario

            const email = document.getElementById('email').value;

            // Validación de formato de correo electrónico
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Ingresa un correo electrónico válido.');
                return;
            }

            // Si la validación pasa
            alert('Se ha enviado un enlace de recuperación a tu correo.');
            recuperarForm.reset(); // Limpia el formulario
        });
    }

});




