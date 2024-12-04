const express=require("express")
const app=express()
const cors = require('cors');
app.use(express.json());
const mp3=require('./Mp3')

app.use(cors({
    origin: "*"
}));
app.use('/ytverterMp3',mp3)
// app.get('/ytverter',(req,res)=>{
//     res.send("hello")

// })
app.listen(3008,()=>{
    console.log("serveur running")
})