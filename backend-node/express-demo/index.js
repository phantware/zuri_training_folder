const config = require('config')
const Joi = require('joi')
const log = require('./logger')
const express = require('express')
const morgan = require('morgan')
const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

//Configuration
console.log('Applicatio Name: ' + config.get('name'))
console.log('Mail Server: ' + config.get('mail.host'))
console.log('Mail Password: ' + config.get('mail.password'))

//if the env is set to development, enable morgan
if (app.get('env') === 'development') {
  app.use(morgan('tiny'))
  console.log('Morgan enabled')
}

//checking the environment variable if it's set to development or undefined
console.log(`NODE_PROCESS.ENV: ${process.env.NODE_ENV}`)
console.log(`app: ${app.get('env')}`)

app.use(log)

app.use(function (req, res, next) {
  console.log('Authenticating....')
  next()
})

const courses = [
  { id: 1, name: 'course 1' },
  { id: 2, name: 'course 2' },
  { id: 3, name: 'course 3' },
]

app.get('/', (req, res) => {
  return res.status(200).json('hello world')
})

app.get('/api/courses', (req, res) => {
  return res.status(200).json(courses)
})

app.get('/api/courses/:id', (req, res) => {
  const course = courses.find((c) => c.id === parseInt(req.params.id))
  if (!course) {
    return res.status(404).json('The course with the given ID was not found')
  }
  return res.status(200).json(course)
})

// app.get("/api/posts/:year/:month",(req,res)=>{
//     return res.status(200).json(req.params)
// })

app.get('/api/posts/:year/:month', (req, res) => {
  return res.status(200).json(req.query)
})

app.post('/api/courses', (req, res) => {
  const { error } = validateCourse(req.body)

  if (error) {
    return res.status(404).json(error.details[0].message)
  }

  const course = {
    id: courses.length + 1,
    name: req.body.name,
  }
  courses.push(course)

  return res.status(201).json(course)
})

app.put('/api/courses/:id', (req, res) => {
  //Lookup the course
  //If not existing, return 404
  const course = courses.find((c) => c.id === parseInt(req.params.id))
  if (!course) {
    return res.status(404).json('Course not found')
  }

  //Validate
  // If invalid, return 404 - Bad request

  const { error } = validateCourse(req.body)

  if (error) {
    return res.status(404).json(error.details[0].message)
  }
  course.name = req.body.name
  return res.status(200).json(course)
})

app.delete('/api/courses/:id', (req, res) => {
  // Lookup the course
  // Not existing, return 404
  const course = courses.find((c) => c.id === parseInt(req.params.id))
  if (!course) {
    return res.status(404).json('The course with the given ID was not found')
  }

  // Delete course
  const index = courses.indexOf(course)
  courses.splice(index, 1)

  // Return same course
  return res.status(200).json(course)
})
const validateCourse = (course) => {
  const schema = Joi.object({
    name: Joi.string().min(3).required(),
  })
  return schema.validate(course)
}
const port = process.env.PORT || 3000

app.listen(port, () => console.log(`App running at port ${port}`))
