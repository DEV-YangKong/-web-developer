// 1. 더하는 방식
// let hen = {
//   name: "Helen",
//   eggCount: 0,
//   layAnEgg() {
//     console.log("EGG");
//     this.eggCount += 1;
//   },
// };

// 2. 증가 하는 방식
// const hen = {
//     name: "Helen",
//     eggCount: 0,
//     layAnEgg() {
//       console.log("EGG");
//       this.eggCount++;
//     },
//   };

// 3. 기능은 같지만, 바로 function 하면 유데미 인터프리터 에러 : 더하는 방식
// const hen = {
//   name: "Helen",
//   eggCount: 0,
//   layAnEgg: function () {
//     this.eggCount += 1;
//     return "EGG";
//   },
// };

// 4. 기능은 같지만, 바로 function 하면 유데미 인터프리터 에러 : 증가하는 방식
const hen = {
  name: "Helen",
  eggCount: 0,
  layAnEgg: function () {
    this.eggCount++;
    return "EGG";
  },
};
