$(function(){
	var isShow = false;

	$('.Skin-botton').click(function(event){

		// if(isShow){
		// 	$('#Skin-peeler').stop().slideUp(500);
		// 	isShow = true;
		// }
		// else{
		$('#Skin-peeler').slideDown(500);
			// isShow = true;
		// }
		return false;
		
	})

	$('body,.bottondown').click(function(event){
		$('#Skin-peeler').slideUp(500);

	})
	

	
	$('#Skin-peeler').click(function(event){
		
		return 	false;
	})
	
	


	
	
	// $('.Skin-center-top ul li').click(function(){
	// 	$(this).css('background','#389CFF').siblings('li').css('background',' white').find('span').css('color','#666666');
	// 	$(this).find('span').css('color','white');
	// })
	
	// $('.Skin-center-top ul li').mousemove(function(){
	// 	$(this).css('background','#389CFF').siblings('li').css('background',' white').find('span').css('color','#666666');
	// 	$(this).find('span').css('color','white');
	// })
	+
	$('.Skin-center-top ul li').click(function(){
		$(this).addClass('Skin-center-import').siblings('li').removeClass('Skin-center-import').find('span').removeClass('Skin-center-Spancolor');
		$(this).find('span').addClass('Skin-center-Spancolor')
	})
	
	$('.Skin-center-top ul li').mousemove(function(){
		$(this).addClass('Skin-center-licolor').siblings('li').removeClass('Skin-center-licolor').find('span').removeClass('Skin-center-Licolor');
		$(this).find('span').addClass('Skin-center-Licolor');
	})
	
	$(document).ready(function(){//在文档加载完毕后执行
	
		$(window).scroll(function(){//开始监听滚动条
	                //获取当前滚动条高度
			var topp = $(document).scrollTop();
			var rettop = $(document).scrollTop();
	                
	        //判断如果滚动条大于220则触发效果        
			if(topp > 210){  
				$('.scroll-search').css('display','block');
			}
			else{
				$('.scroll-search').css('display','none');
			}
			
			if(rettop >35){
				$('.returntop').show();
			}
			else{
				$('.returntop').hide();
			}
		})
	})
	
	var isTop = true;
	$('.returntop').click(function(){
		console.log(111111);
		if ($('html').scrollTop()) {
			$('html').animate({ scrollTop: 0 }, 300);//动画效果
			isTop = false;
		}
	})
	
	var Scli = document.getElementsByClassName('Skin-center-li');
	var sM = document.getElementsByClassName('sMain');
	for(let i = 0;i< Scli.length; i++){
		Scli[i].onclick = function(){
			for(let j = 0;j< sM.length; j++){
				sM[j].style.display = 'none';
			}
			sM[i].style.display = 'inline-block';
		}
	}
	
	var count = 0;
	var Don = document.getElementsByClassName('Dot');
	var insMain = document.getElementsByClassName('in-sMain');
	for(let n = 0; n<Don.length; n++){
		
		Don[n].onclick = function(){
			for(let m = 0; m<insMain.length; m++){
				Don[m].style.color = '#708090';
				insMain[m].style.display = 'none';
			}
			Don[n].style.color = 'red';
			insMain[n].style.display = 'block';

		}
	}
	
	
	var lBut = document.getElementById('lButton');
	var rBut = document.getElementById('rButton');
	
	lBut.onclick = function(){
		count -= 1;
		if(count<0){
			count = 4;
		}
		for(let z = 0; z<Don.length; z++){
			Don[z].style.color = '#708090';
			insMain[z].style.display = 'none';
		}
		Don[count].style.color = 'red';
		insMain[count].style.display = 'block';
	}
	
	rBut.onclick = function(){
		count += 1;
		if(count>4){
			count = 0;
		}
		for(let x = 0; x<Don.length; x++){
			Don[x].style.color = '#708090';
			insMain[x].style.display = 'none';
		}
		Don[count].style.color = 'red';
		insMain[count].style.display = 'block';
	}

		
	
	
})
	
	
