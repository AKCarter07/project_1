let logoutBtn = document.getElementById('logout');
logoutBtn.addEventListener('click', () => 
    {fetch('http://127.0.0.1:8080/logout'),
    window.location.href = 'index.html'});