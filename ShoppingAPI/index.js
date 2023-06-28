require('dotenv').config()

const express = require('express')
const bodyParser = require('body-parser')
const querystring = require('querystring')
const mongoose = require('mongoose')
const Item = require('./models/item')
const Order = require('./models/order')

const app = express()

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

mongoose.connect(process.env.DATABASE_URL)
const db = mongoose.connection
db.on('error', (error) => console.error(error))
db.once('open', () => console.log("Connected to database"))

app.listen(process.env.PORT, () => {
    console.log(`Running on http://localhost:${process.env.PORT}`)
})

app.get('/order', async (req, res) => {
    const orderRefNumber = req.query.orn
    const customerName = req.query.name
    var results = []

    if (!orderRefNumber || !customerName) {
        res.status(401).send({
            error: `Please provide an order reference number and a customer name`
        })

        return
    }

    // TODO: Search DB and capture results


    // TODO: Return results
    res.status(200).send({
        orderRefNumber: orderRefNumber,
        customerName: customerName,
        results: results
    })
})

app.post('/order', async (req, res) => {
    const { customerName, customerAddress, items, totalPrice, orderDate, notes } = req.body
    var alreadyExists = false

    // Check if order exists in DB

    // If order already exists, get orderRefNumber and update values

    // If order doesn't exist, increment orderRefNumber and add order to DB

    if (alreadyExists) {
        res.status(200).send({
            message: `Order successfully replaced`
        })
    } else {
        res.status(201).send({
            message: `New order successfully posted`
        })
    }
})

app.get('/reports', async (req, res) => {
    const itemName = req.query.item

    if (!itemName) {
        res.status(401).send({
            error: `Please provide an item name`
        })

        return
    }

    res.status(200).send({
        item: `Your item is ${itemName}`
    })
})

app.get('/allItems', async (req, res) => {

    try {
        const items = await Item.find()
        res.status(200).send({
            items: items
        })
    } catch (error) {
        res.status(500).send({
            error: error.message
        })
    }
})

app.post('/addItem', async (req, res) => {
    var item = new Item({
        itemName: req.body.itemName,
        quantity: req.body.quantity,
        price: req.body.price,
        description: req.body.description
    })

    try {
        const newItem = await item.save()
        res.status(201).send({ newItem })
    } catch (error) {
        res.status(400).send({
            error: error.message
        })
    }
})