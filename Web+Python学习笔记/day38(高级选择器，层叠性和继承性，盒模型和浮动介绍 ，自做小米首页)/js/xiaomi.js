var prev1 = document.getElementsByClassName('prev1')[0];
var next2 = document.getElementsByClassName('next2')[0];
var next4 = document.getElementsByClassName('next4')[0];
var prev3 = document.getElementsByClassName('prev3')[0];

// function $(Class){
	
// 	return document.getElementsByClassName(Class);
// }

prev3.onmouseout = function(){
	prev3.style.visibility = 'visible';
	prev1.style.visibility = 'hidden';
}
prev3.onmouseover = function(){
	prev3.style.visibility = 'hidden';
	prev1.style.visibility = 'visible';
}
next4.onmouseover = function(){
	next4.style.visibility = 'hidden';
	next2.style.visibility = 'visible';
}
next4.onmouseout = function(){
	next4.style.visibility = 'visible';
	next2.style.visibility = 'hidden';
}