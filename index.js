function prueba() {
    const url = 'https://restcountries.com/v2/callingcode/';
    for (let i = 1; i < 3; i++) {
        fetch(url + i)
        .then(response => response.json())
        .then(data => {
            if (data.status == 404) {
                console.log(`No existe el pais con el codigo de llamada ${i}`);
            } else {
                console.log(`El pais con el codigo de llamada ${i} es ${data[0].name}`);
            }
        })
        .catch(error => console.log(error));
    }
}