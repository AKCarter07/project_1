let logoutBtn = document.getElementById('logout');
logoutBtn.addEventListener('click', () => 
    {fetch('http://127.0.0.1:8080/logout'),
    window.location.href = 'index.html'});

let getReimbsBtn = document.querySelector('#fetch-reimbs');
getReimbsBtn.addEventListener('click', getRes);


async function getRes() {    
    try{
        let getReimbs = await fetch("http://127.0.0.1:8080/fm/reimbursements?filter-status=null&filter-type=null", {
                'credentials': 'include',
                'method': 'GET'
        })
        let reimbsJson = await getReimbs.json();
        addReimbToTable(reimbsJson);
    } catch (err) {
        console.log(err)
    }
}

function testObject (jsonObject){
    var msg = (typeof jsonObject);
    console.log(typeof JSON.stringify(jsonObject));
    console.log(JSON.stringify(jsonObject));
    console.log(msg)
}

function addReimbToTable(reimbs){
    let reimbTable = document.querySelector('#reimbs-table');
    console.log(reimbs);
    Object.keys(reimbs).forEach(k => {
        testObject(reimbs[k]);
        obj = JSON.stringify(reimbs[k]);
        
        console.log(k, ': ', obj['reimb_id']);
    })

    /*

     Object.keys(reimbs[k]).forEach(obj => {
            console.log(reimbs[k][obj])
        })


    for (var key in reimbs) {
        let reimb_key = '${key}';
        let reimb = dict[reimb_key];
        console.log(reimb);
        let row = document.createElement('tr');
        let idCell = document.createElement('td');
        idCell.innerHTML = key.reimb_id;
        let amountCell = document.createElement('td');
        amountCell.innerHTML = key.amount;


        row.appendChild(idCell);
        row.appendChild(amountCell);
        reimbTable.appendChild(row);
    }*/
}
/*
<th>Status</th>
                        <th>R-Id</th>
                        <th>Amount</th>
                        <th>Type</th>
                        <th>Description</th>
                        <th>Submitted By</th>
                        <th>Submitted On</th>
                        <th>Receipt</th>
                        <th>Resolved By</th>
                        <th>Resolved On</th>

                        */