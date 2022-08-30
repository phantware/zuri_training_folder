const express = require('express')
const app = express()

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

const port = process.env.PORT || 3000

app.listen(port, () => console.log(`App running at port ${port}`))
