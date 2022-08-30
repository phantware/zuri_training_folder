const express = require("express")
const app = express()

app.get("/",(req,res)=>{
    return res.status(200).json("hello world")
})

app.get("/api/courses",(req,res)=>{
    return res.status(200).json([1,2,3])
})

app.listen(3000,()=>console.log("App running at port 3000"))