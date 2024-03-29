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

  // Obsługa zmiany języka
  const langButtons = document.querySelectorAll('.lang-switch');
  const translateElements = document.querySelectorAll('.translate');

  // Sprawdź, czy język jest zapisany w localStorage
  const savedLang = localStorage.getItem('preferredLang');

  // Jeśli język jest zapisany, ustaw go
  if (savedLang) {
      translateElements.forEach(function (element) {
          element.textContent = element.dataset['lang' + savedLang];
      });
  }

  // Dodaj obsługę zmiany języka
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
