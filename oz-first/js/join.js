//joinform_check 함수로 유효성 검사
function joinform_check() {
    //변수에 담아주기
    let email = document.getElementById("email");
    let name = document.getElementById("name");
    let pw = document.getElementById("pw");
    let confirm_pw = document.getElementById("confirm_pw");
    let tel = document.getElementById("tel");
    let female = document.getElementById("female");
    let male = document.getElementById("male");

    if (email.value == "") {
        alert("아이디를 입력하세요.");
        email.focus();
        return false;
    }

    if (name.value == "") {
        alert("이름을 입력하세요.");
        name.focus();
        return false;
    }

    if (pw.value == "") {
        alert("비밀번호를 입력하세요.");
        pw.focus();
        return false;
    }

    if (confirm_pw.value !== pw.value) {
        alert("비밀번호가 일치하지 않습니다.");
        confirm_pw.focus();
    }

    if (!female.checked && !male.checked) {
        alert("성별을 선택해주세요.");
        female.focus();
        return false;
    }

    let reg = /^[0-9]+/g;

    if (!reg.test (tel.value)) {
        alert("전화번호는 숫자만 입력할 수 있습니다.");
        tel.focus();
        return false;
    }

    document.join_form.submit();

    function id_check() {
        window.open("", "", "width=600, height=200, left=200, top=100");
    }

}

