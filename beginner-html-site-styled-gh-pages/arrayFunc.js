// const numbers = [0, 1, 2, 3, 4, 5, 6]
// const result = numbers.map((item) => item * 2)
// const result = numbers.filter((item) => item % 2 === 0)
// const result = numbers.reduce((prev, next) => prev + next, 0)
// const result = numbers.find((item) => item > 5)
// console.log('result', result)

// class Person {
//   constructor(name, age) {
//     this.name = name
//     this.age = age
//   }

//   stringSentence() {
//     return `Hello, my name is ${this.name} and I am ${this.age}`
//   }
// }

// const myPerson = new Person('Manu', 23)
// console.log(myPerson.age) // 23
// console.log(myPerson.stringSentence()) // "Hello, my name is Manu and I'm 23

const months = ['March', 'Jan', 'Feb', 'Dec']

// This function returns the length of the array for instance jan is less than feb, dec and feb are thesame length, it returns one of it an march comes last which is greater tha all
function len_compare(a, b) {
  return a.length - b.length
}
months.sort(len_compare)
console.log('months', months)
