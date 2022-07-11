const dni = document.getElementById('dni').innerText
function deletePersona() {
    url = 'http://127.0.0.1:8000/userdelete/?dni=' + dni
    fetch(url,{
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
}
