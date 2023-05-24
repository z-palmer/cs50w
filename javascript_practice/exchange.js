var myHeaders = new Headers();
myHeaders.append('apikey', 'kPR7VQSWUD6kcKDMngcFFIISMfckaD9Z')

document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('form').onsubmit = function () {

        fetch('https://api.apilayer.com/exchangerates_data/latest?base=USD', {
            method: 'GET',
            redirect: 'follow',
            headers: myHeaders
        })
            .then(response => response.json())
            .then(data => {

                const rates = data.rates
                const symbols = data.symbols

                rates.forEach(element => {
                    element = document.createElement('option');
                    element.value
                });

                const currency = document.querySelector('#currency').value.toUpperCase();
                const amount = document.querySelector('#amount').value;
                const rate = data.rates[currency];
                if (rate !== undefined) {
                    result = parseFloat(rate) * parseFloat(amount);
                    document.querySelector('#result').innerHTML = `$${amount} is equal to ${result.toFixed(2)} ${currency}`;
                } else {
                    document.querySelector('#result').innerHTML = 'Invlid Currency.';
                }
            })
            .catch(error => {
                console.log(error);
            })

        return false;
    }
});