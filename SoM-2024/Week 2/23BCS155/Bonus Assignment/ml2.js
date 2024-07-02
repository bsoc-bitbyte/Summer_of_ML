const c2 = 1044.6363090556167;
const c1 = -32.62926507315501;
const m1 = 0.8315620555789317;
const m2 = 0.46912877135387565;
document.getElementById('convert_but').addEventListener('click', function() {
    const codechefRating = document.getElementById('codechef-rating').value;
    const codeforcesRating = document.getElementById('codeforces-rating').value;

    
    if (codechefRating || codeforcesRating) {
       
        const convertedRating = convertRatings(codechefRating, codeforcesRating);

       
        document.getElementById('result').textContent = `Converted Rating: ${convertedRating}`;
    } else {
        document.getElementById('result').textContent = 'Please enter both ratings.';
    }
});

function convertRatings(codechefRating, codeforcesRating) {
   
    if(codechefRating){
        return (parseInt(codechefRating)*m2+c2 )
    }
    else{
        return(parseInt(codeforcesRating)*m1+c1 )
    }
    
}
