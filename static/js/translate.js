document.addEventListener('DOMContentLoaded', function () {
    var translateElements = document.querySelectorAll('.translate');
    var langButtons = document.querySelectorAll('.lang-switch');
    
    // Sprawdzanie, czy zapisany język istnieje w localStorage
    var savedLang = localStorage.getItem('preferredLang');
    
    // Jeśli język jest zapisany, ustaw go
    if (savedLang) {
        translateElements.forEach(function (element) {
            element.textContent = element.dataset['lang' + savedLang];
        });
    }

    langButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var lang = this.dataset.lang;
            
            // Zapisz wybrany język do localStorage
            localStorage.setItem('preferredLang', lang);

            translateElements.forEach(function (element) {
                element.textContent = element.dataset['lang' + lang];
            });
        });
    });
});
