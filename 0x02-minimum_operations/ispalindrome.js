const string = "memem";

function ispalindrome(string) {
  let revers = string.replace(" ", "").split("").reverse().join("");
  console.log(string.replace(" ", "").localeCompare(revers));
}

ispalindrome(string);
