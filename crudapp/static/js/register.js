/* Take the data from the form and post in the api addPersona */
function register() {
    var data = {
        "first_name": document.getElementById("first_name").value,
        "last_name": document.getElementById("last_name").value,
        "dni" : document.getElementById("dni").value,
        "birth_date": document.getElementById("birth_date").value,
        "address": document.getElementById("address").value,
        "phone_number": document.getElementById("phone_number").value
    }
    fetch('http://127.0.0.1:8000/userpost/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(function (response) {
        return response.json();
    })
}
