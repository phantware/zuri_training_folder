const arr = ['a', 'b', 'a', 'a', 'b', 'c', 'c']

const count = {}

for (const element of arr) {
  if (count[element]) {
    count[element] += 1
  } else {
    count[element] = 1
  }
}

console.log(count)
