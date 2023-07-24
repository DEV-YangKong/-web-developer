let userInput = prompt("What would you like to do?");
const toDo = [];

while (userInput !== "quit" && userInput !== "q") {
  if (userInput === "new") {
    const newToDo = prompt("Enter new Todo");
    toDo.push(newToDo);
    console.log(`${newToDo} added to list`);
  } else if (userInput === "list") {
    console.log("******************************");
    for (let list = 0; list < toDo.length; list++) {
      console.log(`${list} : ${toDo[list]}.`);
    }
    console.log("******************************");
  } else if (userInput === "del") {
    let delIndex = parseInt(prompt("Enter index of Todo to delete"));
    while (Number.isNaN(delIndex)) {
      delIndex = parseInt(
        prompt("You didn't choice number. Enter index of Todo to delete")
      );
    }
    if (!Number.isNaN(delIndex)) {
      console.log(`Todo[${delIndex}] ${toDo[delIndex]} removed`);
      const isdeleted = toDo.splice(delIndex, 1);
    }
  }
  userInput = prompt("What would you like to do?");
}

console.log(`OK. YOU QUIT THE APP`);
