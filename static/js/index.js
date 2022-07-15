function confirmDelete() {
    let confirm = window.confirm('Are you sure you want to delete this task?');
    // si no confirma la eliminacion, se redirecciona a la pagina de inicio
    if (!confirm) {
        document.querySelector("id-form-edit").action = "/todolist";
    }

}