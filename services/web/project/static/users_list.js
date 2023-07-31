function users_list(data, layout_element){
    if (Object.keys(data).length !== 0){
        for (user_data of data) {
            const user_element = document.createElement("div");

            const user_data_block = document.createElement("div");
            user_data_block.textContent = `ID: ${user_data.id}, Username: ${user_data.username}, Email: ${user_data.email}`;

            user_element.appendChild(user_data_block)

            if (user_data.in_contacts == 'false'){
                _button_addcontact = button_addcontact(user_data.id)
                user_element.appendChild(_button_addcontact)
            }

            layout_element.appendChild(user_element);
        }
    }
}