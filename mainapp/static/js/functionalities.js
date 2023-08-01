let clima = document.getElementById('clima')
let temperatura = 0
document.getElementById('contenido').style.backgroundColor = '#0077be'
document.getElementById('celcius').style.backgroundColor = '#0077be'
document.getElementById('farenheit').style.backgroundColor = '#0077be'
document.getElementById('header').style.backgroundColor = 'blue'
let temperatura_string = document.getElementById('temperatura')
temperatura = parseInt(temperatura_string.textContent.slice(0,2))
if (temperatura <= 15) {
    temperatura_string.style.color = '#49FFEC'
} else if (temperatura <= 27){
    temperatura_string.style.color = 'white'
} else {
    temperatura_string.style.color = 'orange'
}

function celcius_fn() {
    let temperatura_string = document.getElementById('temperatura')
    if (temperatura_string.textContent.includes("F")) {
        temperatura = Math.round((parseInt(temperatura_string.textContent.slice(0,2))-32)/(9/5))
        temperatura_string.textContent = temperatura + "°C"
    }
}

function farenheit_fn() {
    let temperatura_string = document.getElementById('temperatura')
    if (temperatura_string.textContent.includes("C")) {
        temperatura = Math.round(((parseInt(temperatura_string.textContent.slice(0,2)))*(9/5))+32)
        temperatura_string.textContent = temperatura + "°F"
    }
}