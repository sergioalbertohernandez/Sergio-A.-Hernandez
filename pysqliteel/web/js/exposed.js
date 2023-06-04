
$(document).ready(function() {
  // Asigna un controlador de eventos al bot�n
  $('button').click(async function() {
    // Muestra una alerta en el navegador
    alert('Clicked!');
    
    // Llama a la función expuesta en Python a traves de Eel
    await eel.mostrar_mensaje('Clicked!')();
  });
});
