document.addEventListener('DOMContentLoaded', function() {
    var w=0.8315620555789324;
    var b=-32.629265073164284;
    var aboutDiv = document.querySelector('.about');
    var askDiv = document.querySelector('.ask');
    var askHeading = askDiv.querySelector('h3'); 
    var result= document.querySelector('.result');
    var input= document.querySelector('.input');
    var btn= document.querySelector('.ask button');
    var h3=result.querySelector('h3');
    var h4=result.querySelector('h4');

    if (aboutDiv && askDiv && askHeading) {
        document.querySelectorAll('.button button').forEach(button => {
            button.addEventListener('click', function() {
                aboutDiv.classList.add('hidden');
                askDiv.classList.remove('hidden'); 
                result.classList.add('hidden')
                input.value='';
              
                
                if (button.classList.contains('chef')) {
                    askHeading.textContent = 'Enter Rating (CodeForces=>CodeChef)';
                    

                    btn.addEventListener('click',function(){
                        
        
                        result.classList.remove('hidden');
                        askDiv.classList.add('hidden');
                        const y=input.value;
                        const x=(y-b)/w;
                        h3.textContent='Your CodeChef Rating';
                        h4.textContent=Math.round(x);

                    })
                   


                } else if (button.classList.contains('forces')) {
                    askHeading.textContent = 'Enter Rating (CodeChef=>CodeForces)';
                    btn.addEventListener('click',function(){
                     
        
                        result.classList.remove('hidden');
                        askDiv.classList.add('hidden');
                        const x=input.value;
                        const y=x*w+b;
                        h3.textContent='Your CodeForces Rating';
                        h4.textContent=Math.round(y);


                    })
                }
            });
        });
    } else {
        console.error('One or more of the required elements (about, ask, or ask h3) not found.');
    }
});
