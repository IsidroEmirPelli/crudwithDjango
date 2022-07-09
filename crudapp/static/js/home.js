list = document.getElementById('lista')
document.onkeypress = function (e) {
    e = e || window.event;
    /* wait */
    setTimeout(function () {
        text : document.getElementById("text")
        /* make a fetch get */
        url = 'http://127.0.0.1:8000/userget/?format=json&text='
        fetch(url + text.value)
        .then(res => res.json())
        .then(function (data) {
            console.log(text.value)
            console.log(data);
            list.innerHTML = '';
            for (i = 0; i < data.length; i++) {
                list.innerHTML += `
                <div class="card-header text-white row">
						<p class="h6 col-md-8 text-center mt-2">
							${data[i].first_name} ${data[i].last_name}  ${data[i].dni}
						</p>

						<a href="view?dni=${data[i].dni}" class="btn btn-primary col-md-4">View</a>
                </div>
                `
            }
             list.innerHTML+= `<div class="card-header text-white row">
                    <p class="h6 col-md-8 text-center mt-2">
                        Registrarme
                    </p>

                    <a href="register" class="btn btn-success col-md-4">Register</a>
                </div>`

            document.getElementById('contlista').classList.remove("d-none")

        })
    }, 1000);
}