document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('themeToggle');
    const body = document.body;

    toggleButton.addEventListener('click', function() {
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
        } else {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
        }
    });
});