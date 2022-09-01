const express = require('express')
const router = express.Router()

const courses = [
  { id: 1, name: 'course 1' },
  { id: 2, name: 'course 2' },
  { id: 3, name: 'course 3' },
]

router.get('/', (req, res) => {
  return res.status(200).json(courses)
})

router.get('/:id', (req, res) => {
  const course = courses.find((c) => c.id === parseInt(req.params.id))
  if (!course) {
    return res.status(404).json('The course with the given ID was not found')
  }
  return res.status(200).json(course)
})

// app.get("/api/posts/:year/:month",(req,res)=>{
//     return res.status(200).json(req.params)
// })

router.get('/api/posts/:year/:month', (req, res) => {
  return res.status(200).json(req.query)
})

router.post('', (req, res) => {
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

router.put('/:id', (req, res) => {
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

router.delete('/:id', (req, res) => {
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

module.exports = router
