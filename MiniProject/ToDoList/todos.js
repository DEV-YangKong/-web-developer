let userInput = prompt("What would you like to do?");
let toDo = [];

while (userInput !== "quit") {
  if (userInput === "quit") {
    breaks;
  } else if (userInput === "new") {
    userInput = prompt("Enter new Todo");
    toDo.push(userInput);
    console.log(`${userInput} added to list`);
    userInput = prompt("What would you like to do?");
  } else if (userInput === "list") {
    console.log("******************************");
    for (let list = 0; list < toDo.length; list++) {
      console.log(`${list} : ${toDo[list]}.`);
    }
    console.log("******************************");
    userInput = prompt("What would you like to do?");
  } else if (userInput === "del") {
    userInput = prompt("Enter index of Todo to delete");
    console.log(`Todo[${userInput}] ${toDo[userInput]} removed`);
    toDo.splice(userInput, 1);
    userInput = prompt("What would you like to do?");
  } else {
    userInput = prompt("You choose wrong command. What would you like to do?");
  }
}

console.log(`OK. YOU QUIT THE APP`);
