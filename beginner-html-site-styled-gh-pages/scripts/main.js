// const myHeading = document.querySelector('h1')
// myHeading.textContent = 'Hello World jamiu!'

const img = document.querySelector('img')
img.onclick = () => {
  const mySrc = img.getAttribute('src')
  if (mySrc === 'images/firefox-icon.png') {
    img.setAttribute('src', 'images/sun.png')
  } else {
    img.setAttribute('src', 'images/firefox-icon.png')
  }
}
