function button_addcontact(user_id){
    const button = document.createElement("button")
    button.type = "button"
    button.textContent = "додати"
    button.addEventListener("click", function() {
        adding_contact(user_id);
    });

    return button
}