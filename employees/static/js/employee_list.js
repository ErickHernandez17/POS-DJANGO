document.addEventListener('DOMContentLoaded', () => {
    const changePassButtons = document.querySelectorAll('.change-pass-btn');
    const updateInfoButtons = document.querySelectorAll('.update-info-btn');

    changePassButtons.forEach(button => {
        const userId = button.getAttribute('data-user-id');
        button.addEventListener('click', () => {
            const url = `/employee/change-pass/${userId}/`;
            window.location.href = url;
        });
    });

    updateInfoButtons.forEach(button => {
        const employeeId = button.getAttribute('data-employee-id');
        button.addEventListener('click', () => {
            const url = `/employee/employee/update/${employeeId}/`;
            window.location.href = url;
        });
    });
});
