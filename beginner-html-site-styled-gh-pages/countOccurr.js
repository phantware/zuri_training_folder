// const arr = ['a', 'b', 'a', 'a', 'b', 'c', 'c']

// const count = {}

// for (const element of arr) {
//   if (count[element]) {
//     count[element] += 1
//   } else {
//     count[element] = 1
//   }
// }

// console.log(count)

// const arr = ['a', 'b', 'a', 'a', 'c', 'c']

// const count = {}

// for (let index = 0; index < arr.length; index++) {
//   const element = arr[index]

//   if (count[element]) {
//     count[element] += 1
//   } else {
//     count[element] = 1
//   }
// }

// console.log(count) // 👉️ {a: 3, b: 1, c: 2}

const iterable = new Map([
  ['a', 1],
  ['b', 2],
  ['c', 3],
])

for (const entry of iterable) {
  console.log('entry', entry)
}
console.log('iterable', iterable)

for (const [key, value] of iterable) {
  console.log('value', value)
}
