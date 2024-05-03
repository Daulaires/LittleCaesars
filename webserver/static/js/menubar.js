document.addEventListener('DOMContentLoaded', function() {
    const menuToggleButton = document.getElementById('menuToggle');
    const menu = document.getElementById('menu');

    menuToggleButton.addEventListener('click', function() {
        if (menu.style.display === 'none') {
            menu.style.display = 'block';
        } else {
            menu.style.display = 'none';
        }
    });
});
