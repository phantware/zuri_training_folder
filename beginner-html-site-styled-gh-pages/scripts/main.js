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

let myButton = document.querySelector('button')
let myHeading = document.querySelector('h1')

function setUserName() {
  const myName = prompt('Please enter your name')
  localStorage.setItem('name', myName)
  myHeading.textContent = `Mozillar is cool, ${myName}`
}

if (!localStorage.getItem('name')) {
  setUserName()
} else {
  const storeName = localStorage.getItem('name')
  myHeading.textContent = `Mozilla is cool, ${storeName}`
}

myButton.onclick = () => {
  setUserName()
}
