// const months = ['March', 'Jan', 'Feb', 'Dec']

// // This function returns the length of the array for instance jan is less than feb, dec and feb are thesame length, it returns one of it an march comes last which is greater tha all
// function len_compare(a, b) {
//   return a.length - b.length
// }
// months.sort(len_compare)
// console.log('months', months)

/**
 * numeric sorting
 * define array
 */

const priceList = [1000, 50, 2, 7, 14]

// sort() using function expression
// ascending order
// priceList.sort(function (a, b) {
//   return a - b
// })
// // Output: Ascending - 2,7,14,50,1000
// console.log('Ascending - ' + priceList)

// sort() using arrow function expression
// descending order
priceList.sort((a, b) => b - a)

// Output: Descending - 1000,50,14,7,2
console.log('Descending - ' + priceList)
