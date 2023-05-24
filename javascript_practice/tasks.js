document.addEventListener('DOMContentLoaded', () => {

    // Disable submit button by default
    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
    }

    document.querySelector('form').onsubmit = () => {
        const task = document.querySelector('#task').value;

        const li = document.createElement('li');
        li.innerHTML = task;

        document.querySelector('#tasks').append(li);

        document.querySelector('#task').value = '';

        document.querySelector('#submit').disabled = true;

        return false;
    }
});