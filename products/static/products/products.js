document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('img').forEach(image => {
        image.onmouseover = function () {
            if (document.querySelector(`#${this.dataset.ids}`).style.display === 'none') {
                document.querySelector(`#${this.dataset.ids}`).style.display = 'block';
            }
            else {
                document.querySelector(`#${this.dataset.ids}`).style.display = 'none';
            }
        }
    })
    document.querySelectorAll('#buy').forEach(button => {
        button.onclick = function () {
            let value = this.value -= 1;
            if (value > 0) {
                document.querySelector(`#${this.dataset.value}`).innerHTML = `In Stock: ${value}`;
            }
            else {
                document.querySelector(`#${this.dataset.value}`).innerHTML = `Out of Stock`;
            }
            console.log(value);
        }
    })
})