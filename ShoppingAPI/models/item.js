const mongoose = require('mongoose')

const itemSchema = new mongoose.Schema({
    itemName: {
        type: String,
        required: true
    },
    quantity: {
        type: Number,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    description: {
        type: String
    }
})

module.exports = mongoose.model('Item', itemSchema, "Items")