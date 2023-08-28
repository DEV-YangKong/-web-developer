// DEFINE YOUR FUNCTION BELOW:
function lastElement(number) {
  if (number.length === 0) {
    return null;
  } else {
    return number[number.length - 1];
  }
}

//  배열 마지막 요소를 부를 떄 array[-1] 이 아니라 array[array.length -1] 로 해야함
