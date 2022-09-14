let numbers = [1, 2, 3, 4, 5, 6]
//function that add last two values of  the numbers array

function sum_reducer(accumulator, currentValue) {
  return accumulator + currentValue
}

// returns a single value after reducing the numbers array
let sum = numbers.reduceRight(sum_reducer, 0)

console.log(sum)
