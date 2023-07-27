// 화살표함수로 간결하게
const validUserNames = (usernames) =>
  usernames.filter((username) => username.length < 10);

// 기본 함수 표현식 사용
// function validUserNames(usernames) {
//     // 길이가 10자 미만인 사용자 이름만 필터링하여 새로운 배열로 반환합니다.
//     const filteredUsernames = usernames.filter(
//       (username) => username.length < 10
//     );
//     return filteredUsernames;
//   }
