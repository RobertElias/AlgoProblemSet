console.log("Before Function")
setTimeout(function(){
  console.log("Inside Function")
},3000)
console.log("After Function")


var marks = 40
var grade = (marks < 30) ? 'Fail' : 'Pass'
console.log(grade)

console.log(3+2+"7")


var i;
for (i = 0; i < 5; i++) {
  if (i === 3) {
    continue;
  }
  console.log("Number is: " + i)
}