// 함수식
// function allEvens(numbers) {
//     // 배열의 모든 요소가 짝수인지 확인하여 결과를 반환합니다.
//     return numbers.every(number => number % 2 === 0);
//   }

// 화살표 함수
const allEvens = (num) => num.every((num) => num % 2 === 0);

// 더 간단 하게도 가능!
// const allEvens = num => num.every(num => num % 2 === 0);

// 테스트
console.log(allEvens([2, 4, 6, 8])); // true
console.log(allEvens([1, 4, 6, 8])); // false
console.log(allEvens([1, 2, 3])); // false
