const numbers = [0, 1, 2, 3, 4, 5, 6]
// const result = numbers.map((item) => item * 2)
// const result = numbers.filter((item) => item % 2 === 0)
const result = numbers.reduce((prev, next) => prev + next, 0)
console.log('result', result)
