const WIDTH_HANGMAN=300;
const HEIGHT_HANGMAN=400;
const MARGIN_HANGMAN=10;
const ARMS_HANGMAN=100;
const MAX_INTENTOS=6;

function createEmptyCanvas(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	
	
	ctx.clearRect(0, 0, canvas.width, canvas.height);	
	
	ctx.canvas.width = ctx.canvas.width; //Trick to clear canvas correctly
	ctx.fillStyle = "#CCCCCC";
	ctx.fillRect(0,0,canvas.width,canvas.height);
	
	//Base 
	ctx.moveTo(MARGIN_HANGMAN,canvas.height-MARGIN_HANGMAN);
	ctx.lineTo(WIDTH_HANGMAN+MARGIN_HANGMAN,canvas.height-MARGIN_HANGMAN);
	ctx.stroke();
	
	//Tronco
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN/2,canvas.height-MARGIN_HANGMAN);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN/2,canvas.height-MARGIN_HANGMAN-HEIGHT_HANGMAN);
	ctx.stroke();
	
	//Madero superior
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN/2,canvas.height-MARGIN_HANGMAN-HEIGHT_HANGMAN);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-MARGIN_HANGMAN-HEIGHT_HANGMAN);
	ctx.stroke();
	
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-MARGIN_HANGMAN-HEIGHT_HANGMAN);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-MARGIN_HANGMAN-HEIGHT_HANGMAN+30);
	ctx.stroke();
	
	//context.fillStyle = "#FF0000";
	//context.fillRect(0,0,150,75);
}

function drawHead_1(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.beginPath();
	ctx.arc(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-HEIGHT_HANGMAN+60, ARMS_HANGMAN/2-MARGIN_HANGMAN, 0, 2 * Math.PI);
	ctx.stroke();
}

function drawBody_2(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-MARGIN_HANGMAN);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-MARGIN_HANGMAN+HEIGHT_HANGMAN/2);
	ctx.stroke();
}

function drawArm_3(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30-ARMS_HANGMAN,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-10);
	ctx.stroke();
}

function drawArm_4(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30+ARMS_HANGMAN,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-10);
	ctx.stroke();
}

function drawLeg_5(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-MARGIN_HANGMAN+HEIGHT_HANGMAN/2);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30-ARMS_HANGMAN/2,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-MARGIN_HANGMAN+HEIGHT_HANGMAN/2+ARMS_HANGMAN/2);
	ctx.stroke();
}

function drawLeg_6(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.moveTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-MARGIN_HANGMAN+HEIGHT_HANGMAN/2);
	ctx.lineTo(MARGIN_HANGMAN+WIDTH_HANGMAN+30+ARMS_HANGMAN/2,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-MARGIN_HANGMAN+HEIGHT_HANGMAN/2+ARMS_HANGMAN/2);
	ctx.stroke();
}

function drawGuessingText(word){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.font = "30px Arial";
	ctx.strokeText(word,MARGIN_HANGMAN+WIDTH_HANGMAN+30+ARMS_HANGMAN/2,canvas.height-HEIGHT_HANGMAN+60+ARMS_HANGMAN/2-MARGIN_HANGMAN+HEIGHT_HANGMAN/2+ARMS_HANGMAN/2);
}

function drawCurrentLetters(letters){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	ctx.font = "20px Arial";
	ctx.strokeText("Letras: "+letters,MARGIN_HANGMAN+WIDTH_HANGMAN+80,canvas.height-HEIGHT_HANGMAN+60);
}

function showLoseMessage(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	
	var gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
	gradient.addColorStop("0", "magenta");
	gradient.addColorStop("0.5", "red");
	gradient.addColorStop("1.0", "red");
	var currentStrokeStyle=ctx.strokeStyle;
	ctx.strokeStyle = gradient;
	ctx.font = "20px Arial";
	ctx.strokeText("Fin del Juego!!",MARGIN_HANGMAN+WIDTH_HANGMAN+80,canvas.height-HEIGHT_HANGMAN/2);
	ctx.strokeStyle = currentStrokeStyle;
}

function showWinMessage(){
	var canvas = document.getElementById("ahorcado");
	const ctx = canvas.getContext('2d');
	
	var gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
	gradient.addColorStop("0", "magenta");
	gradient.addColorStop("0.5", "green");
	gradient.addColorStop("1.0", "green");
	var currentStrokeStyle=ctx.strokeStyle;
	ctx.strokeStyle = gradient;
	ctx.font = "20px Arial";
	ctx.strokeText("Felicidades Ganaste!!",MARGIN_HANGMAN+WIDTH_HANGMAN+80,canvas.height-HEIGHT_HANGMAN/2);
	ctx.strokeStyle = currentStrokeStyle;
}



function drawHangman(palabra_mostrar,intentos,letras_intento){
		createEmptyCanvas();
		drawCurrentLetters(letras_intento);
		console.log("Intentos:"+intentos)
		if(intentos>0)
			drawHead_1();
		
		if(intentos>1) 
			drawBody_2();
		
		if(intentos>2) 					
			drawArm_3();				
		
		if(intentos>3) 
			drawArm_4();
		
		if(intentos>4) 			
			drawLeg_5();
		
		if(intentos>5) 
			drawLeg_6();
										
		drawGuessingText(palabra_mostrar);
		console.log(">>"+palabra_mostrar+":"+palabra_mostrar.indexOf("_"));
		if(palabra_mostrar.indexOf("_")<0){
			showWinMessage()
			document.removeEventListener('keydown',handleKeyInput);
		}
		
		if(intentos==MAX_INTENTOS){
			showLoseMessage();
			document.removeEventListener('keydown',handleKeyInput);
		}
}