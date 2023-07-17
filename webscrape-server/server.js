const express = require('express')
const sqlite = require('sqlite3').verbose()
const app = express()
const cors = require('cors')

app.use(cors())

app.get('/search', (req, res) =>{
    //Accessing database
    let db = new sqlite.Database('../webscrape/database/data.db', sqlite.OPEN_READONLY, (err) => {
        if (err){
            console.log(err.message)
        }
    })

    //Query from the database
    const query = `SELECT * FROM Result WHERE NAME LIKE '%${req.query.search}%'`
    //const query2 = `SELECT COUNT(*) AS count FROM Result`
    const query2 = `SELECT COUNT(*) AS count FROM Result WHERE NAME LIKE '%${req.query.search}%'`

    db.all(query, (err1, rows1) =>{
        if(err1){
            console.log(err1.message)
            return
        }
        console.log(rows1)
        db.all(query2, (err2, rows2) =>{
            if(err2){
                console.log(err2.message)
                return
            }
            console.log(rows2)
            
            //Setting up value to send
            res.status(200).json({amount: rows2[0].count,data: rows1})
        })
    })

})

app.listen(4000, ()=>{
    console.log("Listening to port 4000...")
})