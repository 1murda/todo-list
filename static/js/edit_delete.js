let editButton = document.querySelector('#edit-button');
editButton.addEventListener('click', confirmEditTask);

function confirmEditTask() {
    let confirm = window.confirm('Are you sure you want to edit this task?');
    if (confirm) {
        editTask();
    }
}

let deleteButton = document.querySelector('#delete-button');
deleteButton.addEventListener('click', confirmDeleteTask);

function confirmDeleteTask() {
    let confirm = window.confirm('Are you sure you want to delete this task?');
    if (confirm) {
        deleteTask();
    }
}