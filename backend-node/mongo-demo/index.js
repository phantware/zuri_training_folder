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

const courseSchema = mongoose.Schema({
  name: String,
  author: String,
  tags: [String],
  date: { type: Date, default: Date.now },
  isPublished: Boolean,
})

const Course = mongoose.model('Course', courseSchema)
async function createCourse() {
  const course = new Course({
    name: 'Angular Course',
    author: 'Jamiu',
    tags: ['angular', 'frontend'],
    isPublished: true,
  })
  const result = await course.save()
  console.log(result)
}

createCourse()

app.listen(PORT, () => {
  connect()
  console.log(`Server is runing at port ${PORT}.`)
})
