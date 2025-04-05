<script src="{{ url_for('static', filename='script.js') }}"></script>

document.querySelectorAll('form[action*="delete_task"]').forEach(form => {
    form.addEventListener('submit', function (e) {
        if (!confirm('Are you sure you want to delete this task?')) {
            e.preventDefault();
        }
    });
});