function Codeforces(){
    document.getElementById("Stage1").style.visibility = "hidden";
    document.getElementById("Stage2andCodeforces").style.visibility = "visible";
}
function Eval1(){
    var cfRating = document.getElementById("input 1").value;
    var output = 0.76 * parseInt(cfRating) + 575;
    document.getElementById("ans 1").innerHTML = 'Your CodeChef Rating is : ';
    document.getElementById("ans 12").innerHTML = output;
}

function CodeChef(){
    document.getElementById("Stage1").style.visibility = "hidden";
    document.getElementById("Stage2andCodeChef").style.visibility = "visible";
}
function Eval2(){
    var ccRating = document.getElementById("input 2").value;
    var output = 1.15 * parseInt(ccRating) - 550;
    document.getElementById("ans 2").innerHTML = 'Your CodeForces Rating is : ';
    document.getElementById("ans 21").innerHTML = output;
}