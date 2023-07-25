// DEFINE YOUR FUNCTION BELOW:

// 기존 사용방법
function sumArray(arr) {
  if (arr.length < 1) {
    return false;
  } else {
    let total = 0;
    for (let i = 0; i < arr.length; i++) {
      total += arr[i];
    }
    return total;
  }
}

// for of 사용 방법
function sumArray(arr) {
  if (arr.length < 1) {
    return false;
  } else {
    let total = 0;
    for (let i of arr) {
      total += i;
    }
    return total;
  }
}
