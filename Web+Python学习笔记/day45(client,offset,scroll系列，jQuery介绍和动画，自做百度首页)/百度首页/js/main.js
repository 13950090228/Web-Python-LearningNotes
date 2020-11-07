$(function(){

	var Tcamera = document.getElementsByClassName('Tcamera')[0];
	var Bcamera = document.getElementsByClassName('Bcamera')[0];
	Tcamera.onmouseover = function(){
		Tcamera.style.display = 'none';
		Bcamera.style.display = 'inline-block';
	}
	Tcamera.onmouseout = function(){
		Tcamera.style.display = 'inline-block';
		Bcamera.style.display = 'none';
	}

	var cardspan = document.getElementsByClassName('card-top-span');
	var content = document.getElementsByClassName('center-content');
	for(let i=0; i<cardspan.length; i++){
		
		cardspan[i].onmouseover = function(){
			for(let j=0; j<cardspan.length ;j++){
				cardspan[j].style.fontWeight = '400';
				cardspan[j].style.backgroundColor = 'white';
				cardspan[j].style.color = 'black';
				content[j].className += ' displaynone';
			}
			
			cardspan[i].style.backgroundColor = '#9A9DA2';
			cardspan[i].style.fontWeight = '700';
			cardspan[i].style.color = 'white';
			content[i].className = 'center-content';
		}
	}

});
