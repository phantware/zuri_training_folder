const express = require('express')
const dotenv = require('dotenv')
const mongoose = require('mongoose')

const app = express()
dotenv.config()
const PORT = process.env.PORT || 8800
const connect = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URL)
    console.log('Connected to mongoDB.')
  } catch (error) {
    throw error
  }
}

mongoose.connection.on('disconnected', () => {
  console.log('mongoDB disconnected!')
})

const Author = mongoose.model(
  'Author',
  mongoose.Schema({
    name: String,
    bio: String,
    website: String,
  })
)

const Course = mongoose.model(
  'Course',
  mongoose.Schema({
    name: String,
    author: { type: mongoose.Schema.Types.ObjectId, ref: 'Author' },
  })
)

async function createAuthor(name, bio, website) {
  const author = Author({
    name,
    bio,
    website,
  })

  const result = await author.save()
  console.log(result)
}

async function createCourse(name, author) {
  const course = Course({
    name,
    author,
  })

  const result = await course.save()
  console.log(result)
}

async function listCourses() {
  const courses = await Course.find().populate('author').select('name author')
  console.log(courses)
}

// createAuthor('Mosh', 'My bio', 'My Website')

// createCourse('Node Course', '631c5906bb50266869c1aaa0')

listCourses()

app.listen(PORT, () => {
  connect()
  console.log(`Server is runing at port ${PORT}.`)
})
