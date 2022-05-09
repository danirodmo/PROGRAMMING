var palabra_adivinar='';
var estado_actual='';
var letrasIntento='';
var intentos=0;


function startGame(){
	
	intentos=0;
	palabra_adivinar='';
	estado_actual='';
	letrasIntento='';
	palabra_adivinar=document.getElementById('input-nueva-palabra').value;
	palabra_adivinar=palabra_adivinar.toUpperCase();
	
	console.log('Palabra Adivinar:'+palabra_adivinar);
	estado_actual="_ ".repeat(palabra_adivinar.length);
	console.log("Estado Inicial:"+estado_actual);
	drawHangman(estado_actual,0,"");
	document.addEventListener('keydown', handleKeyInput);

}

function handleKeyInput(event) {
	
	//if("ABCDEFGHIJKLMNOPQRSTUVXYZ".includes(String.fromCharCode(event.keyCode))){
		if(event.keyCode >= 65 && event.keyCode <= 90) {
			console.log(event.keyCode);
			letra=String.fromCharCode(event.keyCode);
			console.log(letra);
			if(letrasIntento.includes(letra)){
				alert("Letra ya ingresada intente con otra");
			}else{
					letrasIntento+=letra;
				if(palabra_adivinar.indexOf(letra)<0){
					intentos++;
				}
			
				var palabra_mostrar="";
				for (let c of palabra_adivinar) {
					console.log("Probando letra"+c);
					if(letrasIntento.includes(c))
					palabra_mostrar+=c;
					else
					palabra_mostrar+="_";
					palabra_mostrar+=" ";
				}
			console.log("Palabra final a mostrar"+palabra_mostrar);
				drawHangman(palabra_mostrar,intentos,letrasIntento);
			}			
		}else{
			console.log('Solo letras');
		}		
}


