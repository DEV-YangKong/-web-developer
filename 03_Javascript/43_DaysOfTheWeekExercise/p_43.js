// DEFINE YOUR FUNCTION BELOW:

// 첫 번째 방법:
function returnDay(num) {
  if (num <= 7 && num >= 1) {
    if (num === 1) {
      return `Monday`;
    } else if (num === 2) {
      return `Tuesday`;
    } else if (num === 3) {
      return `Wednesday`;
    } else if (num === 4) {
      return `Thursday`;
    } else if (num === 5) {
      return `Friday`;
    } else if (num === 6) {
      return `Saturday`;
    } else if (num === 7) {
      return `Sunday`;
    }
  } else {
    return null;
  }
}

// 두 번째 방법 :
let week = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday",
];
function returnDay(num) {
  if (num <= 7 && num >= 1) {
    return (day = week[num - 1]);
  } else {
    return null;
  }
}
