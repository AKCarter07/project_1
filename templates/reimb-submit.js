let amount = document.getElementById('amount-input');
let descrip = document.getElementById('descrip-input');
let reimbSubmitBtn = document.getElementById('reimb-submit-btn');
let typeBtns = document.querySelectorAll('input[name="type"]');

reimbSubmitBtn.addEventListener('click', async (e) => {
    
    try {
        console.log('click');
        let selectedType;
        for (let radioBtn of typeBtns) {
            if (radioBtn.checked){
                selectedType = radioBtn;
                break;
            }
        }
        e.preventDefault();


        let result = await fetch('http://127.0.0.1:8080/e/reimbursement', {
            'credentials': 'include',
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': JSON.stringify({
                'amount': amount.value,
                'description': descrip.value,
                'type': selectedType.value
            })
        })
        
        if (result.status == 201) {
            window.location.href = './employee-home.html'
        }/*
        else if (res.status == 400) {
            let data = await res.json();
            
            let errorMessagesDiv = document.getElementById('error-messages')
            errorMessagesDiv.innerHTML = '';

            let errMessages = data.messages;
            for (let errorMessage of errMessages) {
                let errorElement = document.createElement('p');
                errorElement.innerHTML = errorMessage;
                errorElement.style.color = 'red';
                errorElement.style.fontWeight = 'bold';

                errorMessagesDiv.appendChild(errorElement);
            }
        }*/
    }
    catch (err) {
        console.log(err);
    }
})