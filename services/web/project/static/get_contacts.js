function get_contacts(user_id){
    fetch('/get_contacts',
    {
        method: 'GET',
    })
    .then((response) => {
        const contacts = document.getElementById("contacts")
        contacts.innerHTML += _res
    });
}