//NOTE: Udemy's coding exercise platform does NOT support the `**` operator.  You'll need to multiply a number by itself or use the Math.pow() method.

// 스스로를 곱하는 방법
const square = function (x) {
  return x * x;
};

// Math.pow() method 사용 but x가 음수일 때 제곱 시 결과가 직접 곱하는 것과 다름.
// const square = function (x) {
//   return Math.pow(x, x);
// };

// 거듭제곱 할당 연산자 ** 사용 but x가 음수일 때 제곱 시 결과가 직접 곱하는 것과 다름.
// const square = function (x) {
//   return x**x
// };

// 음의 지수의 정의
// '거듭제곱의 지수가 음수이면, 지수의 부호가 양수인 거듭제곱의 역수와 같습니다.' 는 자바스크립트에서 거듭제곱이나 Math.pow로는 바로 적용이 안되는 것 같다.
// 이 개념을 적용하려면 if 문 이용해서 따로 코드를 짜야할 것 같다.
