function click_me() {
  let status = document.getElementById("wraith").style.visibility;

  if (status == "") {
    document.getElementById("wraith").style.visibility = "hidden";
  } else if (status == "hidden") {
    document.getElementById("wraith").style.visibility = "";
  }
}
