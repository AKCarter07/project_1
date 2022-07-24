// mobile menu
const burgerIcon=document.querySelector('#burger');
const navbarMenu = document.querySelector('#nav-links');

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active');
});


// modal
const submitButton = document.querySelector('#submit'); 
const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');

submitButton.addEventListener('click', () => {
   modal.classList.add('is-active'); 
});
document.getElementById('submit').onclick = function() {
    location.href = '/login.html';
};

// modalBg.addEventListener('click', () => {
//     modal.classList.remove('is-active');
// });

const enterButton = document.querySelector('#enter');
enterButton.addEventListener('click', () => {
    modal.classList.add('is-active');
});
document.getElementById('enter').onclick = function() {
    location.href = '/login.html';
};


// Login

// let username = document.getElementById('username')
// let password = document.getElementById('password')


// let loginButton = document.getElementById('login-btn');

// loginButton.addEventListener('click', async () => {

//     let result = await fetch('http://127.0.0.1:8080/login', {
//         'credentials': 'include',
//         'method': 'POST',
//         'headers': {
//             'Content-type': 'application/json'
//         },
//         'body': JSON.stringify({
//             "username": username.value,
//             "password": password.value
//         })
//     })
    
//     let data = result.json()
    

//    if (result.status === 200){
//             console.log(data);
//             console.log(data);
//             data.then(value => {
//                 if (value.role === "finance_manager"){
//                     window.location.href = 'finance-manager-home.html'
//                 }
//                 else if (value.role === "employee"){
//                     window.location.href = 'employee-home.html'
//                 }

//             })
//      //   if 
        
//            // window.location.href = 'home.html'
       
//     }
//     else if (result.status === 400) {
//         let regErrorMessages = document.getElementById('reg-error-msgs')
//         console.log(regErrorMessages)
//     }
//     else {
//         console.log("problem")
//     }
    
// });