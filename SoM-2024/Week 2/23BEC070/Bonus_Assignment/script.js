function processInput1() {
    let w = 0.74430042;
    let b = 0.15470214;
    var inputValue1 = document.getElementById('userinput1').value;
    var result1 = (w * inputValue1) + b;
    document.getElementById('result1').innerText = "Predicted CodeForces Rating: " + result1.toFixed(0);
}

function processInput2() {
    let w = 0.84430042;
    let b = 0.25470214;
    var inputValue2 = document.getElementById('userinput2').value;
    if (inputValue2 == 0) {
        result2 = 0
    }
    else {
        var result2 = (inputValue2 - b) / w;
    }
    document.getElementById('result2').innerText = "Predicted CodeChef Rating: " + result2.toFixed(0);
}