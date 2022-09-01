const startupDebugger = require('debug')('app:startup')
const dbDebugger = require('debug')('app:db')
const config = require('config')
const Joi = require('joi')
const log = require('./middleware/logger')
const express = require('express')
const morgan = require('morgan')
const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.set('view engine', 'pug')
app.set('views', './views')
const courses = require('./routes/courses')
const home = require('./routes/home')

//Configuration
console.log('Applicatio Name: ' + config.get('name'))
console.log('Mail Server: ' + config.get('mail.host'))
console.log('Mail Password: ' + config.get('mail.password'))

//if the env is set to development, enable morgan
if (app.get('env') === 'development') {
  app.use(morgan('tiny'))
  startupDebugger('Morgan enabled')
}
dbDebugger('Conected to database')

//checking the environment variable if it's set to development or undefined
console.log(`NODE_PROCESS.ENV: ${process.env.NODE_ENV}`)
console.log(`app: ${app.get('env')}`)

app.use(log)

app.use(function (req, res, next) {
  console.log('Authenticating....')
  next()
})

app.use('/api/courses', courses)
app.use('/', home)

const port = process.env.PORT || 3000

app.listen(port, () => console.log(`App running at port ${port}`))
