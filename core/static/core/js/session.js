let logoutTimer;


function startLogoutTimer() {
  logoutTimer = setTimeout(function() {
    window.location.href = '/accounts/logout/';  // Reemplaza con la URL de tu vista de cierre de sesión
  }, 1 * 60 * 1000); // 5 minutos en milisegundos
}

function resetLogoutTimer() {
  clearTimeout(logoutTimer);
  startLogoutTimer();
}

// Iniciar el temporizador cuando haya actividad del usuario
document.addEventListener('mousemove', resetLogoutTimer);
document.addEventListener('keydown', resetLogoutTimer);

// Iniciar el temporizador cuando se carga la página
startLogoutTimer();

