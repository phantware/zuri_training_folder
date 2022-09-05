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

// createCourse()

async function getCourse() {
  const courses = await Course.find({ author: 'Jamiu', isPublished: true })
    // .find({ author: /.*Mosh.*/i })
    .limit(1)
    .sort({ name: 1 })
    .select({ name: 1, tags: 1 })

  console.log(courses)
}

getCourse()

/**
 * Comparison Query Operators
 * eq = equal
 * ne = not equal
 * gt = greather than       course.find({price: {$gt: 10}})
 * gte = greather than or equal to      course.find({price: {$gte: 10}})
 * lt = less than    course.find({price: {$lt: 10}})
 * lte = less than or equal to   course.find({price: {$lte: 10}})
 * in    course.find({price: {$in: [10, 15, 20]}})
 * nin = not in
 *
 * Logical Operator
 * or     or([{author: "Jamiu"},{isPublished:true}])
 * and    and([{author: "Jamiu"},{isPublished:true}])
 *
 * Regular Expression
 * Getting course that author starts with Mosh use the below regular expression
 *
 * /pattern/   =  /^Mosh/  course.find({author: /^Mosh/})
 *
 * Getting course that author ends with Hamedani use the below regular expression
 *
 * /pattern/  = /^Hamedani$/ ($ sign indicate end of a string) course.find({author: /Hamedani$/}) to make the expression case insensitive use (i) at the end course.find({author: /Hamedani$/i})
 *
 * or the word contais Mosh use the below query
 * couse.find({author: /.*Mosh./}) make sure it ends with * before /
 *
 */
app.listen(PORT, () => {
  connect()
  console.log(`Server is runing at port ${PORT}.`)
})
