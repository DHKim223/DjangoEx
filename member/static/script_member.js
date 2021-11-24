function check(){
	if(! $("input[name=id]").val()){
		alert("아이디를 입력하세요");
		$("input[name=id]").focus();
		return false
	} else if (! $("input[name=passwd]").val() ){
		alert("비밀번호를 입력하세요");
		$("input[name=passwd]").focus();
		return false
	} else if ( $("input[name=passwd]").val() != $("input[name=passwd1]").val() ){
		alert("비밀번호를 다릅니다.");
		$("input[name=passwd]").focus();
		return false
	} else if (! $("input[name=name]").val() ){
		alert("이름를 입력하세요");
		$("input[name=name]").focus();
		return false
	} else if (! $("input[name=student_id]").val() ){
		alert("학번을 입력하세요");
		$("input[name=student_id]").focus();
		return false
	} 
}

// 아이디 중복 확인
function confirm() {
	if( ! $("input[name=id]").val() ) {
		alert( "아이디를 입력하세요" );
		$("input[name=id]").focus();
		return 		
	} else {
		url = "confirm" + "?id=" + $("input[name=id]").val();
		open( url, "confirm", 
		"toolbar=no, menubar=no, scrollbar=no, status=no, width=400, height=200" );
	}
}

function setid(id){
	opener.document.registerform.id.value = id
	self.close()
}

// 로그인
function logincheck(){
	if(!$("input[name=id]").val() ) {
		alert("아이디를 입력하세요");
		$("input[name=id]").focus();
		return false;
	} else if(!$("input[name=passwd]").val() ){
		alert("비밀번호를 입력하세요");
		$("input[name=passwd]").focus();
		return false;
	}
}
 
//학번 중복확인 Ajax
$(document).ready(
	function () {
		$("#sid_result").html("&nbsp;학번을 입력하세요" );
	}
);

function sidcheck(){
	$.ajax({
			url : "sidcheck",
			type : "POST",
			data : {
				"keyword" : $("input[name=student_id]").val()
			},
			dataType : "text",
			success : function (data) {
				$("#sid_result").html(data);
			},
			error : function () {}
		}
	);
}





