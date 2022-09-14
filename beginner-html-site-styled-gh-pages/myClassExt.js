class Animal {
  constructor(name) {
    this.name = name
  }
  speak() {
    console.log(`${this.name} makes a noise`)
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name)
  }
  speak() {
    console.log(`${this.name} bark.`)
  }
}

const lala = new Dog('Mama')
lala.speak()
// console.log(lala.speak('Dog'))
