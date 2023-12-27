document.addEventListener('DOMContentLoaded', function () {
    var translateElements = document.querySelectorAll('.translate');
    var langButtons = document.querySelectorAll('.lang-switch');

    langButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var lang = this.dataset.lang;
            translateElements.forEach(function (element) {
                element.textContent = element.dataset['lang' + lang];
            });
        });
    });
});