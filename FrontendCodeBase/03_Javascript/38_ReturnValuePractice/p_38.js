// DEFINE YOUR FUNCTION BELOW:
function multiply(num1, num2) {
  if (typeof num1 !== "number" || typeof num2 !== "number") {
    return false;
  }
  let result = num1 * num2;
  return result;
}
