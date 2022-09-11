// const myHeading = document.querySelector('h1')
// myHeading.textContent = 'Hello World jamiu!'

// const img = document.querySelector('img')

// img.onclick = () => {
//   const mySrc = img.getAttribute('src')
//   if (mySrc === 'images/firefox-icon.png') {
//     img.setAttribute('src', 'images/sun.png')
//   } else {
//     img.setAttribute('src', 'images/firefox-icon.png')
//   }
// }

// let myButton = document.querySelector('button')
// let myHeading = document.querySelector('h1')

// function setUserName() {
//   const myName = prompt('Please enter your name')
//   if (!myName) {
//     setUserName()
//   } else {
//     localStorage.setItem('name', myName)
//     myHeading.textContent = `Mozillar is cool, ${myName}`
//   }
// }

// if (!localStorage.getItem('name')) {
//   setUserName()
// } else {
//   const storeName = localStorage.getItem('name')
//   myHeading.textContent = `Mozilla is cool, ${storeName}`
// }

// myButton.onclick = () => {
//   setUserName()
// }

// const buttonlevel = document.querySelector('button')
// const headingLevel = document.querySelector('h2')

// buttonlevel.onclick = () => {
//   const name = prompt('Enter your name')
//   alert(`Hello ${name}, nice to see you`)
//   headingLevel.textContent = `Welcome ${name}`
// }

const textBox = document.querySelector('#textBox')
const output = document.querySelector('#output')

function logKey(event) {
  console.log(`You pressed "${event.key}".`)
}

textBox.addEventListener('keydown', function (event) {
  console.log(`You pressed "${event.key}".`)
})
