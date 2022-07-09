
function deluser(dni) {
    fetch('http://127.0.0.1:8000/userdelete/?dni='+ dni,{
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
        return response.json();
    }
    )
}
