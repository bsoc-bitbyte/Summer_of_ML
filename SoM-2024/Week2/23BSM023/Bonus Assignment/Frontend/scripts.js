let cf=false;
let cc=false;

document.getElementById('chefbutton').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('popup').style.display = 'block';
    document.getElementById('display').innerHTML = 'Predict your CodeChef Rating';
    document.getElementById('numberInput').placeholder='Enter Your Present CodeForces Rating'
    document.getElementById('display').style.alignSelf = 'center';
    cc=true;
    cf=false;

});
document.getElementById('forcesbutton').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('popup').style.display = 'block';
    document.getElementById('numberInput').placeholder='Enter Your Present CodeChef Rating'
    document.getElementById('display').innerHTML = 'Predict your CodeForces Rating';
    cf=true;
    cc=false;

});
document.getElementById('eval').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('popup').style.display = 'block';
    if(cc==true){
        let rate;
        let predict;
        rate=Number(document.getElementById('numberInput').value.trim());
        if(rate<0){
            document.getElementById('display').innerHTML ="Enter Valid Input";
            

        }
        else{
            predict= Math.round(rate*1.6);
            document.getElementById('display').innerHTML ="YOUR PREDICTED CODECHEF SCORE  🏆:  "+predict;


        }
        

    }
    if(cf==true){
        let rate;
        let predict;
        rate=Number(document.getElementById('numberInput').value.trim());
        if(rate<0){
            document.getElementById('display').innerHTML ="Enter Valid Input";
            

        }
        else{
            predict=Math.round(rate*0.625);
            document.getElementById('display').innerHTML ="YOUR PREDICTED CODEFORCES SCORE  🏆:  "+predict;


        }
        

    }
});

document.getElementById('close').addEventListener('click', function(event) {
    
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popup').style.display = 'none';
});

// Optional: Close the pop-up when clicking outside of it
document.getElementById('overlay').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popup').style.display = 'none';
});