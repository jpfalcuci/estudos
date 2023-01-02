let botoes = document.querySelector('.botoes');
let btn = document.querySelectorAll('span');
let result = document.getElementById('result');
let toggleBtn = document.querySelector('.toggleBtn');
let body = document.querySelector('body');

for(let i=0; i<btn.length; i++){
    btn[i].addEventListener("click", function(){
        
        if(this.innerHTML=="="){
            result.innerHTML = eval(result.innerHTML)
        }else{
            if(this.innerHTML=="C"){
                result.innerHTML = "";
            }
            else{
                result.innerHTML += this.innerHTML;
            }
        }
    })
}

toggleBtn.onclick = function(){
    body.classList.toggle('dark');
}
