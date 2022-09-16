//Начальные установки
let show = 0;

$(".slidesButs:eq(0)").addClass('activeSlideButtton');

$(function(){
	$.datepicker.setDefaults({
		closeText: 'Закрыть', prevText: 'Предыдущая', currentText: 'Сегодня', monthNames:['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
		monthNamesShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'], dayNames: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'],
		dayNamesShort: ['Вск', 'Пон', 'Втр', 'Срд', 'Чтв', 'Птн', 'Сбт'], dayNamesMin: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'], weekHeader: 'Не', dateFormat: 'dd.mm.yy', firstDay: 1,
		isRTL: false, showMonthAfterYear: false, yearSuffix: '', nextText: 'Следующая'
	});
});

document.getElementById("rightArrow").addEventListener("mouseenter", function(){
	$("#rightArrow").attr("src", "http://127.0.0.1:8000/static/js/pics/arrow_right_hover.png");
});
document.getElementById("leftArrow").addEventListener("mouseenter", function(){
	$("#leftArrow").attr("src", "http://127.0.0.1:8000/static/js/pics/arrow_left_hover.png");
});
document.getElementById("rightArrow").addEventListener("mouseleave", function(){
	$("#rightArrow").attr("src", "http://127.0.0.1:8000/static/js/pics/arrow_right.png");
});
document.getElementById("leftArrow").addEventListener("mouseleave", function(){
	$("#leftArrow").attr("src", "http://127.0.0.1:8000/static/js/pics/arrow_left.png");
});


// кнопка вверх:
let upper = document.getElementById("upBut");

window.addEventListener('scroll', function(){
	let pageY = window.pageYOffset;
	if(pageY >= document.body.clientHeight / 3){
      	upper.style.opacity = 1;
		upper.style.cursor = "pointer";
		$("button#upBut").removeAttr("disabled");
		$("button#upBut").attr("enabled", "enabled");
      }else{
            upper.style.opacity = 0;
			upper.style.cursor = "default";
			$("button#upBut").removeAttr("enabled");
			$("button#upBut").attr("disabled", "disabled");
      }
      upper.addEventListener('click', function(){
      	function goTo(){
      		pageY -= 50;
      		window.scrollTo(0, pageY);
      		if (pageY <= 0){
      			clearInterval(topInterval);
      		}
      	}
            let topInterval = setInterval(goTo, 15);
      });
});

// слайдер:

// правая стрелка
rightArrow.addEventListener("click", function(){ 
	if(show >= 0 && show <= 4){
		show += 1;
		if(show == 1){
			viewport.classList.add('show2');
			viewport.classList.remove('show1', 'show3', 'show4', 'show5');

			$(".slidesButs:eq(1)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}else if(show == 2){
			viewport.classList.add('show3');
			viewport.classList.remove('show1', 'show2', 'show4', 'show5');

			$(".slidesButs:eq(2)").addClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}else if(show == 3){
			viewport.classList.add('show4');
			viewport.classList.remove('show1', 'show2', 'show3', 'show5');

			$(".slidesButs:eq(3)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}else if(show == 4){
			viewport.classList.add('show5');
			viewport.classList.remove('show1', 'show2', 'show3', 'show4');

			$(".slidesButs:eq(4)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
		}else{
			show = 0;
			viewport.classList.add('show1');
			viewport.classList.remove('show2', 'show3', 'show4', 'show5');

			$(".slidesButs:eq(0)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}
	}
});

// левая стрелка
leftArrow.addEventListener("click", function(){
	if(show >= 0 && show <= 4){
		show -= 1;
		if(show == 0){
			viewport.classList.add('show1');
			viewport.classList.remove('show2', 'show3', 'show4', 'show5');

			$(".slidesButs:eq(0)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}else if(show == 1){
			viewport.classList.add('show2');
			viewport.classList.remove('show1', 'show3', 'show4', 'show5');

			$(".slidesButs:eq(1)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}else if(show == 2){
			viewport.classList.add('show3');
			viewport.classList.remove('show1', 'show2', 'show4', 'show5');

			$(".slidesButs:eq(2)").addClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}else if(show == 3){
			viewport.classList.add('show4');
			viewport.classList.remove('show1', 'show2', 'show3', 'show5');

			$(".slidesButs:eq(3)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
		}else if(show == 4){
			viewport.classList.add('show5');
			viewport.classList.remove('show1', 'show2', 'show3', 'show4');

			$(".slidesButs:eq(4)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
		}
		else{
			show = 4;
			viewport.classList.add('show5');
			viewport.classList.remove('show1', 'show2', 'show3', 'show4');

			$(".slidesButs:eq(4)").addClass('activeSlideButtton');
			$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
			$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
		}
	}
});

// кнопки слайдера
$(".slidesButs:eq(0)").click(function(){
	show = 0
	viewport.classList.add('show1');
	viewport.classList.remove('show2', 'show3', 'show4', 'show5');

	$(".slidesButs:eq(0)").addClass('activeSlideButtton');
	$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
});
$(".slidesButs:eq(1)").click(function(){
	show = 1
	viewport.classList.add('show2');
	viewport.classList.remove('show1', 'show3', 'show4', 'show5');

	$(".slidesButs:eq(1)").addClass('activeSlideButtton');
	$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
});
$(".slidesButs:eq(2)").click(function(){
	show = 2
	viewport.classList.add('show3');
	viewport.classList.remove('show1', 'show2', 'show4', 'show5');

	$(".slidesButs:eq(2)").addClass('activeSlideButtton');
	$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
});
$(".slidesButs:eq(3)").click(function(){
	show = 3
	viewport.classList.add('show4');
	viewport.classList.remove('show1', 'show2', 'show3', 'show5');

	$(".slidesButs:eq(3)").addClass('activeSlideButtton');
	$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(4)").removeClass('activeSlideButtton');
});
$(".slidesButs:eq(4)").click(function(){
	show = 4
	viewport.classList.add('show5');
	viewport.classList.remove('show1', 'show2', 'show3', 'show4');

	$(".slidesButs:eq(4)").addClass('activeSlideButtton');
	$(".slidesButs:eq(2)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(0)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(3)").removeClass('activeSlideButtton');
	$(".slidesButs:eq(1)").removeClass('activeSlideButtton');
});

//Календарь
let date = document.getElementById("inpDate");
let count = 0;
let sum = 3;
let arr = [0, 0, ".", 0, 0, ".", 0, 0 ,0 ,0]; 


$("#pickDate").click(function(){
	$("#choseDate").toggleClass("showInputDate");
});
$("#choseDate input").mouseenter(function(){
	$("#choseDate input").datepicker({
		
	});
});

date.addEventListener("keyup", function(event){
	if((['0','1', '2', '3', '4', '5', '6', '7', '8', '9','Backspace'].includes(event.key))){
		console.log(count);
		if(count==1 || count==3){
			count+=1;
			date.value += ".";
		}else if('Backspace'.includes(event.key)){
			count = 0;
			date.value = "";
		}else{
			count+=1;	
		}
	}else{
		event.preventDefault();
	}
});

let butreg = document.getElementById('registration')
let butlog = document.getElementById('sign_in')
let or = document.getElementById('or')
let pngacc = document.getElementById('boba')
let width = document.getElementById('width')

function getCookie(name) {
	let matches = document.cookie.match(new RegExp(
	  "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
	));
	return matches ? decodeURIComponent(matches[1]) : undefined;
  }
  

var id =  getCookie('id')
if(id != undefined){
	document.getElementById('wow').innerHTML = 'id:'+id;
	butreg.hidden = true;
	butlog.hidden = true;
	or.hidden = true;
	width.hidden = false;
	pngacc.hidden = false;
}


