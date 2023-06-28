function getURL() {
    var longUrl = document.getElementById("longUrl").value
    console.log("URL received:", longUrl)
    return longUrl
}

function createRandomString() {
    var randomString = Math.random().toString(32).substring(2, 9)
    console.log("Random String =", randomString)
    return randomString
}


function createShortURL() {
    var longUrl = getURL()
    if (longUrl == "") { return }

    var randomString = createRandomString()
}

function redirect() {

}

function lookupURL() {
    
}
