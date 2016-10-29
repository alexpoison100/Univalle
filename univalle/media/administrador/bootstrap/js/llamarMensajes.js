// CREADO POR ALEX MUÑOZ

function llamarMensajes	(llamada, mensaje){
    
	/// CARGAR MENSAJES DE  REGISTRO DE CARRERAS

	if(  "Registro".localeCompare(llamada) == 0 ){
	    
		$.notify(mensaje,"success");

	} else if("NoRegistro".localeCompare(llamada) == 0){

	$.notify(mensaje);

	}
}