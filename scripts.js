document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;
    
    if (name && email && message) {
        document.getElementById('contactMessage').textContent = '感谢您的留言，我们会尽快回复！';
        document.getElementById('contactForm').reset();
    } else {
        document.getElementById('contactMessage').textContent = '请填写所有字段。';
    }
});