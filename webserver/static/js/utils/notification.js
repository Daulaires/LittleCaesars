showNotification = (message) => {
    const notificationContainer = document.getElementById('notificationContainer');
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    notificationContainer.appendChild(notification);
    notification.classList.add('show');
    setTimeout(() => {
        notification.classList.add('fadeOut'); // Trigger the fade-out animation
    }, 5000);
    // Automatically hide the notification after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        notificationContainer.removeChild(notification);
    }, 10000);
};