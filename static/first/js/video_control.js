//���� �ڵ鷯
var video=document.getElementById("video");
var modal=document.getElementById('myModal');
//���� �ڵ鷯
var pausing_function = function(){
	//�����ð��� �Ǹ� ��������â�� ����
    if(this.currentTime >= end_time) {
        this.pause();
		
        // remove the event listener after you paused the playback
        this.removeEventListener("timeupdate",pausing_function);
		//alert('start surbay');
		modal.style.display = "block";
		
		document.getElementById("id_reason").focus();
    }
};


//video link setting
video.src=video_link;

video.onloadeddata = function() {
//video.oncanplaythrough = function() {
    //alert("Browser has loaded the current frame");
	
	//�ʱ�ȭ
	start_time=0;
	end_time=0;
	//�ε� �Ϸ�Ǹ� ù��° ���� ������ �����´�.
	get_time();
	//��ġ ����
	//video.currentTime=start_time;
	set_time(start_time);
	//�ڵ鷯 ���
	video.addEventListener("timeupdate", pausing_function);
	


};

//shot counter
var num=0;
var start_time=0;
var end_time=0;
//�������� ������� ������ �迭
var SurveyArray = new Array();

function get_time() {
	//�Ҽ��� �� �� ����
	start_time=Math.floor(start_list[num]);
	end_time=Math.floor(end_list[num]);
	
	//alert("start: "+start_time);
	//alert("end: "+end_time);
	set_per();
}

var next_btn = document.getElementsByClassName("close")[0];

	//��ư�� ������ ���� ������ �̵�
	next_btn.onclick = function() {
		
		//������ üũ �� �������̸� ���ÿ� ����
		var flag=Check_data()
	
		if (flag){
			num+=1;
			//���� ���� �����ִ°��
			if(num<start_list.length){
				get_time();//start, end time�� �о�´�
				//video.currentTime=start_time;//�ٽ� ����
				set_time(start_time);
			} else{
				//������ ������ next�� �������
				num-=1;
				modal.style.display = "none";
				video.removeEventListener("timeupdate", pausing_function);
				//alert("!!");
				
				
				

				//location.reload();
				document.getElementById("surveyForm").submit();
				
			}			
			
		} else{
			alert('Please insert comment')
			return;
		}
		//Clear_input();
		modal.style.display = "none";
		video.removeEventListener("timeupdate", pausing_function);
		video.addEventListener("timeupdate", pausing_function);
		video.play();
	}
	
	function Check_data() {
		//������ �ڸ�Ʈ�� �о�´�
		//var grade=document.getElementsByName("preference")[0].value;
		var grade=0;
		var a=0;
		var count=0; 
		for(a=0;a<10;a++){
			var val=document.getElementsByName('star')[a].checked;
			if(val==true){
				//alert(a+":"+val);
				grade=a+1;
				count++;
			}
			
		}
		if(count==0){
			alert('please select star rating')
			return false;
		}

		var comment=document.getElementsByName("reason")[0].value;
		
		//�ڸ�Ʈ�� üũ
		if (comment.length>0) {
			//������ �Է� �� �� push		
			var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
			xmlhttp.open("POST", "/survey");
			xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
			var param="csrfmiddlewaretoken=" + document.getElementsByName("csrfmiddlewaretoken")[0].value;
			param += '&cID=';
			param += cid;
			param += '&shotID=';
			param += shot_id_list[num];
			param += '&fileName=';
			param += filename;
			param += '&preference=';
			param += grade;
			param += '&reason=';
			param += comment;
			param += '&Islast=';
			
			if(num==(shot_id_list.length-1)){
				document.getElementsByName("preference")[0].value=grade;
				document.getElementsByName("shotID")[0].value=shot_id_list[num];
				param += true;
				return true;
			} else{
				param += false;
			}
			
			
			xmlhttp.send(param);
			


			return true;
			
		} else {
			return false;
		}		
	}
	
	function Clear_input() {
		document.getElementsByName("reason")[0].value="";
	}
	
	var surbay_form=document.getElementById("surveyForm");
	surbay_form.onkeydown=function(event){
		//alert( 'key: ' + event.keyCode );
		//����Ű�ǰ�� next ȣ��
		if(event.keyCode==13){
			
			//����Ʈ �̺�Ʈ�� �����ϸ� �̸� ���
			if(event.preventDefault){
				event.preventDefault();
				var nxt_btn=document.getElementById("PushJson");
				nxt_btn.onclick();
			} else{
				//call next
				var nxt_btn=document.getElementById("PushJson");
				nxt_btn.onclick();
				event.returnValue = false;
			}	
		}
	}
	
	function set_per(){
		var val=shot_id_list[num]/totalShot*100;

		document.getElementById("total_persent").innerHTML =' '+ val.toFixed(2)+'%';
	}
	
	function set_time(time){
		/*
		var len=video.buffered.length;
		var i=0;
		while(1){
			
			for(i=0;i<len;i++){
				if(time<video.buffered.end(i)){
					
					video.currentTime=time;	
					return;
				}
				else{
					wait(1000);
				}
			}
			
		}	
		*/
		//video.currentTime=time;	
		//video.pause();

		video.currentTime=time;


		
	}
	
function wait(msecs)
{
	var start = new Date().getTime();
	var cur = start;
	while(cur - start < msecs){
		cur = new Date().getTime();
	}
}

