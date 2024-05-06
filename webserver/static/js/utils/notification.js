showNotification = (message) => { 
    const notificationContainer = document.getElementById('notificationContainer');
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;

    // Set initial width and height to auto
    notification.style.width = 'auto';
    notification.style.height = 'auto';

    notificationContainer.appendChild(notification);

    // Dynamically adjust width and height based on content
    const style = window.getComputedStyle(notification);
    notification.style.width = `${style.width}px`;
    notification.style.height = `${style.height}px`;

    notification.classList.add('show');

    setTimeout(() => {
        notification.classList.add('hide'); // Trigger the fade-out animation
    }, 5000);

    // Automatically hide the notification after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        notificationContainer.removeChild(notification);
    }, 10000);
}