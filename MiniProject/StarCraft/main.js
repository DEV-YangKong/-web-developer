function click_me() {
  let status = document.getElementById("wraith").style.visibility;

  var audio1 = new Audio("audio1.wav");
  var audio2 = new Audio("audio2.wav");

  if (status == "") {
    document.getElementById("wraith").style.visibility = "hidden";
    audio1.volume = 0.3;
    audio1.play();
    setTimeout(function () {
      audio1.pause();
    }, 2000);
  } else if (status == "hidden") {
    document.getElementById("wraith").style.visibility = "";
    audio2.volume = 0.3;
    audio2.play();
    setTimeout(function () {
      audio2.pause();
    }, 2000);
  }
}
