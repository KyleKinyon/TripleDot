const mongoose = require('mongoose')

const orderSchema = new mongoose.Schema({
    orderRefNumber: {
        type: Number,
        required: true
    },
    customerName: {
        type: String,
        required: true
    },
    customerAddress: {
        type: String,
        required: true
    },
    items: {
        type: String,
        required: true,
        default: []
    },
    totalPrice: {
        type: Number,
        required: true
    },
    orderDate: {
        type: Date,
        required: true,
        default: Date.now
    },
    notes: {
        type: String
    }
})

module.exports = mongoose.model('Order', orderSchema, "Orders")