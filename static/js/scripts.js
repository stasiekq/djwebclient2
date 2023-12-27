// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;
  
    // Sprawdź, czy tryb ciemny jest zapisany w localStorage
    const isDarkMode = localStorage.getItem('darkMode') === 'enabled';
  
    // Jeśli tryb ciemny jest zapisany, włącz go na starcie
    if (isDarkMode) {
      body.classList.add('dark-mode');
      darkModeToggle.checked = true;
    }
  
    // Obsługa zmiany trybu jasnego/ciemnego
    darkModeToggle.addEventListener('change', function () {
      if (darkModeToggle.checked) {
        body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'enabled');
      } else {
        body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', null);
      }
    });
});
  

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