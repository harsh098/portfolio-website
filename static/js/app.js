const sections = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.controls');
const sectBtn = document.querySelectorAll('.control');
const allSections = document.querySelector('.main-content');
const themeBtn = document.querySelector('.theme-btn');

(function(){

    sectBtn.forEach((btn)=>{
        btn.addEventListener('click', (event)=>{
            document.querySelector('.active-btn').classList.replace('active-btn', 'inactive-btn');
            event.target.classList.replace('inactive-btn','active-btn');
            id=event.target.dataset.id;
            if(id){
                document.querySelector('.active').classList.remove('active');
                document.querySelector(`#${id}`).classList.add('active');
            }
        })
    })
    
    themeBtn.addEventListener('click', ()=>{
        if(document.querySelector('body').classList.contains('light-mode')){
            document.querySelector('body').classList.remove('light-mode');
        }else{
            document.querySelector('body').classList.add('light-mode');
        }
    })
})();