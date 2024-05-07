showNotification = (message) => { 
    const _NotificationContainer_ = document.getElementById('notificationContainer');
    const _notification_ = document.createElement('div');
    _notification_.className = 'notification';
    _notification_.textContent = message;

    // Set initial width and height to auto
    _notification_.style.width = 'auto';
    _notification_.style.height = 'auto';

    _NotificationContainer_.appendChild(_notification_);

    // Dynamically adjust width and height based on content
    const style = window.getComputedStyle(_notification_);
    _notification_.style.width = `${style.width}px`;
    _notification_.style.height = `${style.height}px`;

    _notification_.classList.add('show');

    setTimeout(() => {
        _notification_.classList.add('hide'); // Trigger the fade-out animation
    }, 5000);

    // Automatically hide the notification after 3 seconds
    setTimeout(() => {
        _notification_.classList.remove('show');
        _NotificationContainer_.removeChild(_notification_);
    }, 10000);
}